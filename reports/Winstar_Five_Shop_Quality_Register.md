# Winstar Five-Shop Printify Quality Register (durable, running document)

**Status:** LIVE WORKING DOCUMENT — updated incrementally across sessions/batches. This is the single
source of truth requested by the owner; do not recreate parallel registers. Append new rows/sections
rather than rewriting history.

**Owner directive in force (2026-11-17):** Five-shop Printify quality recovery is the standing top
priority. Continuous, nonoverlapping batches across all five shops until every product is assessed.
No live writes (publish/unpublish/price/inventory/account changes) without explicit separate owner
approval. This file tracks real, evidence-backed findings only — no estimates presented as fact.

## 0. Shop directory

| Shop name | Shop ID | Channel | Total products (last confirmed count) |
|---|---|---|---|
| Winstar4U | 26418699 | Shopify | 2,429 |
| Winstar Etsy Store | 26603005 | Etsy | 297 (confirmed via page-by-page walk, supersedes earlier ~287 estimate) |
| Winstardeals4U | 28059412 | eBay | 53 |
| My Tiktok Shop | 28122957 | TikTok | 71 |
| Winstar4U Amazon | 29451844 | Amazon | 62 |
| **Total** | | | **2,912** |

## 1. Shop-level sync-status summary (full population, not samples, where marked)

| Shop | Sync-checked | Gap (external null) | Gap rate | Coverage type |
|---|---|---|---|---|
| eBay (28059412) | 53/53 | 53 | 100% | FULL POPULATION |
| Amazon (29451844) | 62/62 | 45 | 72.6% | FULL POPULATION |
| TikTok (28122957) | 71/71 | 32 | 45.1% | FULL POPULATION |
| Etsy (26603005) | 50/297 | 10 | 20% (of sample) | SAMPLE |
| Shopify (26418699) | ~160/2,429 full-detail metadata; 9/~460 individually sync-checked beyond that | high in sampled ranges (see §3) | varies by batch | SAMPLE, uneven |

**Standing caveat (do not override):** `external: null` / `sales_channel_properties: []` on Printify is
evidence of an absent Printify→marketplace mapping only. It is NOT by itself proof a listing is absent
from the live marketplace storefront — a direct marketplace-side check is required before treating any
SKU as confirmed unsellable or proposing deactivation/resync. No such direct marketplace-side check has
been performed for any SKU in this register as of this entry.

## 2. RESOLVED — the owner's original cribbage-ornament complaint (highest-priority item, now closed out)

**Product:** "Cribbage Board Christmas Tree Christmas Ornament 2026" — Printify ID
`6ad4254232b024bb32043467`, Etsy shop 26603005, live at
https://www.etsy.com/listing/4597769027/cribbage-board-christmas-tree-christmas

**Finding (2026-11-17, this session, actual mockup image downloaded and viewed):** CONFIRMED DEFECT.
Root cause identified: this Etsy-shop listing's print-area places the source photo
(`cribbage-tree-board.jpg`, image id `6ac76dd5f3e4ecb70e96dcdc`) at **scale 1.45**, filling the entire
ornament edge-to-edge with no border padding. This crops out the gold star topper and both side edges
of the wooden cribbage board, so the "cribbage board" context that makes the design legible is largely
lost — the viewer mostly sees a dense cluster of gold pegs that doesn't read clearly at thumbnail size.
Confirmed on both the Circle and Heart mockups.

**Comparison / proof of root cause:** The *same* source image (same `imageId`) is used on a separate,
sibling Printify record for the identical design in the **Shopify** shop (ID `6ac76f2bd317fcb1e80f4bb8`),
where it is placed at **scale 0.8**. That version is clean — full board visible, proper white-space
border, star topper and both edges intact. Side-by-side, this proves the defect is a per-listing
scale/placement setting, not a flaw in the source artwork itself, and gives an exact, low-risk fix.

**Proposed remedy (owner-approval-only — NOT executed):** Reduce the Etsy-listing print-area scale from
1.45 to approximately 0.8 (matching the clean Shopify copy) via Printify's product-update API, then
regenerate mockups. This is a live write and requires explicit owner approval before any attempt.

**Status:** YELLOW→confirmed RED (customer-facing visual defect), sync status GREEN (genuinely live).
Image evidence: both mockups downloaded and visually inspected this session.

