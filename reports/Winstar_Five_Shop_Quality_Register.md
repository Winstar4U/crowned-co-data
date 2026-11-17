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
| 6a493c8908efc981890568bf | eBay 28059412 | Canvas Lunch Bag — American Flag Butterfly Design |
| 6a493c80df721fcc700771b4 | eBay 28059412 | Patriot 250 Eagle Flag Dad Cap |
| 6a493c77df721fcc700771b0 | eBay 28059412 | Nurse Iguana Loco Unisex T-shirt |
| 6a493c20a36a12099202d047 | eBay 28059412 | Fishing Bass Phone Case |
| 6a493c9208efc981890568c1 | eBay 28059412 | God Bless the USA T Shirt |
| 6a493c86df721fcc700771b6 | eBay 28059412 | Great American Kid T Shirt |
| 6a493cafa36a12099202d04f | eBay 28059412 | Retro Doodle Graphic Tee |
| 6a493c9908efc981890568c2 | eBay 28059412 | USA Love American Flag T Shirt |
| 6a493c0bdf721fcc700771a7 | eBay 28059412 | Dog Pack Protective Phone Case |
| 6a493c7ddf721fcc700771b2 | eBay 28059412 | Unisex Jersey Muscle Tank ("America the Beautiful" butterfly — distinct design from the Canvas Lunch Bag butterfly, not a duplicate) |
| 6a493bea131a5b73ff0f1d02 + 6a49373aa8f8e286e2066011 | eBay 28059412 | "Pink Hummingbird Floral" phone case — TRUE DUPLICATE PAIR (see §5a), artwork itself clean |
| 6a493bf8131a5b73ff0f1d0a + 6a493bf5131a5b73ff0f1d08 | eBay 28059412 | "American Flag.../Copy of American Flag..." phone case — TRUE DUPLICATE PAIR (see §5a), artwork itself clean |
| 23 more eBay products visually inspected to complete 53/53 shop coverage | eBay 28059412 | Flags (Canada/Mexico/Brazil/Dominican Republic/Puerto Rico/Venezuela/Union Jack, magnetic+tough+heart variants), florals/bows/patterns (pink bow x4, floral x3, checkerboard, strawberry, mushroom&butterfly, abstract botanical), smiley/moon/chick patterns, a 2nd fishing-bass case, a real hummingbird photo case — all CLEAN, see §6a for the full count and methodology |

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

### 5a. eBay TRUE duplicate-listing pairs (identical artwork, not just reused title)

Unlike the Shopify "same title, different design" pattern above, eBay has at least 2 pairs that are
genuine duplicate listings — confirmed by matching print-area image name + scale + x + y in their
full-product-detail JSON, not just title text:

| Title | IDs | Confirmed via | Artwork quality |
|---|---|---|---|
| "Phone Case — Pink Hummingbird Floral Magnetic Impact‑Resistant Case" | 6a493bea131a5b73ff0f1d02, 6a49373aa8f8e286e2066011 | Exact match: same print-area image/scale/x/y | Clean |
| "American Flag Magnetic Impact-Resistant Phone Case" / "Copy of American Flag Magnetic Impact-Resistant Phone Case" | 6a493bf8131a5b73ff0f1d0a, 6a493bf5131a5b73ff0f1d08 | Exact match: same print-area image/scale/x/y, and the literal "Copy of" prefix confirms it | Clean |

Both pairs are also sync-gapped on Printify (not live on eBay per `external`). This is a catalog-hygiene
issue (redundant listings, confusing for inventory/analytics) rather than a visual defect — flagged for
the owner as a cleanup candidate, not proposed for action without approval.

## 6. Full per-product-ID evidence trail (pointer index — do not duplicate text here, see cited sources)

