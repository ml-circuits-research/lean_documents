"""Rebuild authored audit artifacts in an already prepared v2 workspace.

These are transparent nonblind fixture-author audits, not autonomous analysis or
expected outcomes. Run the actual helper check separately after semantic review.
"""
from pathlib import Path
import argparse
import json
import re
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('workspace', type=Path)
parser.add_argument('variant', choices=['correct', 'mixed'])
args = parser.parse_args()
root = args.workspace
correct = args.variant == 'correct'
ledger = json.loads((root / 'input/source-ledger.json').read_text())
report = ledger['input/report.md']
registry = json.loads((root / 'claims.json').read_text())
registry['claims'] = []
for anchor in registry['anchors']:
    anchor['classification'] = 'non_claim' if anchor['report_anchor'] == 'P01' else 'claims'
    anchor['reason'] = ('Document title only.' if anchor['report_anchor'] == 'P01' else
                        'One substantive conclusion; its supplied premises, citations and inference are audited separately below.')

mapping = {
 'P1': ('policy.md', 'P02'), 'P2': ('policy.md', 'P03'),
 'P3': ('policy.md', 'P04'), 'P4': ('policy.md', 'P05'),
 'O1': ('operations.md', 'P02'), 'O2': ('operations.md', 'P03'),
 'O3': ('operations.md', 'P04'), 'I1': ('invoice.md', 'P02'),
 'I2': ('invoice.md', 'P03')}
source_sets = [['P1','O1'], ['P1','O1','O2'], ['P1','O1','O2'],
 ['P1','P2','O1','O2'], ['P1','P2','O1','O2'], ['P3','I1'],
 ['P3','I2'], ['P3','I1','I2'], ['P4','O3'], ['P4']]
questions = [
 'How many distinct minutes lie in A or B within the actual gross window?',
 'How many distinct minutes lie in A, B or touching C within the actual gross window?',
 'What is the union duration after zero-length, case-scope and window rules are applied to the complete actual inventory?',
 'Does actual gross duration minus its paused union satisfy the inclusive 140-minute SLA?',
 'Does the explicit 181-minute extension satisfy the same inclusive SLA with unchanged intervals?',
 'What integer cent amount does the exact positive half-cent line produce under away-from-zero rounding?',
 'What integer cent amount does the exact negative half-cent credit produce under away-from-zero rounding?',
 'What is the signed sum after rounding each of the three invoice lines separately?',
 'Do the supplied sources establish the necessary prior-quarter breach threshold for historical rebate entitlement?',
 'Does the supplied protocol define an operational standard permitting a reasonableness verdict?']
reasoning = [
 'A covers minutes 20 through 39 and B covers 30 through 49. Their overlap is 30 through 39, so their union is 20 through 49: 30 minutes. Adding 20 and 20 double-counts ten minutes.',
 'A and B already cover [20,50). C covers [50,60). Their touching boundary adds no minute beyond the enumerated 20 through 59, giving 40 minutes.',
 'The complete inventory covers forty actual-window minutes. Z=[60,60) contains no minute; X belongs to H17; Y=[190,200) has no member in [0,180). Neither a zero-length marker nor another case adds a minute.',
 'The ledger gives gross 180, and the approved in-case union is 40. Thus chargeable time is 140. P2 includes equality, establishing that H16 meets the SLA. A premise that gross duration is 130 is contradicted by O1 even though the conclusion is independently supported.',
 'At gross 181, Y still begins after the window. The union stays 40, giving 141 chargeable minutes. P2 allows 140 inclusive and explicitly excludes a tolerance minute, so the extended incident fails.',
 '1005 mills divided by ten is 100.5 cents. P3 sends the exact positive tie away from zero to 101 cents; 100 would implement the wrong tie policy.',
 'The absolute credit magnitude is 1005 mills, or 100.5 cents. Round magnitude to 101 and restore the negative sign: -101 cents. Moving to -100 would round the tie toward zero.',
 'Round +1005 to +101, +1005 to +101, and -1000 to -100. Sum is +102 cents. The aggregate 1010 mills rounds to +101, but P3 expressly requires per-line rounding and excludes the separate CN16 credit note.',
 'P4 makes three earlier-quarter breaches a necessary condition. O3 explicitly provides no earlier-quarter counts or events. Neither a zero count nor three breaches may be asserted as actual. Counts zero and three illustrate why the available history does not select a threshold outcome; meeting the threshold alone is not proved sufficient for entitlement.',
 'P4 explicitly states that no definition, benchmark or test of reasonable compensation is supplied. Full source inspection finds no substitute standard. A substantive reasonableness conclusion cannot be determined without an authorized criterion. This is not a refutation of compensation being reasonable.']
