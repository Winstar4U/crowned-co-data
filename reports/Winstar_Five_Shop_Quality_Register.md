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
across both shops too — Etsy ID `6ad4307c18e0243bd10d533d` and Shopify ID `6ac76f3288d05d5634004c1a`.
**Follow-up resolved (Etsy batch 1/3, see §8c):** the Etsy twin was reviewed and is a completely
**different illustration** from the photo-realistic cribbage-board defect above (a cartoon reindeer
race, not a photo), and despite also using `scale: 1.45`, its mockup is visually clean — no cropping.
This confirms scale alone does not predict a defect; the specific source image's own padding/aspect
ratio determines whether a given scale value crops the design. Each case must still be viewed, not
inferred from the number.

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
2. **eBay is now COMPLETE (53/53 visually inspected, see §6a) — do not re-inspect.** **Amazon is now
   COMPLETE (62/62 visually inspected, see §8a) — do not re-inspect.** **TikTok is now COMPLETE (71/71
   visually inspected, see §8b) — do not re-inspect.** **Etsy batch 1/3 is now COMPLETE (97/291 remaining
   products visually inspected, see §8c) — do not re-inspect the IDs in §11.** Remaining: Etsy batches 2/3
   and 3/3 (194 products, roster pre-split and staged at
   `/tmp/claude-0/-home-user-crowned-co-data/c0034cf5-75d5-55a9-aa8f-5993db7544c2/scratchpad/etsy_batch/batch2.json`
   and `batch3.json` as of this session — re-derive from a fresh shop listing if that scratchpad is gone),
   and Shopify (2,429 total, see item 1 above — by far the largest remaining gap). Recommend finishing
   Etsy batches 2 and 3 next, using the same bulk-list (`include_full=true`, page-by-page) + per-straggler
   method that proved far more context-efficient than one-product-at-a-time fetching for batch 1.
