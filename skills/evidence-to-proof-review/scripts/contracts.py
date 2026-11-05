"""Mechanical v2 claim registration and argument-audit contract.

See ../references/audit-contract-v2.md for an editable JSON example. Callers must
verify the immutable input manifest before using this module and separately check
Lean execution, source fidelity, and the semantic adequacy of the audit.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

CAVEAT = ('Registration reconciles declared claims and reviewed report anchors; '
          'it does not establish semantic completeness, faithful decomposition, '
          'or that declared searches were actually performed.')
OUTCOMES = {'sufficient', 'insufficient', 'invalid', 'unsound', 'disputed', 'nonformal', 'not_provided'}
ASSESSMENTS = {'verified', 'unsupported', 'contradicted', 'disputed', 'nonformal'}


def _read(path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        raise ValueError(f'Cannot read {path}: {exc}') from exc


def _text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label} must be a nonempty string')
    return value


def _object(value, label):
    if not isinstance(value, dict):
        raise ValueError(f'{label} must be an object')
    return value


def _list(value, label, nonempty=False):
    if not isinstance(value, list) or (nonempty and not value):
        raise ValueError(f'{label} must be a {"nonempty " if nonempty else ""}list')
    return value


def _strings(value, label, nonempty=False):
    for item in _list(value, label, nonempty):
        _text(item, label)
    return value


def _hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def _choice(value, choices):
    return isinstance(value, str) and value in choices


def initialize(root):
    """Seed/sync editable claims.json, preserving reviews for unchanged anchors.

    Changed anchors become pending; claims remain for explicit reconciliation.
    Removed anchor reviews are retained in retired_anchors. Returns the registry.
    """
    root = Path(root)
    report = _object(_read(root / 'input/report-ledger.json'), 'report ledger')
    path = root / 'claims.json'
    data = _read(path) if path.exists() else {'schema_version': 2, 'anchors': [], 'claims': []}
    _object(data, 'claims registry')
    if data.get('schema_version') != 2:
        raise ValueError('claims.json schema_version must be 2')
    old = {}
    for row in _list(data.get('anchors'), 'anchors'):
        _object(row, 'anchor classification')
        anchor = _text(row.get('report_anchor'), 'report_anchor')
        if anchor in old:
            raise ValueError(f'Duplicate anchor classification: {anchor}')
        old[anchor] = row
    anchors = []
    for anchor, quote in report.items():
        fingerprint = _hash(_text(quote, f'report {anchor}'))
        row = old.pop(anchor, None)
        if row is None or row.get('report_sha256') != fingerprint:
            replacement = {'report_anchor': anchor, 'report_sha256': fingerprint,
                           'classification': 'pending', 'reason': ''}
            if row is not None:
                replacement['previous_review'] = row
            row = replacement
        anchors.append(row)
    data['anchors'] = anchors
    if old:
        data.setdefault('retired_anchors', []).extend(old.values())
    _list(data.get('claims'), 'claims')
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return data


def _refs(value, size, label):
    refs = _list(value, label)
    seen = set()
    for ref in refs:
        if type(ref) is not int or ref < 0 or ref >= size or ref in seen:
            raise ValueError(f'{label}: invalid or duplicate reference {ref!r}')
        seen.add(ref)
    return refs


def _report_quote(item, report, label):
    anchor = _text(item.get('report_anchor'), label + '.report_anchor')
    quote = _text(item.get('report_quote'), label + '.report_quote')
    if anchor not in report or quote not in report[anchor]:
        raise ValueError(f'{label}: report quote does not match anchored report text')
    return anchor, quote


def _lookup(root, callback):
    blocked = set()
    if (root / 'input/index.sqlite3').is_file():
        import corpus
        docs = corpus.inventory(root)
        report_hashes = {d['original_sha'] for d in docs if d['role'] == 'report'}
        blocked = {d['logical'] for d in docs if d['role'] == 'source' and d['original_sha'] in report_hashes}
        resolve = callback or (lambda path, anchor: corpus.passage(root, path, anchor))
    else:
        ledger = _read(root / 'input/source-ledger.json')
        resolve = callback or (lambda path, anchor: ledger.get(path, {}).get(anchor))
        manifest_path = root / 'input/manifest.json'
        if manifest_path.is_file():
            files = _read(manifest_path)['files']
            report_hash = files.get('input/report.md', {}).get('sha256')
            if report_hash:
                blocked = {path for path, info in files.items()
                           if path.startswith('input/sources/') and info.get('sha256') == report_hash}
    def independent(path, anchor):
        if path in blocked:
            raise ValueError('A byte-identical copy of the report cannot serve as independent source evidence: ' + path)
        return resolve(path, anchor)
    return independent


def _source(item, lookup, label, quote_required=False):
    _object(item, label)
    path = _text(item.get('path'), label + '.path')
    anchor = _text(item.get('anchor'), label + '.anchor')
    if Path(path).is_absolute() or '..' in Path(path).parts:
        raise ValueError(f'{label}: unsafe source path')
    if not path.startswith('input/sources/'):
        raise ValueError(f'{label}: independent source evidence must come from input/sources/, not the report or brief')
    passage = lookup(path, anchor)
    text = passage.get('quote') if isinstance(passage, dict) else passage
    if not isinstance(text, str) or not text:
        raise ValueError(f'{label}: unknown source passage {path}#{anchor}')
    if quote_required:
        quote = _text(item.get('quote'), label + '.quote')
        if quote not in text:
            raise ValueError(f'{label}: source quote does not match anchored source text')


def validate(root, findings, source_lookup=None):
    """Validate v2 declarations; return coverage counts or raise ValueError.

    Optional source_lookup(path, anchor) returns passage text, a dict containing
    quote, or None. It must resolve only supplied, validated source passages.
    Findings' base fields and actual proof execution remain the caller's duty.
    """
    root = Path(root)
    policy_path = root / 'input/audit-policy.json'
    require_traces = _read(policy_path).get('require_claim_traces', False) if policy_path.is_file() else False
    report = _object(_read(root / 'input/report-ledger.json'), 'report ledger')
    registry = _object(_read(root / 'claims.json'), 'claims registry')
    if registry.get('schema_version') != 2:
        raise ValueError('claims.json schema_version must be 2')
    classifications = {}
    for row in _list(registry.get('anchors'), 'anchors'):
        _object(row, 'anchor classification')
        anchor = _text(row.get('report_anchor'), 'report_anchor')
        if anchor in classifications:
            raise ValueError(f'Duplicate anchor classification: {anchor}')
        if anchor not in report:
            raise ValueError(f'Unknown report anchor: {anchor}')
        if row.get('report_sha256') != _hash(report[anchor]):
            raise ValueError(f'{anchor}: report changed; initialize and review again')
        if not _choice(row.get('classification'), {'claims', 'non_claim'}):
            raise ValueError(f'{anchor}: classification is pending or invalid')
        _text(row.get('reason'), f'{anchor}.reason')
        classifications[anchor] = row['classification']
    if set(classifications) != set(report):
        raise ValueError('Every report anchor must have one reviewed classification')
    registered, by_anchor = {}, {anchor: [] for anchor in report}
    for claim in _list(registry.get('claims'), 'claims'):
        _object(claim, 'registered claim')
        ident = _text(claim.get('claim_id'), 'claim_id')
        if ident in registered:
            raise ValueError(f'Duplicate registered claim_id: {ident}')
        anchor, _ = _report_quote(claim, report, ident)
        if classifications[anchor] != 'claims':
            raise ValueError(f'{ident}: claim assigned to a non_claim anchor')
        if not _choice(claim.get('disposition'), {'audited', 'deferred'}):
            raise ValueError(f'{ident}: disposition must be audited or deferred')
        if claim['disposition'] == 'deferred':
            _text(claim.get('reason'), f'{ident}.deferred reason')
        registered[ident] = claim
        by_anchor[anchor].append(ident)
    for anchor, classification in classifications.items():
        if classification == 'claims' and not by_anchor[anchor]:
            raise ValueError(f'{anchor}: claims classification has no registered claims')
    submitted = {}
    for finding in _list(findings, 'findings'):
        _object(finding, 'finding')
        ident = _text(finding.get('claim_id'), 'finding.claim_id')
        if require_traces or 'executive_summary' in finding:
            summary = _object(finding.get('executive_summary'), f'{ident}.executive_summary')
            for field in ('conclusion', 'how_verified', 'limits'):
                _text(summary.get(field), f'{ident}.executive_summary.{field}')
        if ident in submitted:
            raise ValueError(f'Duplicate finding claim_id: {ident}')
        if ident not in registered:
            raise ValueError(f'Unknown finding claim_id: {ident}')
        claim = registered[ident]
        if claim['disposition'] != 'audited':
            raise ValueError(f'{ident}: deferred claim cannot have a finding')
        if any(finding.get(key) != claim[key] for key in ('report_anchor', 'report_quote')):
            raise ValueError(f'{ident}: finding altered registered claim quote or anchor')
        submitted[ident] = finding
    expected = {key for key, claim in registered.items() if claim['disposition'] == 'audited'}
    if set(submitted) != expected:
        raise ValueError('Audited registered claims missing findings: ' + ', '.join(sorted(expected - set(submitted))))
    lookup = _lookup(root, source_lookup) if submitted else None
    dependencies = {}
    for ident, finding in submitted.items():
        criteria = _object(finding.get('criteria'), ident + '.criteria')
        if not _choice(criteria.get('origin'), {'inferred', 'provided', 'source'}):
            raise ValueError(f'{ident}: invalid criteria origin')
        for key in ('operational_question', 'scope'):
            _text(criteria.get(key), f'{ident}.criteria.{key}')
        _strings(criteria.get('decision_criteria'), ident + '.criteria.decision_criteria', True)
        for key in ('missing_definitions', 'alternatives'):
            _strings(criteria.get(key), f'{ident}.criteria.{key}')
        evidence = _list(finding.get('evidence'), ident + '.evidence')
        proofs = _list(finding.get('proofs'), ident + '.proofs')
        if not evidence and finding.get('semantic_state') in {'supported', 'refuted', 'both'}:
            direct = {'supported': 'proved', 'refuted': 'refuted'}.get(finding['semantic_state'])
            if not direct or finding.get('formal_status') != direct or not proofs:
                raise ValueError(f'{ident}: a substantive positive/negative verdict requires source evidence or a direct checked proof; an empty search is insufficient')
        for item in evidence:
            _source(item, lookup, ident + '.evidence', True)
        argument = _object(finding.get('argument_audit'), ident + '.argument_audit')
        outcome = argument.get('outcome')
        if not _choice(outcome, OUTCOMES):
            raise ValueError(f'{ident}: invalid report argument outcome')
        expected_status = {'insufficient': 'insufficient_support', 'invalid': 'invalid_inference',
                           'unsound': 'unsound_argument', 'not_provided': 'insufficient_support'}.get(outcome, outcome)
        if finding.get('argument_status') != expected_status:
            raise ValueError(f'{ident}: argument_status disagrees with report argument outcome')
        _strings(argument.get('independent_reasoning'), ident + '.argument_audit.independent_reasoning', True)
        _refs(argument.get('evidence_refs'), len(evidence), ident + '.argument_audit.evidence_refs')
        _refs(argument.get('proof_refs'), len(proofs), ident + '.argument_audit.proof_refs')
        items = _list(argument.get('report_items'), ident + '.argument_audit.report_items')
        if outcome == 'not_provided' and items:
            raise ValueError(f'{ident}: not_provided argument cannot contain report justification items')
        if outcome != 'not_provided' and not items:
            raise ValueError(f'{ident}: report argument requires quoted report items or not_provided outcome')
        for item in items:
            _object(item, ident + '.report item')
            if not _choice(item.get('kind'), {'premise', 'citation', 'inference'}) or not _choice(item.get('assessment'), ASSESSMENTS):
                raise ValueError(f'{ident}: invalid report argument item kind/assessment')
            _report_quote(item, report, ident + '.report argument item')
            _text(item.get('reasoning'), ident + '.report argument item.reasoning')
            _refs(item.get('evidence_refs'), len(evidence), ident + '.report item.evidence_refs')
            _refs(item.get('proof_refs'), len(proofs), ident + '.report item.proof_refs')
        if outcome == 'unsound' and not any(
                item['kind'] == 'premise' and item['assessment'] == 'contradicted'
                and (item['evidence_refs'] or item['proof_refs']) for item in items):
            raise ValueError(f'{ident}: unsound argument requires a contradicted report premise with evidence or proof references')
        deps = _strings(argument.get('claim_dependencies'), ident + '.claim_dependencies')
        if len(deps) != len(set(deps)) or any(dep not in submitted for dep in deps):
            raise ValueError(f'{ident}: dependencies must name distinct audited claim IDs')
        dependencies[ident] = deps
        formal = _object(finding.get('formalization'), ident + '.formalization')
        _text(formal.get('rationale'), ident + '.formalization.rationale')
        correspondence = _list(formal.get('correspondence'), ident + '.formalization.correspondence')
        covered = []
        for item in correspondence:
            _object(item, ident + '.formalization.correspondence item')
            ref = item.get('proof_ref')
            _refs([ref], len(proofs), ident + '.formalization.proof_ref')
            _text(item.get('explanation'), ident + '.formalization.explanation')
            covered.append(ref)
        if sorted(covered) != list(range(len(proofs))):
            raise ValueError(f'{ident}: every proof requires exactly one source-to-target correspondence')
        needs_search = outcome in {'insufficient', 'not_provided'} or finding.get('semantic_state') == 'undetermined' or not evidence
        search = finding.get('support_search')
        if needs_search or search is not None:
            search = _object(search, ident + '.support_search')
            for key in ('scope', 'conclusion'):
                _text(search.get(key), ident + '.support_search.' + key)
            _strings(search.get('queries'), ident + '.support_search.queries')
            _strings(search.get('limitations'), ident + '.support_search.limitations', True)
            inspected = _list(search.get('inspected'), ident + '.support_search.inspected')
            if not inspected:
                _text(search.get('uninspected_reason'), ident + '.support_search.uninspected_reason')
            for item in inspected:
                _source(item, lookup, ident + '.support_search.inspected')
    # Topological elimination avoids recursion limits for long claim chains.
    remaining = {ident: len(deps) for ident, deps in dependencies.items()}
    dependents = {ident: [] for ident in dependencies}
    for ident, deps in dependencies.items():
        for dep in deps:
            dependents[dep].append(ident)
    ready = [ident for ident, count in remaining.items() if count == 0]
    processed = 0
    while ready:
        ident = ready.pop()
        processed += 1
        for dependent in dependents[ident]:
            remaining[dependent] -= 1
            if remaining[dependent] == 0:
                ready.append(dependent)
    if processed != len(dependencies):
        unresolved = next(ident for ident, count in remaining.items() if count)
        raise ValueError(f'Circular claim support dependency involves unresolved claim: {unresolved}')
    deferred = len(registered) - len(submitted)
    return {'contract_version': 2, 'report_anchors': len(report),
            'claim_anchors': sum(value == 'claims' for value in classifications.values()),
            'non_claim_anchors': sum(value == 'non_claim' for value in classifications.values()),
            'registered_claims': len(registered), 'audited_claims': len(submitted),
            'deferred_claims': deferred, 'coverage': 'partial' if deferred else 'complete_registration',
            'limitation': CAVEAT}


def render_coverage(root, findings):
    """Return concise registration coverage and explicit deferrals."""
    coverage = validate(root, findings)
    registry = _read(Path(root) / 'claims.json')
    lines = ['## Registered claim coverage', '',
             f"Coverage: **{coverage['coverage']}**; {coverage['report_anchors']} reviewed anchors; "
             f"{coverage['audited_claims']} audited and {coverage['deferred_claims']} deferred claims.", '', CAVEAT, '']
    for anchor in registry['anchors']:
        lines += [f"- `{anchor['report_anchor']}`: {anchor['classification']} — {anchor['reason']}"]
    for claim in registry['claims']:
        if claim['disposition'] == 'deferred':
            lines += ['', f"Deferred `{claim['claim_id']}` at `{claim['report_anchor']}`: {claim['reason']}", '',
                      '> ' + claim['report_quote'].replace('\n', '\n> ')]
    return lines


def render_finding(finding):
    """Render criteria and argument details next to this finding's evidence."""
    lines = []
    ident, criteria, argument = finding['claim_id'], finding['criteria'], finding['argument_audit']
    lines += ['', f'### {ident}: criteria and report argument audit', '',
              f"Criteria origin: **{criteria['origin']}**. Scope: {criteria['scope']}", '',
              criteria['operational_question'], '']
    lines += ['- Decision criterion: ' + item for item in criteria['decision_criteria']]
    for key in ('missing_definitions', 'alternatives'):
        lines += ['', key.replace('_', ' ').capitalize() + ': ' + ('; '.join(criteria[key]) or 'None declared.')]
    lines += ['', f"Report justification outcome: **{argument['outcome']}**.", '']
    def links(item):
        result = []
        for ref in item['evidence_refs']:
            e = finding['evidence'][ref]
            result.append(f"[evidence {ref}]({e['path']}) at `{e['anchor']}`")
        for ref in item['proof_refs']:
            p = finding['proofs'][ref]
            result.append(f"[proof {ref}: {p['theorem']}](models/{p['module'].replace('.', '/')}.lean)")
        return ', '.join(result) or 'No linked evidence or proof.'
    for item in argument['report_items']:
        lines += [f"Report {item['kind']} at `{item['report_anchor']}`:", '',
                  '> ' + item['report_quote'].replace('\n', '\n> '), '',
                  f"Assessment: **{item['assessment']}**. {item['reasoning']}", '', links(item), '']
    lines += ['Independent audit reasoning:', ''] + ['- ' + item for item in argument['independent_reasoning']]
    if not finding['evidence']:
        lines += ['', 'No independent source evidence is cited; see the bounded search and its limits.']
    lines += ['', links(argument), '', 'Audited claim dependencies: ' + (', '.join(argument['claim_dependencies']) or 'None declared.'), '',
              'Formalization rationale: ' + finding['formalization']['rationale'], '']
    for item in finding['formalization']['correspondence']:
        lines += [f"- Proof {item['proof_ref']} source-to-target correspondence: {item['explanation']}"]
    if 'support_search' in finding:
        search = finding['support_search']
        lines += ['', 'Declared bounded support search: ' + search['scope'], '',
                  'Queries: ' + ('; '.join(search['queries']) or 'No text queries; see inspection scope.'), '']
        lines += [f"- Inspected [{item['path']}]({item['path']}) at `{item['anchor']}`." for item in search['inspected']]
        if not search['inspected']:
            lines += ['No passages inspected: ' + search['uninspected_reason']]
        lines += ['', search['conclusion'], '', 'Search limits: ' + '; '.join(search['limitations']), '']
    return lines


def render(root, findings):
    """Compatibility composition of registration and per-finding details."""
    lines = render_coverage(root, findings)
    for finding in findings:
        lines += render_finding(finding)
    return lines