if correct:
    reasoning[3] = reasoning[3].split(' A premise that')[0]
recommendations = [
 'Use a 30-minute union for A and B.', 'Use a 40-minute union after adding C.',
 'Retain 40 actual paused minutes and exclude Z, X and Y under the separate rules.',
 'Retain SLA compliance using gross 180, paused 40 and chargeable 140.',
 'Record the extension as failing at 141 chargeable minutes.',
 'Record L1 as +101 cents.', 'Record CN16 as -101 cents.',
 'Record invoice N16 as +102 cents; keep CN16 separate.',
 'Obtain the August–October breach records and any additional entitlement requirements before deciding the historical rebate.',
 'Obtain an authorized definition or benchmark before assessing reasonableness.']
# Tuple entries are (theorem name, exact typed target).
supported = [
 ('overlap30','Settlement.unionMinutes 180 [Settlement.a, Settlement.b] = 30'),
 ('touching40','Settlement.unionMinutes 180 [Settlement.a, Settlement.b, Settlement.c] = 40'),
 ('actual40','Settlement.unionMinutes Settlement.actualGross Settlement.inventory = 40'),
 ('exactDeadline','Settlement.meets Settlement.actualGross'),
 ('extensionFails','¬ Settlement.meets 181'),
 ('positiveTie','Settlement.roundCents 1005 = 101'),
 ('negativeTie','Settlement.roundCents (-1005) = -101'),
 ('invoice102','Settlement.invoiceTotal = 102')]
refuted = [
 ('overlapNot40','Settlement.unionMinutes 180 [Settlement.a, Settlement.b] ≠ 40'),
 ('touchingNot41','Settlement.unionMinutes 180 [Settlement.a, Settlement.b, Settlement.c] ≠ 41'),
 ('actualNot51','Settlement.unionMinutes Settlement.actualGross Settlement.inventory ≠ 51'),
 supported[3], supported[4],
 ('positiveNot100','Settlement.roundCents 1005 ≠ 100'),
 ('negativeNot100','Settlement.roundCents (-1005) ≠ -100'),
 ('invoiceNot101','Settlement.invoiceTotal ≠ 101')]

def proof(entry, relation):
    return dict(module='IntervalModel', theorem='Settlement.'+entry[0], target=entry[1], relation=relation)

