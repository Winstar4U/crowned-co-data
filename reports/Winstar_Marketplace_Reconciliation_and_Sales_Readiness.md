# Winstar Enterprises — Marketplace Reconciliation and Sales Readiness

**Prepared:** 2026-11-18, under "VP OPERATIONS DIRECTIVE — Marketplace Reconciliation and Sales Readiness"
**Scope:** Winstar's 5 Printify-connected shops only (Etsy 26603005, Amazon 29451844, eBay 28059412, TikTok 28122957, Shopify 26418699). Luzilly Bridal, Luzilly Fragrances, Halcyon Intimate, and KDP are explicitly out of scope and untouched.

---

## EXECUTIVE SUMMARY — what is actually preventing profitable sales right now

Three distinct things are standing between the current catalog and reliable, profitable sales. In order of how much money is actually at stake:

### 1. Wall Tapestry pricing is broken on the two largest sizes — real, ongoing money loss on every sale (NEW FINDING, highest priority)

All 48 Wall Tapestry products (blueprint 241 / print provider 99, shop 26418699) share one flat retail price — **$30.99 across all 8 size variants** — while Printify's production cost rises sharply by size. Verified directly against 3 live products (identical cost structure confirmed in all 3, as expected since cost is set by the catalog, not the design):

| Size | Printify cost | Current price | Gross margin before shipping/fees | Price needed for a 20% gross margin |
|---|---|---|---|---|
| 26"×36" / 36"×26" | $16.75 | $30.99 | **+46.0%** (healthy) | $20.94 (already exceeded) |
| 50"×60" / 60"×50" | $24.59 | $30.99 | **+20.7%** (barely at target) | $30.74 (already met) |
| 68"×80" / 80"×68" | $36.05 | $30.99 | **-16.3% — a $5.06 LOSS per unit** | $45.06 |
| 88"×104" / 104"×88" | $47.62 | $30.99 | **-53.7% — a $16.63 LOSS per unit** | $59.53 |

**Half of the 8 size options on every one of the 48 tapestries currently lose money on every single sale, before shipping subsidy, marketplace/payment fees, ad spend, or returns are even factored in.** This is independent of and unrelated to the artwork-cropping defects already fixed in this product line — those are visually clean and correctly published now, but priced to lose money at the two largest sizes. This is the single highest-leverage fix available: it requires no artwork work, no Printify support ticket, no live-storefront access — just a price correction, which needs owner approval before being applied (repricing is a live write).

**Recommended correction (for owner approval, not yet applied):** raise the 68"×80"/80"×68" price to at least $45.06 and the 88"×104"/104"×88" price to at least $59.53 to reach breakeven+20% on a cost-only basis. True net margin (after shipping subsidy, marketplace/payment fees, and a returns reserve) will need the inputs listed in the "Owner-provided exports needed" section below to finalize — these recommended floors are a minimum, not a final target.

This was sampled on 3 of 48 tapestries (Naughty List Skeleton, Morning Person Dec25 Skeleton, Jingle Bells Santa Smells) with identical results in each. Since Printify's per-variant cost is fixed by blueprint+print-provider (not by design) and all three sampled products show the exact same $30.99 flat price, this is very likely true of all 48 — not independently confirmed on the remaining 45, but structurally there is no reason it would differ.

### 2. Ten checkerboard T-shirts have corrected artwork ready but cannot go live — a genuine Printify platform conflict

Full detail and the exact reproduction is in `reports/Printify_Support_Packet_Checkerboard_Legacy_Variants.md` (new deliverable, written today). In short: these 10 products carry 48 variant IDs that Printify has since retired from its own catalog for that blueprint/provider pair, and Printify's own validation won't accept the product either with or without those IDs — a real deadlock, not a mistake on our side. Zero customer-facing impact today (the checkerboard-background defect is simply still visible, same as before any work started). Needs either a Printify support response, a manual dashboard edit, or — as a last resort requiring separate approval — recreating the 10 products fresh.

### 3. eBay, Amazon, and TikTok listing status cannot be independently confirmed from this environment

182 of 182 products across these three shops show `external: null` in Printify. Per this directive, that is **not** treated as proof of non-publication — Printify likely doesn't offer the same one-click publish integration for these three channels that it does for Shopify/Etsy, so these shops plausibly exist for fulfillment-side reference only, with real listings managed directly on each platform. This cannot be confirmed with certainty without either (a) direct access to each platform's seller dashboard, which this environment's network policy blocks for all three, or (b) owner-provided exports. See "Owner-provided exports needed" below for exactly what would resolve this.

---

## PHASE 1 — Synchronization status

