# Release R17 evidence assessment

Report identifier `REP-R17-04`; author `Lumen Evidence Review Desk`; cutoff `2030-03-14T12:00:00Z`. This assessment concerns the supplied documents for release `R17`, target `EU-A`.

<a id="report-cec01"></a>
**CEC-01.** The supplied release manifest contains exactly three distinct entry IDs: `A-01`, `A-02`, and `A-03`. This count applies to the exported manifest, not to all deployed instances or dependencies. Basis: [inventory-p2](sources/release-inventory.md#inventory-p2).

<a id="report-cec02"></a>
**CEC-02.** QA and Operations supply contradictory assertions about the same inbound API TLS enabled state for release `R17`, target `EU-A`, at `2030-03-14T11:45:00Z`: QA asserts enabled; Operations asserts disabled. This is a conflict in testimony, not a finding that contradictory deployment facts are simultaneously true. Neither supplied source has precedence. Basis: [qa-p2](sources/qa-attestation.md#qa-p2), [ops-p2](sources/ops-attestation.md#ops-p2), [ops-p3](sources/ops-attestation.md#ops-p3), and [policy-p3](sources/release-policy.md#policy-p3).

<a id="report-cec03"></a>
**CEC-03.** The supplied package includes no penetration-test certificate. This attachment fact leaves whether testing occurred outside the package undetermined. Basis: [inventory-p3](sources/release-inventory.md#inventory-p3).

<a id="report-cec04"></a>
**CEC-04.** The supplied policy rule says that `SmokePassed` together with `SecurityApproved` implies `Ready`. It does not itself assert `SecurityApproved`; QA reports smoke-check success but does not assert that all security review requirements passed. These passages alone do not establish unconditional readiness. Basis: [policy-p1](sources/release-policy.md#policy-p1), [policy-p2](sources/release-policy.md#policy-p2), and [qa-p3](sources/qa-attestation.md#qa-p3).

<a id="report-cec05"></a>
**CEC-05.** The archived independent-verification support links from `REP-R17-03` are circular: its `CE-05` points to its verification appendix, and that appendix points back to `CE-05`. That cycle does not supply an independent review artifact. This does not establish that no independent review happened elsewhere. Basis: [excerpt-p1](sources/verification-excerpt.md#excerpt-p1), [excerpt-ce05](sources/verification-excerpt.md#excerpt-ce05), and [excerpt-appendix](sources/verification-excerpt.md#excerpt-appendix).

<a id="report-cec06"></a>
**CEC-06.** The supplied QA transcription contains a scenario signature marker but no signing key, signature bytes, certificate chain, or authenticity verification result. The transcription alone therefore does not establish verified cryptographic authenticity. Basis: [qa-p1](sources/qa-attestation.md#qa-p1).
