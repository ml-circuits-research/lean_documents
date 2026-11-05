// Start the local readable-document audit workspace.
process.env.AUDIT_DOCUMENT_PILOT = '1';
process.env.AUDIT_EXAMPLES_ROOT = 'examples/pilot';
process.env.AUDIT_RUNS_ROOT = 'tmp/readable-pilot/runs';
process.env.AUDIT_CONCURRENCY ||= '4';
await import('./audit-ui.mjs');
