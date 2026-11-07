import Foundation
import SwiftSyntax
import SwiftParser

// Syntax observations only: this tool does not typecheck or infer accessibility semantics.
final class Probe: SyntaxVisitor {
    var functions: [[String: Any]] = []
    var accessibilityCalls: [[String: Any]] = []
    let locations: SourceLocationConverter
    init(tree: SourceFileSyntax, file: String) {
        locations = SourceLocationConverter(fileName: file, tree: tree)
        super.init(viewMode: .sourceAccurate)
    }
    override func visit(_ node: FunctionDeclSyntax) -> SyntaxVisitorContinueKind {
        let calls = Calls(locations: locations)
        if let body = node.body { calls.walk(body) }
        var owners: [String] = []
        var parent = node.parent
        while let current = parent {
            if let type = current.as(ClassDeclSyntax.self) { owners.insert(type.name.text, at: 0) }
            if let type = current.as(StructDeclSyntax.self) { owners.insert(type.name.text, at: 0) }
            if let type = current.as(ExtensionDeclSyntax.self) { owners.insert(type.extendedType.trimmedDescription, at: 0) }
            parent = current.parent
        }
        functions.append([
            "name": node.name.text,
            "ownerType": owners.joined(separator: "."),
            "line": locations.location(for: node.positionAfterSkippingLeadingTrivia).line,
            "startByte": node.positionAfterSkippingLeadingTrivia.utf8Offset,
            "endByte": node.endPositionBeforeTrailingTrivia.utf8Offset,
            "assertionCalls": calls.assertions,
            "assertionSites": calls.sites,
            "attributes": node.attributes.description.trimmingCharacters(in: .whitespacesAndNewlines)
        ])
        return .visitChildren
    }
    override func visit(_ node: FunctionCallExprSyntax) -> SyntaxVisitorContinueKind {
        let callee = node.calledExpression.description.trimmingCharacters(in: .whitespacesAndNewlines)
        if callee.lowercased().contains("accessibility") {
            accessibilityCalls.append(["callee": callee, "line": locations.location(for: node.positionAfterSkippingLeadingTrivia).line])
        }
        return .visitChildren
    }
}
final class Calls: SyntaxVisitor {
    var assertions: [String] = []
    var sites: [[String: Any]] = []
    let locations: SourceLocationConverter
    init(locations: SourceLocationConverter) {
        self.locations = locations
        super.init(viewMode: .sourceAccurate)
    }
    override func visit(_ node: FunctionCallExprSyntax) -> SyntaxVisitorContinueKind {
        let name = node.calledExpression.description.trimmingCharacters(in: .whitespacesAndNewlines)
        if name.hasPrefix("XCTAssert") || name == "XCTFail" {
            assertions.append(name)
            var conditions: [String] = []
            var parent = node.parent
            while let current = parent {
                if let clause = current.as(IfConfigClauseSyntax.self) {
                    conditions.insert(clause.poundKeyword.text + " " + (clause.condition?.trimmedDescription ?? ""), at: 0)
                }
                parent = current.parent
            }
            sites.append([
                "callee": name,
                "expression": node.trimmedDescription,
                "line": locations.location(for: node.positionAfterSkippingLeadingTrivia).line,
                "startByte": node.positionAfterSkippingLeadingTrivia.utf8Offset,
                "endByte": node.endPositionBeforeTrailingTrivia.utf8Offset
                , "conditionalCompilation": conditions
            ])
        }
        return .visitChildren
    }
}
var records: [[String: Any]] = []
for file in CommandLine.arguments.dropFirst() {
    let source = try String(contentsOfFile: file, encoding: .utf8)
    let tree = Parser.parse(source: source)
    let probe = Probe(tree: tree, file: file)
    probe.walk(tree)
    records.append(["path": file, "hasParserError": tree.hasError, "functions": probe.functions, "accessibilityCalls": probe.accessibilityCalls])
}
let data = try JSONSerialization.data(withJSONObject: records, options: [.prettyPrinted, .sortedKeys])
FileHandle.standardOutput.write(data)