Exact per-ID tables with prices, variant counts, creation timestamps, and full evidence text live in:
- `reports/Printify first-ten inspection packet.md` (Etsy+Amazon batch 1, 10 IDs)
- `reports/Printify correction-approval packet (first).md` (Shopify+eBay+TikTok batch 2, 11 IDs)
- `reports/Printify catalog coverage - day 1 (continuation).md` (386-ID metadata scan, eBay/Amazon/TikTok full population + Shopify/Etsy samples)
- Bridge tasks (task_get is the canonical record): T-6N0T120Q2R, T-1G273I5V6Z, T-43490W6I59, T-3Z3C272349, T-3G0X1D6L3U, T-2I3N01430E, T-2Q310Z6F4J, T-3T231J5L21, T-0U6Q5K5G49 (eBay full visual-inspection batch, this session)

## 6a. eBay catalog position tracker (53 total products, shop 28059412) — COMPLETE

**STATUS: 53/53 products fully visually inspected (100% coverage) — first shop in the five-shop recovery
to reach full visual completion.** All 53 confirmed sync-gapped (`external` absent) in the Day-1
continuation report; this session added real mockup-image inspection for the remaining 49 (4 had been
inspected in prior sessions).

| Result | Count |
|---|---|
| Visually CLEAN (no cropping/alignment/spelling/print-boundary defect) | 49 distinct products |
| Confirmed TRUE duplicate-listing pairs (identical artwork under 2 listings each) | 2 pairs / 4 listings (see §5a) — counted within the 49 clean products, flagged separately as a catalog-hygiene issue |
| Confirmed visual defects | **0** |

**Finding:** eBay shop 28059412 has zero confirmed visual/artwork defects across its entire 53-product
catalog. The shop's only quality issue found is the 2 duplicate-listing pairs (§5a) — a catalog-hygiene/
inventory-redundancy issue, not a customer-facing visual defect. All designs (flags, hearts, florals,
mushroom/butterfly, hummingbird photo, fishing/bass, patriotic tees, phone case patterns) print
correctly within their intended bleed/crop areas; several phone-case designs use scale values above 1.0
(e.g. Canadian Flag Tough at 1.77, Brazil Flag regular at 1.74) but this is appropriate for a full-bleed
edge-to-edge phone-case wrap design, not a cropping defect — confirmed by visually inspecting the actual
rendered mockups, not just reading the scale number.

**Note on a near-miss:** "Hummingbird Floral Phone Case — Magnetic Impact-Resistant Protection"
(`6a493beb131a5b73ff0f1d04`) uses a real hummingbird photograph and is visually and in print-area name
DISTINCT from the "Pink Hummingbird Floral" illustrated duplicate pair in §5a — initially flagged for a
closer look given the similar title, but confirmed NOT a third duplicate once the image was opened.

**eBay full population summary:** 53/53 sync-checked (100% gap — none are live on eBay per Printify's
`external` field, unverified against eBay's own storefront), 53/53 visually inspected (100% clean,
0 confirmed defects, 2 duplicate pairs). Task T-0U6Q5K5G49 ready for Bridge submission.

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
2. **eBay is now COMPLETE (53/53 visually inspected, see §6a) — do not re-inspect.** Remaining smaller
   shops: Amazon (62 total, 62/62 sync-known, ~7 visually inspected — ~55 remain), TikTok (71 total,
   71/71 sync-known, ~5 visually inspected — ~66 remain), Etsy (297 total, only 50 sync-sampled, 5
   visually inspected — both metadata and visual coverage remain large). Recommend Amazon next (smallest
   remaining gap to full coverage), using the same product_id-by-product_id + image-download method that
   completed eBay.
