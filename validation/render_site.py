#!/usr/bin/env python3
"""Render human-readable HTML from completed, exported audit records."""
from collections import Counter
from html import escape as e
import json
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent
DOCS = BASE.parent / 'docs'


def page(title, content, nested=False):
    prefix = '../' if nested else ''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(title)} · Evidence-to-Proof Review</title><link rel="stylesheet" href="{prefix}assets/style.css"></head><body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="{prefix}index.html">Evidence-to-Proof Review</a><p>Executed validation · Lean 4.24.0 · 4 November 2026</p><nav aria-label="Validation navigation"><a href="{prefix}validation.html">Validation results</a><a href="{prefix}verification.html">Argument contract</a><a href="{prefix}implementation.html">Implementation plan</a></nav></header><main id="main">{content}</main><footer>Technical proof checks and documentary interpretation are separate assurance layers.</footer></body></html>'''


def main():
    summary = json.loads((BASE / 'summary.json').read_text())
    (DOCS / 'audits').mkdir(exist_ok=True)
    rows = []
    totals = Counter()
    for result in summary['runs']:
        run_id = result['run_id']
        run = BASE / 'runs' / run_id
        findings = json.loads((run / 'findings.json').read_text())
        index = sqlite3.connect(f'file:{run / "input/index.sqlite3"}?mode=ro', uri=True) if (run / 'input/index.sqlite3').exists() else None
        prefix = '../../validation/runs/' + run_id + '/'
        body = f'<p class="eyebrow">Executed claim audit</p><h1>{e(run_id)}</h1>'
        body += '<div class="note"><p>Formal results hold in the documented model under its transcription and interpretation assumptions. Documentary support is not a Lean proof. Auxiliary proofs do not certify the underlying event claim.</p></div>'
        body += f'<p><a href="{prefix}audit-report.md">Markdown audit</a> · <a href="{prefix}model-notes.md">Model interpretation</a> · <a href="{prefix}semantic-review.md">Semantic review</a> · <a href="{prefix}proof-results.json">Executed proof results</a> · <a href="{prefix}coverage.md">Coverage</a></p>'
        body += '<p>Claims: ' + ' · '.join(f'<a href="#{e(f["claim_id"])}">{e(f["claim_id"])}</a>' for f in findings) + '</p>'
        for f in findings:
            totals[f['formal_status']] += 1
            body += f'<article class="card" id="{e(f["claim_id"])}"><h2>{e(f["claim_id"])}</h2><p><span class="tag">Evidence: {e(f["semantic_state"])}</span> <span class="tag">Argument: {e(f["argument_status"])}</span> <span class="tag">Formal: {e(f["formal_status"])}</span></p>'
            body += f'<h3>Exact report claim</h3><blockquote>{e(f["report_quote"])}</blockquote><p>Report anchor: {e(f["report_anchor"])}</p><h3>Verification problem</h3><p>{e(f["question"])}</p><h3>Evidence used</h3>'
            for evidence in f['evidence']:
                body += f'<p><a href="{prefix}{e(evidence["path"])}">{e(evidence["path"])}</a> · {e(evidence["anchor"])}</p><blockquote><pre>{e(evidence["quote"])}</pre></blockquote>'
                if index:
                    segment = index.execute('SELECT locator,method,uncertainty FROM segments WHERE path=? AND anchor=?', (evidence['path'], evidence['anchor'])).fetchone()
                    locator = json.loads(segment[0]); compact = {k:v for k,v in locator.items() if k != 'words'}
                    body += f'<p><a href="{prefix}{e(locator["original"])}">Original source</a> · Extraction: {e(segment[1])}</p><details><summary>Original coordinates and extraction limits</summary><pre>{e(json.dumps(compact, indent=2))}</pre><p>{e("; ".join(json.loads(segment[2])))}</p></details>'
            for key in ('rules', 'assumptions', 'reasoning', 'limits'):
                body += f'<h3>{key.capitalize()}</h3>'
                tag = 'ol' if key == 'reasoning' else 'ul'
                body += f'<{tag}>' + ''.join(f'<li>{e(item)}</li>' for item in f[key]) + f'</{tag}>' if f[key] else '<p>None stated.</p>'
            body += '<h3>Formal evidence</h3>'
            if not f['proofs']: body += '<p>No formal proof is claimed for this finding.</p>'
            for proof in f['proofs']:
                body += f'<p><a href="{prefix}models/{e(proof["module"])}.lean">{e(proof["theorem"])}</a> — {e(proof["relation"])}</p><pre>{e(proof["target"])}</pre>'
            body += f'<h3>Recommended correction or next evidence</h3><p>{e(f["recommendation"])}</p></article>'
        if index: index.close()
        (DOCS / 'audits' / (run_id + '.html')).write_text(page(run_id, body, True))
        states = ', '.join(f'{k}: {v}' for k, v in result['semantic_counts'].items())
        rows.append(f'<tr><td><a href="audits/{e(run_id)}.html">{e(run_id)}</a></td><td>{result["matched_claims"]}/{result["expected_claims"]}</td><td>{result["audited_atomic_findings"]}</td><td>{result["checked_theorems"]}</td><td>{e(states)}</td></tr>')
    run_count = len(summary['runs'])
    dossier_count = len({r['run_id'].rsplit('-',1)[0] for r in summary['runs']})
    body = f'<p class="eyebrow">Implementation and executed validation</p><h1>{dossier_count} dossiers, {run_count} actual audits</h1>'
    body += f'<p class="lead">{summary["total_expected_claims"]} original report findings were assessed as {summary["total_atomic_findings"]} atomic findings. {summary["total_matched_claims"]} original findings agree with the separate editorial expectations. {summary["total_checked_theorems"]} theorem declarations were checked across the {run_count} separate run bundles.</p>'
    body += '<div class="note"><p>These are results on a small synthetic regression set. Agreement with editorial expectations is not a statistical reliability estimate or independent expert certification. Every formal result depends on its explicit source transcription and model interpretation.</p></div>'
    body += '<p>The final suite includes one transparent correction to a supplied report: its original ambiguous wording produced an appropriate unresolved finding (initial extended comparison: 155/156). A new report revision was fully reviewed and rechecked. <a href="../validation/extended/fixture-corrections/09-report-wording/correction.json">Old/new hashes and reconciliation</a> · <a href="../validation/extended/fixture-corrections/09-report-wording/original-audit/audit-report.md">Original disputed audit</a>.</p>'
    body += '<h2>Read the actual arguments</h2><div class="table-wrap"><table><thead><tr><th>Audit</th><th>Expectation agreement</th><th>Atomic findings</th><th>Checked theorems</th><th>Documentary outcomes</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div>'
    body += '<h2>Formal coverage, not blanket certification</h2><ul>' + ''.join(f'<li>{e(k)}: {v} atomic findings</li>' for k, v in sorted(totals.items())) + '</ul>'
    body += '<p>Theorem counts include direct and auxiliary results. The same theorem can support multiple related atomic findings, and a compound finding can require several results. Auxiliary proofs show facts such as a missing inference or contradictory testimony; they do not settle an unknown event.</p>'
    body += '<h2>Implemented capabilities</h2><p>The <a href="../skills/evidence-to-proof-review/SKILL.md">skill</a> directs claim extraction, documentary argumentation, model selection, semantic review and honest delivery. The Python helper prepares temporary workspaces, preserves source hashes and anchors, checks exact quotations, builds explicit Lean modules, checks theorem target types and axioms, rejects stale artifacts, renders audits and exports reproducible bundles. Its indexed engine also handles native DOCX, PDF and OCR, original coordinates and uncertainty, resumable processing and changed-source invalidation. Semantic interpretation remains agent work. See <a href="extensions.html">formats and scale</a>.</p>'
    body += '<h2>Validation method and independence</h2><p>Each selected report was audited in its own temporary workspace. Initial auditing agents were instructed not to access expected answers, alternate reports or prior reviews. Some agents were reused for unrelated dossiers due to the session thread limit; no agent audited both variants of the same dossier or a dossier whose expected answers it had authored. Shared filesystem access was not a security boundary. The coordinator reviewed source-to-model correspondence and was familiar with fixture design. The independent review record describes additional checks and any corrections.</p>'
    body += '<p><a href="../validation/summary.json">Claim-level comparison</a> · <a href="../validation/reproduction.json">Fresh-workspace reproduction results</a> · <a href="../validation/review.md">Independent review and reconciliation</a> · <a href="../tests/validation.log">Behavioral test log</a> · <a href="../validation/toolchain.json">Pinned toolchain provenance</a></p>'
    body += '<h2>Limits</h2><p>A compatible lean4checker was built and actually used for selected fresh environment replays; per-run proof results distinguish passed replay from not run. It uses the same Lean kernel, not an independent kernel implementation. Source authenticity and interpretation are not established by Lean. Calendar offsets are cross-checked against Gregorian calculations outside Lean. Native adapters and a 1,000-source ingestion benchmark were exercised; OCR corrections are attributed review actions, not machine-certified fidelity. Source-code filters are defensive checks, not a sandbox for hostile Lean programs. The historical preparation-only fixture briefs are superseded for these runs by the user’s later execution authorization, recorded separately in every workspace.</p>'
    body += '<p><a href="../validation/extended/scale.json">Executed scale benchmark</a> · <a href="../validation/extended/portability.json">Portable-package smoke test</a> · <a href="../validation/checker-toolchain.json">Optional checker provenance and actual replay</a></p><p><a href="../validation/extended/semantic-review/review.json">Extended independent semantic review</a> · <a href="../validation/extended/code-review/review.md">Implementation review and repaired defects</a> · <a href="../validation/extended/invalidation.json">Changed-source negative control</a>. All 91 implementation and regression tests passed.</p><p><a href="../validation/reproduction-06-procurement-contract-mixed.json">Fresh-workspace reproduction with optional checker</a> passed on the final exported procurement audit.</p><h2>Use and reproduce</h2><p>Give a coding agent the skill path, report, review brief and source locations. The skill creates a new temporary workspace for each request. See <a href="../validation/README.md">reproduction instructions</a> for commands and interpretation of the exported evidence.</p>'
    (DOCS / 'validation.html').write_text(page('Validation results', body))


if __name__ == '__main__': main()
