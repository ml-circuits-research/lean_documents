"""V2 declarations for explicitly authored synthetic unit fixtures only.

This is not a semantic migration tool. Callers supply every audited finding,
heading classification and deferred claim. Unknown report anchors fail instead
of being silently classified or omitted.
"""
import hashlib
import json


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')


def annotate_synthetic_finding(finding):
    """Annotate statement-only test reports with their known missing argument."""
    evidence_refs = list(range(len(finding['evidence'])))
    proof_refs = list(range(len(finding['proofs'])))
    finding['criteria'] = {
        'origin': 'inferred',
        'operational_question': finding['question'],
        'decision_criteria': list(finding['rules']),
        'scope': 'Only the explicitly authored synthetic fixture statement and supplied source passages.',
        'missing_definitions': [],
        'alternatives': [],
    }
    finding['argument_audit'] = {
        'outcome': 'not_provided',
        'report_items': [],
        'independent_reasoning': list(finding['reasoning']),
        'evidence_refs': evidence_refs,
        'proof_refs': proof_refs,
        'claim_dependencies': [],
    }
    finding['formalization'] = {
        'rationale': 'The fixture uses an arithmetic target when a proof is supplied; documentary checks require no Lean target.',
        'correspondence': [
            {'proof_ref': index,
             'explanation': 'The declared fixture target checks the arithmetic named in the verification question; source accuracy remains an assumption.'}
            for index in proof_refs
        ],
    }
    inspected = [{'path': item['path'], 'anchor': item['anchor']}
                 for item in finding['evidence'] if item['path'].startswith('input/sources/')]
    finding['support_search'] = {
        'scope': 'The explicitly cited synthetic source passages were inspected when constructing this test fixture.',
        'queries': [],
        'inspected': inspected,
        'limitations': ['No exhaustive corpus search or real-world source authentication is asserted by this unit fixture.'],
        'conclusion': 'Independent fixture evidence is assessed separately; the report statement supplies no derivation.',
    }
    if not inspected:
        finding['support_search']['uninspected_reason'] = 'This negative-control fixture intentionally supplies no valid independent source passage.'
    return finding


def register_synthetic_report(root, findings, *, non_claim_anchors=None, deferred=()):
    """Register supplied fixture declarations before any deliberate mutation."""
    non_claim_anchors = non_claim_anchors or {}
    report = json.loads((root / 'input/report-ledger.json').read_text())
    claims = [{key: finding[key] for key in ('claim_id', 'report_anchor', 'report_quote')}
              | {'disposition': 'audited'} for finding in findings]
    claims.extend(dict(claim, disposition='deferred') for claim in deferred)
    claim_anchors = {claim['report_anchor'] for claim in claims}
    if set(non_claim_anchors) & claim_anchors:
        raise AssertionError('Synthetic heading and claim declarations overlap')
    if set(non_claim_anchors) | claim_anchors != set(report):
        raise AssertionError('Every synthetic report anchor requires an explicit fixture declaration')
    for claim in claims:
        if claim['report_quote'] not in report[claim['report_anchor']]:
            raise AssertionError('Fixture claim must match report before negative-test mutation')
    anchors = [
        {'report_anchor': anchor,
         'report_sha256': hashlib.sha256(quote.encode()).hexdigest(),
         'classification': 'non_claim' if anchor in non_claim_anchors else 'claims',
         'reason': non_claim_anchors.get(anchor, 'This synthetic paragraph contains the explicitly registered fixture claim.')}
        for anchor, quote in report.items()
    ]
    write(root / 'claims.json', {'schema_version': 2, 'anchors': anchors, 'claims': claims})