**Sibling record also checked:** "Reindeer Cribbage Peg Race Christmas Ornament 2026" exists as a pair
across both shops too — Etsy ID `6ad4307c18e0243bd10d533d` (not yet re-viewed this session) and Shopify
ID `6ac76f3288d05d5634004c1a` (viewed this session, clean, scale not yet compared — flagged for a
follow-up scale check against its Etsy twin).

## 3. Confirmed visual defects (actual mockup image opened and inspected — not metadata-inferred)

| Printify ID | Shop | Title | Defect | Evidence |
|---|---|---|---|---|
| 6ad4254232b024bb32043467 | Etsy 26603005 | Cribbage Board Christmas Tree Ornament | Over-scaled photo (1.45x) crops star + board edges | Image viewed 2026-11-17, this session |
| 6ac8f919149425f38d04bedd | Shopify 26418699 | Dracula With A Drink Halloween Ornament | Illustration cropped at left/bottom edge, excess blank space | Image viewed prior session (T-2I3N01430E) |
| 6ac8f8f29b2660e139034102 | Shopify 26418699 | Basic Witch Halloween Ornament | "B" and "C" of text clipped by circular edge | Image viewed prior session (T-2I3N01430E) |

## 4. Confirmed CLEAN on visual inspection (no defect found — real images opened)

