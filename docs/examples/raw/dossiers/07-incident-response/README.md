# 07-incident-response: synthetic native-document audit dossier

This dossier is wholly invented. Its standards, organizations, agreements, testimony, incidents, currencies, and dates are not claims about actual entities or real legal/operational requirements. It tests auditing supplied findings against a substantial finite corpus, including document extraction and semantic uncertainty.

The audit inputs are `brief.md`, exactly one selected report (`report.md` or `report-correct.md`), and these seven actual source files:

- `containment-attestations.scan.pdf`
- `incident-timeline.md`
- `maintenance-authorization.pdf`
- `monitoring-coverage.md`
- `notification-register.md`
- `response-playbook.docx`
- `review-correspondence.md`

Each report contains eighteen findings. Run the two report variants separately over the same corpus. The mixed variant intentionally contains incorrect or unsupported assertions; the careful alternative states documented conclusions and evidentiary limits. Neither is a source for the other. The selected report is always visible to the auditor; expected outcomes are separate under `examples/evaluator/` and withheld in blind evaluation.

The DOCX is native structured text, the ordinary PDF has a searchable text layer, and the `.scan.pdf` consists of raster page images without a hidden text layer. Native plaintext masters remain only in `authoring/` for reproducible fixture construction. They are not audit inputs and must not be used to bypass DOCX/PDF extraction or OCR. All other source documents are Markdown with stable anchors. `manifest.json` hashes actual brief, report, and source bytes after native rendering.

`build-notes.md` documents source markers and deterministic generation. No Lean audit or independent review of these new cases is claimed by the fixture author. Evaluation targets remain editorial until independently audited and checked.
