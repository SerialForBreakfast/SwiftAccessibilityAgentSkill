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
        let calls = Calls(viewMode: .sourceAccurate)
        if let body = node.body { calls.walk(body) }
        functions.append([
            "name": node.name.text,
            "line": locations.location(for: node.positionAfterSkippingLeadingTrivia).line,
            "assertionCalls": calls.assertions,
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
    override func visit(_ node: FunctionCallExprSyntax) -> SyntaxVisitorContinueKind {
        let name = node.calledExpression.description.trimmingCharacters(in: .whitespacesAndNewlines)
        if name.hasPrefix("XCTAssert") || name == "XCTFail" { assertions.append(name) }
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
