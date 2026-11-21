# Wall Tapestry Pricing Correction — Owner Approval Packet

**Prepared:** 2026-11-19 · **Status:** READ-ONLY PLAN. No price has been changed. Every change below needs explicit owner approval.
**Scope:** 48 Wall Tapestries, Printify shop 26418699 (Winstar4U Shopify), blueprint 241 / provider 99. 48 × 8 = **384 variants**.
**Full per-variant table (384 rows, exact product ID + variant ID):** `reports/Winstar_Tapestry_Pricing_Correction_Table.csv`
**Inputs reused, not re-fetched:** cost + current price for all 48 products from the 48/48 live verification (commits 0d86c9f, 8b1fc8c; Bridge P-230L64342K). **One new API call:** blueprint 241/provider 99 shipping profile (2026-11-19).

## Assumptions (stated, owner can change)

| Input | Value | Source |
|---|---|---|
| Production cost | $16.75 / $24.59 / $36.05 / $47.62 by size | VERIFIED, live Printify reads, all 48 |
| US shipping, first item | $5.69 / $6.99 / $9.29 / $9.29 | VERIFIED Printify shipping profile; the higher of the two US profiles per size (conservative) |
| Transaction fee | 2.9% + $0.30 | ASSUMED (Shopify Payments, Basic plan). Not verified against this store's actual payment settings |
| Returns allowance | 5% of price | ASSUMED. POD sells most items final-sale; 5% covers misprint reprints/refunds |
| Target | ≥20% net margin | Owner directive |

Formula: net = price − cost − shipping(if absorbed) − (2.9% × price + $0.30) − 5% × price.
Minimum price for 20% net = (cost + shipping + $0.30) ÷ 0.721.

- **Scenario A — customer pays shipping:** shipping is excluded from merchant cost.
- **Scenario B — merchant absorbs shipping (free shipping):** shipping included.
- **Not verified:** which scenario Winstar4U actually uses. Each product carries a Shopify `shipping_template_id`, but the rates in those templates are not visible through Printify. **The owner should confirm this before approving** — it changes which price column applies.

## Results by size tier (47 flat-priced products at $30.99)

| Size (variant IDs) | Cost | Net % at $30.99, A | Net % at $30.99, B | Min price for 20% net, A | Min price for 20% net, B | **Recommended price** |
|---|---|---|---|---|---|---|
| 26×36 / 36×26 (41686, 46152) | $16.75 | 37.1% ✅ | 18.7% ⚠️ | $23.65 | $31.54 | **$31.99** |
| 50×60 / 60×50 (41687, 46153) | $24.59 | 11.8% ⚠️ | **−10.8%** ❌ | $34.52 | $44.22 | **$44.99** |
| 68×80 / 80×68 (45130, 46154) | $36.05 | **−25.2%** ❌ | **−55.2%** ❌ | $50.42 | $63.30 | **$63.99** |
| 88×104 / 104×88 (61899, 46151) | $47.62 | **−62.5%** ❌ | **−92.5%** ❌ | $66.46 | $79.35 | **$79.99** |

The recommended column is the Scenario B price. It reaches ≥20% net in both scenarios, so it is safe even before the owner confirms the shipping setup. If the owner confirms customers pay shipping, the lower Scenario A prices are $23.99 (keep $30.99), $34.99, $50.99 and $66.99.

**Chic Happens Cocktail** (`6ac70ebbf0a0ce97bc0c8ff2`), currently $34.99 / $34.99 / $40.99 / $52.99:
- Scenario A net: 43.4% / 21.0% / 3.4% / 1.7%
- Scenario B net: 27.1% / 1.0% / −19.2% / −15.9%

It needs the same top-three-tier correction. Its smallest tier already clears 20% at $34.99, so keep that price.

## Reconciliation — the "188 below-cost size options"

**Confirmed: 188 = 47 products × 2 sizes (68×80 and 88×104) × 2 orientations.** The price is below production cost alone, before shipping, fees or returns. Chic Happens has 0 below-cost variants. 47 × 4 = 188, exactly.

Classification of all 384 variants at current prices:

| Risk | Count | What it covers |
|---|---|---|
| 🔴 RED — price below production cost | **188** | 68×80 and 88×104 tiers, 47 products |
| 🟠 AMBER — under 20% net in both scenarios | **98** | 50×60 tier on 47 products (94) + Chic Happens 68×80 / 88×104 (4) |
| 🟡 AMBER — under 20% net only if shipping is absorbed | **96** | 26×36 tier on 47 products (94) + Chic Happens 50×60 (2) |
| 🟢 GREEN — at least 20% net in both scenarios | **2** | Chic Happens 26×36 / 36×26 |

