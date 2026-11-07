// Forward-use classification only. Historical adapters and receipts stay unchanged.
export function classifyUnitFailure(process, log, summary) {
  if (process.error || process.signal || ![0, 65].includes(process.status)) {
    return {kind: 'infrastructure', creditedTests: 0};
  }
  const diagnostics = [...log.matchAll(/^(.+\.swift):(\d+):(\d+): error: (.+)$/gm)]
    .map(m => ({file: m[1], line: Number(m[2]), column: Number(m[3]), message: m[4]}));
  if (process.status === 65 && summary?.totalTestCount === 0 && diagnostics.length &&
      /Testing cancelled because the build failed/.test(log) &&
      !/Test Case '.+' (passed|failed)/.test(log)) {
    return {kind: diagnostics.every(d => /\/Tests\//.test(d.file)) ? 'test-source-compilation' : 'source-compilation',
      creditedTests: 0, diagnostics};
  }
  return null;
}
