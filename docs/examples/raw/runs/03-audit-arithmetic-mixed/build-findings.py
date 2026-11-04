import json
from pathlib import Path
root = Path('/tmp/claim-audit-pq063j_v')
report = json.loads((root/'input/report-ledger.json').read_text())
sources = json.loads((root/'input/source-ledger.json').read_text())

def e(file, anchor):
    path = 'input/sources/' + file + '.md'
    return {'path':path, 'anchor':anchor, 'quote':sources[path][anchor]}

def p(theorem, target, relation='supports'):
    return {'module':'Audit', 'theorem':'Audit.'+theorem, 'target':target, 'relation':relation}

findings=[]
def add(cid, anchor, question, evidence, rules, reasoning, semantic='supported', argument='sufficient', formal='proved', proofs=None, limits=None, recommendation='Retain this claim within the stated scope.', quote=None, assumptions=None):
    findings.append(dict(claim_id=cid, report_quote=quote or report[anchor], report_anchor=anchor, question=question,
        evidence=evidence, rules=rules, assumptions=assumptions if assumptions is not None else ['The supplied synthetic documents accurately describe the stated sample and cutoff; this audit does not independently authenticate them.'],
        reasoning=reasoning, semantic_state=semantic, argument_status=argument, formal_status=formal, proofs=proofs or [],
        limits=limits or ['The result applies to the complete selected sample at the 30 June 2031 cutoff and does not establish unobserved population attributes.'], recommendation=recommendation))

add('C03-01','C03-01','Do all four listed payments sum to exactly 275000 cents, equivalent to EUR 2750.00?',
    [e('ledger','L-01'),e('ledger','L-02')],
    ['The selected ledger is complete for four distinct entries, so each row is counted once.','B-02 defines exact integer cents and 100 cents per euro.'],
    ['1. Extract P01=120000, P02=80000, P03=50000 and P04=25000 cents from L-02.','2. Add the four values: 120000 + 80000 + 50000 + 25000 = 275000.','3. 2750 × 100 = 275000, so the EUR 2750.00 rendering has no rounding discrepancy.'],
    proofs=[p('paymentTotal','Audit.sampleTotal = 275000 ∧ Audit.sampleTotal = 2750 * 100')])

add('C03-02','C03-02','Is the sample-only budget minus the actual four-payment total 35000 cents?',
    [e('ledger','L-02'),e('ledger','L-03')],
    ['B-02 defines budget difference as budget minus the four sampled payments.','Budget and payments must be compared in the same exact cent unit.'],
    ['1. L-02 sums to 275000 cents; L-03 supplies a budget of 300000 cents.','2. 300000 - 275000 = 25000 cents, or EUR 250.00.','3. 25000 is unequal to the reported 35000. This exact finite arithmetic contradiction refutes the claimed difference; the positive excess itself is correctly implied by budget being larger.'],
    semantic='refuted',argument='invalid_inference',formal='refuted',
    proofs=[p('budgetDifference','Audit.budget - Audit.sampleTotal = 25000 ∧ Audit.budget - Audit.sampleTotal ≠ 35000 ∧ Audit.sampleTotal ≤ Audit.budget','refutes')],
    recommendation='Replace 35000 cents / EUR 350.00 with 25000 cents / EUR 250.00.')

add('C03-03','C03-03','Are exactly two of the four selected entries approval exceptions, and is the exact sample rate 50%?',
    [e('ledger','L-01'),e('ledger','L-02'),e('method','M-02')],
    ['Count one exception for each entry whose required approval was absent at the cutoff.','B-02 defines sample rate as exception count divided by the sample count, without amount weighting.'],
    ['1. P01 and P02 show approvals present; P03 and P04 show approvals absent.','2. Therefore exactly two of the four sample entries count as exceptions under M-02.','3. The denominator is four and nonzero; 2/4 = 50/100. The Lean target checks this exact equality by cross multiplication.'],
    proofs=[p('sampleExceptionRate','Audit.sample.length = 4 ∧ Audit.exceptionCount = 2 ∧ Audit.exceptionCount * 100 = 50 * Audit.sample.length')])