findings = []
for i in range(10):
    number = i + 1
    anchor = f'P{number+1:02d}'
    text = report[anchor].split('] ', 1)[1]
    quote, argument = text.split('. ', 1)
    quote += '.'
    cid = f'C16-{number:02d}'
    registry['claims'].append(dict(claim_id=cid, report_anchor=anchor, report_quote=quote, disposition='audited'))
    evidence = []
    for key in source_sets[i]:
        name, source_anchor = mapping[key]
        path = 'input/sources/' + name
        evidence.append(dict(path=path, anchor=source_anchor, quote=ledger[path][source_anchor]))
    semantic = 'supported' if correct or number == 4 else ('refuted' if number <= 8 else 'undetermined')
    outcome = 'sufficient' if correct else ('unsound' if number <= 7 else ('invalid' if number in (8,9) else 'insufficient'))
    argument_status = {'unsound':'unsound_argument','invalid':'invalid_inference','insufficient':'insufficient_support'}.get(outcome,outcome)
    proofs = []
    if number <= 8:
        proofs.append(proof((supported if correct else refuted)[i], 'supports' if semantic == 'supported' else 'refutes'))
    if number == 2:
        proofs.append(proof(('touching_union', '∀ (lo mid hi minute : Nat), lo ≤ mid → mid ≤ hi → (((lo ≤ minute ∧ minute < mid) ∨ (mid ≤ minute ∧ minute < hi)) ↔ (lo ≤ minute ∧ minute < hi))'), 'auxiliary'))
    if number == 3:
        proofs.append(proof(('empty_interval','∀ (point minute : Nat), ¬ (point ≤ minute ∧ minute < point)'), 'auxiliary'))
    if number == 4 and not correct:
        proofs.append(proof(('falseGross','Settlement.actualGross ≠ 130'), 'auxiliary'))
    if number == 8:
        proofs.append(proof(('aggregateIs101','Settlement.roundCents Settlement.invoiceLines.sum = 101'), 'auxiliary'))
    if number == 9 and not correct:
        proofs.append(proof(('historicalAlternatives','(¬ Settlement.historicalThresholdMet 0) ∧ Settlement.historicalThresholdMet 3'), 'auxiliary'))
    formal = ('proved' if semantic == 'supported' else 'refuted') if number <= 8 else ('auxiliary' if proofs else ('blocked' if not correct else 'not_attempted'))
    item = dict(kind='inference' if outcome == 'invalid' else 'premise', report_anchor=anchor,
                report_quote=argument, assessment='verified' if correct else ('contradicted' if outcome == 'unsound' else 'unsupported'),
                reasoning=reasoning[i], evidence_refs=list(range(len(evidence))), proof_refs=list(range(len(proofs))))
    items = [item]
    # Check literal source references independently from the rest of the offered argument.
    for token in re.findall(r'\b[PO][1-4]\b', argument):
        if token in source_sets[i]:
            items.append(dict(kind='citation', report_anchor=anchor, report_quote=token,
                assessment='contradicted' if not correct and number in (6,7) else 'verified',
                reasoning=('The cited policy prescribes away-from-zero ties, contradicting the report attribution.' if not correct and number in (6,7) else 'The cited passage exists and its content matches the attributed bounded statement.'),
                evidence_refs=[source_sets[i].index(token)], proof_refs=[]))
    correspondence = []
    for ref, p in enumerate(proofs):
        explanation = reasoning[i] + ' The model transcribes the cited integer values and the explicit policy, assuming faithful source transcription and protocol applicability. It does not authenticate records.'
        if p['theorem'].endswith('touching_union'):
            explanation = 'This symbolic half-open membership equivalence applies to ordered endpoints, independently of incident values. It explains why touching intervals do not add an extra boundary minute; it is auxiliary rather than a source authenticity result.'
        elif p['theorem'].endswith('empty_interval'):
            explanation = 'The symbolic target states no natural minute is both at least and below the same endpoint. P1 uses that half-open convention, so Z contributes zero. This does not establish other interval scopes.'
        elif p['theorem'].endswith('falseGross'):
            explanation = 'O1 gives gross 180; actualGross is exactly that transcription. Its inequality with 130 refutes the report premise separately from the independently supported SLA conclusion.'
        elif p['theorem'].endswith('aggregateIs101'):
            explanation = 'The three I1 signed mills sum to 1010, which rounds to 101 cents. This verifies the alternative aggregate calculation only; P3 prohibits using it as the invoice total. The direct total target instead sums rounded lines.'
        elif p['theorem'].endswith('historicalAlternatives'):
            explanation = 'P4 supplies the necessary threshold of three, while O3 leaves the actual count unconstrained. This target computes failure at count zero and satisfaction at count three only. It is an auxiliary illustration of two possible threshold counts, not a formal proof of documentary completeness, actual entitlement or sufficient entitlement conditions.'
        correspondence.append(dict(proof_ref=ref, explanation=explanation))
    findings.append(dict(claim_id=cid, report_anchor=anchor, report_quote=quote, question=questions[i],
        evidence=evidence, rules=[ledger['input/sources/'+mapping[key][0]][mapping[key][1]] for key in source_sets[i] if key.startswith('P')],
        assumptions=['The synthetic source transcriptions are faithful and SR-16 applies to H16; no external facts are added.'],
        reasoning=[reasoning[i]], semantic_state=semantic, argument_status=argument_status, formal_status=formal,
        proofs=proofs, limits=['The supplied corpus is the entire search boundary. The model does not authenticate sources or establish missing historical events. Partial-window clipping is not independently exercised by this dossier.'],
        recommendation=recommendations[i],
        criteria=dict(origin='inferred', operational_question=questions[i], decision_criteria=[reasoning[i]],
            scope='H16 actual and explicitly identified extension scenario, invoice N16, separate CN16, and the explicitly scoped August–October historical prerequisite.',
            missing_definitions=['Operational reasonableness criterion.'] if number == 10 else [], alternatives=[]),
        argument_audit=dict(outcome=outcome, report_items=items, independent_reasoning=[reasoning[i]], evidence_refs=list(range(len(evidence))), proof_refs=list(range(len(proofs))), claim_dependencies=[]),
        formalization=dict(rationale=('Use finite interval union and exact signed integer rounding, with direct targets and explicitly auxiliary checks.' if number <= 8 else ('The proof only illustrates the threshold gap; no historical count or sufficient entitlement test is supplied.' if proofs else 'A bounded documentary metaclaim is checked by source inspection; no historical fact or undefined qualitative judgment is encoded as a theorem.')), correspondence=correspondence),
        support_search=dict(scope='Read the complete three-file source corpus and this report paragraph, including policy, full pause inventory, invoice and explicit historical limitations.',
            queries=['H16', 'pause', 'SLA', 'round', 'historical', 'reasonable'],
            inspected=[dict(path=path, anchor=a) for path, passages in ledger.items() if path.startswith('input/sources/') for a in passages],
            limitations=['No external sources, missing historical records, or alternate report were used as evidence.'],
            conclusion=reasoning[i])))
