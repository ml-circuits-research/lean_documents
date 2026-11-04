<a id="document-preamble"></a>
# Synthetic supplied report: 08-scanned-inventory (correct)

Audit this supplied report independently against the source packet.

<a id="C08-OK-01"></a>
**C08-OK-01.** Lot A accepted inbound quantity was 96 units.

Citations: sources/06-shipping-tickets-scan.pdf#[T01]; sources/01-stock-rules.md#[R01].

<a id="C08-OK-02"></a>
**C08-OK-02.** Lot B accepted inbound quantity was 12 units.

Citations: sources/06-shipping-tickets-scan.pdf#[T02]; sources/01-stock-rules.md#[R01].

<a id="C08-OK-03"></a>
**C08-OK-03.** Lot A book on-hand at cutoff was 148 units.

Citations: sources/02-opening-and-journal.md#[J01]; sources/02-opening-and-journal.md#[J02]; sources/01-stock-rules.md#[R02].

<a id="C08-OK-04"></a>
**C08-OK-04.** Lot A available book stock was 141 units.

Citations: sources/01-stock-rules.md#[R03]; sources/02-opening-and-journal.md#[J02].

<a id="C08-OK-05"></a>
**C08-OK-05.** Lot B book on-hand was 40 units.

Citations: sources/02-opening-and-journal.md#[J01]; sources/02-opening-and-journal.md#[J03].

<a id="C08-OK-06"></a>
**C08-OK-06.** Lot B available stock was 32 units.

Citations: sources/01-stock-rules.md#[R03]; sources/02-opening-and-journal.md#[J03].

<a id="C08-OK-07"></a>
**C08-OK-07.** The A customer accepted 48 units and the warehouse accepted a 12-unit return.

Citations: sources/06-shipping-tickets-scan.pdf#[T03]; sources/01-stock-rules.md#[R01].

<a id="C08-OK-08"></a>
**C08-OK-08.** The B order was not fully delivered: twelve of eighteen requested units were delivered.

Citations: sources/06-shipping-tickets-scan.pdf#[T04]; sources/04-receiving-messages.md#[M03].

<a id="C08-OK-09"></a>
**C08-OK-09.** The supplied A physical counts conflict, recording 148 and 147 for the same scope.

Citations: sources/03-signed-counts.md#[N01]; sources/03-signed-counts.md#[N02].

<a id="C08-OK-10"></a>
**C08-OK-10.** The imported C book balance is minus one after postings of minus nine and plus eight from zero.

Citations: sources/02-opening-and-journal.md#[J04].

<a id="C08-OK-11"></a>
**C08-OK-11.** The D accepted quantity remains unresolved because the receiver has not signed and messages propose different amounts.

Citations: sources/06-shipping-tickets-scan.pdf#[T05]; sources/04-receiving-messages.md#[M01].

<a id="C08-OK-12"></a>
**C08-OK-12.** Movement completeness is asserted for A and B that day, not for D.

Citations: sources/05-custody-register.md#[K03].

<a id="C08-OK-13"></a>
**C08-OK-13.** A reservation changes allocation without transferring stock across the boundary.

Citations: sources/01-stock-rules.md#[R02]; sources/01-stock-rules.md#[R03].

<a id="C08-OK-14"></a>
**C08-OK-14.** No supplied approved correction resolves the C import anomaly.

Citations: sources/02-opening-and-journal.md#[J04].