add('C03-04','C03-04','Does the sample establish that exactly ten of the twenty population entries had missing approvals?',
    [e('ledger','L-01'),e('ledger','L-02'),e('method','M-01')],
    ['Sample counts and population counts concern different domains.','An exact population rate requires the missing-approval count among the other sixteen entries or another sufficient completeness argument.','A compatible hypothetical completion diagnoses non-entailment and is not an observed actual-world counterexample.'],
    ['1. L-01/L-02 identify two missing approvals in the complete four-entry sample, but give no statuses for the other sixteen population entries.','2. M-01 explicitly states judgmental selection and no assertion of representativeness; it does not license the exact 50% extrapolation.','3. A compatible completion with zero additional missing approvals gives 2/20 = 10%; another with eight additional missing approvals gives 10/20 = 50%. Both additional counts fit within sixteen.','4. The auxiliary Lean result verifies these alternative arithmetic completions. Thus the proposed inference is invalid, while the actual exact population rate remains undetermined; the 50% statement could happen to be true.'],
    semantic='undetermined',argument='invalid_inference',formal='auxiliary',
    proofs=[p('populationCompletionAlternatives','Audit.populationExceptions 0 * 100 ≠ 50 * 20 ∧ Audit.populationExceptions 8 * 100 = 50 * 20 ∧ (0 : Nat) ≤ 16 ∧ (8 : Nat) ≤ 16','auxiliary')],
    limits=['No actual statuses for the sixteen unsampled entries are supplied.','Alternative completions show failure of entailment and do not refute 50% as an actual population fact.','The actual population rate could range from 10% to 90% under the supplied distinct-entry model; neither endpoint is asserted as actual.'],
    recommendation='Report the 50% sample rate separately; obtain approval statuses for all sixteen other entries before asserting an exact population rate.')

add('C03-05','C03-05','Do the sampled payments with absent required approvals sum to 75000 cents?',
    [e('ledger','L-02'),e('method','M-02')],
    ['Select entries by approval status at the cutoff, then sum their amounts once.'],
    ['1. The only missing-approval entries in the complete selected sample are P03 and P04.','2. Their amounts are 50000 and 25000 cents.','3. 50000 + 25000 = 75000 cents, matching the report.'],
    proofs=[p('missingApprovalTotal','Audit.exceptionTotal = 75000')])

add('C03-06-premise','C03-06','Did all four sampled payments match their invoices?',
    [e('inspection','I-01'),e('ledger','L-01')],
    ['Preserve a true factual premise separately from an invalid inference drawn from it.'],
    ['1. I-01 explicitly says all four sampled payments matched their invoices.','2. L-01 fixes the complete sample domain to four entries.','3. The model assigns matched=true to those four entries and checks their universal matching statement; this does not imply approval.'],
    proofs=[p('allInvoicesMatched','∀ p ∈ Audit.sample, p.matched = true')],
    quote='all four invoices matched',
    recommendation='Retain invoice matching as a separate control observation, without an approval inference.')

add('C03-06','C03-06','Does universal invoice matching establish that every sampled payment had required approval at the cutoff?',
    [e('inspection','I-01'),e('method','M-02'),e('ledger','L-02')],
    ['M-02 treats invoice matching and required approval as separate controls.','A universal approval statement fails when an in-scope sampled entry has approval absent at the same cutoff.'],
    ['1. The invoice-matching premise is supported, but M-02 supplies no implication from matching to approval.','2. I-01 and L-02 identify P03 and P04 as sampled entries missing required approval at the cutoff.','3. P03 is an explicit in-scope counterexample: it matched its invoice and lacked approval. Hence the universal approval conclusion is false, as well as unsupported by the proposed inference.','4. The Lean target checks sample membership, matched=true, approved=false, and the negation of universal sample approval.'],
    semantic='refuted',argument='invalid_inference',formal='refuted',
    proofs=[p('approvalCounterexample','Audit.p03 ∈ Audit.sample ∧ Audit.p03.matched = true ∧ Audit.p03.approved = false ∧ ¬ (∀ p ∈ Audit.sample, p.approved = true)','refutes')],
    recommendation='State invoice matching separately and report the two missing approvals at the cutoff. Do not infer fraud or later approval status.')

add('C03-07','C03-07','Does I-01 literally state that no sampled payments were missing required approvals?',
    [e('inspection','I-01')],
    ['A claim about what a cited paragraph says must match its literal attributed content and temporal scope.'],
    ['1. Read all of I-01, rather than only the invoice-matching sentence.','2. Its next sentence explicitly says required approvals were absent for P03 and P04 at the cutoff.','3. That named absence directly contradicts the report’s characterization that I-01 says no sampled payments lacked approval. This is a textual citation refutation, independently consistent with L-02.'],
    semantic='refuted',argument='invalid_inference',formal='not_attempted',
    limits=['The refutation is documentary: Lean is not being claimed to interpret the English paragraph.','Approval absence at cutoff does not imply fraud or establish subsequent approval history.'],
    recommendation='Correct the citation summary to say I-01 identifies missing approvals for P03 and P04 at the cutoff.')