| Printify ID | Shop | Title |
|---|---|---|
| 6ac76f2bd317fcb1e80f4bb8 | Shopify 26418699 | Cribbage Board Christmas Tree Ornament (Shopify copy) |
| 6ac76f3288d05d5634004c1a | Shopify 26418699 | Reindeer Cribbage Peg Race Ornament (Shopify copy) |
| 6ac8f0e30a804851a800986b | Shopify 26418699 | Boo Crew Halloween Ornament |
| 6ac787d6b0e9879054061f08 | Shopify 26418699 | Funny Ornament Gift Set of 3 (raccoon design shown) |
| 6acf7900e87647fdb402d5db | Shopify 26418699 | Dog Mom Christmas T-Shirt (the one synced product in the #161-260 batch) |
| 6acf8436e87647fdb402e201 / 6acf842fac15b498a10fdde6 | Shopify 26418699 | "Electricians Make a Merry Christmas" (2 of the 4 duplicate-titled listings — confirmed genuinely different designs, not a visual duplicate) |
| 5 Etsy hoodies (6af90c15626b8d7aa001936c, 6af90c02383728621d011dd8, 6af90bdec745d035040e95ab, 6af90bf06d67bf35520cbead, 6af90b7eca5d307abc016117) | Etsy 26603005 | Christmas hoodies, batch 1 |
| 5 Amazon tees (6af1072a421fd94ad304e54b, 6af1073ce16bc2f471089f76, 6af10718421fd94ad304e53e, 6af1070681fb6450380f0dda, 6af106f4421fd94ad304e520) | Amazon 29451844 | Christmas tees, batch 1 |
| 4 Shopify + 4 eBay + 3 TikTok (batch 2, see T-6N0T120Q2R evidence for exact IDs) | mixed | Christmas/holiday designs |
| 9 more sync-gap products visually spot-checked (batch 2 supplementary, T-1G273I5V6Z) | mixed | see that task's evidence for exact IDs |

**Important nuance:** Visual defects are NOT uniform across the ornament blueprint. 6/9 ornaments
actually opened across this whole investigation are clean; 3/9 show a defect. The defect is
design/placement-specific (a scale or margin setting on that specific listing), not a flaw in the
ceramic-ornament blueprint itself. Do not generalize "all ornaments are defective" from the 3 confirmed
cases — each must be checked individually.

## 5. Duplicate-title findings (exact title collisions within Printify, product-type-specific)

| Title | Shop | Product type | IDs | Status |
|---|---|---|---|---|
| "Adulting Is A Witch Stress And Then You Fly" | Shopify 26418699 | T-Shirt (2x) | see T-2I3N01430E | Not visually compared |
| "Adulting Is A Witch Stress And Then You Fly" | Shopify 26418699 | Ornament (2x) | 6ac8f8eff06adcd24901f872, 6ac8f8ebaf7641b637093735 | Confirmed different artwork files, not visual duplicates |
| "Adulting Is A Witch Stress And Then You Fly" | Shopify 26418699 | Mug (2x) | 6ac8f402f06adcd24901f310, 6ac8f3ff9b2660e139033c22 | Not yet visually compared |
| "Santa's Blood Pressure Is Through the Roof!" | Shopify 26418699 | T-Shirt (2x) | 6acf85acefdf69fc8202c68c, 6acf85a63c4fbad1a80e6b79 | Not yet visually compared |
| "Hairstylists Make the Holidays Brighter" | Shopify 26418699 | T-Shirt (2x) | 6acf84958d1c8ce67a0c691a, 6acf848e24fd66683e02e7a6 | Not yet visually compared |
| "Electricians Make a Merry Christmas" | Shopify 26418699 | T-Shirt (4x) | 6acf8436e87647fdb402e201, 6acf842fac15b498a10fdde6, 6acf8428efdf69fc8202c58d, 6acf8421ac15b498a10fddd0 | 2 of 4 confirmed genuinely different designs under a reused title (not duplicate artwork) |

**Pattern:** the "Adulting Is A Witch..." phrase alone now recurs across 3 separate product types
(Shirt, Ornament, Mug), each as a duplicate-titled pair. This looks like a recurring upload-template
reuse habit, worth flagging to the owner as a process issue (title field not being made unique per
upload), separate from any individual artwork defect.

## 6. Full per-product-ID evidence trail (pointer index — do not duplicate text here, see cited sources)

Exact per-ID tables with prices, variant counts, creation timestamps, and full evidence text live in:
- `reports/Printify first-ten inspection packet.md` (Etsy+Amazon batch 1, 10 IDs)
- `reports/Printify correction-approval packet (first).md` (Shopify+eBay+TikTok batch 2, 11 IDs)
- `reports/Printify catalog coverage - day 1 (continuation).md` (386-ID metadata scan, eBay/Amazon/TikTok full population + Shopify/Etsy samples)
- Bridge tasks (task_get is the canonical record): T-6N0T120Q2R, T-1G273I5V6Z, T-43490W6I59, T-3Z3C272349, T-3G0X1D6L3U, T-2I3N01430E, T-2Q310Z6F4J, T-3T231J5L21

## 7. Shopify catalog position tracker (most important coverage gap — 2,429 of 2,912 total products)

| Range | Status | Task |
|---|---|---|
| #1-150 | Metadata-sampled (sync status only) | T-1G273I5V6Z |
| #151-160 | Metadata+sync, 0 images | T-43490W6I59 |
| #161-260 | Metadata+sync (9 IDs) + 5 images viewed | T-2I3N01430E |
| #261-360 | Metadata (100/100) + sync (9 IDs) + 6 images viewed | T-2Q310Z6F4J (this session) |
| #361-2,429 | **NOT STARTED** (2,069 products) | Next batch(es) |

## 8. Next eligible batch (for whichever session/dispatcher firing picks this up next)

1. Shopify shop 26418699, pages 37 onward (product #361+), 10 pages (100 products) at a time, using
   compact list calls first (cheap) and individual `product_id` full-detail pulls for sync-status on a
   meaningful sample per batch, prioritizing ornament/mug/shape-sensitive categories for actual image
   viewing.
2. In parallel (smaller, more tractable — consider finishing these to 100% before continuing deep into
   Shopify): eBay (53 total, 53/53 sync-known, only ~7 visually inspected — ~46 remain for visual-only
   pass), Amazon (62 total, 62/62 sync-known, ~7 visually inspected — ~55 remain), TikTok (71 total,
   71/71 sync-known, ~5 visually inspected — ~66 remain), Etsy (297 total, only 50 sync-sampled, 5
   visually inspected — both metadata and visual coverage remain large).
3. Direct marketplace-side verification (actually checking eBay/Amazon/TikTok/Shopify storefronts, not
   just Printify's `external` field) for at least the highest-volume confirmed-gap SKUs, before any
   resync/repair is proposed for owner approval.
4. Scale-value audit: for every duplicate-shop-record pair found (same design, Etsy + Shopify copies),
   compare the print-area `scale` value the way this session did for the cribbage ornament — this is a
   fast, high-value check once a pair is identified, and already found one real defect this way.
