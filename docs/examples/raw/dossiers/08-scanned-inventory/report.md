# Synthetic supplied report: 08-scanned-inventory (flawed)

Audit this supplied report independently against the source packet.

<a id="C08-ERR-01"></a>
**C08-ERR-01.** Lot A accepted inbound quantity was 96 units.

Citations: sources/06-shipping-tickets-scan.pdf#[T01]; sources/01-stock-rules.md#[R01].

<a id="C08-ERR-02"></a>
**C08-ERR-02.** Lot B accepted inbound quantity was 24 units because a carton equals a crate.

Citations: sources/06-shipping-tickets-scan.pdf#[T02]; sources/01-stock-rules.md#[R01].

<a id="C08-ERR-03"></a>
**C08-ERR-03.** Lot A book on-hand was 136 units.

Citations: sources/02-opening-and-journal.md#[J01]; sources/02-opening-and-journal.md#[J02].

<a id="C08-ERR-04"></a>
**C08-ERR-04.** Lot A available book stock was 148 units because quarantine remains on site.

Citations: sources/01-stock-rules.md#[R03]; sources/02-opening-and-journal.md#[J02].

<a id="C08-ERR-05"></a>
**C08-ERR-05.** Lot B book on-hand was 34 units after all three requested cartons shipped.

Citations: sources/06-shipping-tickets-scan.pdf#[T04]; sources/02-opening-and-journal.md#[J03].

<a id="C08-ERR-06"></a>
**C08-ERR-06.** Lot B available stock was 32 units.

Citations: sources/01-stock-rules.md#[R03]; sources/02-opening-and-journal.md#[J03].

<a id="C08-ERR-07"></a>
**C08-ERR-07.** All 60 A units dispatched were delivered to the customer.

Citations: sources/06-shipping-tickets-scan.pdf#[T03].

<a id="C08-ERR-08"></a>
**C08-ERR-08.** The B customer order was completely delivered.

Citations: sources/04-receiving-messages.md#[M03].

<a id="C08-ERR-09"></a>
**C08-ERR-09.** The physical A count was exactly 148 units.

Citations: sources/03-signed-counts.md#[N01]; sources/03-signed-counts.md#[N02].

<a id="C08-ERR-10"></a>
**C08-ERR-10.** The physical C shortage is exactly one unit.

Citations: sources/02-opening-and-journal.md#[J04].

<a id="C08-ERR-11"></a>
**C08-ERR-11.** Exactly 78 D units were accepted by the receiver, conclusively established by the scanned line.

Citations: sources/06-shipping-tickets-scan.pdf#[T05-QTY]; sources/04-receiving-messages.md#[M01].

<a id="C08-ERR-12"></a>
**C08-ERR-12.** Every warehouse lot was reconciled at cutoff.

Citations: sources/05-custody-register.md#[K03]; sources/02-opening-and-journal.md#[J04].

<a id="C08-ERR-13"></a>
**C08-ERR-13.** Subtracting the A quarantine from B stock gives B availability.

Citations: sources/01-stock-rules.md#[R03]; sources/02-opening-and-journal.md#[J03].

<a id="C08-ERR-14"></a>
**C08-ERR-14.** The return workflow is elegantly designed.

Citations: sources/05-custody-register.md#[K01].