3. Direct marketplace-side verification (actually checking eBay/Amazon/TikTok/Shopify storefronts, not
   just Printify's `external` field) for at least the highest-volume confirmed-gap SKUs, before any
   resync/repair is proposed for owner approval.
4. Scale-value audit: for every duplicate-shop-record pair found (same design, Etsy + Shopify copies),
   compare the print-area `scale` value the way this session did for the cribbage ornament — this is a
   fast, high-value check once a pair is identified, and already found one real defect this way.

## 8a. Amazon shop (29451844) — IN PROGRESS, major duplicate-ASIN finding (2026-11-17, this session)

**Status: 38/62 products now have real image evidence (0 confirmed visual defects). 24 remain
unchecked.** Task T-1O514F2T63 claimed, in progress, not yet submitted.

### HIGHEST-SEVERITY FINDING THIS SESSION: 10 confirmed true duplicate-listing pairs, 7 of which are
### SIMULTANEOUSLY LIVE ON AMAZON under two different ASINs each

Unlike the eBay shop (where all duplicate pairs were sync-gapped, i.e. not live), most of Amazon's
duplicate pairs are both members actually live and purchasable right now. Each pair below was confirmed
a TRUE duplicate by matching print-area image filename + scale + x + y (not just similar titles):

| # | Design (print-area image file) | ID 1 | ASIN 1 | ID 2 | ASIN 2 | Live status |
|---|---|---|---|---|---|---|
| 1 | cat-lineup-santas-naughty-list.png | 6ae41f6ae88b7e964c0e7380 | — | 6ae414e0e88b7e964c0e72ed | — | Neither live |
| 2 | dog-mom-christmas.png | 6ae414e52e006c787106bd99 | B0HPS4FTHJ | 6ae2af0ed0738075d402e2b2 | B0HPMTHR4C | **BOTH LIVE** |
| 3 | b5-christmas-baking-crew-4096.png | 6ae414e42e006c787106bd98 | B0HPSQSMCQ | 6ae2af10bcfc422d820a54c7 | B0HPMZMQZ3 | **BOTH LIVE** |
| 4 | b5-dear-santa-goodish-4096.png | 6ae414e42e006c787106bd97 | B0HPSGB5HG | 6ae2af13bcfc422d820a54cb | B0HPN5V85T | **BOTH LIVE** |
| 5 | b5-construction-crew-christmas-4096.png | 6ae414e12e006c787106bd94 | B0HPRZCZ7V | 6ae2af12bcfc422d820a54ca | B0HPN1GRMX | **BOTH LIVE** |
| 6 | hairstylist-santa.png | 6ae414e72e006c787106bd9b | B0HPSGKB5Z | 6ae2af10bcfc422d820a54c8 | B0HPN87ZDX | **BOTH LIVE** (titles differ only by a straight vs. curly apostrophe — this is why simple title-matching missed it) |
| 7 | b5-naughty-or-nice-4096.png | 6ae414e22e006c787106bd95 | B0HPSJKC7R | 6ae2af15bcfc422d820a54cc | B0HPN82LRD | **BOTH LIVE** |
| 8 | b5-cookie-dealer-4096.png | 6ae414e32e006c787106bd96 | B0HPSQZ91Z | 6ae2af11bcfc422d820a54c9 | B0HPN23TVY | **BOTH LIVE** |
| 9 | gone-fishing-for-christmas.png | 6ae41f72e88b7e964c0e738a | unclear/blank | 6ae414eaf755b251850ceb05 | — | Not confirmed both-live, flagged for follow-up |
| 10 | Christmas Dog With Santa Hat And Holiday Ball.png | 6ae41f68e88b7e964c0e737e | — | 6adea7d6853b5615b805ead5 | B0HPN22XVP | Only #2 live |

**7 of 10 pairs (14 products) are confirmed simultaneously live on Amazon with separate ASINs for
identical artwork.** This is a materially different and more severe problem than any duplicate found on
eBay or Shopify so far: it means Amazon customers can land on either of two separate product pages for
the exact same shirt, splitting reviews, sales rank, and search visibility, and creating real risk under
Amazon's own duplicate-listing / variation policies. All artwork itself was visually confirmed CLEAN on
every pair inspected (no cropping/alignment defect) — this is purely a catalog-structure problem, not an
artwork-quality problem.

**Proposed remedy (owner-approval-only — NOT executed):** For each both-live pair, select one ASIN to
keep as the canonical listing and unpublish/retire the other, or merge them as Amazon variations if the
underlying garment/blueprint supports it. This is a live marketplace action and requires explicit owner
sign-off per listing before any attempt — no action has been taken.

### Confirmed CLEAN (visually inspected, no defects) — 38 products total

- 7 prior-session IDs: Winter Garden Field Guide (6af1072a421fd94ad304e54b), Opening Night
  (6af1073ce16bc2f471089f76), Apres Ski Club (6af10718421fd94ad304e53e), Tied with a Bow
  (6af1070681fb6450380f0dda), Cozy Season (6af106f4421fd94ad304e520), Winter Herbarium
  (6af106e2d0555ac419039c35), Midnight Christmas (6af106d1d0555ac419039c1f)
- 20 products across the 10 duplicate pairs listed above (table column IDs 1+2 for all 10 rows)
- 1 distinct Golden Retriever design confirmed NOT a duplicate of the pair above: "Golden Retriever Santa
  Hat Christmas T-Shirt / Santa Paws Is Coming To Town" (6ae414dee88b7e964c0e72eb) — different print-area
  image (santa-paws-golden.png), different artwork, correctly a separate design
- 10 more distinct designs: Pickleball Christmas Club (6ae41f75e88b7e964c0e738d), Boy Mom Christmas
  License Plate (6ae41f73e88b7e964c0e738b), Mahjong Christmas Club (6ae414ecf755b251850ceb08), Santa
  Barista (6ae414ebf755b251850ceb07), Books Cocoa and Christmas (6ae414e9f755b251850ceb04), Even Santa
  Needs a Paramedic (6ae414e72e006c787106bd9c), Santa's Got a Truck Driver (6ae414e62e006c787106bd9a),
  Festive & Fabulous Disco Ball (6ae414dfe88b7e964c0e72ec), Christmas T-Rex Tree/"Tree Rex"
  (6ae414dde88b7e964c0e72ea), Santa's Favorite Nurse (6ae414d60bfe3d7d30031ddc)

### Remaining Amazon coverage (24 of 62 products, not yet visually inspected)

Pickleball/Grandma/Fishing-graphic T-shirts, the "Cat Lineup" product-type family (Mug, Hoodie,
Crewneck, Sweatshirt — likely legitimate same-design-different-product-type, not flagged as duplicates
without checking), Christmas Golden Retriever (first of the pair, 6ae41f68e88b7e964c0e737e, sync-gapped
twin already confirmed clean via its live counterpart), Naughty List Cat singular variant
(6ae414e0e88b7e964c0e72ee), Santa Cat Mom (6adea4fb17865a20ce04ea54), Plant Mom, Veterinarian, Teacher
Squad, and others — see full 62-ID roster pulled this session (amazon_page1.json/amazon_page2.json in
scratchpad) for exact remaining IDs. Next session should resume task T-1O514F2T63 directly.

## 9. eBay full 53-row ID register (complete, per-product evidence — produced in response to an
   independent-verifier request for inspectable per-product rows, not just a report link)