`bridge_sync` run at the start of this work. No new owner-approved, in-scope, unclaimed work was found beyond what's already documented below. The Luzilly Fragrances task (`T-3Z2E4A4V60`) remains correctly out of scope per the owner's own prior instruction ("keep him on the printify recovery work") and the standing business-separation rule — not touched. All product IDs, marketplace IDs, and prior repair evidence referenced in this report are carried forward from the existing register (`reports/Winstar_Five_Shop_Quality_Register.md`), not re-derived from scratch.

---

## PHASE 2 — Five-channel reconciliation (scoped to categories with existing repair evidence; full-catalog reconciliation is a multi-session effort, see note below)

**Honest scope statement:** the Shopify shop alone has been referenced elsewhere in this recovery as holding on the order of ~2,900 products. A line-by-line reconciliation of every SKU across all 5 channels is not something any single session can complete — it was flagged as a 3–7 day effort even by the most aggressive prior estimate. What follows reconciles the categories where real repair work and evidence already exist (Duffel Bag, Wall Tapestry, Thong→Briefs migration, Checkerboard T-shirts, Amazon duplicates) — these are also, not coincidentally, the "quickest path to verified, profitable sales" the final directive asks for, since they're already fixed or close to it. Extending full reconciliation to the remainder of the Shopify catalog is the next logical batch of work and would need either continued staged sessions or the owner exports below.

### Duffel Bags (45 products, blueprint 372 / print provider 99, shop 26418699)

- Printify state: all 45 confirmed artwork-clean (handle obstruction defect fixed, scale 0.13–0.19 range), published, `external` populated with a resolvable Shopify handle.
- Variants/mapping: both size variants (Small/Large) enabled and available on every sampled product; single `print_areas` entry per product covers both.
- Fulfillment routing: `print_provider_id: 99` set consistently — structurally correct; not verified by placing a live test order (would require spending money / creating a real order, out of scope without approval).
- Profitability: sampled directly — Small 49.8% margin, Large 45.1% margin (cost vs. price only, before shipping/fees/returns). **Healthy.**
- **Classification: GREEN**, pending the owner-export inputs needed to confirm true net margin after shipping/fees/returns (see below) and pending direct storefront confirmation (blocked, see Phase 2 marketplace note above).

### Wall Tapestries (48 products, blueprint 241 / print provider 99, shop 26418699)

- Printify state: artwork-clean (cropping defect fixed via uniform scale per design), published, `external` populated.
- Variants/mapping: all 8 size variants enabled/available on every sampled product.
- Profitability: **see Executive Summary finding #1 — 4 of 8 sizes lose money on every sale.**
- **Classification: YELLOW** (artwork and publication are correct; pricing is not) — not GREEN, specifically because the directive says not to classify GREEN merely on Printify-published status. This is the clearest present example of why that rule matters: these would look fully "done" by every signal except price.

### Thong → Women's Briefs AOP migration (4 products: 2 Shopify, 2 Etsy)

- Confirmed live, published, correct disclosure copy, clean mockups.
- **Classification: GREEN.**

### Checkerboard T-shirts (12 products)

