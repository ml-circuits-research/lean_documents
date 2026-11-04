#!/usr/bin/env python3
"""Publish an offline, byte-preserving study catalog of supplied audit bundles.

No audit, proof checker, extraction tool, network access, or evaluator comparison
is executed here. All displayed statuses come from the supplied artifacts.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
from html import escape
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/examples"
SKIP = {".lake", ".git", "__pycache__", "node_modules", ".venv", "toolchains"}
BINARY_CACHE = {".pyc", ".olean", ".ilean", ".o", ".so", ".a", ".exe"}
TEXT = {".md", ".lean", ".json", ".jsonl", ".log", ".toml", ".txt", ".py", ".csv", ".tsv", ".lock", ".yaml", ".yml", ".xml", ".html", ".xhtml", ".hocr", ".sh"}
DESCRIPTIONS = {
    "01": "Approval timing, alternative emergency authorization, explicit negative records, an incomplete handoff, and conflicting attestations.",
    "02": "Version applicability, amendments, leap-day arithmetic, inclusive and exclusive deadlines, misleading labels, and a missing annex.",
    "03": "Integer arithmetic, denominators, budget balances, evidentiary completeness, and the difference between missing support and false conclusions.",
    "04": "Narrative chronology, flashbacks, identity and causal continuity, competing testimony, and claims beyond a finite fictional world.",
    "05": "Release authorization across conflicting attestations, source authority, inventory omissions, and a supplied verification excerpt.",
    "06": "Procurement rules and amendments across DOCX, searchable PDF, scanned attestations, purchase records, delegated authority, and exceptions.",
    "07": "Incident-response timing, maintenance authorization, notifications, monitoring coverage, and conflicting scanned containment attestations.",
    "08": "Inventory reconciliation and custody with a five-page image-only shipping PDF; a pale numeral and unsigned quantity remain distinct uncertainty problems.",
    "09": "Multiple native DOCX specifications and exception tables, PDF test runs, units, applicability, calibration authority, and unresolved faults.",
    "10": "Sixty operational records plus cross-document identity, delegated authority, rule transitions, board exceptions, and differently bounded completeness claims.",
    "11": "Report-derived criteria without a separate brief: arithmetic, bounded exceptions, citation fidelity, conclusion versus argument, dependencies, conflicts, and population scope.",
    "12": "An actually empty source file: distinguish a verified observation about zero bytes from unsupported clearance claims, without fabricated quotations or closed-world assumptions.",
}
ARTIFACTS = [
    ("Input snapshots and manifests", "input/report*, input/sources/, input/originals/, manifest.json, input/manifest.json", "Identify the exact selected report and supplied evidence; hashes bind bytes and native originals remain downloadable.", "Hashes do not authenticate a document or certify its factual truth. The alternate report is never evidence for the selected report."),
    ("Claim registry", "claims.json, input/report-ledger.json", "Record report anchors, registered claims, and (v2) anchor classifications and premise/citation/inference spans.", "Legacy v1 registries do not satisfy the v2 coverage contract merely because old proofs pass."),
    ("Extraction and provenance", "ingestion.json, extraction/, extraction-lock.json, input/source-ledger.json, source-ledger.jsonl", "Retain extracted passages, document/page/coordinate provenance where available, uncertainty, and extraction review.", "Extraction is not source authentication. OCR uncertainty, tables, and layout require review against native bytes."),
    ("Disk index and retrieval", "input/index.sqlite3, search-history.jsonl, search-ledger.json, search-records/, retrieval-scope.json", "Preserve indexed corpus and recorded search scope, queries, and inspected passages. SQLite is downloadable.", "A search log is not proof that every relevant real-world record exists in the supplied corpus."),
    ("Criteria and argument audit", "findings.json: criteria, argument_audit, support_search", "Expose operational questions, decision criteria, source rules, separate premise/citation/inference assessments, and independent conclusion reasoning.", "Missing support is a support gap, not proof of a false underlying claim. Historical records can lack these structured v2 fields."),
    ("Model and correspondence", "models/*.lean, model-notes.md, findings.json: formalization", "Show definitions, source transcription, assumptions, theorem statements, and explanations linking the model to the finding.", "Lean checks the encoded statement; source-to-model fidelity and the adequacy of chosen assumptions require semantic review."),
    ("Executed target checks and axioms", "checks/*.lean, logs/target-*.log, logs/lake-build.log, proof-results.json", "Show actual recorded execution status, explicit target checks, theorem names, model hashes, and reported axioms.", "A successful build alone does not establish that the target matches the report claim. An auxiliary theorem may prove only a limited support gap or countermodel."),
    ("Environment and original exports", "lean-toolchain, lakefile.toml, lake-manifest.json, environment.lock, export-manifest.json", "Record toolchain requirements and original export integrity metadata; these files are copied unchanged.", "Publication does not rerun Lean or modify an original export manifest. Toolchain binaries and build caches are intentionally excluded."),
    ("Semantic review and coverage", "semantic-review.md, independent-review/, coverage.md, audit-report.md", "Expose human/agent review findings, unresolved issues, exclusions, argument findings, and reported coverage.", "An executed proof is not an independent semantic review. A review file is a recorded assessment, not a guarantee of completeness."),
    ("Revision and fresh reproduction", "history/, attempts/, invalidation.json; separate reproduction snapshots", "Preserve failed attempts, changes, stale-dependency information and separately recorded later rechecks when available.", "A later proof recheck does not retroactively upgrade a legacy registry to v2 or repeat a blind domain audit."),
]
CSS = """body{margin:0;background:#f5f3ed;color:#172731;font:16px/1.6 system-ui,sans-serif}header,main,footer{max-width:1180px;margin:auto;padding:22px 30px}header{border-bottom:1px solid #bac4c6}a{color:#075e78;text-underline-offset:3px}nav{display:flex;gap:20px;flex-wrap:wrap}h1{font-size:2.2rem;line-height:1.2}h2{margin-top:2rem}h3{margin-top:1.4rem}p{max-width:100ch}.card,article{background:white;padding:22px;border:1px solid #d0d8d8;border-radius:8px;margin:18px 0}.note{background:#fff3d6;padding:16px;border-left:4px solid #c67b22}.badge{display:inline-block;background:#dcecf0;border-radius:5px;padding:3px 8px;margin-right:7px}table{width:100%;border-collapse:collapse;background:white}td,th{padding:10px;border-bottom:1px solid #d0d8d8;text-align:left;vertical-align:top}table{display:block;overflow:auto}pre,code{font-family:ui-monospace,monospace}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#eef2f2;padding:16px;font-size:13px}dt{font-weight:650;margin-top:10px}dd{margin-left:18px;overflow-wrap:anywhere}blockquote{border-left:4px solid #7195a4;margin-left:0;padding-left:16px}.line{display:block;min-height:1.3em}.line:target{background:#ffe6a1}.ln{color:#667e88;display:inline-block;width:5em;text-decoration:none;user-select:none}summary{cursor:pointer;font-weight:600;padding:8px}.muted{color:#526773}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px}.grid .card{margin:0}img{max-width:100%}iframe{width:100%;height:70vh;border:1px solid #bac4c6}ul{padding-left:24px}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;text-size-adjust:100%}
header,main,footer,.grid>*,.card,article,section,details,dd{min-width:0}
h1,h2,h3,a,p,li,td,th,summary,code{overflow-wrap:anywhere}
nav{gap:8px 18px}nav a{display:inline-flex;align-items:center;min-height:44px}
pre,table{max-width:100%;min-width:0;overscroll-behavior-x:contain}
.line{position:relative;padding-left:3.7em;min-height:1.6em}.ln{position:absolute;left:0;top:0;width:3.2em;text-align:right;padding-right:.5em}
a:focus-visible,summary:focus-visible{outline:3px solid #c67b22;outline-offset:3px}
@media(max-width:600px){
 header,main,footer{padding:16px 12px}
 nav{gap:4px 14px;font-size:.9rem}
 h1{font-size:1.65rem}h2{font-size:1.3rem;margin-top:1.6rem}h3{font-size:1.08rem}
 .grid{grid-template-columns:minmax(0,1fr);gap:14px}
 .card,article{padding:14px;margin:14px 0}.note{padding:12px}
 dd{margin-left:10px}ul{padding-left:20px}blockquote{padding-left:12px;margin-right:0}
 pre{padding:10px;font-size:12px}iframe{height:60vh;min-height:280px}
 table,tbody,tr,td{display:block;width:100%}table{background:transparent;overflow:visible}
 thead{position:absolute;width:1px;height:1px;padding:0;overflow:hidden;clip-path:inset(50%)}
 tr{background:white;border:1px solid #d0d8d8;border-radius:6px;margin:12px 0;padding:10px}
 td{border:0;padding:5px 0}td::before{content:attr(data-label);display:block;font-size:.75rem;font-weight:650;color:#526773}
 td a{display:inline-block;padding:6px 0}
}
"""


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path, default=None):
    return json.loads(path.read_text()) if path.exists() else default


def data_html(value) -> str:
    """Render data as escaped HTML, without executing embedded Markdown/HTML."""
    if isinstance(value, dict):
        return "<dl>" + "".join(f"<dt>{escape(str(k).replace('_', ' '))}</dt><dd>{data_html(v)}</dd>" for k, v in value.items()) + "</dl>"
    if isinstance(value, list):
        return "<ul>" + "".join(f"<li>{data_html(v)}</li>" for v in value) + "</ul>" if value else '<span class="muted">None recorded.</span>'
    return escape(str(value)) if value is not None else '<span class="muted">Not recorded.</span>'


class Publisher:
    def __init__(self):
        self.inventory = {}
        self.files = {}
        previous = read_json(OUT / "publication-integrity.json", {})
        self.old = previous.get("files", {})
        self.old_runs = {run["id"]: run for run in previous.get("runs", [])}

    def write(self, rel: str, data: bytes, source: str | None = None):
        path = OUT / rel
        if not path.resolve().is_relative_to(OUT.resolve()):
            raise ValueError(f"Publication path escapes docs/examples: {rel}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        self.inventory[rel] = {"sha256": sha(data), "bytes": len(data), "kind": "snapshot" if source else "generated"}
        if source:
            self.inventory[rel]["source"] = source

    def link(self, current: str, target: str, label: str, fragment: str = "") -> str:
        relative = os.path.relpath(OUT / target, (OUT / current).parent)
        href = quote(relative, safe="/.-_") + ("#" + quote(fragment, safe="-_") if fragment else "")
        return f'<a href="{escape(href, quote=True)}">{escape(label)}</a>'

    def page(self, rel: str, title: str, body: str):
        nav = "".join(self.link(rel, p, t) for p, t in [("index.html", "Example catalog"), ("artifact-guide.html", "How to read the artifacts"), ("files.html", "All published files")])
        css = os.path.relpath(OUT / "style.css", (OUT / rel).parent)
        html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} | Evidence audit examples</title><link rel="stylesheet" href="{escape(css)}"></head><body><header><nav>{nav}</nav></header><main><h1>{escape(title)}</h1>{body}</main><footer>Static study edition · works from file:// · no network or JavaScript required. Sources, audits, and evaluator expectations have different roles.</footer></body></html>'
        self.write(rel, html.encode())

    def snapshot(self, source: Path, prefix: str, exclude=()):
        paths = [source] if source.is_file() else sorted(source.rglob("*"))
        copied = []
        for path in paths:
            sub = Path(path.name) if source.is_file() else path.relative_to(source)
            if not path.is_file() or path.is_symlink() or any(p in SKIP or p in exclude for p in sub.parts) or path.suffix in BINARY_CACHE:
                continue
            raw = f"raw/{prefix}/{sub.as_posix()}"
            data = path.read_bytes()
            source_label = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
            if path.resolve() == (OUT / raw).resolve() and raw in self.old:
                source_label = self.old[raw].get("source", source_label)
            self.write(raw, data, source_label)
            viewer = f"view/{prefix}/{sub.as_posix()}.html"
            self.files[raw] = viewer
            self.viewer(viewer, raw, data)
            copied.append(raw)
        return copied

    def viewer(self, rel: str, raw: str, data: bytes):
        meta = self.inventory[raw]
        body = f'<p>{self.link(rel, raw, "Open / download original bytes")}</p><p class="muted">{escape(meta["source"])} · {len(data):,} bytes · SHA-256 <code>{meta["sha256"]}</code></p>'
        ext = Path(raw).suffix.lower()
        text = None
        if ext in TEXT or not ext:
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                pass
        if text is not None:
            if not data:
                body += '<p class="note">This is an actual zero-byte file. It contains no text, source passage, or quotation. An empty document does not establish that an unrecorded event did not occur.</p>'
            body += '<p>Escaped, verbatim text with line links; the download retains the original bytes.</p><pre>'
            body += "".join(f'<span class="line" id="L{i}"><a class="ln" href="#L{i}">{i}</a>{escape(line)}</span>' for i, line in enumerate(text.splitlines(), 1))
            body += "</pre>"
        elif ext in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".pdf"}:
            src = quote(os.path.relpath(OUT / raw, (OUT / rel).parent), safe="/.-_")
            if ext == ".pdf":
                body += f'<p>Browser-native PDF preview. If unavailable, use the original-byte link above.</p><iframe title="Original PDF" src="{src}"></iframe>'
            else:
                body += f'<img alt="Published original artifact" src="{src}">'
        else:
            body += "<p>Native binary artifact retained unchanged. Download DOCX files for a document viewer, or SQLite files for inspection with a SQLite client. This page does not substitute a transcription for the original.</p>"
        body = '<p class="muted">Published path: <code>' + escape(raw.removeprefix("raw/")) + '</code></p>' + body
        self.page(rel, Path(raw).name, body)

    def artifact_link(self, page: str, raw: str, label: str | None = None):
        if raw not in self.files:
            return f'<span class="muted">{escape(label or raw)} — not supplied in this snapshot</span>'
        return self.link(page, self.files[raw], label or raw)

    def file_table(self, page: str, files: list[str]):
        rows = []
        for raw in sorted(files):
            info = self.inventory[raw]
            rows.append(f'<tr><td data-label="Artifact">{self.artifact_link(page, raw, raw.removeprefix("raw/"))}</td><td data-label="Bytes">{info["bytes"]:,}</td><td data-label="Download">{self.link(page, raw, "Original bytes")}</td></tr>')
        return '<table><thead><tr><th>Artifact / text or native viewer</th><th>Bytes</th><th>Download</th></tr></thead><tbody>' + "".join(rows) + "</tbody></table>"

    def source_table(self, page: str, files: list[str]):
        rows = []
        for raw in sorted(files):
            path = OUT / raw
            if path.stat().st_size == 0:
                description = "Zero-byte source: no textual evidence or quotation exists."
            elif path.suffix.lower() in {".md", ".txt"}:
                lines = [s.strip() for s in path.read_text().splitlines() if s.strip()]
                description = " ".join(lines[:2])[:380]
            elif path.suffix.lower() == ".docx":
                description = "Native DOCX source with structured paragraphs/tables. Compare the run’s extraction and provenance records against these original bytes."
            elif path.suffix.lower() == ".pdf":
                description = "Native PDF source; inspect page layout and the run’s extraction/OCR provenance. Text extraction alone does not resolve uncertain fields."
            else:
                description = "Supplied source artifact; inspect its native format and the run’s provenance records."
            rows.append('<tr><td data-label="Source document">' + self.artifact_link(page, raw, raw.split("/sources/", 1)[-1]) + '</td><td data-label="Description">' + escape(description) + '</td><td data-label="Download">' + self.link(page, raw, "Original bytes") + '</td></tr>')
        return '<table><thead><tr><th>Source document</th><th>Document opening / format and inspection context</th><th>Download</th></tr></thead><tbody>' + "".join(rows) + '</tbody></table>'

    def run(self, run_id: str, source: Path, dossier: str):
        page = f"runs/{run_id}.html"
        prefix = f"runs/{run_id}"
        files = self.snapshot(source, prefix, exclude=("evaluator",))
        registry = read_json(source / "claims.json", {})
        findings = read_json(source / "findings.json", [])
        if isinstance(findings, dict):
            findings = findings.get("findings", [])
        proofs = read_json(source / "proof-results.json", {})
        version = registry.get("schema_version", 1) if isinstance(registry, dict) else 1
        label = "v2 registered audit" if version == 2 else "Legacy v1 audit"
        source_label = str(source.relative_to(ROOT)) if source.is_relative_to(ROOT) else str(source)
        if source.resolve() == (OUT / "raw/runs" / run_id).resolve():
            source_label = self.old_runs.get(run_id, {}).get("source", source_label)
        def link(name, title=None):
            return self.artifact_link(page, f"raw/{prefix}/{name}", title or name)
        body = f'<p>{self.link(page, f"dossiers/{dossier}.html", "Back to dossier and both report variants")}</p><p class="badge">{label}</p>'
        if version != 2:
            body += '<p class="note">Historical legacy v1 bundle. Its executed checks are preserved as historical evidence; this publication does not claim it passed the v2 registration, criteria, or separate argument-audit contract. Missing structured fields remain visibly missing.</p>'
        else:
            body += '<p>Registry schema version 2 is recorded in the supplied claims.json. This label describes the artifact format; inspect execution and independent review separately below.</p>'
        body += f'<p>Snapshot provenance: <code>{escape(source_label)}</code>. {len(findings)} finding records. Recorded proof status: <strong>{escape(str(proofs.get("status", "not supplied")))}</strong>; execution: <strong>{escape(str(proofs.get("execution_status", "not recorded")))}</strong>. No proof execution is performed by this publisher.</p>'
        body += '<p>' + " · ".join(link(n) for n in ["input/report.md", "claims.json", "findings.json", "audit-report.md", "coverage.md", "semantic-review.md", "model-notes.md", "proof-results.json"]) + '</p>'
        body += '<h2>Recorded dispositions</h2>' + data_html({field: dict(Counter(str(f.get(field, "not recorded")) for f in findings)) for field in ["semantic_state", "argument_status", "formal_status"]})
        body += '<p>Conclusion status, quality of the report’s argument, and formal proof status are independent dimensions. “Correct” and “mixed” describe authored report variants, not proof-check results.</p>'
        if dossier.startswith("12-"):
            body += '<p class="note">This empty-evidence case was authored and audited by the coordinator, with independent post-review recorded separately when supplied. It is not a blind audit by its own author.</p>'
        body += '<h2>Finding index</h2><ul>' + "".join(f'<li>{self.link(page, page, str(f.get("claim_id", i)), f"finding-{i}")} — {escape(str(f.get("question", "")))}</li>' for i, f in enumerate(findings, 1)) + '</ul>'
        for i, finding in enumerate(findings, 1):
            body += f'<article id="finding-{i}"><h2>{escape(str(finding.get("claim_id", i)))}</h2><h3>Exact report claim</h3><blockquote>{escape(str(finding.get("report_quote", "Not recorded")))}</blockquote>'
            for field in ["report_anchor", "question", "criteria", "rules", "assumptions", "reasoning", "argument_audit", "support_search", "formalization", "semantic_state", "argument_status", "formal_status", "limits", "recommendation"]:
                body += f'<h3>{escape(field.replace("_", " ").capitalize())}</h3>' + data_html(finding.get(field, "Not present in this supplied record."))
            body += '<h3>Source evidence</h3>'
            if not finding.get("evidence"):
                body += '<p>No quoted source evidence is recorded. Inspect the source snapshot, support-search scope, assumptions and limits; this absence is not itself a refutation.</p>'
            for ev in finding.get("evidence", []):
                body += '<div class="card">' + link(ev.get("path", ""), ev.get("path", "Source")) + data_html(ev) + '</div>'
            body += '<h3>Formal statements and execution records</h3>'
            for proof in finding.get("proofs", []):
                body += '<div class="card">' + data_html(proof)
                module = str(proof.get("module", "Audit")).replace(".", "/")
                body += '<p>' + link(f"models/{module}.lean", "Read Lean model and theorem") + '</p>'
                matched = [t for t in proofs.get("targets", []) if t.get("theorem") == proof.get("theorem") and t.get("module") == proof.get("module")]
                for target in matched:
                    title = "Exact requested target check" if target.get("target") == proof.get("target") and target.get("target") is not None else "Theorem check (inspect its target)"
                    body += f'<details><summary>{title}: {escape(str(target.get("status", "unknown")))}</summary>' + data_html(target)
                    body += '<p>' + " · ".join(link(target[n], n) for n in ["check_file", "log"] if target.get(n)) + '</p></details>'
                if not matched:
                    body += '<p class="note">No corresponding theorem execution record supplied.</p>'
                body += '</div>'
            if not finding.get("proofs"):
                body += '<p>No formal proof reference recorded for this finding. Read the documentary reasoning and its limits.</p>'
            body += '</article>'
        repro = ROOT / "validation/reproduction" / run_id
        if not repro.is_dir():
            repro = OUT / "raw/reproduction" / run_id
        if repro.is_dir():
            rp = read_json(repro / "proof-results.json", {})
            reproduction = self.snapshot(repro, f"reproduction/{run_id}")
            body += '<h2>Separate reproduction snapshot</h2><p>This later recheck is distinct from the original audit and does not upgrade its schema. Recorded status: <strong>' + escape(str(rp.get("status", "not supplied"))) + '</strong>.</p>'
            body += self.file_table(page, reproduction)
        body += '<h2>Complete run artifact browser</h2><p>Includes intermediate artifacts and retained failures, when present. Inputs, proof logs and original export manifests are copied byte for byte; caches are omitted.</p>' + self.file_table(page, files)
        self.page(page, run_id, body)
        return {"id": run_id, "dossier": dossier, "schema_version": version, "findings": len(findings), "proof_status": proofs.get("status", "not supplied"), "execution_status": proofs.get("execution_status", "not recorded"), "source": source_label}

    def dossier(self, source: Path, runs: list[dict]):
        dossier = source.name
        page = f"dossiers/{dossier}.html"
        files = self.snapshot(source, f"dossiers/{dossier}", exclude=("evaluator", "authoring"))
        body = '<p>' + escape(DESCRIPTIONS.get(dossier[:2], "Supplied synthetic report audit dossier.")) + '</p><p class="note">Audit one supplied report against the shared sources. The other report and evaluator expectations are not evidence. Fixture README statements about preparation describe the original input package; executed audit records are linked separately below.</p>'
        body += '<h2>Report variants and actual audit records</h2><div class="grid">'
        for variant, filename in [("mixed", "report.md"), ("correct", "report-correct.md")]:
            body += f'<section class="card"><h3>{variant.capitalize()} supplied report</h3><p>' + self.artifact_link(page, f"raw/dossiers/{dossier}/{filename}", filename) + '</p>'
            related = [r for r in runs if r["dossier"] == dossier and r["id"].endswith("-" + variant)]
            for run in related:
                body += '<p>' + self.link(page, f'runs/{run["id"]}.html', "Open detailed audit, arguments, Lean targets and actual logs") + f'</p><p>{run["findings"]} findings · {"v2" if run["schema_version"] == 2 else "legacy v1"} · recorded proof status: {escape(str(run["proof_status"]))}</p>'
            if not related:
                body += '<p>No audit bundle published for this variant.</p>'
            body += '</section>'
        body += '</div><h2>Source documents</h2><p>Open any file to inspect its text or native original. Run input snapshots retain the exact bytes and extraction state used by that audit; the dossier files below describe the supplied fixture.</p>'
        body += self.source_table(page, [f for f in files if "/sources/" in f])
        body += '<h2>Context and input inventory</h2>' + self.file_table(page, [f for f in files if "/sources/" not in f])
        body += '<p>Authoring masters are excluded: native DOCX/PDF/OCR ingestion must be assessed against the actual source files. A separate review brief is optional; dossier 11 intentionally has none.</p>'
        expectations = source / "evaluator"
        shared = ROOT / "examples/evaluator" / (dossier + ".json")
        if expectations.exists() or shared.exists():
            evaluator = self.snapshot(expectations if expectations.exists() else shared, f"evaluator/{dossier}")
            ep = f"evaluator/{dossier}.html"
            self.page(ep, dossier + " — evaluator-only study reference", '<p class="note">Read only after completing an independent audit. These are editorial design expectations, not source evidence, proof results, or a certified truth oracle. They were not included in the published run input snapshots.</p>' + self.file_table(ep, evaluator))
            body += '<h2>After-audit study reference</h2><p>' + self.link(page, ep, "Evaluator-only expectations — do not give to blind auditors") + '</p>'
        self.page(page, dossier, body)

    def finish(self, runs: list[dict], extras: list[str]):
        self.page("files.html", "Published file browser", '<p>All snapshots are downloadable as original bytes. Text viewers escape embedded markup. Evaluator files are separately labeled and are never audit evidence.</p>' + self.file_table("files.html", list(self.files)))
        command = "python validation/publish_examples.py" + "".join(" --extra-run " + arg.split("=", 1)[0] + "=docs/examples/raw/runs/" + arg.split("=", 1)[0] for arg in extras)
        self.write("README.md", ("# Offline example catalog\n\nOpen `index.html` directly in a browser. No web server, network, JavaScript, or fetch is needed.\n\nRegenerate from the repository root after cloning, without the original temporary workspaces:\n\n```sh\npython validation/publish_examples.py\npython validation/publish_examples.py --check\n```\n\nThe generator automatically reuses additional runs listed in the previous publication inventory from their committed `raw/runs/` snapshots. An equivalent explicit command is:\n\n```sh\n" + command + "\n```\n\nTo refresh a snapshot from a retained workspace, pass `--extra-run ID=tmp/WORKSPACE` for each additional run to include. Original workspace provenance is preserved when rebuilding from the published snapshots.\n\n`raw/` contains byte-preserving snapshots; `view/` provides escaped text or native previews. `publication-integrity.json` records source paths and SHA-256 hashes. Original manifests are preserved unchanged. The publication inventory excludes itself to avoid a recursive hash. Native document originals, SQLite indexes, and proof logs are retained; toolchain/build caches, symlinks and fixture authoring masters are excluded. Evaluator expectations are in a separate after-audit study area.\n\nThis generator reports stored results and never executes Lean, re-audits a claim, or declares a legacy bundle compliant with v2. Running the same command against unchanged inputs produces the same files. Working directories under `tmp/` are not changed or deleted.\n").encode())
        # Remove only stale files from this generator's previous inventory.
        for rel in self.old.keys() - self.inventory.keys():
            path = OUT / rel
            if path.resolve().is_relative_to(OUT.resolve()) and path.is_file():
                path.unlink()
        inventory = {"schema_version": 1, "algorithm": "sha256", "scope": "All generated pages and published snapshots except this self-referential inventory", "generator": "validation/publish_examples.py", "command": command, "runs": runs, "files": self.inventory}
        (OUT / "publication-integrity.json").write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n")


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.links.append(value)
            if key == "id":
                self.ids.add(value)


def check_site():
    manifest = read_json(OUT / "publication-integrity.json", {})
    errors = []
    pages = {}
    for rel, entry in manifest.get("files", {}).items():
        path = OUT / rel
        if not path.resolve().is_relative_to(OUT.resolve()):
            errors.append(f"Escaping inventory path: {rel}")
            continue
        if not path.exists() or sha(path.read_bytes()) != entry["sha256"]:
            errors.append(f"Missing or changed published file: {rel}")
        if entry["kind"] == "generated" and path.suffix == ".html" and path.exists():
            parser = Links()
            parser.feed(path.read_text())
            pages[path.resolve()] = parser
    links = 0
    for path, parser in pages.items():
        for value in parser.links:
            links += 1
            url = urlsplit(value)
            if url.scheme or url.netloc:
                errors.append(f"Unexpected external dependency: {value}")
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(OUT.resolve()) or not target.is_file():
                errors.append(f"Broken or escaping link: {path.relative_to(OUT)} -> {value}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"Missing fragment: {path.relative_to(OUT)} -> {value}")
    if not manifest.get("files"):
        errors.append("Publication inventory is missing or empty")
    result = {"status": "passed" if not errors else "failed", "files": len(manifest.get("files", {})), "bytes": sum(e["bytes"] for e in manifest.get("files", {}).values()), "html_pages": len(pages), "local_links_checked": links, "errors": errors}
    print(json.dumps(result, indent=2))
    if errors:
        raise SystemExit(1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--extra-run", action="append", default=[], metavar="ID=PATH", help="Additional run; ID must start with the dossier name and end in -mixed or -correct")
    parser.add_argument("--check", action="store_true", help="Verify publication hashes, offline links and fragments without regenerating")
    args = parser.parse_args()
    if args.check:
        check_site()
        return
    dossiers = sorted(p for p in (ROOT / "examples").glob("[0-9][0-9]-*") if p.is_dir())
    sources = {p.name: p for p in sorted((ROOT / "validation/runs").iterdir()) if p.is_dir()}
    if not args.extra_run:
        previous = read_json(OUT / "publication-integrity.json", {})
        for run in previous.get("runs", []):
            if run["id"] not in sources:
                published = OUT / "raw/runs" / run["id"]
                if published.is_dir():
                    args.extra_run.append(run["id"] + "=" + str(published))
    for spec in args.extra_run:
        name, sep, value = spec.partition("=")
        if not sep or not re.fullmatch(r"[a-zA-Z0-9_-]+", name):
            parser.error("Extra runs require a safe ID=PATH")
        path = Path(value).expanduser().resolve()
        if name in sources or not path.is_dir():
            parser.error(f"Duplicate run ID or missing run directory: {name}")
        sources[name] = path
    assignments = {}
    for name in sources:
        matches = [d.name for d in dossiers if name.startswith(d.name + "-") and name.endswith(("-mixed", "-correct"))]
        if len(matches) != 1:
            parser.error(f"Cannot assign run to dossier and report variant: {name}")
        assignments[name] = matches[0]
    pub = Publisher()
    pub.write("style.css", CSS.encode())
    runs = [pub.run(name, source, assignments[name]) for name, source in sources.items()]
    for dossier in dossiers:
        pub.dossier(dossier, runs)
    guide = '<p>The product audits findings in supplied reports against supplied documents. It does not generate the original substantive report. Read the claim, decision criteria, source evidence, applicable rules, assumptions, reasoning, and limits together.</p>'
    for title, paths, establishes, limits in ARTIFACTS:
        guide += f'<section class="card"><h2>{escape(title)}</h2><p><code>{escape(paths)}</code></p><p>{escape(establishes)}</p><p class="note">{escape(limits)}</p></section>'
    guide += '<h2>Publication integrity and omissions</h2><p>' + pub.link("artifact-guide.html", "publication-integrity.json", "Publication SHA-256 inventory") + ' records every snapshot source and every generated file. Original audit/export manifests are retained untouched. A publication hash establishes byte identity with the copied artifact; it is not a new audit or proof check. Toolchain binaries, build caches, symlinks, and fixture authoring masters are excluded. Native originals and intermediate indexes are retained.</p><h2>Missing and partial coverage</h2><p>Only artifacts present in the supplied bundles are shown. No missing criterion, argument audit, provenance coordinate, proof, review, or failed attempt is reconstructed as though it had been executed. Legacy results and fresh rechecks remain separately labeled. Evaluator expectations are available only in the explicitly marked study area.</p>'
    pub.page("artifact-guide.html", "How to read an evidence-backed audit", guide)
    cards = []
    for dossier in dossiers:
        related = [r for r in runs if r["dossier"] == dossier.name]
        cards.append('<section class="card"><h2>' + pub.link("index.html", f"dossiers/{dossier.name}.html", dossier.name) + '</h2><p>' + escape(DESCRIPTIONS.get(dossier.name[:2], "")) + f'</p><p>{len(related)} separate report audits · {sum(r["findings"] for r in related)} recorded findings</p></section>')
    body = f'<p>Explore {len(dossiers)} synthetic dossiers and {len(runs)} separately supplied report audits: the source documents, exact claims, intermediate decisions, Lean code, and actual saved proof logs. Each dossier pairs a deliberately mixed report with a cautious report intended to be correct.</p><p class="note">The first ten dossiers retain legacy v1 audit bundles. Dossier 11 exercises v2 registration, inferred criteria, and separate audits of report arguments and conclusions without a separate brief. Dossier 12 tests an empty evidence file; it is coordinator-authored and audited, not blind, with independent post-review recorded separately. A proof passing does not certify source authenticity, extraction accuracy, or model adequacy.</p><p>Start with a dossier, choose one report variant, then follow its detailed findings to source snapshots and exact target logs. Missing arguments can be valuable support-gap findings without establishing that a conclusion is false.</p><div class="grid">' + "".join(cards) + '</div><h2>Offline inspection and reproducibility</h2><p>Every link stays inside this published catalog. HTML contains all displayed data; no fetch, server, network, or JavaScript is needed. PDFs and images use the browser’s native viewer, while DOCX and SQLite files can be downloaded unchanged.</p><p>' + pub.link("index.html", "README.md", "Regeneration instructions") + ' · ' + pub.link("index.html", "publication-integrity.json", "Publication integrity inventory") + '</p>'
    pub.page("index.html", "Evidence audit example catalog", body)
    pub.finish(runs, args.extra_run)
    check_site()


if __name__ == "__main__":
    main()