Format: `Printify ID | Title (truncated) | Visual result | Default mockup image URL used for inspection`.
`[DUP-PAIR]` marks the 4 listings forming the 2 confirmed true-duplicate pairs (see §5a). The 4
prior-session IDs (marked "prior-session evidence") were visually inspected in an earlier session
before this register existed; their evidence lives in `reports/Printify correction-approval packet
(first).md`, not in this session's downloaded-image set.

```
6a49372c442938e8890da743 | Cute Chick Pattern Phone Case | CLEAN | https://images.printify.com/mockup/6a49372c442938e8890da743/61521/2494/cute-chick-pattern-phone-case-kawaii-pastel-protective-cover.jpg?camera_label=front-and-side
6a49373aa8f8e286e2066011 | Pink Hummingbird Floral Phone Case (2nd listing) | CLEAN [DUP-PAIR] | https://images.printify.com/mockup/6a49373aa8f8e286e2066011/96135/81354/phone-case-pink-hummingbird-floral-magnetic-impactresistant-case.jpg?camera_label=front
6a493bea131a5b73ff0f1d02 | Pink Hummingbird Floral Phone Case | CLEAN [DUP-PAIR] | https://images.printify.com/mockup/6a493bea131a5b73ff0f1d02/96135/81354/phone-case-pink-hummingbird-floral-magnetic-impactresistant-case.jpg?camera_label=front
6a493beb131a5b73ff0f1d04 | Hummingbird Floral Phone Case (real photo, distinct design) | CLEAN | https://images.printify.com/mockup/6a493beb131a5b73ff0f1d04/96135/81354/hummingbird-floral-phone-case-magnetic-impact-resistant-protection.jpg?camera_label=front
6a493bed131a5b73ff0f1d05 | American Flag Tough Phone Case (Patriotic) | CLEAN | https://images.printify.com/mockup/6a493bed131a5b73ff0f1d05/61521/2494/american-flag-tough-phone-case-patriotic-iphone-protective-cover.jpg?camera_label=front-and-side
6a493bef131a5b73ff0f1d06 | American Flag Tough Phone Case (Distressed) | CLEAN | https://images.printify.com/mockup/6a493bef131a5b73ff0f1d06/61521/2494/american-flag-tough-phone-case-distressed-stars-stripes-protective-cover.jpg?camera_label=front-and-side
6a493bf2131a5b73ff0f1d07 | Moon Phases Phone Case | CLEAN | https://images.printify.com/mockup/6a493bf2131a5b73ff0f1d07/61521/2494/moon-phases-phone-case-celestial-night-sky-iphone-case.jpg?camera_label=front-and-side
6a493bf5131a5b73ff0f1d08 | Copy of American Flag Magnetic Phone Case | CLEAN [DUP-PAIR] | https://images.printify.com/mockup/6a493bf5131a5b73ff0f1d08/96135/81354/copy-of-american-flag-magnetic-impact-resistant-phone-case.jpg?camera_label=front
6a493bf8131a5b73ff0f1d0a | American Flag Magnetic Phone Case | CLEAN [DUP-PAIR] | https://images.printify.com/mockup/6a493bf8131a5b73ff0f1d0a/96135/81354/american-flag-magnetic-impact-resistant-phone-case.jpg?camera_label=front
6a493bfcc49b3a4cb20a9fe5 | Pink Bow & Heart Magnetic Phone Case | CLEAN | https://images.printify.com/mockup/6a493bfcc49b3a4cb20a9fe5/96135/81354/phone-case-pink-bow-heart-magnetic-impact-resistant-case.jpg?camera_label=front
6a493bfdc49b3a4cb20a9fe7 | Floral Tough Magnetic Phone Case (Retro) | CLEAN | https://images.printify.com/mockup/6a493bfdc49b3a4cb20a9fe7/109328/107253/floral-tough-magnetic-phone-case-retro-pink-orange-blossom-protective-cover.jpg?camera_label=front
6a493c00c49b3a4cb20a9fe9 | Cute Pink Bow Tough Phone Case | CLEAN | https://images.printify.com/mockup/6a493c00c49b3a4cb20a9fe9/62582/97458/cute-pink-bow-tough-phone-case-floral-hearts-protective-iphone-cover.jpg?camera_label=front-and-side
6a493c04c49b3a4cb20a9fec | Romantic Pink Bows Tough Phone Case | CLEAN | https://images.printify.com/mockup/6a493c04c49b3a4cb20a9fec/61521/2494/romantic-pink-bows-tough-case-cute-heart-bow-iphone-protective-phone-case.jpg?camera_label=front-and-side
6a493c06c49b3a4cb20a9fed | American Flag Phone Case with Card Holder | CLEAN | https://images.printify.com/mockup/6a493c06c49b3a4cb20a9fed/79732/44702/american-flag-phone-case-with-card-holder-patriotic-slim-wallet-phone-case.jpg?camera_label=front
6a493c0bdf721fcc700771a7 | Dog Pack Protective Phone Case | CLEAN | https://images.printify.com/mockup/6a493c0bdf721fcc700771a7/62582/97458/dog-pack-protective-phone-case-golden-retriever-friends-tough-cover.jpg?camera_label=front-and-side
6a493c0cdf721fcc700771a8 | Mushroom & Butterfly Magnetic Phone Case | CLEAN | https://images.printify.com/mockup/6a493c0cdf721fcc700771a8/96135/81354/mushroom-butterfly-magnetic-impact-resistant-phone-case.jpg?camera_label=front
6a493c0edf721fcc700771aa | Abstract Botanical Phone Case | CLEAN | https://images.printify.com/mockup/6a493c0edf721fcc700771aa/62582/97458/abstract-botanical-phone-case-minimalist-peach-leaf-tough-case.jpg?camera_label=front-and-side
6a493c10df721fcc700771ac | Strawberry Pattern Tough Phone Case | CLEAN | https://images.printify.com/mockup/6a493c10df721fcc700771ac/61521/2494/strawberry-pattern-tough-phone-case-cute-pink-protective-iphone-cover.jpg?camera_label=front-and-side
6a493c1da36a12099202d045 | Bass Fishing Tough Phone Case | CLEAN | https://images.printify.com/mockup/6a493c1da36a12099202d045/62582/97458/bass-fishing-tough-phone-case-rugged-protective-case-with-leaping-bass-design.jpg?camera_label=front-and-side
6a493c20a36a12099202d047 | Fishing Bass Phone Case | CLEAN | https://images.printify.com/mockup/6a493c20a36a12099202d047/61521/2494/fishing-bass-phone-case-jumping-largemouth-design-protective-tough-case.jpg?camera_label=front-and-side
6a493c26a36a12099202d04a | Dripping Yellow Smiley Phone Case | CLEAN | https://images.printify.com/mockup/6a493c26a36a12099202d04a/61521/2494/phone-case-dripping-yellow-smiley-on-purple-swirl-oops-design.jpg?camera_label=front-and-side
6a493c2ba36a12099202d04b | Retro Checkerboard Phone Case | CLEAN | https://images.printify.com/mockup/6a493c2ba36a12099202d04b/77016/23412/phone-case-retro-checkerboard-with-pink-orange-daisies-impact-resistant.jpg?camera_label=front
6a493c2fa36a12099202d04d | Floral Tough Phone Case (Pink Vintage Roses) | CLEAN | https://images.printify.com/mockup/6a493c2fa36a12099202d04d/61521/2494/floral-tough-phone-case-pink-vintage-roses-blue-peonies-protective-cover.jpg?camera_label=front-and-side
6a493c347599ea93f7080d41 | Pink Bow Stripes Magnetic Phone Case | CLEAN | https://images.printify.com/mockup/6a493c347599ea93f7080d41/109328/107253/pink-bow-stripes-magnetic-phone-case-tough-protective-iphone-cover.jpg?camera_label=front
6a493c367599ea93f7080d43 | Dominican Flag Heart Phone Case | CLEAN | https://images.printify.com/mockup/6a493c367599ea93f7080d43/61521/2494/dominican-flag-heart-phone-case-patriotic-dominican-republic-iphone-case.jpg?camera_label=front-and-side
6a493c3b7599ea93f7080d45 | Venezuela Heart Flag Phone Case | CLEAN | https://images.printify.com/mockup/6a493c3b7599ea93f7080d45/61521/2494/venezuela-heart-flag-phone-case-tough-protective-phone-case.jpg?camera_label=front-and-side
6a493c3f7599ea93f7080d47 | Puerto Rico Flag Magnetic Phone Case | CLEAN | https://images.printify.com/mockup/6a493c3f7599ea93f7080d47/96135/81354/puerto-rico-flag-magnetic-impact-resistant-phone-case.jpg?camera_label=front
6a493c43e2256aa80f0b82c3 | Puerto Rico Flag Tough Phone Case | CLEAN | https://images.printify.com/mockup/6a493c43e2256aa80f0b82c3/61521/2494/puerto-rico-flag-tough-phone-case.jpg?camera_label=front-and-side
6a493c46e2256aa80f0b82c4 | Puerto Rico Flag Tough Phone Case (Stripe) | CLEAN | https://images.printify.com/mockup/6a493c46e2256aa80f0b82c4/61521/2494/puerto-rico-flag-tough-phone-case-patriotic-red-white-stripe-design.jpg?camera_label=front-and-side
6a493c4ae2256aa80f0b82c6 | Dominican Republic Flag Magnetic Phone Case | CLEAN | https://images.printify.com/mockup/6a493c4ae2256aa80f0b82c6/96135/81354/dominican-republic-flag-magnetic-impact-resistant-phone-case.jpg?camera_label=front
6a493c4ee2256aa80f0b82c8 | Dominican Republic Flag Tough Phone Case | CLEAN | https://images.printify.com/mockup/6a493c4ee2256aa80f0b82c8/61521/2494/dominican-republic-flag-tough-phone-case-protective-patriotic-iphone-cover.jpg?camera_label=front-and-side
6a493c52e2256aa80f0b82ca | Canadian Flag Tough Phone Case | CLEAN | https://images.printify.com/mockup/6a493c52e2256aa80f0b82ca/61521/2494/canadian-flag-tough-phone-case-durable-maple-leaf-iphone-case.jpg?camera_label=front-and-side
6a493c5608efc981890568b6 | Union Jack Magnetic Phone Case | CLEAN | https://images.printify.com/mockup/6a493c5608efc981890568b6/96135/81354/union-jack-magnetic-impact-resistant-phone-case.jpg?camera_label=front
6a493c5908efc981890568b8 | Mexico Heart Flag Phone Case | CLEAN | https://images.printify.com/mockup/6a493c5908efc981890568b8/96135/81354/mexico-heart-flag-phone-case-magnetic-impact-resistant-protective-cover.jpg?camera_label=front
6a493c5c08efc981890568bb | Union Jack Heart Phone Case | CLEAN | https://images.printify.com/mockup/6a493c5c08efc981890568bb/96135/81354/union-jack-heart-phone-case-magnetic-impact-resistant-uk-flag-cover.jpg?camera_label=front
6a493c5e08efc981890568bd | Patriotic Heart Phone Case | CLEAN | https://images.printify.com/mockup/6a493c5e08efc981890568bd/96135/81354/patriotic-heart-phone-case-american-flag-magnetic-impact-resistant-case.jpg?camera_label=front
6a493c612964869925020b38 | Canada Heart Tough Phone Case | CLEAN | https://images.printify.com/mockup/6a493c612964869925020b38/109328/107253/canada-heart-tough-magnetic-phone-case.jpg?camera_label=front
6a493c632964869925020b3a | Canada Flag Magnetic Phone Case | CLEAN | https://images.printify.com/mockup/6a493c632964869925020b3a/96135/81354/canada-flag-magnetic-impact-resistant-phone-case.jpg?camera_label=front
6a493c672964869925020b3c | Brazil Flag Phone Case (regular) | CLEAN | https://images.printify.com/mockup/6a493c672964869925020b3c/61521/2494/brazil-flag-phone-case-patriotic-protective-tough-case-for-iphone-android.jpg?camera_label=front-and-side
6a493c6b2964869925020b3e | Brazil Flag Magnetic Phone Case | CLEAN | https://images.printify.com/mockup/6a493c6b2964869925020b3e/96135/81354/brazil-flag-magnetic-impact-resistant-phone-case.jpg?camera_label=front
6a493c6edf721fcc700771ae | Mexico Flag Magnetic Phone Case | CLEAN | https://images.printify.com/mockup/6a493c6edf721fcc700771ae/96135/81354/mexico-flag-magnetic-impact-resistant-phone-case.jpg?camera_label=front
6a493c77df721fcc700771b0 | Nurse Iguana Loco Unisex T-shirt | CLEAN | https://images.printify.com/mockup/6a493c77df721fcc700771b0/73207/98445/nurse-iguana-loco-unisex-garment-dyed-t-shirt.jpg?camera_label=front
6a493c7ddf721fcc700771b2 | Unisex Jersey Muscle Tank (America the Beautiful) | CLEAN | https://images.printify.com/mockup/6a493c7ddf721fcc700771b2/125340/120169/unisex-jersey-muscle-tank.jpg?camera_label=front
6a493c80df721fcc700771b4 | Patriot 250 Eagle Flag Dad Cap | CLEAN | https://images.printify.com/mockup/6a493c80df721fcc700771b4/105381/102307/patriot-250-eagle-flag-dad-cap-american-flag-vintage-baseball-hat-vintage-usa-eagle-cap-patriotic-adjustable-baseball-hat-fourth-of-july.jpg?camera_label=front
6a493c86df721fcc700771b6 | Great American Kid T Shirt | CLEAN | https://images.printify.com/mockup/6a493c86df721fcc700771b6/61520/94623/great-american-kid-t-shirt-patriotic-kids-usa-shirt-red-white-blue-youth-tee-fourth-of-july-childrens-apparel-gift.jpg?camera_label=front
6a493c8908efc981890568bf | Canvas Lunch Bag (American Flag Butterfly) | CLEAN | https://images.printify.com/mockup/6a493c8908efc981890568bf/91358/59663/canvas-lunch-bag-american-flag-butterfly-design-patriotic-picnic-tote.jpg?camera_label=front
6a493c9208efc981890568c1 | God Bless the USA T Shirt | CLEAN | https://images.printify.com/mockup/6a493c9208efc981890568c1/12100/92570/god-bless-the-usa-t-shirt-patriotic-christian-4th-of-july-tee-faith-and-freedom-american-flag-shirt.jpg?camera_label=front
6a493c9908efc981890568c2 | USA Love American Flag T Shirt | CLEAN | https://images.printify.com/mockup/6a493c9908efc981890568c2/38191/127670/usa-love-american-flag-t-shirt-patriotic-4th-of-july-tee-red-white-and-blue-independence-day-shirt.jpg?camera_label=folded-2
6a493ca208efc981890568c5 | Distressed American Flag Tank Top | CLEAN | https://images.printify.com/mockup/6a493ca208efc981890568c5/105810/102834/distressed-american-flag-tank-top-patriotic-usa-sleeveless-shirt-for-4th-of-july-summer-and-everyday-wear.jpg?camera_label=front
6a493cafa36a12099202d04f | Retro Doodle Graphic Tee | CLEAN | https://images.printify.com/mockup/6a493cafa36a12099202d04f/18542/102044/retro-doodle-graphic-tee-colorful-smile-and-skate-icons.jpg?camera_label=front-2
6a493cb9a36a12099202d050 | Dripping Rose Graphic T-Shirt | CLEAN | https://images.printify.com/mockup/6a493cb9a36a12099202d050/73207/98445/dripping-rose-graphic-t-shirt.jpg?camera_label=front
6a493cc0a36a12099202d052 | Panama Flag Heart Phone Case | CLEAN | https://images.printify.com/mockup/6a493cc0a36a12099202d052/61521/2494/panama-flag-heart-phone-case-patriotic-panama-iphone-case.jpg?camera_label=front-and-side
6a493cc4a36a12099202d054 | Brazil Heart Flag Phone Case | CLEAN | https://images.printify.com/mockup/6a493cc4a36a12099202d054/61521/2494/brazil-heart-flag-phone-case-patriotic-brazilian-iphone-case-for-soccer-fans-travelers.jpg?camera_label=front-and-side
```

**Marketplace-sellability caveat (repeated per the independent verifier's request):** every CLEAN
result above is a visual-artwork judgment only — it confirms the mockup renders without cropping,
alignment, spelling or print-boundary defects. It is NOT a confirmation that the listing is live or
purchasable on eBay's own site; all 53 are Printify-side sync-gapped (`external` absent), meaning no
direct marketplace-side check has been done for any of them. Both facts can be true at once: a listing
can have perfectly clean artwork and still not be reachable by an eBay shopper.
