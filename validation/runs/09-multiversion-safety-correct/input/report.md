<a id="document-preamble"></a>
# Synthetic supplied report: 09-multiversion-safety (correct)

Audit this supplied report independently against the source packet.

<a id="C09-OK-01"></a>
**C09-OK-01.** L01 satisfies the historical revision 1 delay demonstration; its maximum is 118 milliseconds, below the 120-millisecond limit.

Citations: sources/01-specification-v1.docx#[V1-02]; sources/04-test-runs.pdf#[P01].

<a id="C09-OK-02"></a>
**C09-OK-02.** Revision 2 governs the N01 and N02 tests executed on 3 June.

Citations: sources/02-specification-v2.docx#[V2-01]; sources/04-test-runs.pdf#[P02].

<a id="C09-OK-03"></a>
**C09-OK-03.** All three N01 valid delay runs satisfy the applicable 100-millisecond limit.

Citations: sources/02-specification-v2.docx#[V2-02]; sources/04-test-runs.pdf#[P02].

<a id="C09-OK-04"></a>
**C09-OK-04.** N02 has a concrete failing valid run of 101 milliseconds.

Citations: sources/04-test-runs.pdf#[P02]; sources/02-specification-v2.docx#[V2-02].

<a id="C09-OK-05"></a>
**C09-OK-05.** E17 satisfies its applicable 110-millisecond exception limit for all three named runs.

Citations: sources/03-exception-annex.docx#[X01]; sources/04-test-runs.pdf#[P03].

<a id="C09-OK-06"></a>
**C09-OK-06.** The E17 exception does not apply to N02.

Citations: sources/03-exception-annex.docx#[X01].

<a id="C09-OK-07"></a>
**C09-OK-07.** C01 satisfies the COLD-profile 150-millisecond delay limit.

Citations: sources/02-specification-v2.docx#[V2-02]; sources/04-test-runs.pdf#[P04].

<a id="C09-OK-08"></a>
**C09-OK-08.** N03 lacks channel B measurement and a third valid repeated run.

Citations: sources/06-applicability-and-open-items.md#[AP02]; sources/04-test-runs.pdf#[P05].

<a id="C09-OK-09"></a>
**C09-OK-09.** K2 was expired when used for N03 on 3 June.

Citations: sources/05-calibration-and-authority.md#[CAL01]; sources/04-test-runs.pdf#[P05].

<a id="C09-OK-10"></a>
**C09-OK-10.** X99 cannot count as a valid repeated run because synchronization was lost.

Citations: sources/06-applicability-and-open-items.md#[AP02]; sources/04-test-runs.pdf#[P05].

<a id="C09-OK-11"></a>
**C09-OK-11.** A passed delay demonstration alone is insufficient for release under revision 2.

Citations: sources/02-specification-v2.docx#[V2-03].

<a id="C09-OK-12"></a>
**C09-OK-12.** The listed three-run route is sufficient for the bounded delay demonstration, not stated necessary for every conceivable method.

Citations: sources/01-specification-v1.docx#[V1-03]; sources/03-exception-annex.docx#[X04].

<a id="C09-OK-13"></a>
**C09-OK-13.** N01, E17, and C01 have authorized release signatures in the supplied ledger.

Citations: sources/05-calibration-and-authority.md#[AUTH01].

<a id="C09-OK-14"></a>
**C09-OK-14.** The packet supplies no HOT-profile qualification route.

Citations: sources/06-applicability-and-open-items.md#[AP01]; sources/02-specification-v2.docx#[V2-02].
