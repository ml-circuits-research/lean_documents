# Release policy excerpt POL-4

<a id="policy-p1"></a>
**policy-p1.** Scope: readiness rule for release `R17`, target `EU-A`, as of the review cutoff. Define `SmokePassed` as all three manifest entries passing the smoke checks; define `SecurityApproved` as an authorized security reviewer approving this release and target; define `Ready` as satisfying this policy's release-readiness criterion.

<a id="policy-p2"></a>
**policy-p2.** The rule is conditional: if `SmokePassed` and `SecurityApproved`, then `Ready`. This excerpt neither states `SecurityApproved` nor grants security approval. It supplies a sufficient condition, not a necessary-and-sufficient characterization of readiness.

<a id="policy-p3"></a>
**policy-p3.** Evidence from QA and Operations must retain separate provenance. This excerpt assigns neither source priority and supplies no rule for deriving approval from the absence of a rejection or from a later document timestamp.