3. Direct marketplace-side verification (actually checking eBay/Amazon/TikTok/Shopify storefronts, not
   just Printify's `external` field) for at least the highest-volume confirmed-gap SKUs, before any
   resync/repair is proposed for owner approval.
4. Scale-value audit: for every duplicate-shop-record pair found (same design, Etsy + Shopify copies),
   compare the print-area `scale` value the way this session did for the cribbage ornament — this is a
   fast, high-value check once a pair is identified, and already found one real defect this way.

## 8a. Amazon shop (29451844) — COMPLETE: 62/62 visually inspected, major duplicate-ASIN finding
## (2026-11-17/18, this session)

**Status: 62/62 products now have real image evidence. 0 confirmed visual/artwork defects.** Second
shop (after eBay) to reach full visual-inspection completion. Task T-1O514F2T63 ready for submission.

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
| 11 | "THE NAUGHTY LIST" cat-mugshot art (two different internal filenames: cat-lineup-the-naughty-list.png / cat-lineup-naughty-list-cats-only.png, but the RENDERED artwork is visually identical — same 4 cats, same hats, same banner — confirmed by opening both images, not just filename matching) | 6ae414e0e88b7e964c0e72ee | B0HPSD8268 | 6ae41f6ce88b7e964c0e7383 | — | Only #1 live |

**CAVEAT ADDED PER INDEPENDENT REVIEW (correct and accepted):** "Live" in the table above means Printify
records a populated `external.handle` (ASIN) for that listing — this is Printify-side mapping evidence
only. It does NOT by itself prove the Amazon offer is currently buyable, has active inventory, or that
reviews/sales-rank are actually split between the two ASINs. No Amazon Seller Central / marketplace-side
read has been performed for any of these 14 ASINs; their real-world buyable status is UNKNOWN, not
asserted. The proposed remedy (retire/merge one ASIN per pair) is now explicitly conditioned on a
marketplace-side verification pass first, including confirming whether Amazon's own variation policy
would even permit a merge — this verification has not been done and is the natural next step before any
remedy decision, separate from this visual-inspection task.

**7 of 11 pairs (14 products) show both Printify records carrying a populated ASIN.** Note: pair #11 was
caught only by visually comparing the two mockup images side by side — their internal Printify filenames differ, so the filename+scale matching method used for pairs
1-10 would have missed it. This means the 10 filename-matched pairs are a reliable floor, not a ceiling:
the true count of near-identical-artwork duplicates could be modestly higher than what automated
filename matching finds alone; a dedicated title-similarity + visual-compare pass across the full
catalog (beyond what this session's manual review covered) would be the thorough way to close that gap.

**Checked and ruled OUT as a duplicate:** "Santa Called For Backup" Firefighter Funny Christmas T-Shirt
(6ae41f6be88b7e964c0e7382) vs. "Santa Called Backup Firefighter T-Shirt" (6ae414d9e88b7e964c0e72e7) —
very similar titles, but the two print-area images (santa-called-for-backup-firefighter.png vs.
firefighter-backup.png) are genuinely different artwork (different illustration style/composition),
confirmed by viewing both. Flagged and cleared, not counted as a duplicate. This is a materially different and more severe problem than any duplicate found on
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

### Remaining 24 products, completed in the second half of this session

Highland Cow, Frosted Star, Tartan & Tradition, Nutcracker Season, Nonna's Christmas Kitchen, Grandma's
Christmas Crew, Santa's Favorite Mechanic, Gardeners Grow Merry Christmas, Hooked on Christmas, Santa Cat
Mom, the "Cat Lineup" product-type family (Mug 6ae41f72e88b7e964c0e7389, Hoodie 6ae41f71e88b7e964c0e7388,
Crewneck Sweatshirt 6ae41f70e88b7e964c0e7387, Sweatshirt 6ae41f6de88b7e964c0e7384, T-Shirt
6ae41f6be88b7e964c0e7381 — all share print-area image cat-lineup-evergreen.png, confirmed legitimate
same-design-different-product-type reuse, not duplicates), the "Santa's Naughty List" Mug
(6ae41f6fe88b7e964c0e7386) and Crewneck (6ae41f6ee88b7e964c0e7385) — same pattern, share
cat-lineup-santas-naughty-list.png with the already-known Naughty-List-Cat-Lineup T-shirt pair, Veterinarian
Christmas Dog, Plant Mom Christmas Botanical, Teacher Christmas Squad, the Firefighter pair (checked and
cleared, see above), and the "Naughty List Cat" singular vs. "The Naughty List Cats" pair (confirmed an
11th true duplicate, see above). All 24 are visually CLEAN — 0 defects found in this half either.

**Amazon shop is now fully closed out: 62/62 visually inspected, 0 artwork defects, 11 confirmed
duplicate pairs (7 both-live) as the one standing finding requiring an owner decision.**

## 8b. TikTok shop (28122957, My Tiktok Shop) — COMPLETE: 71/71 visually inspected, 0 defects, 0
## confirmed duplicates (2026-11-18, this session)

**Status: 71/71 products now have real image evidence. 0 confirmed visual/artwork defects. 0 confirmed
true duplicate pairs.** Third shop (after eBay and Amazon) to reach full visual-inspection completion.
Sync-status: 39/71 have a populated Printify `external` channel-mapping field, 32/71 show `external: null`
(45.1% gap rate) — this matches the full-population figure already recorded in §1, and carries the same
standing caveat: a populated/absent `external` field is Printify-side mapping evidence only, not confirmed
TikTok-side buyability.

**Notable methodology finding, distinct from eBay/Amazon — a near-miss that was checked and ruled OUT:**
This shop runs what is effectively two full parallel product lines sharing the same roster of character
concepts (Dog Dad, Dog Mom, Cat Mom, Mama/Papa/Nana/Grandma/Auntie Claus, Howdy, Cozy Season, Joy to the
World, Faith Hope Love, Merry & Bright, Merry & Booked, Dash Away All, Doxie Claus) — a **"Badge" style**
(photorealistic pet/object photo inside an oval badge) and a **"Retro Varsity" style** (flat vector
lettering/illustration, gingham or varsity-text treatment). This produced 18 same-main-title candidate
pairs that superficially look exactly like the Amazon duplicate-ASIN pattern. Each of the 18 pairs was
checked by BOTH methods used in this recovery effort:
- Print-area image filename + scale + x/y position: all 18 pairs use **completely different internal
  filenames** (e.g. `sw-dash-away-all-badge-4096.png` vs `dash-away-all-dachshund-4096.png`) with
  non-matching scale/position values — no filename or placement match on any pair.
- Direct visual comparison of both mockup images (the ground-truth method, per the lesson learned on
  Amazon's Naughty-List-Cat pair): all 18 pairs were opened and viewed side by side. Every pair showed
  genuinely distinct artwork — different illustration style, different composition, not the same image
  reused. None of the 18 is a true duplicate.

The 18 checked-and-ruled-out pairs (Badge ID / Retro ID): Dash Away All (6adec782a02eb7366a027554 /
6ada37b8e722ba383a04d99d), Doxie Claus (6ade503e265c71475d0579e6 / 6ada37a6f09eaff83506fe81), Merry &
Bright (6adec7a61320136327024b32 / 6ada375d4546c925a8082fd5), Merry & Booked (6ade7a75d4524eaf210e45d7 /
6ad9fe3e590d21532607c2be), Auntie Claus (6adecae2a02eb7366a0277e5 / 6ad9fe05a9063187d908e62e), Faith Hope
Love (6adf6da49d15ca1a990f6a40 / 6ad9e765a84ca20cc21000d7), Nana Claus (6adecab859a53cf55f030c14 /
6ad9e72f14510fbba8093d07), Papa Claus (6adecaa51320136327024d4d / 6ad9e71d14510fbba8093cfe), Howdy
(6adecaf559a53cf55f030c45 / 6ad9e70b3612b5771905f0f4), Cozy Season (6ade7ad480e75cb4ea09a135 /
6ad9e6f33612b5771905f0e8), Joy to the World (6adf6d92c60cddcb060105af / 6ad9e57b385590147b0be0e1), Dog Dad
(6ade7a3b9760402ba10b71b2 / 6ad9e55614510fbba8093bf4), Cat Mom (6ade7a1491f7e585510c842a /
6ad9e544e70d4d290c05ee2f), Dog Mom (6ade7a28aa1ddebc870c112a / 6ad98e5e4d5521405502a781), Grandma Claus
(6adecacc59a53cf55f030c1c / 6ad98e4b13800a74da04df4e), Mama Claus (6adec793259305e1d1049ae9 /
6ad98e3913800a74da04df33), Merry Nurse (6ade7a623757c80615075085 / 6ad98e2613800a74da04df1d), Merry
Teacher (6ade7a4fd4524eaf210e45b8 / 6ad98e109d94429bd0047c9a).

Also checked and ruled OUT: the "Santa Called For Backup" phrase appears twice (a reindeer-themed
sweatshirt, 6adf6d46b95bee5547043b54, vs. a firefighter-themed t-shirt, 6ad40ff99c8f61e787077eb5) — two
completely different illustrations and product types, same pattern as the eBay Firefighter pair, not a
duplicate. "Everyone Go Home," "Bah Humbug," and "Dog Mom" phrases also each appear on both a sweatshirt
(oval-badge or crest art) and a separate t-shirt (different composition) — legitimate separate designs,
not duplicates. The Golden Retriever/Tabby Cat/stethoscope/apple photos are legitimately reused across
product types (sweatshirt + matching mug) within the Badge line, consistent with the normal, non-defect
same-design-different-product-type pattern already documented for Amazon's Cat Lineup family.

**TikTok shop is now fully closed out: 71/71 visually inspected, 0 artwork defects, 0 confirmed duplicate
pairs — the cleanest of the three shops completed so far.**

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

## 8c. Etsy shop (26603005) batch 1/3 — COMPLETE: 97/97 visually inspected, 1 confirmed content-mismatch
## defect, 0 confirmed duplicate pairs (2026-11-18, this session)

**Status: 97 of the 291 remaining Etsy products (291 = 297 total minus 6 already inspected in a prior
session: the cribbage-ornament defect in §2 and 5 Christmas hoodies in §4) now have real image evidence.**
This is batch 1 of 3; batches 2 and 3 (194 products) remain, rosters pre-staged in the scratchpad (see
§8). 1 confirmed customer-facing defect. 0 confirmed true duplicate-listing pairs.

**Method note (efficiency improvement for future batches):** fetching each product individually via
`product_id` (as done for eBay/Amazon/TikTok) is far more expensive in context for this shop, because
many Etsy listings carry large multi-size/multi-color variant arrays (e.g. a baby bodysuit with 60+
variants, a poster with 46 size options). Fetching the shop's product **list** with `include_full=true`
two pages at a time (100 products) and parsing the bulk JSON with a `python3 -I` extraction script,
falling back to individual `product_id` fetches only for the handful of stragglers a given batch's roster
split across a page boundary, cut the number of MCP tool calls from ~97 to ~4 for the metadata/sync/
print-area side of this batch. Recommend this method for batches 2 and 3.

### CONFIRMED DEFECT: "Funny Ornament Gift Set of 3" advertises 3 designs, Printify record has only 1

**Product:** "Funny Ornament Gift Set of 3 - Ceramic Holiday Tree Ornaments, Gag Gift Set, White Elephant
Gift Set", Printify ID `6ad42970f1aeec4b590f6d00`, Etsy shop 26603005, live at
https://www.etsy.com/listing/4597799742/funny-ornament-gift-set-of-3-ceramic

The listing description explicitly promises: "**This set includes:** Mischievous Raccoon, Merry Chaos
Cat, Wine O'Clock" — three distinct designs across the product's 4 shape options (Circle, Heart, Star,
Snowflake). Printify's print-area data shows only **one** image assigned across all 4 shape variants:
`funny-raccoon.jpg` (scale 1.45). There is no Cat or Wine O'Clock artwork anywhere in the product record.
Confirmed by downloading and viewing the mockups for both the Circle (69370) and Heart (74403) shape
variants — both show the identical raccoon-with-Christmas-lights illustration; neither shows a cat or a
wine-themed design.

**Customer impact:** a buyer paying for a "set of 3" with named distinct designs would receive 3
identical raccoon ornaments (or whatever the actual fulfillment behavior is for an under-populated
multi-shape listing) instead of the 3 advertised designs — a listing-content/fulfillment mismatch, not an
artwork-quality defect. This is RED, customer-facing.

**Proposed remedy (owner-approval-only — NOT executed):** Either (a) upload the two missing designs
(Merry Chaos Cat, Wine O'Clock) and assign them to the Star and Snowflake shape variants respectively so
the listing matches its own description, or (b) correct the listing description/title to describe what
is actually being sold (a single raccoon design in a choice of shape) if a 3-design version was never
actually built. This is a live content change and requires explicit owner sign-off before any attempt.

### Duplicate-candidate groups checked and ruled OUT (same artwork, different product type — normal reuse)

9 groups of 2 were flagged by matching print-area image filename + scale + position, each pairing a
"...Christmas **Sweatshirt**" listing with a "...Christmas **Shirt**" (t-shirt) listing sharing the
identical artwork file: Cozy Season, Gardeners Grow Merry Christmas, Teacher Christmas Squad, Santa's
Favorite Nurse, Cat Mom, Hooked on Christmas, Golden Retriever, Nutcracker/Nutcracker Season, Books Cocoa
and Christmas, Highland Cow. Confirmed via title inspection that each pair spans two different product
types (sweatshirt vs. t-shirt), consistent with the established normal, non-defect same-design-different-
product-type reuse pattern already documented for Amazon's Cat Lineup family (§8a) and TikTok's Badge/
Retro lines (§8b) — not counted as duplicates. No same-product-type duplicate was found in this batch.

### Sync-mapping status (batch 1/3)

75/97 have a populated Printify `external` channel-mapping field; 22/97 show `external: null`. Standing
caveat applies (§1): this is Printify-side mapping evidence only, not confirmed Etsy-side buyability.

### Resolved follow-up from §2

The "Reindeer Cribbage Peg Race" Etsy twin (`6ad4307c18e0243bd10d533d`) is in this batch and is confirmed
CLEAN — see the updated note in §2.

**Etsy batch 1/3 is closed out: 97/97 visually inspected, 1 confirmed content-mismatch defect (the
ornament gift-set), 0 confirmed duplicate pairs. See §11 for the full per-product ID table.**

## 10. TikTok full 71-row ID register (complete, per-product evidence, same format as §9)

Format: `Printify ID | Title (truncated) | Visual result | Default mockup image URL used for inspection`.
Same standing caveat as §9: CLEAN is a visual-artwork judgment only (no cropping/alignment/spelling/
print-boundary defects found) — it is NOT confirmation of live TikTok-side buyability. 39/71 have a
populated Printify `external` field (channel-mapping evidence only); 32/71 show `external: null`.

6adf6def3a852e6fa20e6caa | Hot Cocoa Club Christmas Sweatshirt / Cocoa Bar and Peppermint Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adf6def3a852e6fa20e6caa/25458/98502/hot-cocoa-club-christmas-sweatshirt-cocoa-bar-and-peppermint-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adf6ddcc60cddcb06010608 | Merry Catmas Christmas Sweatshirt / Tabby Cat and Christmas Tree Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adf6ddcc60cddcb06010608/25458/98502/merry-catmas-christmas-sweatshirt-tabby-cat-and-christmas-tree-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adf6dc9250930614e0f3bce | Dachshund Through the Snow Christmas Sweatshirt / Dachshund in Santa Hat Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adf6dc9250930614e0f3bce/25458/98502/dachshund-through-the-snow-christmas-sweatshirt-dachshund-in-santa-hat-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adf6db7250930614e0f3bba | Let It Snow Winter Sweatshirt / Red Mittens, Scarf and Snowflake Badge Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adf6db7250930614e0f3bba/25458/98502/let-it-snow-winter-sweatshirt-red-mittens-scarf-and-snowflake-badge-crewneck-unisex.jpg?camera_label=front
6adf6da49d15ca1a990f6a40 | Faith Hope Love Christmas Sweatshirt / Advent Candles and Wreath Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adf6da49d15ca1a990f6a40/25458/98502/faith-hope-love-christmas-sweatshirt-advent-candles-and-wreath-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adf6d92c60cddcb060105af | Joy to the World Christmas Sweatshirt / Gold Star and Brass Bell Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adf6d92c60cddcb060105af/25458/98502/joy-to-the-world-christmas-sweatshirt-gold-star-and-brass-bell-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adf6d7f10aa455cb00a1608 | Snack Season Christmas Sweatshirt / Holiday Snack Board Badge Funny Foodie Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adf6d7f10aa455cb00a1608/25458/98502/snack-season-christmas-sweatshirt-holiday-snack-board-badge-funny-foodie-crewneck-unisex.jpg?camera_label=front
6adf6d6b2c5edee2420ad5d8 | Morning Person Dec 25 Christmas Sweatshirt / Vintage Alarm Clock and Presents Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adf6d6b2c5edee2420ad5d8/25458/98502/morning-person-dec-25-christmas-sweatshirt-vintage-alarm-clock-and-presents-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adf6d599d15ca1a990f69ba | Everyone Go Home Christmas Sweatshirt / Cozy Slippers and Cocoa Badge Funny Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adf6d599d15ca1a990f69ba/25458/98502/everyone-go-home-christmas-sweatshirt-cozy-slippers-and-cocoa-badge-funny-holiday-crewneck-unisex.jpg?camera_label=front
6adf6d46b95bee5547043b54 | Santa Called for Backup Christmas Sweatshirt / Reindeer with Jingle Bells Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adf6d46b95bee5547043b54/25458/98502/santa-called-for-backup-christmas-sweatshirt-reindeer-with-jingle-bells-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adecb5e1320136327024db7 | Cookie Season Christmas Sweatshirt / Christmas Cookies and Milk Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adecb5e1320136327024db7/25458/98502/cookie-season-christmas-sweatshirt-christmas-cookies-and-milk-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adecb44305999dc2d067254 | Merry 2026 Christmas Sweatshirt / Evergreen Wreath with Red Velvet Bow Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adecb44305999dc2d067254/25458/98502/merry-2026-christmas-sweatshirt-evergreen-wreath-with-red-velvet-bow-holiday-crewneck-unisex.jpg?camera_label=front
6adecb3059a53cf55f030c69 | Bah Humbug Christmas Sweatshirt / Stocking with Coal Badge Funny Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adecb3059a53cf55f030c69/25458/98502/bah-humbug-christmas-sweatshirt-stocking-with-coal-badge-funny-holiday-crewneck-unisex.jpg?camera_label=front
6adecb1c59a53cf55f030c5b | Snowman Season Winter Sweatshirt / Snowman in Scarf and Top Hat Badge Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adecb1c59a53cf55f030c5b/25458/98502/snowman-season-winter-sweatshirt-snowman-in-scarf-and-top-hat-badge-crewneck-unisex.jpg?camera_label=front
6adecb086d10f640af0603a7 | Chill Penguin Winter Sweatshirt / Baby Penguin in Scarf and Beanie Badge Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adecb086d10f640af0603a7/25458/98502/chill-penguin-winter-sweatshirt-baby-penguin-in-scarf-and-beanie-badge-crewneck-unisex.jpg?camera_label=front
6adecaf559a53cf55f030c45 | Howdy Christmas Sweatshirt / Cowboy Boots and Santa Hat Western Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adecaf559a53cf55f030c45/25458/98502/howdy-christmas-sweatshirt-cowboy-boots-and-santa-hat-western-holiday-crewneck-unisex.jpg?camera_label=front
6adecae2a02eb7366a0277e5 | Auntie Claus Christmas Sweatshirt / Santa Hat and Gift Boxes Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adecae2a02eb7366a0277e5/25458/98502/auntie-claus-christmas-sweatshirt-santa-hat-and-gift-boxes-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adecacc59a53cf55f030c1c | Grandma Claus Christmas Sweatshirt / Santa Hat, Reading Glasses and Cocoa Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adecacc59a53cf55f030c1c/25458/98502/grandma-claus-christmas-sweatshirt-santa-hat-reading-glasses-and-cocoa-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adecab859a53cf55f030c14 | Nana Claus Christmas Sweatshirt / Santa Hat, Yarn and Cookies Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adecab859a53cf55f030c14/25458/98502/nana-claus-christmas-sweatshirt-santa-hat-yarn-and-cookies-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adecaa51320136327024d4d | Papa Claus Christmas Sweatshirt / Santa Hat and Plaid Flannel Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adecaa51320136327024d4d/25458/98502/papa-claus-christmas-sweatshirt-santa-hat-and-plaid-flannel-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adec7a61320136327024b32 | Merry & Bright Christmas Sweatshirt / Vintage Ornaments and Tinsel Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adec7a61320136327024b32/25458/98502/merry-bright-christmas-sweatshirt-vintage-ornaments-and-tinsel-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adec793259305e1d1049ae9 | Mama Claus Christmas Sweatshirt / Santa Hat Cocoa and Cookies Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adec793259305e1d1049ae9/25458/98502/mama-claus-christmas-sweatshirt-santa-hat-cocoa-and-cookies-badge-holiday-crewneck-unisex.jpg?camera_label=front
6adec782a02eb7366a027554 | Dash Away All Christmas Sweatshirt / Leaping Dachshund in Santa Hat Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6adec782a02eb7366a027554/25458/98502/dash-away-all-christmas-sweatshirt-leaping-dachshund-in-santa-hat-badge-holiday-crewneck-unisex.jpg?camera_label=front
6ade7ad480e75cb4ea09a135 | Cozy Season Christmas Sweatshirt / Hot Cocoa and Plaid Blanket Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ade7ad480e75cb4ea09a135/25458/98502/cozy-season-christmas-sweatshirt-hot-cocoa-and-plaid-blanket-badge-holiday-crewneck-unisex.jpg?camera_label=front
6ade7a75d4524eaf210e45d7 | Merry & Booked Christmas Sweatshirt / Book Lover Santa Hat Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ade7a75d4524eaf210e45d7/25458/98502/merry-booked-christmas-sweatshirt-book-lover-santa-hat-badge-holiday-crewneck-unisex.jpg?camera_label=front
6ade7a623757c80615075085 | Merry Nurse Christmas Sweatshirt / Stethoscope and Santa Hat Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ade7a623757c80615075085/25458/98502/merry-nurse-christmas-sweatshirt-stethoscope-and-santa-hat-badge-holiday-crewneck-unisex.jpg?camera_label=front
6ade7a4fd4524eaf210e45b8 | Merry Teacher Christmas Sweatshirt / Apple, Pencil and Books Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ade7a4fd4524eaf210e45b8/25458/98502/merry-teacher-christmas-sweatshirt-apple-pencil-and-books-badge-holiday-crewneck-unisex.jpg?camera_label=front
6ade7a3b9760402ba10b71b2 | Dog Dad Christmas Sweatshirt / Labrador in Santa Hat and Plaid Bandana Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ade7a3b9760402ba10b71b2/25458/98502/dog-dad-christmas-sweatshirt-labrador-in-santa-hat-and-plaid-bandana-holiday-crewneck-unisex.jpg?camera_label=front
6ade7a28aa1ddebc870c112a | Dog Mom Christmas Sweatshirt / Golden Retriever in Santa Hat Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ade7a28aa1ddebc870c112a/25458/98502/dog-mom-christmas-sweatshirt-golden-retriever-in-santa-hat-badge-holiday-crewneck-unisex.jpg?camera_label=front
6ade7a1491f7e585510c842a | Cat Mom Christmas Sweatshirt / Tabby Cat in Santa Hat Badge Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ade7a1491f7e585510c842a/25458/98502/cat-mom-christmas-sweatshirt-tabby-cat-in-santa-hat-badge-holiday-crewneck-unisex.jpg?camera_label=front
6ade503e265c71475d0579e6 | Doxie Claus Christmas Sweatshirt / Dachshund in Santa Hat Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ade503e265c71475d0579e6/25458/98502/doxie-claus-christmas-sweatshirt-dachshund-in-santa-hat-holiday-crewneck-unisex.jpg?camera_label=front
6ade501caa01a54ae306fd7f | Teacher Fuel Christmas Mug / 15oz Ceramic Coffee Mug with Apple, Pencil and Books | CLEAN | https://images.printify.com/mockup/6ade501caa01a54ae306fd7f/104692/101750/teacher-fuel-christmas-mug-15oz-ceramic-coffee-mug-with-apple-pencil-and-books.jpg?camera_label=front
6ade50143757c80615072f2a | Nurse Fuel Christmas Mug / 15oz Ceramic Coffee Mug with Stethoscope and Santa Hat | CLEAN | https://images.printify.com/mockup/6ade50143757c80615072f2a/104692/101750/nurse-fuel-christmas-mug-15oz-ceramic-coffee-mug-with-stethoscope-and-santa-hat.jpg?camera_label=front
6ade500d580ff194290bcdbb | Cat Mom Fuel Christmas Mug / 15oz Ceramic Coffee Mug with Tabby Cat in Santa Hat | CLEAN | https://images.printify.com/mockup/6ade500d580ff194290bcdbb/104692/101750/cat-mom-fuel-christmas-mug-15oz-ceramic-coffee-mug-with-tabby-cat-in-santa-hat.jpg?camera_label=front
6ade5004aa01a54ae306fd68 | Dog Mom Fuel Christmas Mug / 15oz Ceramic Coffee Mug with Golden Retriever in Santa Hat | CLEAN | https://images.printify.com/mockup/6ade5004aa01a54ae306fd68/104692/101750/dog-mom-fuel-christmas-mug-15oz-ceramic-coffee-mug-with-golden-retriever-in-santa-hat.jpg?camera_label=front
6ada37b8e722ba383a04d99d | Dash Away All Christmas Sweatshirt / Leaping Dachshund Santa Hat Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ada37b8e722ba383a04d99d/25458/98502/dash-away-all-christmas-sweatshirt-leaping-dachshund-santa-hat-holiday-crewneck-unisex.jpg?camera_label=front
6ada37a6f09eaff83506fe81 | Doxie Claus Christmas Sweatshirt / Dachshund in Santa Hat Retro Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ada37a6f09eaff83506fe81/25458/98502/doxie-claus-christmas-sweatshirt-dachshund-in-santa-hat-retro-holiday-crewneck-unisex.jpg?camera_label=front
6ada379473b8f5726400fb91 | Tartan & Tinsel Christmas Sweatshirt / Plaid Bow and Gold Tinsel Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ada379473b8f5726400fb91/25458/98502/tartan-tinsel-christmas-sweatshirt-plaid-bow-and-gold-tinsel-holiday-crewneck-unisex.jpg?camera_label=front
6ada3782f09eaff83506fe54 | Retro Christmas Sweatshirt / Big-Bulb Lights Vintage Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ada3782f09eaff83506fe54/25458/98502/retro-christmas-sweatshirt-big-bulb-lights-vintage-holiday-crewneck-unisex.jpg?camera_label=front
6ada377073b8f5726400fb7d | Tinsel Time Christmas Sweatshirt / Retro Tinsel Garland Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ada377073b8f5726400fb7d/25458/98502/tinsel-time-christmas-sweatshirt-retro-tinsel-garland-holiday-crewneck-unisex.jpg?camera_label=front
6ada375d4546c925a8082fd5 | Merry & Bright Christmas Sweatshirt / Retro Baubles and Tinsel Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ada375d4546c925a8082fd5/25458/98502/merry-bright-christmas-sweatshirt-retro-baubles-and-tinsel-holiday-crewneck-unisex.jpg?camera_label=front
6ad9fe3e590d21532607c2be | Merry & Booked Christmas Sweatshirt / Book Lover Santa Hat Retro Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad9fe3e590d21532607c2be/25458/98502/merry-booked-christmas-sweatshirt-book-lover-santa-hat-retro-holiday-crewneck-unisex.jpg?camera_label=front
6ad9fe2ca9063187d908e64d | Merry Mom Life Christmas Sweatshirt / Retro Varsity Gingham Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad9fe2ca9063187d908e64d/25458/98502/merry-mom-life-christmas-sweatshirt-retro-varsity-gingham-holiday-crewneck-unisex.jpg?camera_label=front
6ad9fe1917756d1fdc0bd0fd | Cozy & Blessed Christmas Sweatshirt / Retro Gold Star Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad9fe1917756d1fdc0bd0fd/25458/98502/cozy-blessed-christmas-sweatshirt-retro-gold-star-holiday-crewneck-unisex.jpg?camera_label=front
6ad9fe05a9063187d908e62e | Auntie Claus Christmas Sweatshirt / Retro Varsity Santa Hat Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad9fe05a9063187d908e62e/25458/98502/auntie-claus-christmas-sweatshirt-retro-varsity-santa-hat-holiday-crewneck-unisex.jpg?camera_label=front
6ad9e765a84ca20cc21000d7 | Faith Hope Love Christmas Sweatshirt / Gold Star Retro Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad9e765a84ca20cc21000d7/25458/98502/faith-hope-love-christmas-sweatshirt-gold-star-retro-holiday-crewneck-unisex.jpg?camera_label=front
6ad9e72f14510fbba8093d07 | Nana Claus Christmas Sweatshirt / Retro Varsity Santa Hat Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad9e72f14510fbba8093d07/25458/98502/nana-claus-christmas-sweatshirt-retro-varsity-santa-hat-holiday-crewneck-unisex.jpg?camera_label=front
6ad9e71d14510fbba8093cfe | Papa Claus Christmas Sweatshirt / Retro Varsity Santa Hat Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad9e71d14510fbba8093cfe/25458/98502/papa-claus-christmas-sweatshirt-retro-varsity-santa-hat-holiday-crewneck-unisex.jpg?camera_label=front
6ad9e70b3612b5771905f0f4 | Howdy Christmas Sweatshirt / Western Cowboy Hat Holly Retro Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad9e70b3612b5771905f0f4/25458/98502/howdy-christmas-sweatshirt-western-cowboy-hat-holly-retro-holiday-crewneck-unisex.jpg?camera_label=front
6ad9e6f33612b5771905f0e8 | Cozy Season Christmas Sweatshirt / Retro Hot Cocoa Snowflake Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad9e6f33612b5771905f0e8/25458/98502/cozy-season-christmas-sweatshirt-retro-hot-cocoa-snowflake-holiday-crewneck-unisex.jpg?camera_label=front
6ad9e57b385590147b0be0e1 | Joy to the World Christmas Sweatshirt / Gold Star Retro Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad9e57b385590147b0be0e1/25458/98502/joy-to-the-world-christmas-sweatshirt-gold-star-retro-holiday-crewneck-unisex.jpg?camera_label=front
6ad9e55614510fbba8093bf4 | Dog Dad Christmas Sweatshirt / Retro Varsity Paw Print Santa Hat Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad9e55614510fbba8093bf4/25458/98502/dog-dad-christmas-sweatshirt-retro-varsity-paw-print-santa-hat-crewneck-unisex.jpg?camera_label=front
6ad9e544e70d4d290c05ee2f | Cat Mom Christmas Sweatshirt / Retro Varsity Santa Hat Cat Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad9e544e70d4d290c05ee2f/25458/98502/cat-mom-christmas-sweatshirt-retro-varsity-santa-hat-cat-holiday-crewneck-unisex.jpg?camera_label=front
6ad98e5e4d5521405502a781 | Dog Mom Christmas Sweatshirt / Retro Varsity Paw Print Santa Hat Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad98e5e4d5521405502a781/25458/98502/dog-mom-christmas-sweatshirt-retro-varsity-paw-print-santa-hat-crewneck-unisex.jpg?camera_label=front
6ad98e4b13800a74da04df4e | Grandma Claus Christmas Sweatshirt / Retro Varsity Santa Hat Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad98e4b13800a74da04df4e/25458/98502/grandma-claus-christmas-sweatshirt-retro-varsity-santa-hat-holiday-crewneck-unisex.jpg?camera_label=front
6ad98e3913800a74da04df33 | Mama Claus Christmas Sweatshirt / Retro Varsity Santa Hat Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad98e3913800a74da04df33/25458/98502/mama-claus-christmas-sweatshirt-retro-varsity-santa-hat-holiday-crewneck-unisex.jpg?camera_label=front
6ad98e2613800a74da04df1d | Merry Nurse Christmas Sweatshirt / Candy Cane Stethoscope Gingham Holiday Crewneck | CLEAN | https://images.printify.com/mockup/6ad98e2613800a74da04df1d/25458/98502/merry-nurse-christmas-sweatshirt-candy-cane-stethoscope-gingham-holiday-crewneck.jpg?camera_label=front
6ad98e109d94429bd0047c9a | Merry Teacher Christmas Sweatshirt / Retro Varsity Gingham Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad98e109d94429bd0047c9a/25458/98502/merry-teacher-christmas-sweatshirt-retro-varsity-gingham-holiday-crewneck-unisex.jpg?camera_label=front
6ad98d1b9d94429bd0047bd6 | Merry Mama Christmas Sweatshirt / Retro Varsity Gingham Holiday Crewneck, Unisex | CLEAN | https://images.printify.com/mockup/6ad98d1b9d94429bd0047bd6/25458/98502/merry-mama-christmas-sweatshirt-retro-varsity-gingham-holiday-crewneck-unisex.jpg?camera_label=front
6ad410369c8f61e787077ed0 | Chill Penguin Winter Hoodie — Cozy Pullover Hoodie, Winter Gift / Winstar4U | CLEAN | https://images.printify.com/mockup/6ad410369c8f61e787077ed0/32912/98424/chill-penguin-winter-hoodie-cozy-pullover-hoodie-winter-gift-winstar4u.jpg?camera_label=front
6ad410313af1c130250b630e | Snowflake Mandala Winter Hoodie — Cozy Pullover Hoodie, Winter Gift / Winstar4U | CLEAN | https://images.printify.com/mockup/6ad410313af1c130250b630e/32912/98424/snowflake-mandala-winter-hoodie-cozy-pullover-hoodie-winter-gift-winstar4u.jpg?camera_label=front
6ad4102c07b78bf56e0d2986 | Snowman Winter Hoodie — Cozy Pullover Hoodie, Winter Gift / Winstar4U | CLEAN | https://images.printify.com/mockup/6ad4102c07b78bf56e0d2986/32912/98424/snowman-winter-hoodie-cozy-pullover-hoodie-winter-gift-winstar4u.jpg?camera_label=front
6ad4102711e95e7c5f0cc68a | "Christmas Wreath 2026" Funny Christmas T-Shirt — Humorous Christmas Graphic Tee / Unisex Heavy Cotton Shirt | CLEAN | https://images.printify.com/mockup/6ad4102711e95e7c5f0cc68a/12100/102005/christmas-wreath-2026-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt.jpg?camera_label=front-2
6ad4102107b78bf56e0d297d | "I'm Only a Morning Person on Dec 25th" Funny Christmas T-Shirt — Humorous Christmas Graphic Tee / Unisex Heavy Cotton Shirt | CLEAN | https://images.printify.com/mockup/6ad4102107b78bf56e0d297d/12100/102005/im-only-a-morning-person-on-dec-25th-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt.jpg?camera_label=front-2
6ad4101c11e95e7c5f0cc687 | "Ho Ho Ho" Funny Christmas T-Shirt — Humorous Christmas Graphic Tee / Unisex Heavy Cotton Shirt | CLEAN | https://images.printify.com/mockup/6ad4101c11e95e7c5f0cc687/12100/102005/ho-ho-ho-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt.jpg?camera_label=front-2
6ad41016247ecdee090be983 | "I'm Just Here for the Christmas Snacks" Funny Christmas T-Shirt — Humorous Christmas Graphic Tee / Unisex Heavy Cotton Shirt | CLEAN | https://images.printify.com/mockup/6ad41016247ecdee090be983/12100/102005/im-just-here-for-the-christmas-snacks-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt.jpg?camera_label=front-2
6ad41011236d14a85901c8d7 | "All I Want for Christmas Is for Everyone to Go Home" Funny Christmas T-Shirt / Unisex Heavy Cotton Shirt | CLEAN | https://images.printify.com/mockup/6ad41011236d14a85901c8d7/12100/102005/all-i-want-for-christmas-is-for-everyone-to-go-home-funny-christmas-t-shirt-unisex-heavy-cotton-shirt.jpg?camera_label=front-2
6ad4100b07b78bf56e0d2977 | "I'm Full of Holiday Spirit. And Cookies." Funny Christmas T-Shirt — Humorous Christmas Graphic Tee / Unisex Heavy Cotton Shirt | CLEAN | https://images.printify.com/mockup/6ad4100b07b78bf56e0d2977/12100/102005/im-full-of-holiday-spirit-and-cookies-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt.jpg?camera_label=front-2
6ad41005247ecdee090be974 | "Dog Mom Christmas" Funny Christmas T-Shirt — Humorous Christmas Graphic Tee / Unisex Heavy Cotton Shirt | CLEAN | https://images.printify.com/mockup/6ad41005247ecdee090be974/12100/102005/dog-mom-christmas-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt.jpg?camera_label=front-2
6ad40fff247ecdee090be96e | "Bah Humbug, Pass the Eggnog" Funny Christmas T-Shirt — Humorous Christmas Graphic Tee / Unisex Heavy Cotton Shirt | CLEAN | https://images.printify.com/mockup/6ad40fff247ecdee090be96e/12100/102005/bah-humbug-pass-the-eggnog-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt.jpg?camera_label=front-2
6ad40ff99c8f61e787077eb5 | "Santa Called For Backup" Firefighter Funny Christmas T-Shirt — Humorous Holiday Graphic Tee / Unisex Heavy Cotton Shirt | CLEAN | https://images.printify.com/mockup/6ad40ff99c8f61e787077eb5/12100/102005/santa-called-for-backup-firefighter-funny-christmas-t-shirt-humorous-holiday-graphic-tee-unisex-heavy-cotton-shirt.jpg?camera_label=front-2


## 11. Etsy batch 1/3 full 97-row ID register (complete, per-product evidence, same format as §9/§10)

Format: `Printify ID | Title | Visual result | Default mockup image URL used for inspection`. Same
standing caveat as §9/§10: CLEAN is a visual-artwork judgment only; DEFECT marks the confirmed
content-mismatch finding in §8c. 75/97 have a populated Printify `external` field (channel-mapping
evidence only); 22/97 show `external: null`.

```
| 6afb724b037a5f765201a853 | My First Lunar New Year Baby Bodysuit 2027, Year of the Goat Baby Outfit, Chinese New Year Baby Gift, Newborn Goat One Piece | CLEAN | https://images.printify.com/mockup/6afb724b037a5f765201a853/31436/67/my-first-lunar-new-year-baby-bodysuit-2027-year-of-the-goat-baby-outfit-chinese-new-year-baby-gift-newborn-goat-one-piece.jpg?camera_label=front |
| 6afb7247452e689d0f0fd2cf | Year of the Goat Sticker, Lunar New Year 2027 Baby Goat Kiss-Cut Sticker, Chinese New Year Red Envelope Filler, Cute Goat Decal | CLEAN | https://images.printify.com/mockup/6afb7247452e689d0f0fd2cf/45750/16655/year-of-the-goat-sticker-lunar-new-year-2027-baby-goat-kiss-cut-sticker-chinese-new-year-red-envelope-filler-cute-goat-decal.jpg?camera_label=front |
| 6afb7235452e689d0f0fd2b5 | It's My Year Goat Shirt, Funny Year of the Goat 2027 Tee, Lunar New Year Funny T-Shirt, Chinese Zodiac Goat Gift | CLEAN | https://images.printify.com/mockup/6afb7235452e689d0f0fd2b5/12100/102005/its-my-year-goat-shirt-funny-year-of-the-goat-2027-tee-lunar-new-year-funny-t-shirt-chinese-zodiac-goat-gift.jpg?camera_label=front-2 |
| 6afb7231231f5a78fa02582f | Born in the Year of the Goat Shirt, Chinese Zodiac Goat T-Shirt, Goat Year Birthday Gift, Lunar New Year Zodiac Tee | CLEAN | https://images.printify.com/mockup/6afb7231231f5a78fa02582f/12100/102005/born-in-the-year-of-the-goat-shirt-chinese-zodiac-goat-t-shirt-goat-year-birthday-gift-lunar-new-year-zodiac-tee.jpg?camera_label=front-2 |
| 6afb721681a10a445510dcc4 | Family Lunar New Year 2027 Shirt, Matching Year of the Goat Family Tee, Chinese New Year Family Photo T-Shirt, Mom and Baby Goat | CLEAN | https://images.printify.com/mockup/6afb721681a10a445510dcc4/12100/102005/family-lunar-new-year-2027-shirt-matching-year-of-the-goat-family-tee-chinese-new-year-family-photo-t-shirt-mom-and-baby-goat.jpg?camera_label=front-2 |
| 6afb7205a1efd1254e00294f | Year of the Goat 2027 T-Shirt, Mountain Goat Sunrise Lunar New Year Tee, Chinese Zodiac Goat Shirt, Plum Blossom Gift | CLEAN | https://images.printify.com/mockup/6afb7205a1efd1254e00294f/12100/102005/year-of-the-goat-2027-t-shirt-mountain-goat-sunrise-lunar-new-year-tee-chinese-zodiac-goat-shirt-plum-blossom-gift.jpg?camera_label=front-2 |
| 6afb71f3b49d64decd050906 | Happy Lunar New Year 2027 Poster, Year of the Goat Wall Art, Chinese New Year Decor, Red Paper Cut Goat Print | CLEAN | https://images.printify.com/mockup/6afb71f3b49d64decd050906/43138/94683/happy-lunar-new-year-2027-poster-year-of-the-goat-wall-art-chinese-new-year-decor-red-paper-cut-goat-print.jpg?camera_label=front |
| 6afb71e898d0423f460f01a5 | Lucky Goat 2027 Mug, Year of the Goat Coffee Mug, Lunar New Year Gift, Chinese New Year Red Envelope Ceramic Mug 11oz 15oz | CLEAN | https://images.printify.com/mockup/6afb71e898d0423f460f01a5/65216/6310/lucky-goat-2027-mug-year-of-the-goat-coffee-mug-lunar-new-year-gift-chinese-new-year-red-envelope-ceramic-mug-11oz-15oz.jpg?camera_label=front |
| 6afb71d2141ec6078808799e | Year of the Fire Goat 2027 Sweatshirt, Lunar New Year Crewneck, Chinese Zodiac Goat Sweater, New Year 2027 Gift | CLEAN | https://images.printify.com/mockup/6afb71d2141ec6078808799e/25458/98502/year-of-the-fire-goat-2027-sweatshirt-lunar-new-year-crewneck-chinese-zodiac-goat-sweater-new-year-2027-gift.jpg?camera_label=front |
| 6afb71af231f5a78fa0257ae | Year of the Goat 2027 Shirt, Lunar New Year 2027 Tee, Chinese New Year Gift, Cute Baby Goat Red Lantern T-Shirt | CLEAN | https://images.printify.com/mockup/6afb71af231f5a78fa0257ae/12100/102005/year-of-the-goat-2027-shirt-lunar-new-year-2027-tee-chinese-new-year-gift-cute-baby-goat-red-lantern-t-shirt.jpg?camera_label=front-2 |
| 6af90b6cca5d307abc0160ff | Hooked on Christmas Hoodie, Crochet Christmas Hoodie, Crocheter Gift, Yarn Lover Holiday Hooded Sweatshirt | CLEAN | https://images.printify.com/mockup/6af90b6cca5d307abc0160ff/32912/98424/hooked-on-christmas-hoodie-crochet-christmas-hoodie-crocheter-gift-yarn-lover-holiday-hooded-sweatshirt.jpg?camera_label=front |
| 6af90b5dca5d307abc0160e1 | Golden Retriever Christmas Hoodie, Golden Christmas Hoodie, Dog Mom Gift, Golden Retriever Holiday Hooded Sweatshirt | CLEAN | https://images.printify.com/mockup/6af90b5dca5d307abc0160e1/32912/98424/golden-retriever-christmas-hoodie-golden-christmas-hoodie-dog-mom-gift-golden-retriever-holiday-hooded-sweatshirt.jpg?camera_label=front |
| 6af90b48948a470d5206d7db | Nutcracker Christmas Hoodie, Nutcracker Season Hoodie, Ballet Christmas Gift, Dance Mom Holiday Hooded Sweatshirt | CLEAN | https://images.printify.com/mockup/6af90b48948a470d5206d7db/32912/98424/nutcracker-christmas-hoodie-nutcracker-season-hoodie-ballet-christmas-gift-dance-mom-holiday-hooded-sweatshirt.jpg?camera_label=front |
| 6af90b36ca5d307abc0160a4 | Books Cocoa and Christmas Hoodie, Book Lover Christmas Hoodie, Reader Gift, Bookish Holiday Hooded Sweatshirt | CLEAN | https://images.printify.com/mockup/6af90b36ca5d307abc0160a4/32912/98424/books-cocoa-and-christmas-hoodie-book-lover-christmas-hoodie-reader-gift-bookish-holiday-hooded-sweatshirt.jpg?camera_label=front |
| 6af90b08c745d035040e94cf | Highland Cow Christmas Hoodie, Farmhouse Christmas Hoodie, Highland Cow Lover Gift, Tartan Bow Holiday Hooded Sweatshirt | CLEAN | https://images.printify.com/mockup/6af90b08c745d035040e94cf/32912/98424/highland-cow-christmas-hoodie-farmhouse-christmas-hoodie-highland-cow-lover-gift-tartan-bow-holiday-hooded-sweatshirt.jpg?camera_label=front |
| 6af8ffc7c745d035040e8965 | Cozy Season Christmas Sweatshirt, Snowy Window Hot Cocoa Crewneck, Cozy Winter Sweatshirt, Holiday Gift | CLEAN | https://images.printify.com/mockup/6af8ffc7c745d035040e8965/25458/98502/cozy-season-christmas-sweatshirt-snowy-window-hot-cocoa-crewneck-cozy-winter-sweatshirt-holiday-gift.jpg?camera_label=front |
| 6af8ffb6b2e1366dcb03a161 | Gardeners Grow Merry Christmas Sweatshirt, Gardener Christmas Gift, Plant Lover Crewneck, Vintage Seed Packet Sweatshirt | CLEAN | https://images.printify.com/mockup/6af8ffb6b2e1366dcb03a161/25458/98502/gardeners-grow-merry-christmas-sweatshirt-gardener-christmas-gift-plant-lover-crewneck-vintage-seed-packet-sweatshirt.jpg?camera_label=front |
| 6af8ffa7b2e1366dcb03a14e | Teacher Christmas Sweatshirt, Teacher Christmas Squad Crewneck, Teacher Gift, Matching School Staff Holiday Sweatshirt | CLEAN | https://images.printify.com/mockup/6af8ffa7b2e1366dcb03a14e/25458/98502/teacher-christmas-sweatshirt-teacher-christmas-squad-crewneck-teacher-gift-matching-school-staff-holiday-sweatshirt.jpg?camera_label=front |
| 6af8ff93383728621d0110c3 | Nurse Christmas Sweatshirt, Santa's Favorite Nurse Crewneck, Nurse Gift, RN Holiday Sweatshirt | CLEAN | https://images.printify.com/mockup/6af8ff93383728621d0110c3/25458/98502/nurse-christmas-sweatshirt-santas-favorite-nurse-crewneck-nurse-gift-rn-holiday-sweatshirt.jpg?camera_label=front |
| 6af8ff826d67bf35520cb20f | Cat Mom Christmas Sweatshirt, Santa Hat Tabby Cat Crewneck, Cat Lover Gift, Cat Mom Holiday Sweatshirt | CLEAN | https://images.printify.com/mockup/6af8ff826d67bf35520cb20f/25458/98502/cat-mom-christmas-sweatshirt-santa-hat-tabby-cat-crewneck-cat-lover-gift-cat-mom-holiday-sweatshirt.jpg?camera_label=front |
| 6af8ff6bc745d035040e88f4 | Hooked on Christmas Sweatshirt, Crochet Christmas Crewneck, Crocheter Gift, Yarn Lover Holiday Sweatshirt | CLEAN | https://images.printify.com/mockup/6af8ff6bc745d035040e88f4/25458/98502/hooked-on-christmas-sweatshirt-crochet-christmas-crewneck-crocheter-gift-yarn-lover-holiday-sweatshirt.jpg?camera_label=front |
| 6af8ff5ea62de2d61c0c2d2d | Golden Retriever Christmas Sweatshirt, Golden Christmas Crewneck, Dog Mom Gift, Golden Retriever Holiday Sweatshirt | CLEAN | https://images.printify.com/mockup/6af8ff5ea62de2d61c0c2d2d/25458/98502/golden-retriever-christmas-sweatshirt-golden-christmas-crewneck-dog-mom-gift-golden-retriever-holiday-sweatshirt.jpg?camera_label=front |
| 6af8ff4bc8d016720c098bf5 | Nutcracker Christmas Sweatshirt, Nutcracker Season Crewneck, Ballet Christmas Gift, Dance Mom Holiday Sweatshirt | CLEAN | https://images.printify.com/mockup/6af8ff4bc8d016720c098bf5/25458/98502/nutcracker-christmas-sweatshirt-nutcracker-season-crewneck-ballet-christmas-gift-dance-mom-holiday-sweatshirt.jpg?camera_label=front |
| 6af8ff3b6d67bf35520cb1af | Books Cocoa and Christmas Sweatshirt, Book Lover Christmas Crewneck, Reader Gift, Bookish Holiday Sweatshirt | CLEAN | https://images.printify.com/mockup/6af8ff3b6d67bf35520cb1af/25458/98502/books-cocoa-and-christmas-sweatshirt-book-lover-christmas-crewneck-reader-gift-bookish-holiday-sweatshirt.jpg?camera_label=front |
| 6af8feaa383728621d010fc2 | Highland Cow Christmas Sweatshirt, Farmhouse Christmas Crewneck, Highland Cow Lover Gift, Tartan Bow Holiday Sweatshirt | CLEAN | https://images.printify.com/mockup/6af8feaa383728621d010fc2/25458/98502/highland-cow-christmas-sweatshirt-farmhouse-christmas-crewneck-highland-cow-lover-gift-tartan-bow-holiday-sweatshirt.jpg?camera_label=front |
| 6af8e188edd1928e090c83ef | Winter Garden Field Guide Christmas Shirt, Luna Moth Mushroom T-Shirt, Cottagecore Holiday Tee, Nature Lover Gift | CLEAN | https://images.printify.com/mockup/6af8e188edd1928e090c83ef/12100/102005/winter-garden-field-guide-christmas-shirt-luna-moth-mushroom-t-shirt-cottagecore-holiday-tee-nature-lover-gift.jpg?camera_label=front-2 |
| 6af8e15fedd1928e090c839f | Frosted Star Christmas Shirt, Blue and Silver Star T-Shirt, Elegant Winter Holiday Tee, Pearl Star Christmas Gift | CLEAN | https://images.printify.com/mockup/6af8e15fedd1928e090c839f/12124/102005/frosted-star-christmas-shirt-blue-and-silver-star-t-shirt-elegant-winter-holiday-tee-pearl-star-christmas-gift.jpg?camera_label=front-2 |
| 6af8e1506d67bf35520c8bea | Tied with a Bow Christmas Shirt, Pink Satin Bow T-Shirt, Coquette Holiday Tee, Pearl Heart Christmas Gift for Her | CLEAN | https://images.printify.com/mockup/6af8e1506d67bf35520c8bea/12100/102005/tied-with-a-bow-christmas-shirt-pink-satin-bow-t-shirt-coquette-holiday-tee-pearl-heart-christmas-gift-for-her.jpg?camera_label=front-2 |
| 6af8e0c3a62de2d61c0c06c4 | Golden Retriever Christmas Shirt, Golden Christmas T-Shirt, Dog Lover Christmas Gift, Santa Hat Golden Retriever Holiday Tee | CLEAN | https://images.printify.com/mockup/6af8e0c3a62de2d61c0c06c4/12100/102005/golden-retriever-christmas-shirt-golden-christmas-t-shirt-dog-lover-christmas-gift-santa-hat-golden-retriever-holiday-tee.jpg?camera_label=front-2 |
| 6af8e0b4edd1928e090c8308 | Even Santa Needs a Paramedic Shirt, Paramedic Christmas Gift, EMT EMS Holiday T-Shirt, Ambulance Xmas Tee, First Responder | CLEAN | https://images.printify.com/mockup/6af8e0b4edd1928e090c8308/12100/102005/even-santa-needs-a-paramedic-shirt-paramedic-christmas-gift-emt-ems-holiday-t-shirt-ambulance-xmas-tee-first-responder.jpg?camera_label=front-2 |
| 6af8d8d2a62de2d61c0bff5d | Cat Mom Christmas Shirt, Santa Hat Tabby Cat T-Shirt, Cat Lover Christmas Gift, Cat Mama Holiday Tee, Gift for Cat Owner | CLEAN | https://images.printify.com/mockup/6af8d8d2a62de2d61c0bff5d/12100/102005/cat-mom-christmas-shirt-santa-hat-tabby-cat-t-shirt-cat-lover-christmas-gift-cat-mama-holiday-tee-gift-for-cat-owner.jpg?camera_label=front-2 |
| 6af8d8c0383728621d00e292 | Santa's Favorite Hairstylist Christmas Shirt, Hair Stylist Gift, Salon Holiday T-Shirt, Hairdresser Xmas Tee, Barber Gift | CLEAN | https://images.printify.com/mockup/6af8d8c0383728621d00e292/12100/102005/santas-favorite-hairstylist-christmas-shirt-hair-stylist-gift-salon-holiday-t-shirt-hairdresser-xmas-tee-barber-gift.jpg?camera_label=front-2 |
| 6af8d8af626b8d7aa001565b | Naughty or Nice Christmas Shirt, Santa's List T-Shirt, Vintage Scroll Holiday Tee, Funny Christmas Party Shirt, Xmas Gift | CLEAN | https://images.printify.com/mockup/6af8d8af626b8d7aa001565b/12100/102005/naughty-or-nice-christmas-shirt-santas-list-t-shirt-vintage-scroll-holiday-tee-funny-christmas-party-shirt-xmas-gift.jpg?camera_label=front-2 |
| 6af8d89e626b8d7aa0015637 | Santa's Favorite Nurse Christmas Shirt, Nurse Christmas Gift, Stethoscope Santa Hat T-Shirt, RN Holiday Tee, Nursing Gift | CLEAN | https://images.printify.com/mockup/6af8d89e626b8d7aa0015637/12100/102005/santas-favorite-nurse-christmas-shirt-nurse-christmas-gift-stethoscope-santa-hat-t-shirt-rn-holiday-tee-nursing-gift.jpg?camera_label=front-2 |
| 6af8d8912ffca93f7e0c7c2c | Teacher Christmas Squad Shirt, Teacher Christmas Gift, Chalkboard Holiday T-Shirt, School Staff Xmas Tee, Teacher Team Shirt | CLEAN | https://images.printify.com/mockup/6af8d8912ffca93f7e0c7c2c/12100/102005/teacher-christmas-squad-shirt-teacher-christmas-gift-chalkboard-holiday-t-shirt-school-staff-xmas-tee-teacher-team-shirt.jpg?camera_label=front-2 |
| 6af8d6309e4469c0080fb7bc | Midnight Christmas Shirt, Stained Glass Moon and Stars T-Shirt, Celestial Holiday Tee, Holly Christmas Gift | CLEAN | https://images.printify.com/mockup/6af8d6309e4469c0080fb7bc/12100/102005/midnight-christmas-shirt-stained-glass-moon-and-stars-t-shirt-celestial-holiday-tee-holly-christmas-gift.jpg?camera_label=front-2 |
| 6af8d6034643b0e30509224f | Opening Night Christmas Shirt, Theater Lover Gift, Broadway Fan Holiday T-Shirt, Red Stage Curtain Tee, Drama Gift | CLEAN | https://images.printify.com/mockup/6af8d6034643b0e30509224f/12100/102005/opening-night-christmas-shirt-theater-lover-gift-broadway-fan-holiday-t-shirt-red-stage-curtain-tee-drama-gift.jpg?camera_label=front-2 |
| 6af8d5d4383728621d00df34 | Apres Ski Club Christmas Shirt, Skier Gift, Ski Lover Holiday T-Shirt, Ski Goggles Mountain Tee, Ski Trip Shirt | CLEAN | https://images.printify.com/mockup/6af8d5d4383728621d00df34/12100/102005/apres-ski-club-christmas-shirt-skier-gift-ski-lover-holiday-t-shirt-ski-goggles-mountain-tee-ski-trip-shirt.jpg?camera_label=front-2 |
| 6af8d5caca5d307abc0120fd | Cozy Season Christmas Shirt, Snowy Window Hot Cocoa Books T-Shirt, Hygge Holiday Tee, Cozy Winter Gift for Her | CLEAN | https://images.printify.com/mockup/6af8d5caca5d307abc0120fd/12100/102005/cozy-season-christmas-shirt-snowy-window-hot-cocoa-books-t-shirt-hygge-holiday-tee-cozy-winter-gift-for-her.jpg?camera_label=front-2 |
| 6af8d5b4a2664d401605a9fe | Tartan and Tradition Christmas Shirt, Red Plaid Bow T-Shirt, Blue and White Ornament Holiday Tee, Classic Christmas Gift | CLEAN | https://images.printify.com/mockup/6af8d5b4a2664d401605a9fe/12100/102005/tartan-and-tradition-christmas-shirt-red-plaid-bow-t-shirt-blue-and-white-ornament-holiday-tee-classic-christmas-gift.jpg?camera_label=front-2 |
| 6af8c9ef4643b0e305091687 | Winter Herbarium Christmas Shirt, Vintage Botanical T-Shirt, Holly Pine Dried Orange Tee, Nature Lover Holiday Gift | CLEAN | https://images.printify.com/mockup/6af8c9ef4643b0e305091687/12100/102005/winter-herbarium-christmas-shirt-vintage-botanical-t-shirt-holly-pine-dried-orange-tee-nature-lover-holiday-gift.jpg?camera_label=front-2 |
| 6af8c9df4643b0e305091678 | Nonna's Christmas Kitchen Shirt, Nonna Gift, Italian Grandma Christmas T-Shirt, Baking Holiday Tee, Gift for Grandma | CLEAN | https://images.printify.com/mockup/6af8c9df4643b0e305091678/12100/102005/nonnas-christmas-kitchen-shirt-nonna-gift-italian-grandma-christmas-t-shirt-baking-holiday-tee-gift-for-grandma.jpg?camera_label=front-2 |
| 6af8c9cec745d035040e4b79 | Nutcracker Season Christmas Shirt, Classic Nutcracker T-Shirt, Ballet Christmas Gift, Vintage Holiday Tee, Nutcracker Lover | CLEAN | https://images.printify.com/mockup/6af8c9cec745d035040e4b79/12100/102005/nutcracker-season-christmas-shirt-classic-nutcracker-t-shirt-ballet-christmas-gift-vintage-holiday-tee-nutcracker-lover.jpg?camera_label=front-2 |
| 6af8c9bf626b8d7aa00147c2 | Highland Cow Christmas Shirt, Farmhouse Christmas T-Shirt, Highland Cow Lover Gift, Tartan Bow Holiday Tee, Cow Shirt | CLEAN | https://images.printify.com/mockup/6af8c9bf626b8d7aa00147c2/12100/102005/highland-cow-christmas-shirt-farmhouse-christmas-t-shirt-highland-cow-lover-gift-tartan-bow-holiday-tee-cow-shirt.jpg?camera_label=front-2 |
| 6af8c98c948a470d52068d4d | Cat Lineup Shirt, Funny Cat T-Shirt, Cat Lover Gift, Cats in Prison Stripes Police Lineup Tee, Cat Mom Cat Dad Shirt | CLEAN | https://images.printify.com/mockup/6af8c98c948a470d52068d4d/12100/102005/cat-lineup-shirt-funny-cat-t-shirt-cat-lover-gift-cats-in-prison-stripes-police-lineup-tee-cat-mom-cat-dad-shirt.jpg?camera_label=front-2 |
| 6af8c97da2664d4016059f77 | Hooked on Christmas Shirt, Crochet Lover Christmas Gift, Yarn Knitting Holiday T-Shirt, Crocheter Xmas Tee for Her | CLEAN | https://images.printify.com/mockup/6af8c97da2664d4016059f77/12100/102005/hooked-on-christmas-shirt-crochet-lover-christmas-gift-yarn-knitting-holiday-t-shirt-crocheter-xmas-tee-for-her.jpg?camera_label=front-2 |
| 6af8c96c2ffca93f7e0c6dce | Santa's Favorite Mechanic Christmas Shirt, Auto Mechanic Gift, Car Guy Holiday T-Shirt, Funny Garage Xmas Tee for Him | CLEAN | https://images.printify.com/mockup/6af8c96c2ffca93f7e0c6dce/12100/102005/santas-favorite-mechanic-christmas-shirt-auto-mechanic-gift-car-guy-holiday-t-shirt-funny-garage-xmas-tee-for-him.jpg?camera_label=front-2 |
| 6af8c95cc745d035040e4b00 | Books Cocoa and Christmas Shirt, Book Lover Christmas Gift, Bookworm Holiday T-Shirt, Reading Teacher Librarian Xmas Tee | CLEAN | https://images.printify.com/mockup/6af8c95cc745d035040e4b00/12100/102005/books-cocoa-and-christmas-shirt-book-lover-christmas-gift-bookworm-holiday-t-shirt-reading-teacher-librarian-xmas-tee.jpg?camera_label=front-2 |
| 6af8c913a62de2d61c0befd3 | Santa's Got a Truck Driver Christmas Shirt, Funny Trucker Christmas Gift, Semi Truck Holiday T-Shirt, CDL Driver Xmas Tee | CLEAN | https://images.printify.com/mockup/6af8c913a62de2d61c0befd3/12100/102005/santas-got-a-truck-driver-christmas-shirt-funny-trucker-christmas-gift-semi-truck-holiday-t-shirt-cdl-driver-xmas-tee.jpg?camera_label=front-2 |
| 6af8c4374643b0e30509119d | Gardeners Grow Merry Christmas Shirt, Gardener Christmas Gift, Plant Lover Holiday T-Shirt, Vintage Seed Packet Tee | CLEAN | https://images.printify.com/mockup/6af8c4374643b0e30509119d/12100/102005/gardeners-grow-merry-christmas-shirt-gardener-christmas-gift-plant-lover-holiday-t-shirt-vintage-seed-packet-tee.jpg?camera_label=front-2 |
| 6adf9fb0c392daed6500ee05 | Christmas Coffee Club Mug - 15oz Ceramic Coffee Mug, Santa Hat Latte Art, Coffee Lover Gift | CLEAN | https://images.printify.com/mockup/6adf9fb0c392daed6500ee05/104692/101750/christmas-coffee-club-mug-15oz-ceramic-coffee-mug-santa-hat-latte-art-coffee-lover-gift.jpg?camera_label=front |
| 6ade4bc3aa01a54ae306f9ad | Read Sip Repeat Christmas Mug - 15oz Ceramic Coffee Mug, Book Lover Gift, Bookworm Holiday Present | CLEAN | https://images.printify.com/mockup/6ade4bc3aa01a54ae306f9ad/104692/101750/read-sip-repeat-christmas-mug-15oz-ceramic-coffee-mug-book-lover-gift-bookworm-holiday-present.jpg?camera_label=front |
| 6ade4bbc3757c80615072b6d | Dad Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Santa Hat and Plaid Scarf, Gift for Dad | CLEAN | https://images.printify.com/mockup/6ade4bbc3757c80615072b6d/104692/101750/dad-fuel-christmas-mug-15oz-ceramic-coffee-mug-santa-hat-and-plaid-scarf-gift-for-dad.jpg?camera_label=front |
| 6ade4bb4580ff194290bca02 | Grandma Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Santa Hat, Glasses and Yarn, Gift for Grandma | CLEAN | https://images.printify.com/mockup/6ade4bb4580ff194290bca02/104692/101750/grandma-fuel-christmas-mug-15oz-ceramic-coffee-mug-santa-hat-glasses-and-yarn-gift-for-grandma.jpg?camera_label=front |
| 6ade4bab580ff194290bc9f7 | Mama Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Santa Hat and Cookies, Gift for Mom | CLEAN | https://images.printify.com/mockup/6ade4bab580ff194290bc9f7/104692/101750/mama-fuel-christmas-mug-15oz-ceramic-coffee-mug-santa-hat-and-cookies-gift-for-mom.jpg?camera_label=front |
| 6ade4ba0478a7d4f5f01f3c8 | Teacher Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Apple and Holly, Teacher Gift | CLEAN | https://images.printify.com/mockup/6ade4ba0478a7d4f5f01f3c8/104692/101750/teacher-fuel-christmas-mug-15oz-ceramic-coffee-mug-apple-and-holly-teacher-gift.jpg?camera_label=front |
| 6ade4b96aa1ddebc870bedc0 | Nurse Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Stethoscope Santa Hat, Nurse Gift | CLEAN | https://images.printify.com/mockup/6ade4b96aa1ddebc870bedc0/104692/101750/nurse-fuel-christmas-mug-15oz-ceramic-coffee-mug-stethoscope-santa-hat-nurse-gift.jpg?camera_label=front |
| 6ade4b8dd51db081ef0e7d2c | Cat Mom Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Tabby Cat Santa Hat, Cat Lover Gift | CLEAN | https://images.printify.com/mockup/6ade4b8dd51db081ef0e7d2c/104692/101750/cat-mom-fuel-christmas-mug-15oz-ceramic-coffee-mug-tabby-cat-santa-hat-cat-lover-gift.jpg?camera_label=front |
| 6ade4b78813f94035306f51a | Dog Mom Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Golden Retriever Santa Hat, Dog Lover Gift | CLEAN | https://images.printify.com/mockup/6ade4b78813f94035306f51a/104692/101750/dog-mom-fuel-christmas-mug-15oz-ceramic-coffee-mug-golden-retriever-santa-hat-dog-lover-gift.jpg?camera_label=front |
| 6add66f672b7b9abb209542a | Our First Christmas Mr. & Mrs. Mug - 15oz Ceramic Coffee Mug, Newlywed Gift, Married Christmas | CLEAN | https://images.printify.com/mockup/6add66f672b7b9abb209542a/104692/101750/our-first-christmas-mr-mrs-mug-15oz-ceramic-coffee-mug-newlywed-gift-married-christmas.jpg?camera_label=front |
| 6add66ef21de5de625024db6 | Be Gentle With Yourself Mug - 15oz Ceramic Coffee Mug, Retro Groovy Daisy, Positive Vibes Gift | CLEAN | https://images.printify.com/mockup/6add66ef21de5de625024db6/104692/101750/be-gentle-with-yourself-mug-15oz-ceramic-coffee-mug-retro-groovy-daisy-positive-vibes-gift.jpg?camera_label=front |
| 6adbc9485fff939bb8036a70 | Tabby Cat Christmas Ornament 2026 - Ceramic Cat Tree Ornament, Cat Lover Gift, Cat Mom Present | CLEAN | https://images.printify.com/mockup/6adbc9485fff939bb8036a70/69370/100661/tabby-cat-christmas-ornament-2026-ceramic-cat-tree-ornament-cat-lover-gift-cat-mom-present.jpg?camera_label=front |
| 6adbc9405fff939bb8036a6d | Pug Christmas Ornament 2026 - Ceramic Dog Tree Ornament, Pug Lover Gift, Stocking Stuffer | CLEAN | https://images.printify.com/mockup/6adbc9405fff939bb8036a6d/69370/100661/pug-christmas-ornament-2026-ceramic-dog-tree-ornament-pug-lover-gift-stocking-stuffer.jpg?camera_label=front |
| 6adbc9380c4296642f0b2121 | Corgi Christmas Ornament 2026 - Ceramic Dog Tree Ornament, Corgi Lover Gift | CLEAN | https://images.printify.com/mockup/6adbc9380c4296642f0b2121/69370/100661/corgi-christmas-ornament-2026-ceramic-dog-tree-ornament-corgi-lover-gift.jpg?camera_label=front |
| 6adbc92edc3e5f08af09eec5 | German Shepherd Christmas Ornament 2026 - Ceramic Dog Tree Ornament, GSD Lover Gift | CLEAN | https://images.printify.com/mockup/6adbc92edc3e5f08af09eec5/69370/100661/german-shepherd-christmas-ornament-2026-ceramic-dog-tree-ornament-gsd-lover-gift.jpg?camera_label=front |
| 6adbc925b28ea00167091751 | French Bulldog Christmas Ornament 2026 - Ceramic Frenchie Tree Ornament, Dog Lover Gift | CLEAN | https://images.printify.com/mockup/6adbc925b28ea00167091751/69370/100661/french-bulldog-christmas-ornament-2026-ceramic-frenchie-tree-ornament-dog-lover-gift.jpg?camera_label=front |
| 6adbc91d09f4718717100103 | Labrador Christmas Ornament 2026 - Ceramic Dog Tree Ornament, Yellow Lab Gift, Dog Lover Present | CLEAN | https://images.printify.com/mockup/6adbc91d09f4718717100103/69370/100661/labrador-christmas-ornament-2026-ceramic-dog-tree-ornament-yellow-lab-gift-dog-lover-present.jpg?camera_label=front |
| 6adbc915ac1177c7f010283f | Golden Retriever Christmas Ornament 2026 - Ceramic Dog Tree Ornament, Golden Lover Gift | CLEAN | https://images.printify.com/mockup/6adbc915ac1177c7f010283f/69370/100661/golden-retriever-christmas-ornament-2026-ceramic-dog-tree-ornament-golden-lover-gift.jpg?camera_label=front |
| 6adbc8d30c4296642f0b20b0 | Dachshund Christmas Ornament 2026 - Ceramic Dog Tree Ornament, Doxie Gift, Dog Lover Christmas Gift | CLEAN | https://images.printify.com/mockup/6adbc8d30c4296642f0b20b0/69370/100661/dachshund-christmas-ornament-2026-ceramic-dog-tree-ornament-doxie-gift-dog-lover-christmas-gift.jpg?camera_label=front |
| 6adbc5c5dc3e5f08af09eb7a | Pet Memorial Christmas Ornament, Paw Print Angel Wings, Dog Cat Remembrance Keepsake, Ceramic Ornament | CLEAN | https://images.printify.com/mockup/6adbc5c5dc3e5f08af09eb7a/111546/109570/pet-memorial-christmas-ornament-paw-print-angel-wings-dog-cat-remembrance-keepsake-ceramic-ornament.jpg?camera_label=front |
| 6adbc5aa04ff64518d0e7067 | Teacher Christmas Ornament, Jeweled Apple and Books Teacher Gift, Ceramic Holiday Keepsake 2026 | CLEAN | https://images.printify.com/mockup/6adbc5aa04ff64518d0e7067/111546/109570/teacher-christmas-ornament-jeweled-apple-and-books-teacher-gift-ceramic-holiday-keepsake-2026.jpg?camera_label=front |
| 6adbc58f04ff64518d0e704e | Nurse Christmas Ornament, Candy Cane Stethoscope Heart Nurse Gift, Ceramic Holiday Keepsake 2026 | CLEAN | https://images.printify.com/mockup/6adbc58f04ff64518d0e704e/111546/109570/nurse-christmas-ornament-candy-cane-stethoscope-heart-nurse-gift-ceramic-holiday-keepsake-2026.jpg?camera_label=front |
| 6adbc573c2c3b6a62f0bc564 | Celestial Christmas Ornament, Blue and Silver Moon and Star, Winter Snowflake Ceramic Tree Decor 2026 | CLEAN | https://images.printify.com/mockup/6adbc573c2c3b6a62f0bc564/111546/109570/celestial-christmas-ornament-blue-and-silver-moon-and-star-winter-snowflake-ceramic-tree-decor-2026.jpg?camera_label=front |
| 6adbc558bfae79f6740255ec | Nutcracker Christmas Ornament, Jeweled Velvet Soldier Holiday Wreath, Whimsical Ceramic Tree Decor 2026 | CLEAN | https://images.printify.com/mockup/6adbc558bfae79f6740255ec/111546/109570/nutcracker-christmas-ornament-jeweled-velvet-soldier-holiday-wreath-whimsical-ceramic-tree-decor-2026.jpg?camera_label=front |
| 6adbc53bc2c3b6a62f0bc540 | Tartan Bow Christmas Ornament, Plaid Velvet Bow Evergreen Wreath, Heirloom Ceramic Tree Decor 2026 | CLEAN | https://images.printify.com/mockup/6adbc53bc2c3b6a62f0bc540/111546/109570/tartan-bow-christmas-ornament-plaid-velvet-bow-evergreen-wreath-heirloom-ceramic-tree-decor-2026.jpg?camera_label=front |
| 6adbc51dac1177c7f010245e | Orange Tabby Cat Christmas Ornament 2026, Cat Mom Gift, Realistic Santa Hat Portrait, Merry Christmas Wreath Ceramic Keepsake | CLEAN | https://images.printify.com/mockup/6adbc51dac1177c7f010245e/111546/109570/orange-tabby-cat-christmas-ornament-2026-cat-mom-gift-realistic-santa-hat-portrait-merry-christmas-wreath-ceramic-keepsake.jpg?camera_label=front |
| 6adbc503ac1177c7f0102440 | Chocolate Lab Christmas Ornament 2026, Labrador Dog Mom Gift, Realistic Santa Hat Portrait, Merry Christmas Wreath Ceramic Keepsake | CLEAN | https://images.printify.com/mockup/6adbc503ac1177c7f0102440/111546/109570/chocolate-lab-christmas-ornament-2026-labrador-dog-mom-gift-realistic-santa-hat-portrait-merry-christmas-wreath-ceramic-keepsake.jpg?camera_label=front |
| 6adbc4e8ac1177c7f010242d | Corgi Christmas Ornament 2026, Corgi Mom Gift, Realistic Santa Hat Portrait, Merry Christmas Wreath Ceramic Keepsake | CLEAN | https://images.printify.com/mockup/6adbc4e8ac1177c7f010242d/111546/109570/corgi-christmas-ornament-2026-corgi-mom-gift-realistic-santa-hat-portrait-merry-christmas-wreath-ceramic-keepsake.jpg?camera_label=front |
| 6adbc4ce09f47187170ffd46 | French Bulldog Christmas Ornament 2026, Frenchie Mom Gift, Realistic Santa Hat Portrait, Merry Christmas Wreath Ceramic Keepsake | CLEAN | https://images.printify.com/mockup/6adbc4ce09f47187170ffd46/111546/109570/french-bulldog-christmas-ornament-2026-frenchie-mom-gift-realistic-santa-hat-portrait-merry-christmas-wreath-ceramic-keepsake.jpg?camera_label=front |
| 6adbc4b3ac1177c7f01023f4 | Golden Retriever Christmas Ornament 2026, Golden Mom Gift, Realistic Santa Hat Portrait, Merry Christmas Wreath Ceramic Keepsake | CLEAN | https://images.printify.com/mockup/6adbc4b3ac1177c7f01023f4/111546/109570/golden-retriever-christmas-ornament-2026-golden-mom-gift-realistic-santa-hat-portrait-merry-christmas-wreath-ceramic-keepsake.jpg?camera_label=front |
| 6adbc48c1406181c4108061e | Dachshund Christmas Ornament 2026, Doxie Dog Mom Gift, Realistic Santa Hat Portrait, Merry Christmas Wreath Ceramic Keepsake | CLEAN | https://images.printify.com/mockup/6adbc48c1406181c4108061e/111546/109570/dachshund-christmas-ornament-2026-doxie-dog-mom-gift-realistic-santa-hat-portrait-merry-christmas-wreath-ceramic-keepsake.jpg?camera_label=front |
| 6ad50c137e86416ffc09854a | Cheers Dears Wine Tumbler 20oz | Retro Christmas Wine Tumbler, Holiday Gift | CLEAN | https://images.printify.com/mockup/6ad50c137e86416ffc09854a/44519/849/cheers-dears-wine-tumbler-20oz-retro-christmas-wine-tumbler-holiday-gift.jpg?camera_label=front |
| 6ad50c1233bc1400d808831d | Made It Wine Tumbler 20oz | Funny Christmas Lights Wine Tumbler, Holiday Gift | CLEAN | https://images.printify.com/mockup/6ad50c1233bc1400d808831d/44519/849/made-it-wine-tumbler-20oz-funny-christmas-lights-wine-tumbler-holiday-gift.jpg?camera_label=front |
| 6ad50c0fc5bf429b0a083b1e | Cozy Season Sunburst Phone Case | Magnetic Impact-Resistant Case, Retro Holiday Gift | CLEAN | https://images.printify.com/mockup/6ad50c0fc5bf429b0a083b1e/96135/81354/cozy-season-sunburst-phone-case-magnetic-impact-resistant-case-retro-holiday-gift.jpg?camera_label=front |
| 6ad50c0dc5bf429b0a083b1d | Cute Reindeer Lights Phone Case | Magnetic Impact-Resistant Case, Festive Christmas Gift | CLEAN | https://images.printify.com/mockup/6ad50c0dc5bf429b0a083b1d/96135/81354/cute-reindeer-lights-phone-case-magnetic-impact-resistant-case-festive-christmas-gift.jpg?camera_label=front |
| 6ad50c0be2ff8ddc0b0e6f3c | Christmas Fox Scarf Phone Case | Magnetic Impact-Resistant Case, Cute Holiday Gift | CLEAN | https://images.printify.com/mockup/6ad50c0be2ff8ddc0b0e6f3c/96135/81354/christmas-fox-scarf-phone-case-magnetic-impact-resistant-case-cute-holiday-gift.jpg?camera_label=front |
| 6ad4ed6d55fae0bc720d564b | 25th Anniversary Silver Bauble Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Silver Anniversary Gift for Couples - Winstar4U | CLEAN | https://images.printify.com/mockup/6ad4ed6d55fae0bc720d564b/69370/100661/25th-anniversary-silver-bauble-christmas-ornament-2026-ceramic-holiday-tree-ornament-silver-anniversary-gift-for-couples-winstar4u.jpg?camera_label=front |
| 6ad456e49c8f61e78707bfa1 | Buffalo Plaid Ornament Phone Case | Magnetic Impact-Resistant Case, Rustic Christmas Gift | CLEAN | https://images.printify.com/mockup/6ad456e49c8f61e78707bfa1/96135/81354/buffalo-plaid-ornament-phone-case-magnetic-impact-resistant-case-rustic-christmas-gift.jpg?camera_label=front |
| 6ad4561cf1aeec4b590f9b48 | Merry and Bright Christmas Mug - 15oz Ceramic Coffee Mug, Retro Holiday Gift | CLEAN | https://images.printify.com/mockup/6ad4561cf1aeec4b590f9b48/62014/2711/merry-and-bright-christmas-mug-15oz-ceramic-coffee-mug-retro-holiday-gift.jpg?camera_label=front |
| 6ad455ac18e0243bd10d7d4f | Cozy Holiday Brew Christmas Mug - 15oz Ceramic Coffee Mug, Festive Cocoa and Coffee Gift | CLEAN | https://images.printify.com/mockup/6ad455ac18e0243bd10d7d4f/62014/2711/cozy-holiday-brew-christmas-mug-15oz-ceramic-coffee-mug-festive-cocoa-and-coffee-gift.jpg?camera_label=front |
| 6ad455435a892ab3e300fe69 | Candy Cane and Holly Christmas Mug - 15oz Ceramic Coffee Mug, Vintage Holiday Gift | CLEAN | https://images.printify.com/mockup/6ad455435a892ab3e300fe69/62014/2711/candy-cane-and-holly-christmas-mug-15oz-ceramic-coffee-mug-vintage-holiday-gift.jpg?camera_label=front |
| 6ad432a411e95e7c5f0ce1ea | 5th Anniversary Wooden Heart Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Wood Anniversary Gift for Couples | CLEAN | https://images.printify.com/mockup/6ad432a411e95e7c5f0ce1ea/69370/100661/5th-anniversary-wooden-heart-christmas-ornament-2026-ceramic-holiday-tree-ornament-wood-anniversary-gift-for-couples.jpg?camera_label=front |
| 6ad431b65492c45147091870 | Golden Wedding Rings on Pine Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Golden Anniversary Gift for Couples | CLEAN | https://images.printify.com/mockup/6ad431b65492c45147091870/69370/100661/golden-wedding-rings-on-pine-christmas-ornament-2026-ceramic-holiday-tree-ornament-golden-anniversary-gift-for-couples.jpg?camera_label=front |
| 6ad4307c18e0243bd10d533d | Reindeer Cribbage Peg Race Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Game Night Gift for Card Players | CLEAN | https://images.printify.com/mockup/6ad4307c18e0243bd10d533d/69370/100661/reindeer-cribbage-peg-race-christmas-ornament-2026-ceramic-holiday-tree-ornament-game-night-gift-for-card-players.jpg?camera_label=front |
| 6ad42ff6f1aeec4b590f726e | Christmas Cards and Holly Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Game Night Gift for Card Players | CLEAN | https://images.printify.com/mockup/6ad42ff6f1aeec4b590f726e/69370/100661/christmas-cards-and-holly-christmas-ornament-2026-ceramic-holiday-tree-ornament-game-night-gift-for-card-players.jpg?camera_label=front |
| 6ad429db236d14a85901de42 | Buffalo Plaid Heart Christmas Mug - 15oz Ceramic Coffee Mug, Cozy Rustic Holiday Gift | CLEAN | https://images.printify.com/mockup/6ad429db236d14a85901de42/62014/2711/buffalo-plaid-heart-christmas-mug-15oz-ceramic-coffee-mug-cozy-rustic-holiday-gift.jpg?camera_label=front |
| 6ad42970f1aeec4b590f6d00 | Funny Ornament Gift Set of 3 - Ceramic Holiday Tree Ornaments, Gag Gift Set, White Elephant Gift Set | DEFECT | https://images.printify.com/mockup/6ad42970f1aeec4b590f6d00/69370/100661/funny-ornament-gift-set-of-3-ceramic-holiday-tree-ornaments-gag-gift-set-white-elephant-gift-set.jpg?camera_label=front |
```
