# Native fixture construction notes

These notes are fixture-authoring metadata, not audit evidence.

The retained construction scripts are in the repository ignored directory `tmp/prepare-dossiers-06-07/`. Native rendering uses `examples/builders/fixture_formats.py`: `write_docx`, `write_pdf`, and `write_scan_pdf`. The source body is substantive author-written material. Native Markdown masters are outside `sources/`, so no plaintext duplicate is supplied in an audit.

PDF generation normalizes curly quotation marks/apostrophes and dash punctuation to ASCII equivalents for the standard embedded font. The DOCX preserves Unicode punctuation. This normalization changes no numeric, conditional, attribution, or polarity content. Each source section starts with a visible bracketed semantic marker; paragraph/page coordinates must come from the actual extraction, not this authoring record. Scan PDFs use rendered page images and no text layer.

## Native source mappings

- `authoring/procurement-standard.md` → `sources/procurement-standard.docx`; markers `[P01]`, `[P02]`, `[P03]`, `[P04]`, `[P05]`, `[P06]`, `[P07]`, `[P08]`.
- `authoring/revision-amendment.md` → `sources/revision-amendment.pdf`; markers `[V01]`, `[V02]`, `[V03]`, `[V04]`, `[V05]`, `[V06]`.
- `authoring/approval-attestations.md` → `sources/approval-attestations.scan.pdf`; markers `[A01]`, `[A02]`, `[A03]`, `[A04]`.

## Separation and checks

The manifest inventories only actual audit materials: the brief, both selectable supplied reports, and the seven source files. Each run selects one report. README, build notes, authoring masters, and evaluator outcomes are excluded. Structural checks cover file presence, marker uniqueness, claim coverage, and SHA-256 correspondence. These are fixture-integrity checks, not a blind audit or proof validation.