Under merchant-absorbed shipping, **286 of 384 variants lose money on every sale** (188 + 94 at 50×60 + 4 Chic Happens).

## Owner decision (pick one per line — nothing executes without it)

1. **Approve repricing the 47 flat-priced tapestries** to $31.99 / $44.99 / $63.99 / $79.99 by size tier, using the variant IDs above. Alternative: approve the Scenario A prices after confirming customers pay shipping.
2. **Approve repricing Chic Happens Cocktail** to $34.99 (keep) / $44.99 / $63.99 / $79.99.
3. **Optional, lower-risk interim step:** disable variants 45130, 46154, 61899 and 46151 (the two largest sizes) on all 48 products until repricing is decided. This stops loss-making orders immediately without touching the prices customers see on the popular sizes.
4. **Conversion risk:** $79.99 for the largest tapestry is a big jump from $30.99. If the owner considers it unsellable, option 3 (drop the two large sizes permanently) avoids the loss without the price shock.

Execution, once approved: one `printify-set-product-prices` call per product (48 calls), then a re-fetch to verify. Re-publish only if Printify requires it to push prices to Shopify.

---

## Duffel Bag mapping investigation — 5 products with no `external` field

| Product | Printify ID | Printify `updated_at` (2026-11-18 UTC) |
|---|---|---|
| Dreaming Stress Free Christmas | `6ac70ec73925bc76b9037099` | 14:04:16 |
| Blessed Christmas | `6ac70ed8050d0f25a70917f4` | 14:04:19 |
| God Bless Christmas | `6ac70ee24bfa32451c0548b1` | 14:04:22 |
| Greatest Gift | `6ac70ee64bfa32451c0548b6` | 14:04:24 |
| Joy To World Christian | `6ac70eed0aa3686f380d3c23` | 14:04:27 |

**Evidence (all read-only):**

1. **VERIFIED:** All 5 return `visible: true` with no `external` key. The other 40 duffels all carry an `external` Shopify ID and handle (live fetch, 2026-11-19).
2. **VERIFIED:** All 5 were updated within 11 seconds of each other. The register (lines 548–562) records that this session upserted 8 duffels at that moment to fix artwork scale, while a parallel session was editing the same products (one upsert hit Printify error 8252, "disabled for editing"). The other 3 of those 8 (Christmas Calories Dont Count, Dear Santa Explain, Deck The Halls Sit Down) kept their `external` mapping.
3. **BLOCKED — Shopify side:** the public Winstar4U storefront (4juy1i-kq.myshopify.com) is refused by this environment's egress proxy. The Shopify app connected to this session is a different store, "Winstar Marketing" (winstarmarketing.shop). A control search there also fails to find a correctly mapped Winstar4U duffel (Christmas Wishes Sta), so that store cannot answer the question.
4. **Most likely explanation (not confirmed):** the concurrent edits on Nov 18 left these 5 in a lost-sync state. The Shopify listing may still exist but be unlinked, or may have been removed. Printify no longer tracks it, so future artwork or price updates will not reach Shopify, and orders may not route to fulfillment.

**Next step:**
- **Owner (2 minutes):** in Winstar4U Shopify admin, search for the 5 titles and report whether each listing exists and is active.
- **Then, only with approval:** re-publish the 5 from Printify, which re-links the mapping. If old listings exist, decide first whether to keep them (they hold any reviews and sales history) or let Printify create fresh ones.

---

## Next five highest-impact unblocked actions (after this packet)

1. **Owner decision on tapestry pricing** (this packet). Every sale of a large tapestry loses $5–$27 today. This is the single biggest money leak found.
2. **Confirm Winstar4U shipping settings** (does the customer pay?). This settles the Scenario A vs B choice for all products, not only tapestries. It is a single checkbox in Shopify admin.
3. **Re-link the 5 unmapped duffel bags** (owner check above, then a Printify re-publish with approval). These are 5 live-looking products that may not be orderable.
4. **Submit the checkerboard Printify support ticket** (`reports/Printify_Support_Packet_Checkerboard_Legacy_Variants.md`, ready). It unblocks 10 corrected T-shirts, and the owner already chose this path.
5. **Approve the 10 staged checkerboard T-shirt swap-ins** (Bridge T-4P5P5J571N) once support resolves the variant conflict. Those are visibly broken products customers can see today.

Deliberately not on this list: new engineering, new product creation, and further catalog-wide inspection.