add('C03-08','C03-08','Does the supplied evidence establish Annex C’s contents or that both missing approvals were obtained after the cutoff?',
    [e('annex-register','A-01'),e('annex-register','A-02'),e('inspection','I-01')],
    ['A document-index entry establishes a listing, not the document’s contents.','Absence of supplied evidence does not establish that later approvals did or did not occur.'],
    ['1. A-01 lists Annex C under the title “Post-cutoff approval follow-up,” but explicitly says Annex C is not included.','2. The same paragraph records no finding about whether either approval was subsequently obtained; A-02 expressly distinguishes listing from contents.','3. I-01 establishes only approval absence at cutoff. Reading the complete supplied packet finds no follow-up approval evidence.','4. The report’s claim about confirmation in Annex C and the underlying subsequent approvals is therefore insufficiently supported and remains undetermined. Missing material is not a refutation of later approval.'],
    semantic='undetermined',argument='insufficient_support',formal='not_attempted',
    limits=['Annex C is unavailable; its content and the subsequent approval events cannot be inferred.','The title does not establish that both, one, or neither approval was obtained.'],
    recommendation='Obtain Annex C and underlying dated approval records; until then identify post-cutoff clearance as unverified.')

add('C03-09','C03-09','Is “impressively elegant” an operationally defined, evidence-verifiable assessment here?',
    [e('inspection','I-02')],
    ['No supplied source or brief defines a measurable criterion for elegance.','Preserve qualitative observations as attributed judgments; do not convert them into control-effectiveness claims.'],
    ['1. I-02 attributes the description “orderly” to a reviewer.','2. “Impressively elegant” is an evaluative embellishment without an operational standard in the supplied corpus.','3. This subjective judgment is not classified as a true or false finite proposition. It receives no formal proof and implies nothing about population-wide approval controls.'],
    semantic='not_applicable',argument='nonformal',formal='not_attempted',assumptions=[],
    limits=['No objective elegance criterion or audience preference is supplied.','I-02 explicitly disclaims a population-wide control adequacy assessment.'],
    recommendation='Label this as the report author’s subjective assessment, or use the accurately attributed reviewer description “orderly.”')

add('C03-10','C03-10','Does the known sample establish at least two missing-approval entries in the twenty-entry population at cutoff?',
    [e('ledger','L-01'),e('ledger','L-02'),e('inspection','I-01')],
    ['The four distinct sample entries belong to the target population described in L-01.','Known missing approvals in a subset provide a lower bound for the whole domain; unknown additional entries cannot subtract known exceptions.'],
    ['1. L-01 identifies the four listed entries as the selected sample of a twenty-entry population.','2. P03 and P04 are two distinct sample members missing required approvals at the cutoff, as L-02 and I-01 agree.','3. Write the population exception count as 2+n, where n is the unknown exception count among sixteen other entries and 0≤n≤16.','4. For every such n, 2+n≥2. This lower bound is supported even though an exact population rate remains unknown.'],
    proofs=[p('populationLowerBound','∀ unknownExceptions : Nat, unknownExceptions ≤ 16 → 2 ≤ Audit.populationExceptions unknownExceptions')],
    assumptions=['Sample identifiers denote distinct population entries, as the L-01/L-02 sample representation indicates.','The unknown additional exception count is a nonnegative integer no greater than sixteen.'],
    limits=['The result supplies a lower bound only; it does not identify an exact population rate or any unsampled entry’s approval status.'],
    recommendation='Retain this population lower bound and keep it separate from unsupported exact-rate extrapolation.')

(root/'findings.json').write_text(json.dumps(findings,indent=2,ensure_ascii=False)+'\n')
claims=[]
for f in findings:
    claims.append({'claim_id':f['claim_id'],'parent_report_anchor':f['report_anchor'],'report_quote':f['report_quote'],
        'verification_question':f['question'],'coverage':'reviewed','finding_id':f['claim_id']})
register={'scope':'All ten numbered findings in the selected report; C03-06 separates its factual premise from its inference/conclusion.',
    'numbered_report_findings':10,'audit_records':len(claims),'claims':claims,
    'compound_claims':{'C03-01':['275000-cent sum','EUR 2750.00 equivalence'],
        'C03-02':['Positive budget excess','Reported exact 35000-cent / EUR 350.00 amount'],
        'C03-03':['Exactly two sample exceptions','Four-entry sample denominator','Exact 50% sample rate'],
        'C03-08':['Claimed Annex C confirmation','Both approvals obtained after cutoff']},
    'exclusions':[], 'independent_semantic_review':'Not performed by this author.'}
(root/'claims.json').write_text(json.dumps(register,indent=2,ensure_ascii=False)+'\n')
