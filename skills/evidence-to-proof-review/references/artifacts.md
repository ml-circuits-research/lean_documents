# Runtime artifacts

The following contract is used by `scripts/audit.py`. All paths in evidence are relative to the workspace. Every finding has these fields:

```json
{
  "claim_id": "R-01",
  "report_quote": "Exact finding text from the selected report.",
  "report_anchor": "R-01",
  "question": "Does the finite table contradict the claimed total?",
  "evidence": [{"path": "input/sources/ledger.md", "anchor": "L-02", "quote": "An exact substring of that anchored passage."}],
  "rules": ["Sum each in-scope amount once."],
  "assumptions": ["The transcribed rows faithfully represent the cited table."],
  "reasoning": ["List the values.", "Compute their sum.", "Compare with the original claim."],
  "semantic_state": "refuted",
  "argument_status": "invalid_inference",
  "formal_status": "refuted",
  "proofs": [{"module": "Audit", "theorem": "Audit.claimFalse", "relation": "refutes", "target": "(120 + 80 : Nat) ≠ 210"}],
  "limits": ["The calculation does not authenticate the underlying entries."],
  "recommendation": "Correct the claimed total to 200."
}
```

`findings.json` is an array of these records. This example is a schema illustration, not a completed audit or proof. `proofs` must be empty when no proof was run. A planned proof reference may be authored before checking, but must not be delivered as verified until the check succeeds. `assumptions` may be empty; other explanatory lists must contain meaningful content. Under v2, evidence may be empty when accompanied by the required bounded search; never add irrelevant evidence to fill this field. Rules can state that no operational criterion was provided for an aesthetic assessment.

Required run artifacts beyond findings:

- `manifest.json`: immutable input paths and SHA-256 digests.
- `source-ledger.jsonl`: extracted anchored passages; supplement with attribution, uncertainty and temporal records as needed.
- `claims.json`: original material claim register and review coverage; add explicit exclusions rather than silently dropping claims.
- `review-plan.md`: verification questions, search boundaries, method and budget.
- `models/*.lean` and `model-notes.md`: checked model sources and their interpretation.
- `proof-results.json` and `logs/`: actual command outcomes, target checks, axiom audits and version.
- `semantic-review.md`: independent correspondence review, disagreements, corrections and limitations.
- `audit-report.md` and `coverage.md`: human output and scope.

The helper validates literal quote/anchor correspondence and formal artifacts. It cannot validate that a quotation semantically entails an interpretation. The agent and reviewer must do that work and disclose any limitation.

New workspaces additionally enforce [contract v2](audit-contract-v2.md): criteria, structured report-argument audit, formalization correspondence and a reconciled claims registry. This page describes the shared base format; legacy bundles retain their older requirements.

Export of v2 runs requires nonempty review-plan.md and semantic-review.md, plus model-notes.md when models exist. Final review notes and any independent-review.md must be present before the final check. These files are hashed with the checked inputs; writing them afterward requires rechecking.
