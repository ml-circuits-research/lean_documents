# Coordinator source-first review

I read the supplied report and all 14 lines of `supplied/sources/stock.html` before inspecting the proposed Lean models or findings. I knew the synthetic fixture's design from coordinating the portability test; this is source-first rederivation, not a blind benchmark or domain-expert certification.

- R1: the current population is explicitly complete. The count rule admits A (18 active) and B (27 quarantined), and excludes C (15 archived). Counted stock is 45. The offered argument follows the source rule.
- R2: 18 + 27 + 15 = 60 is arithmetically true. The population premise is false for counted stock because archived C is excluded. The conclusion is contradicted by the independently reconstructed total 45. Do not describe the defect as bad arithmetic.
- R3: A is active and signed, so the conclusion is supported by both conditions. The report's proposed universal sufficiency rule for a signature is false: B is signed but quarantined, hence ineligible. A deduction from a false rule can have a true conclusion; modus ponens itself is not invalid. The actual defect is the offered rule.
- R4: current snapshot completeness does not cover prior clearance history. A past clearance and no past clearance are both compatible with this source. The conclusion is unsupported, not contradicted by positive clearance evidence. The report's closed-world inference is not warranted.

Relevant limitations: original HTML identity and line mapping are inspectable; no source authenticity is inferred. Definitions come from the supplied rule, not universal inventory practice. Whole units and the finite current domain are explicitly given; historical completeness is explicitly absent.

Final model and artifact review will be recorded separately after the audit agent finishes.
