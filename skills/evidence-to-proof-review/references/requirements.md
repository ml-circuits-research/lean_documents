# Runtime requirements

The complete skill folder is portable: its scripts import only Python standard-library modules and sibling modules. It does not need this repository's examples, evaluator answers or prior audit outputs. Python 3.9+ APIs are used; current validation uses Python 3.14. SQLite must provide FTS5 for the indexed engine. A coding agent supplies semantic analysis and model authoring.

| Capability | Required tools |
| --- | --- |
| UTF-8 text and DOCX | Python and standard-library ZIP/XML/SQLite |
| Searchable PDF and original coordinates | Poppler: pdfinfo, pdftotext, pdfimages |
| Scanned/mixed PDF | Poppler pdftoppm plus Tesseract and the selected language data |
| PNG/JPEG OCR | Tesseract and language data |
| Formal proofs | Lean 4.24.0 and its sibling Lake executable; core Init/Std only |
| Separate environment replay | Optional compatible lean4checker executable; never imply availability from a passed Lean build |

Use `python3 /path/to/skill/scripts/audit.py doctor --lean /absolute/path/to/lean` to inspect availability. Missing converters yield explicit blocked/partial ingestion records, not fabricated extracted text. The helper never downloads or installs packages automatically. Install the documented dependencies with the environment's approved package mechanism or a verified user-local distribution.

No pip package is required by the skill. The repository's synthetic scanned-fixture builder uses Pillow and a local font; those are fixture-development dependencies, not runtime requirements. Local extraction and proof checking need no network after tools are installed; the coding agent may have its own service connection.

Use a writable work root outside the supplied source directories. The default is `tmp/` under the current working directory. Keep it ignored by Git and retain every run for inspection. Timeouts are per external command; batch time budgets stop between documents. For adversarial binaries or generated code, use an appropriate execution sandbox; lexical checks and document parsing are not a substitute for process isolation.