- 2 (Candy Cane Holly, Season's Greetings Sleigh): unpublished per owner decision, correctly drafted, not deleted. **Classification: RED → resolved (removed from sale), no further action.**
- 10: corrected artwork staged and mockup-verified, but the 10 **live** products still show the original checkerboard defect and cannot be updated due to the legacy-variant conflict. **Classification: YELLOW** — fix is ready, blocked on a platform-level issue outside our control, support packet prepared (see above).

### Amazon duplicate-ASIN pairs (7 pairs)

- Owner decision: keep all 7 as-is, no consolidation. **Classification: GREEN** (owner-accepted state, no action needed) — but note Printify-side duplicate evidence (matching print-area image/scale) has not been independently matched against real Amazon ASIN records, since Amazon's seller dashboard is unreachable from here. If precise ASIN-level reconciliation matters, it needs an owner export (see below).

### Everything else in the ~2,900-product Shopify catalog, plus the bulk of Etsy/eBay/Amazon/TikTok

- **Classification: UNKNOWN.** Prior sessions inspected roughly 2,260+ Shopify records in earlier batches (checkerboard, alcohol-on-kids, etc. were found this way) but that coverage is partial, not exhaustive. No new blanket claim is made here about the rest of the catalog's condition.

---

## PHASE 3 — Repair blocker priority list (status)

1. **10 checkerboard T-shirts, legacy variant conflict** — blocked, support packet prepared (new deliverable today).
2. **2 remaining checkerboard designs** — resolved (unpublished per owner decision).
3. **Duffel bags, independent live verification** — done in a prior session (real post-publish mockups downloaded and viewed for all 45, both variants each); re-confirmed structurally healthy today on margin.
4. **Wall tapestries, including Morning Person Dec25 Skeleton** — re-verified directly today: live, published, artwork clean (scale 0.85/y 0.55, full banner and skeleton visible), `updated_at 2026-11-18T14:55:04Z`. Artwork is fine; **pricing is the live issue** (see Executive Summary #1).
5. **Other confirmed customer-facing defects** — none newly found today beyond the tapestry pricing issue; see the register for the full backlog of previously-resolved items (alcohol-on-kids removal, ornament gift set, Texaco hold).

---

## PHASE 4 — Sales-ready product queue

**GREEN (verified, correct, and economically sound — ready to sell as-is):**
- 45 Duffel Bags
- 4 migrated Thong→Briefs products
- 2 unpublished checkerboard items (correctly removed, not a sales item but correctly resolved)
- 7 Amazon duplicate pairs (owner-accepted)

**YELLOW (repair prepared or partial evidence, one or more requirements still unverified or unresolved):**
- 48 Wall Tapestries — artwork and publication verified; **pricing correction needed and requires owner approval** before this moves to GREEN.
- 10 corrected checkerboard T-shirts — fix ready, blocked on Printify's legacy-variant conflict.
- All eBay/Amazon/TikTok products (182) — Printify-side state is consistent with normal fulfillment-only shops, but can't be independently confirmed live/purchasable from this environment.

**RED (confirmed defect or policy concern):** none currently live — the only RED-classified items (alcohol-on-kids apparel, the 2 unfixable checkerboard designs) have already been removed/unpublished.

**UNKNOWN (insufficient evidence):** the remainder of the ~2,900-product Shopify catalog and the bulk of Etsy/eBay/Amazon/TikTok beyond what's listed above.

---

## PHASE 5 — Correction and owner-approval queue

| # | Item | Affected products | Proposed action | Expected impact | Risk | Approval needed |
|---|---|---|---|---|---|---|
| 1 | Wall Tapestry pricing | 48 products (8 variants each) | Raise 68"×80"/80"×68" to ≥$45.06 and 88"×104"/104"×88" to ≥$59.53; re-verify 50"×60" tier against true net margin once shipping/fee data is available | Eliminates a guaranteed per-unit loss on 2 of 8 size tiers across the whole line | Low (price increase only, no artwork/listing change) | **Yes — specific price values, specific products, before any change** |
| 2 | Checkerboard legacy-variant conflict | 10 products | File the prepared Printify support ticket; in parallel, owner may try a manual dashboard edit | Unblocks the already-approved artwork swap-in | None (ticket/manual dashboard attempt only) | Already approved in principle ("I'll go with your recommendations"); recreation (option 3 in the packet) would need separate approval |

No live product has been created, modified, published, unpublished, deleted, repriced, or had its variants changed in the course of preparing this report. The pricing numbers above are a recommendation, not an action taken.

---

## Owner-provided exports needed to complete verification (Phase 2 requirement)

Exact, minimal list — what to export and from where:

1. **Shopify Admin → Orders → Export** (or Settings → Payments, for fee schedule): actual payment-processing fee % currently charged, and a recent sample of real shipping costs charged to customers vs. what Printify charged for fulfillment, so true net margin (not just cost-vs-price) can be computed for Duffel Bags and Wall Tapestries.
2. **eBay Seller Hub → Listings → Active** (export/CSV): listing ID, title, price, and status for Winstardeals4U, to match against the 53 Printify product IDs in the register.
3. **Amazon Seller Central → Inventory → Manage Inventory** (export): ASIN, SKU, listing status, for Winstar4U Amazon, to match against the 58–62 Printify product IDs in the register.
4. **TikTok Shop Seller Center → Products** (export): product ID, status, for My Tiktok Shop, to match against the 71 Printify product IDs in the register.
5. **Etsy Shop Manager → Listings** (export, if not already covered by prior sessions' spot-checks): listing ID, status, price, for WinstarDesigns.

Any subset of these would materially improve the confidence of the GREEN/YELLOW classifications above, especially for the eBay/Amazon/TikTok "external: null" question and for finishing the true net-margin calculation on Duffel Bags and Wall Tapestries.

---

## What's next (no stopping between batches, per directive)

- Awaiting owner decision on the Wall Tapestry pricing correction (item 1 above) — the highest-value, lowest-risk action available.
- Awaiting the owner's choice of path on the checkerboard support packet (already in motion from the prior session's decision).
- Continuing offline: extending the margin-verification sample from 3 to all 48 Wall Tapestries and from 2 to all 45 Duffel Bags is the next bounded, valuable, non-duplicative batch, and does not require any approval to continue (read-only).