(root/'claims.json').write_text(json.dumps(registry, indent=2)+'\n')
(root/'findings.json').write_text(json.dumps(findings, indent=2)+'\n')
(root/'models').mkdir(exist_ok=True)
shutil.copyfile(Path(__file__).with_name('IntervalModel.lean'), root/'models/IntervalModel.lean')
(root/'review-plan.md').write_text('''# Review plan

Contract v2; criteria are inferred from the selected supplied report and SR-16. No separate brief exists. Read all three source files and every report paragraph. Register ten numbered conclusions; audit each offered premise, citation and inference separately. Search all authorized sources for counterevidence. Check interval union, inclusive deadline and exact signed rounding using finite typed definitions; retain missing history and undefined reasonableness as support gaps. No alternate report or evaluator outcomes are audit evidence. This is a nonblind fixture-author audit, explicitly disclosed; a separate root reviewer derives a source-first view before checking model correspondence. Keep all runs and logs.
''')
(root/'model-notes.md').write_text('''# Model correspondence and limits

`Pause` uses nonnegative integer minute offsets from 09:00 UTC, 2 November 2026, as defined in P1. Source O1 provides a=[20,40), b=[30,50), actualGross=180; O2 provides c=[50,60), z=[60,60), x=[70,80) with inCase=false, and y=[190,200). All listed records are approved. `inventory` includes all six records. `unionMinutes` enumerates each minute of [0,gross) exactly once and counts any qualifying interval membership, thus it cannot double-count overlap and inherently clips the window. No partial-clipping interval is exercised here. The observed and extension windows are 180 and 181. Nat subtraction cannot underflow for this construction because paused minutes are filtered from the gross-minute list; no general cardinality theorem is claimed. P2 gives inclusive threshold 140.

P3 defines signed mills and half-away-from-zero cent rounding. `roundCents` adds five to the absolute magnitude and divides by ten, then restores sign. I1 maps to [1005,1005,-1000]; CN16=-1005 from I2 is tested separately and is excluded from invoiceTotal. Both exact half ties are checked. P4's three breaches is a necessary condition only. `historicalThresholdMet` tests that necessary threshold without asserting sufficient eligibility. The auxiliary zero/three witness illustrates unobserved alternatives, not an actual history or a formal documentary entailment theorem.

Generic `touching_union` establishes interval membership equivalence for ordered endpoints; `empty_interval` establishes impossibility of membership in a zero-length half-open interval. Concrete targets establish counts or exact negations. Mixed R4 uses a direct compliance theorem and a distinct auxiliary refutation of gross=130. R9 and R10 documentary limitations are not proofs of actual non-entitlement or unreasonable compensation. The only external trust assumptions are source fidelity and policy applicability; all premises remain visible in the source mapping. Lean checks are ordinary kernel proofs with no custom axioms or native-decision shortcuts.
''')
(root/'semantic-review.md').write_text('''# Semantic review

This audit is nonblind: the fixture author authored both reports and reviewed the selected variant against original sources. No evaluator-only expected-outcome file is used. The author reviewed source mappings, exact targets, interval membership, signed tie rounding, and the distinction between argument and conclusion. The source inventory is complete only for actual H16 pauses; historical events remain open.

A separate root reviewer independently read the original sources and both reports before reading this proposed model. Its source-first view found union durations 30/40, actual chargeable 140 inclusive, extension 141 failing, positive/negative tie results +101/-101, and invoice total 102 versus aggregate 101. It identified mixed R4 as a supported conclusion with a contradicted gross premise, historical threshold as necessary rather than sufficient, and reasonableness as undefined. The author adopted that threshold distinction. The reviewer noted that no partial-clipping case is exercised; this limitation is disclosed rather than claiming coverage. Final model correspondence review is pending and must be appended before the delivered final check. This is independent review of source interpretation but not a blind audit experiment.
''')
print(json.dumps({'workspace': str(root.resolve()), 'variant': args.variant, 'findings':len(findings)}))
