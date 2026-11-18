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
| #361-460 | **Full visual inspection (100/100), see §8f** — 30/100 confirmed defects, 2 true duplicates | T-33172S0T0O (this session) |
| #461-560 | **Full visual inspection (100/100), see §8g** — 46/100 confirmed defects (highest rate yet), 1 true duplicate pair | T-3F0A655857 (this session) |
| #561-2,429 | **NOT STARTED** (1,869 products) | Next batch(es) |

## 8. Next eligible batch (for whichever session/dispatcher firing picks this up next)

1. Shopify shop 26418699, #561 onward, continuing in ~100-product batches with full visual inspection
   (every default mockup viewed, not sampled) — see §8f and §8g for the major defect-rate finding (now
   confirmed across two consecutive batches, 30% then 46%) that makes full inspection (not sampling)
   essential for this shop, and specifically for the Backpack and Laptop Sleeve blueprints. 1,869 products
   remain unstarted.
2. **eBay is now COMPLETE (53/53 visually inspected, see §6a) — do not re-inspect.** **Amazon is now
   COMPLETE (62/62 visually inspected, see §8a) — do not re-inspect.** **TikTok is now COMPLETE (71/71
   visually inspected, see §8b) — do not re-inspect.** **Etsy is now FULLY COMPLETE — all 297 products
   visually inspected across the pre-existing inspection round plus batches 1/3 (§8c), 2/3 (§8d), and 3/3
   (§8e) — do not re-inspect any ID in §9–§13.** Only Shopify (2,429 remaining of 2,912 total, see item 1
   above) remains as an unstarted shop in this five-shop recovery.
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

## 8d. Etsy shop (26603005) batch 2/3 — COMPLETE: 97/97 visually inspected, 0 confirmed defects, 2
## confirmed true duplicate pairs, 1 IP/trademark flag (2026-11-18, this session)

**Status: batch 2 of 3 for the Etsy shop, following batch 1 (§8c, 97/97, 1 confirmed defect).** 97/97
products in this batch visually inspected (every default mockup downloaded and opened). 0 confirmed
artwork/cropping/spelling defects. 2 confirmed true duplicate-listing pairs (same artwork, same Printify
blueprint/product template). 1 trademark/IP risk flagged for owner review. 194/291 of the Etsy backlog
is now covered across batches 1+2; batch 3 (97 products) remains, roster pre-staged at
`batch3.json` in the scratchpad.

### CONFIRMED TRUE DUPLICATE PAIR 1: Puerto Rico Flag Phone Case

`6a493c49e2256aa80f0b82c5` ("Puerto Rico Flag Phone Case | Tough Cases") and `6a493c41e2256aa80f0b82c2`
("Puerto Rico Flag Phone Case | Tough Case") — identical print-area image (`fd-pr-starfix-bp421.jpg`),
identical scale (1.01) and position (0.5/0.5), **identical Printify blueprint (421, same case model)**.
Confirmed pixel-identical by viewing both default mockups side by side. Titles differ only by "Cases" vs
"Case." This is the same severity class as the Amazon duplicate-ASIN finding in §8a: two separate Printify
product records selling the exact same physical item.

### CONFIRMED TRUE DUPLICATE PAIR 2: American Flag Sea Turtle T-Shirt

`6a5196c03a9be4cece03732d` ("...Patriotic Ocean Turtle Tee") and `6a51901cc25325ab6a026059`
("...Patriotic Turtle Shirt USA") — identical print-area image (`Turtle Americana.png`), identical scale
(0.966) and position, **identical Printify blueprint (145, same T-shirt template)**. Confirmed
pixel-identical by viewing both default mockups side by side.

### Duplicate-candidate groups checked and ruled OUT (same artwork, different blueprint/product-type — normal reuse)

This batch surfaced an unusually large "American Flag Sea Turtle" product family (11 listings: T-shirt
×3, phone case ×4, canvas wall art ×2 (framed + stretched), lunch bag, beach towel) and several
flag/pattern phone-case pairs that share artwork across **different Printify blueprints** (e.g. "Pink Bow
and Hearts Phone Case" bp421 vs "Pink Bow Hearts Phone Case" bp269; "Dominican Republic Flag Phone Case"
bp1273 vs bp421; "Brazil Flag Phone Case" bp421 vs bp1273; multiple Sea Turtle phone cases across bp421/
bp1273/bp1521/bp6). In every one of these cases the print-area scale/position differs between the two
records even when the filename matches, consistent with an artist re-cropping the same source artwork for
a different case model/phone model's placeholder — a legitimate, deliberate product-line pattern (same
style offered across phone brands/case types), not a duplicate-listing defect, consistent with the
Amazon Cat-Lineup (§8a) and TikTok Badge/Retro (§8b) precedent. Also ruled out: the two "Jumping Bass
Phone Case" listings (different filenames, different artwork — confirmed by direct visual comparison,
one more muted/realistic style, one brighter/stylized), and the "I Put the Boo in Booty Call" family (4
product types — sticker, hoodie, shirt, tote — sharing one design, normal cross-product-type reuse).
**Only the 2 pairs above share both an identical artwork fingerprint AND an identical Printify blueprint
— the bar this register uses for a true duplicate finding.**

### IP/TRADEMARK FLAG (not a visual defect — flagged per the directive's IP-review dimension)

`6a53ee979296b919210641d5` ("Matte Canvas, Framed (Multi-color)") — a framed canvas print whose artwork
is a vintage-style photo/illustration prominently featuring a "TEXACO" branded gas station storefront and
pump signage (plus a "Texaco" roundel). This was not previously flagged in the register. Recommend an
owner/counsel review of whether this specific stock/AI-generated image carries a clear usage right before
continued sale; no live action taken.

### Sync-mapping status (batch 2/3)

80/97 have a populated Printify `external` channel-mapping field; 17/97 show `external: null`. Standing
caveat applies (§1): Printify-side mapping evidence only, not confirmed Etsy-side buyability.

**Etsy batch 2/3 is closed out: 97/97 visually inspected, 0 artwork defects, 2 confirmed true duplicate
pairs, 1 IP flag. See §12 for the full per-product ID table.**

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

## 12. Etsy batch 2/3 full 97-row ID register (complete, per-product evidence, same format as §9/§10/§11)

Format: `Printify ID | Title | Visual result | Default mockup image URL used for inspection`.
`[DUP-PAIR]` marks the two confirmed true-duplicate pairs (§8d); `[IP-FLAG]` marks the one
trademark/IP risk flagged for owner review (§8d). Same standing caveat as prior ID registers:
CLEAN is a visual-artwork judgment only, not a confirmed Etsy-side buyability/sync claim.

| 6ad410659c8f61e787077ef0 | Construction Workers Make a Merry Christmas Funny Christmas T-Shirt - Humorous Christmas Graphic Tee, Unisex Heavy Cotton Shirt | CLEAN | https://images.printify.com/mockup/6ad410659c8f61e787077ef0/12100/102005/construction-workers-make-a-merry-christmas-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt.jpg?camera_label=front-2 |
| 6a493c02c49b3a4cb20a9feb | Pink Bow and Hearts Phone Case | Tough Case | CLEAN | https://images.printify.com/mockup/6a493c02c49b3a4cb20a9feb/61521/2494/pink-bow-and-hearts-phone-case-tough-case.jpg?camera_label=front-and-side |
| 6a493c3d7599ea93f7080d46 | Venezuela Heart Flag phone case | Tough Case | CLEAN | https://images.printify.com/mockup/6a493c3d7599ea93f7080d46/61521/2494/venezuela-heart-flag-phone-case-tough-case.jpg?camera_label=front-and-side |
| 6a493c1fa36a12099202d046 | Jumping Bass Phone Case | Fishing Lake Illustration, Durable Tough Case | CLEAN | https://images.printify.com/mockup/6a493c1fa36a12099202d046/62582/97458/jumping-bass-phone-case-fishing-lake-illustration-durable-tough-case.jpg?camera_label=front-and-side |
| 6a493c4ce2256aa80f0b82c7 | Dominican Republic Flag Phone Case | Magnetic Impact-Resistant Case | CLEAN | https://images.printify.com/mockup/6a493c4ce2256aa80f0b82c7/96135/81354/dominican-republic-flag-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 6a4d9a16069947de980417ae | Main Stage Marsupial Tee | Band Animal Orchestra T-Shirt | CLEAN | https://images.printify.com/mockup/6a4d9a16069947de980417ae/12100/92570/main-stage-marsupial-tee-band-animal-orchestra-t-shirt.jpg?camera_label=front |
| 6ad4288511e95e7c5f0cdab2 | Accountant Santa Calculator Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, CPA Gift, Office Christmas Gift - Winstar4U | CLEAN | https://images.printify.com/mockup/6ad4288511e95e7c5f0cdab2/69370/100661/accountant-santa-calculator-christmas-ornament-2026-ceramic-holiday-tree-ornament-cpa-gift-office-christmas-gift-winstar4u.jpg?camera_label=front |
| 6a91ea5ca9aca0129704ed8e | Spiral Notebook - Ruled Line | CLEAN | https://images.printify.com/mockup/6a91ea5ca9aca0129704ed8e/34240/3024/spiral-notebook-ruled-line.jpg?camera_label=front |
| 6a493ca508efc981890568c6 | Retro Doodle Collage Tee | Neon Smiley, Lightning, Stars, Sticker Art | CLEAN | https://images.printify.com/mockup/6a493ca508efc981890568c6/18542/92547/retro-doodle-collage-tee-neon-smiley-lightning-stars-sticker-art.jpg?camera_label=front |
| 6a9393a10b0a3612b7065bb8 | I Put the Boo in Booty Call Halloween Stickers - Funny Ghost Kiss-Cut Sticker, Spooky Laptop Decal | CLEAN | https://images.printify.com/mockup/6a9393a10b0a3612b7065bb8/45750/16655/i-put-the-boo-in-booty-call-halloween-stickers-funny-ghost-kiss-cut-sticker-spooky-laptop-decal.jpg?camera_label=front |
| 6a493c5808efc981890568b7 | Union Jack Flag Phone Case | Magnetic Impact-Resistant Case | CLEAN | https://images.printify.com/mockup/6a493c5808efc981890568b7/96135/81354/union-jack-flag-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 6ac2f508368bb1b26d051cd7 | Cookie Dealer Funny Christmas T-Shirt - Humorous Christmas Graphic Tee - Unisex Heavy Cotton Shirt | CLEAN | https://images.printify.com/mockup/6ac2f508368bb1b26d051cd7/12100/102005/cookie-dealer-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt.jpg?camera_label=front-2 |
| 6a9393a103cee7960c039cca | I Put the Boo in Booty Call Halloween Hoodie - Funny Ghost Spooky Season Sweatshirt Gift | CLEAN | https://images.printify.com/mockup/6a9393a103cee7960c039cca/32912/98424/i-put-the-boo-in-booty-call-halloween-hoodie-funny-ghost-spooky-season-sweatshirt-gift.jpg?camera_label=front |
| 6a493cbda36a12099202d051 | Dripping Rose Illustration T-shirt | Melting Floral Graphic Tee | CLEAN | https://images.printify.com/mockup/6a493cbda36a12099202d051/73207/98445/dripping-rose-illustration-t-shirt-melting-floral-graphic-tee.jpg?camera_label=front |
| 6a519288dee7682ac20a71d7 | American Flag Sea Turtle Lunch Bag | Patriotic Turtle Ocean | CLEAN | https://images.printify.com/mockup/6a519288dee7682ac20a71d7/74699/19826/american-flag-sea-turtle-lunch-bag-patriotic-turtle-ocean.jpg?camera_label=front |
| 6a493cc8a36a12099202d055 | Brazil Heart Flag phone case | Tough Cases | CLEAN | https://images.printify.com/mockup/6a493cc8a36a12099202d055/61521/2494/brazil-heart-flag-phone-case-tough-cases.jpg?camera_label=front-and-side |
| 6a518db03a9be4cece0363ae | American Flag Sea Turtle phone case | iPhone Samsung patriotic turtle | CLEAN | https://images.printify.com/mockup/6a518db03a9be4cece0363ae/112191/105690/american-flag-sea-turtle-phone-case-iphone-samsung-patriotic-turtle.jpg?camera_label=front |
| 6a493c5a08efc981890568b9 | Mexican Flag Heart Phone Case | Magnetic Impact-Resistant Case | CLEAN | https://images.printify.com/mockup/6a493c5a08efc981890568b9/96135/81354/mexican-flag-heart-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 6a53f01e80e93ca2e00be91c | Fly Fishing Canvas Wall Art - Framed Mountain River Print, Rustic Cabin Decor, Gift for Fishermen | CLEAN | https://images.printify.com/mockup/6a53f01e80e93ca2e00be91c/244002/169199/fly-fishing-canvas-wall-art-framed-mountain-river-print-rustic-cabin-decor-gift-for-fishermen.jpg?camera_label=front |
| 6a53ec619296b91921063ffc | American Flag Sea Turtle Canvas Wall Art - Framed Patriotic Ocean Print, Coastal Beach Decor Gift | CLEAN | https://images.printify.com/mockup/6a53ec619296b91921063ffc/244002/169199/american-flag-sea-turtle-canvas-wall-art-framed-patriotic-ocean-print-coastal-beach-decor-gift.jpg?camera_label=front |
| 6a493c5508efc981890568b5 | Canadian Flag Phone Case | Tough Case | CLEAN | https://images.printify.com/mockup/6a493c5508efc981890568b5/61521/2494/canadian-flag-phone-case-tough-case.jpg?camera_label=front-and-side |
| 6ac2f50abde50e6b7a0cb4a6 | Festive AF Funny Christmas T-Shirt - Humorous Christmas Graphic Tee - Unisex Heavy Cotton Shirt | CLEAN | https://images.printify.com/mockup/6ac2f50abde50e6b7a0cb4a6/12100/102005/festive-af-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt.jpg?camera_label=front-2 |
| 6a518e6d3a9be4cece0364c7 | American Flag Sea Turtle phone case | Phone Case | CLEAN | https://images.printify.com/mockup/6a518e6d3a9be4cece0364c7/130091/111262/american-flag-sea-turtle-phone-case-phone-case.jpg?camera_label=front |
| 6a53ed8256fc14f8d20264b4 | Owl Family Canvas Wall Art - Framed Woodland Owl and Owlets Print, Rustic Nursery Cabin Decor Gift | CLEAN | https://images.printify.com/mockup/6a53ed8256fc14f8d20264b4/244002/169199/owl-family-canvas-wall-art-framed-woodland-owl-and-owlets-print-rustic-nursery-cabin-decor-gift.jpg?camera_label=front |
| 6a518f9a88a0f72a6207dc03 | American Flag Sea Turtle T-Shirt | Patriotic Turtle Tee | CLEAN | https://images.printify.com/mockup/6a518f9a88a0f72a6207dc03/12100/92570/american-flag-sea-turtle-t-shirt-patriotic-turtle-tee.jpg?camera_label=front |
| 6ad423ddf1aeec4b590f682a | Mahjong Christmas Ornament 2026 - Ceramic Tile Wreath Tree Ornament, Game Night Gift for Mahjong Players | CLEAN | https://images.printify.com/mockup/6ad423ddf1aeec4b590f682a/69370/100661/mahjong-christmas-ornament-2026-ceramic-tile-wreath-tree-ornament-game-night-gift-for-mahjong-players.jpg?camera_label=front |
| 6a493cc2a36a12099202d053 | Panama Flag Heart Phone Case Patriotic Panama iPhone Case | CLEAN | https://images.printify.com/mockup/6a493cc2a36a12099202d053/61521/2494/panama-flag-heart-phone-case-patriotic-panama-iphone-case.jpg?camera_label=front-and-side |
| 6a493c24a36a12099202d049 | Drippy Smiley Face Phone Case | Purple Swirl Oops Pattern | CLEAN | https://images.printify.com/mockup/6a493c24a36a12099202d049/61521/2494/drippy-smiley-face-phone-case-purple-swirl-oops-pattern.jpg?camera_label=front-and-side |
| 6a5196c03a9be4cece03732d | American Flag Sea Turtle T-Shirt | Patriotic Ocean Turtle Tee | CLEAN [DUP-PAIR] | https://images.printify.com/mockup/6a5196c03a9be4cece03732d/38191/97992/american-flag-sea-turtle-t-shirt-patriotic-ocean-turtle-tee.jpg?camera_label=front |
| 6a53ebfa9296b91921063fb1 | American Flag Sea Turtle Canvas Wall Art - Stretched Patriotic Ocean Print, Coastal Beach Decor Gift | CLEAN | https://images.printify.com/mockup/6a53ebfa9296b91921063fb1/95209/78945/american-flag-sea-turtle-canvas-wall-art-stretched-patriotic-ocean-print-coastal-beach-decor-gift.jpg?camera_label=front |
| 6a53edf3fa4d54eeeb0835d2 | Cows in Pasture Canvas Wall Art - Framed Farm Landscape Print, Rustic Country Farmhouse Decor Gift | CLEAN | https://images.printify.com/mockup/6a53edf3fa4d54eeeb0835d2/244002/169199/cows-in-pasture-canvas-wall-art-framed-farm-landscape-print-rustic-country-farmhouse-decor-gift.jpg?camera_label=front |
| 6aa5b4a1836de9f29f08aea4 | Positive Doodle Pattern Phone Case | Tough Phone Case | CLEAN | https://images.printify.com/mockup/6aa5b4a1836de9f29f08aea4/76611/97514/positive-doodle-pattern-phone-case-tough-phone-case.jpg?camera_label=front |
| 6ad4116c3af1c130250b6447 | Christmas Calories Don't Count Shirt - Funny Foodie Holiday Tee, Xmas Gift for Bakers & Cookie Lovers | CLEAN | https://images.printify.com/mockup/6ad4116c3af1c130250b6447/12100/102005/christmas-calories-dont-count-shirt-funny-foodie-holiday-tee-xmas-gift-for-bakers-cookie-lovers.jpg?camera_label=front-2 |
| 6ad426a6236d14a85901dbdd | 10th Anniversary Tin Star Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Tin Anniversary Gift for Couples - Winstar4U | CLEAN | https://images.printify.com/mockup/6ad426a6236d14a85901dbdd/69370/100661/10th-anniversary-tin-star-christmas-ornament-2026-ceramic-holiday-tree-ornament-tin-anniversary-gift-for-couples-winstar4u.jpg?camera_label=front |
| 6a9393a16a6b71db650295d3 | I Put the Boo in Booty Call Halloween Shirt - Funny Ghost Halloween Tee, Spooky Party Gift | CLEAN | https://images.printify.com/mockup/6a9393a16a6b71db650295d3/79038/98448/i-put-the-boo-in-booty-call-halloween-shirt-funny-ghost-halloween-tee-spooky-party-gift.jpg?camera_label=person-2 |
| 6a493c5d08efc981890568bc | American Flag Heart Phone Case | Magnetic Impact-Resistant Case | CLEAN | https://images.printify.com/mockup/6a493c5d08efc981890568bc/96135/81354/american-flag-heart-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 6a493c01c49b3a4cb20a9fea | Pink Bow Hearts Phone Case | Tough Phone Case | CLEAN | https://images.printify.com/mockup/6a493c01c49b3a4cb20a9fea/62582/97458/pink-bow-hearts-phone-case-tough-phone-case.jpg?camera_label=front-and-side |
| 6a93901d86d78c685200e2a0 | Alien Rating Graphic Tee | HUMANS: 0/10 Would Not Abduct Again T-Shirt | CLEAN | https://images.printify.com/mockup/6a93901d86d78c685200e2a0/12100/92570/alien-rating-graphic-tee-humans-010-would-not-abduct-again-t-shirt.jpg?camera_label=front |
| 6a4d989f9a0edbf1560cfb4b | Colorful Hummingbird Floral Patch Hat | Washed Cap | CLEAN | https://images.printify.com/mockup/6a4d989f9a0edbf1560cfb4b/288219/128148/colorful-hummingbird-floral-patch-hat-washed-cap.jpg?camera_label=front |
| 6a51901cc25325ab6a026059 | American Flag Sea Turtle T-Shirt | Patriotic Turtle Shirt USA | CLEAN [DUP-PAIR] | https://images.printify.com/mockup/6a51901cc25325ab6a026059/38191/97992/american-flag-sea-turtle-t-shirt-patriotic-turtle-shirt-usa.jpg?camera_label=front |
| 6a493c397599ea93f7080d44 | Dominican Republic Heart Phone Case | Tough Case | CLEAN | https://images.printify.com/mockup/6a493c397599ea93f7080d44/61521/2494/dominican-republic-heart-phone-case-tough-case.jpg?camera_label=front-and-side |
| 6a493c8a08efc981890568c0 | God Bless the USA Tee | Patriotic Flag Letters, Fireworks 4th of July | CLEAN | https://images.printify.com/mockup/6a493c8a08efc981890568c0/12100/92570/god-bless-the-usa-tee-patriotic-flag-letters-fireworks-4th-of-july.jpg?camera_label=front |
| 6ad4281d07b78bf56e0d3d80 | Mountain Lake Pine Wreath Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Wilderness Lover Gift, Nature Ornament - Winstar4U | CLEAN | https://images.printify.com/mockup/6ad4281d07b78bf56e0d3d80/69370/100661/mountain-lake-pine-wreath-christmas-ornament-2026-ceramic-holiday-tree-ornament-wilderness-lover-gift-nature-ornament-winstar4u.jpg?camera_label=front |
| 6a91ea5c94f23b466e08d75d | Sipper Glass, 16oz | CLEAN | https://images.printify.com/mockup/6a91ea5c94f23b466e08d75d/105129/101837/sipper-glass-16oz.jpg?camera_label=front |
| 6a493c357599ea93f7080d42 | Pink Striped Bow Pattern Phone Case | Tough Magnetic Case | CLEAN | https://images.printify.com/mockup/6a493c357599ea93f7080d42/109328/107253/pink-striped-bow-pattern-phone-case-tough-magnetic-case.jpg?camera_label=front |
| 6a493c0ddf721fcc700771a9 | Red Toadstool Mushrooms Phone Case | Butterflies, Floral Nature Design | CLEAN | https://images.printify.com/mockup/6a493c0ddf721fcc700771a9/96135/81354/red-toadstool-mushrooms-phone-case-butterflies-floral-nature-design.jpg?camera_label=front |
| 6a91ea5c1c993de91b03e981 | Cotton Canvas Tote Bag | CLEAN | https://images.printify.com/mockup/6a91ea5c1c993de91b03e981/101409/93895/cotton-canvas-tote-bag.jpg?camera_label=front |
| 6a493bfdc49b3a4cb20a9fe6 | Pink Bow Pattern Phone Case | Magnetic Impact-Resistant Case | CLEAN | https://images.printify.com/mockup/6a493bfdc49b3a4cb20a9fe6/96135/81354/pink-bow-pattern-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 6a9393a16a6b71db650295d2 | I Put the Boo in Booty Call Halloween Tote Bag - Funny Ghost Trick or Treat Canvas Bag Gift | CLEAN | https://images.printify.com/mockup/6a9393a16a6b71db650295d2/101409/93895/i-put-the-boo-in-booty-call-halloween-tote-bag-funny-ghost-trick-or-treat-canvas-bag-gift.jpg?camera_label=front |
| 6ad411615492c4514708fcb1 | Baker Christmas Shirt - Funny Baking Holiday Tee, Gift for Bakers & Christmas Baking Crews | CLEAN | https://images.printify.com/mockup/6ad411615492c4514708fcb1/12100/102005/baker-christmas-shirt-funny-baking-holiday-tee-gift-for-bakers-christmas-baking-crews.jpg?camera_label=front-2 |
| 6ad41166236d14a85901ca0c | Dear Santa I Was Goodish Shirt - Funny Christmas Tee, Sarcastic Santa Letter Holiday Party Gift | CLEAN | https://images.printify.com/mockup/6ad41166236d14a85901ca0c/12100/102005/dear-santa-i-was-goodish-shirt-funny-christmas-tee-sarcastic-santa-letter-holiday-party-gift.jpg?camera_label=front-2 |
| 6a4d9953d023be308b09aa8e | Colorful Watercolor Hummingbird T-Shirt | Floral Bird Tee | CLEAN | https://images.printify.com/mockup/6a4d9953d023be308b09aa8e/12100/92570/colorful-watercolor-hummingbird-t-shirt-floral-bird-tee.jpg?camera_label=front |
| 6a53ee979296b919210641d5 | Matte Canvas, Framed (Multi-color) | CLEAN [IP-FLAG] | https://images.printify.com/mockup/6a53ee979296b919210641d5/244004/169259/matte-canvas-framed-multi-color.jpg?camera_label=front |
| 6a493c2ea36a12099202d04c | Retro Daisy Checkerboard iPhone Case | Impact-Resistant Case | CLEAN | https://images.printify.com/mockup/6a493c2ea36a12099202d04c/77016/23412/retro-daisy-checkerboard-iphone-case-impact-resistant-case.jpg?camera_label=front |
| 6ad428ed11e95e7c5f0cdb14 | Teacher Books and Apple Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Teacher Gift, Classroom Christmas Gift | CLEAN | https://images.printify.com/mockup/6ad428ed11e95e7c5f0cdb14/69370/100661/teacher-books-and-apple-christmas-ornament-2026-ceramic-holiday-tree-ornament-teacher-gift-classroom-christmas-gift.jpg?camera_label=front |
| 6ad4271084e559ec0e0b8e78 | Snowy Mountain Peaks Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Wilderness Lover Gift, Nature Ornament - Winstar4U | CLEAN | https://images.printify.com/mockup/6ad4271084e559ec0e0b8e78/69370/100661/snowy-mountain-peaks-christmas-ornament-2026-ceramic-holiday-tree-ornament-wilderness-lover-gift-nature-ornament-winstar4u.jpg?camera_label=front |
| 6ad425b8236d14a85901db0e | Golden 50th Anniversary Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Golden Anniversary Gift for Couples - Winstar4U | CLEAN | https://images.printify.com/mockup/6ad425b8236d14a85901db0e/69370/100661/golden-50th-anniversary-christmas-ornament-2026-ceramic-holiday-tree-ornament-golden-anniversary-gift-for-couples-winstar4u.jpg?camera_label=front |
| 6a493c08df721fcc700771a5 | American Flag Phone Case with Card Holder | Patriotic USA Wallet Case | CLEAN | https://images.printify.com/mockup/6a493c08df721fcc700771a5/79732/44702/american-flag-phone-case-with-card-holder-patriotic-usa-wallet-case.jpg?camera_label=front |
| 6a91ea5da9aca0129704ed8f | Pink Bows Phone Case - Coquette Bow Pattern Tough Case, Cute Girly iPhone Samsung Cover Gift | CLEAN | https://images.printify.com/mockup/6a91ea5da9aca0129704ed8f/67996/7968/pink-bows-phone-case-coquette-bow-pattern-tough-case-cute-girly-iphone-samsung-cover-gift.jpg?camera_label=front-and-side |
| 6ad4105a9c8f61e787077ee9 | Firefighter Christmas Shirt - Funny Santa Rescue Tee, Gift for Firefighter & First Responders, Holiday Party Shirt | CLEAN | https://images.printify.com/mockup/6ad4105a9c8f61e787077ee9/12100/102005/firefighter-christmas-shirt-funny-santa-rescue-tee-gift-for-firefighter-first-responders-holiday-party-shirt.jpg?camera_label=front-2 |
| 6a493c9d08efc981890568c3 | American Flag LOVE T-Shirt | Patriotic Floral Sunflower Design | CLEAN | https://images.printify.com/mockup/6a493c9d08efc981890568c3/38191/97992/american-flag-love-t-shirt-patriotic-floral-sunflower-design.jpg?camera_label=front |
| 6a493c652964869925020b3b | Brazil Flag Phone Case | Tough Phone Case | CLEAN | https://images.printify.com/mockup/6a493c652964869925020b3b/61521/2494/brazil-flag-phone-case-tough-phone-case.jpg?camera_label=front-and-side |
| 6a5191a1c25325ab6a0261d4 | American Flag Sea Turtle Beach Cloth | Boho Coastal Towel | CLEAN | https://images.printify.com/mockup/6a5191a1c25325ab6a0261d4/79535/45467/american-flag-sea-turtle-beach-cloth-boho-coastal-towel.jpg?camera_label=front |
| 6a493c0adf721fcc700771a6 | Golden Retriever and Dog Portraits Phone Case | Tough Phone Case | CLEAN | https://images.printify.com/mockup/6a493c0adf721fcc700771a6/62582/97458/golden-retriever-and-dog-portraits-phone-case-tough-phone-case.jpg?camera_label=front-and-side |
| 6a493c70df721fcc700771af | Iguana Loco Nurse Illustration T-shirt | Tropical Retro Graphic Tee | CLEAN | https://images.printify.com/mockup/6a493c70df721fcc700771af/73207/98445/iguana-loco-nurse-illustration-t-shirt-tropical-retro-graphic-tee.jpg?camera_label=front |
| 6a493c337599ea93f7080d40 | Vintage Watercolor Floral Tough Case | Blue Pink Roses Phone Cover | CLEAN | https://images.printify.com/mockup/6a493c337599ea93f7080d40/61521/2494/vintage-watercolor-floral-tough-case-blue-pink-roses-phone-cover.jpg?camera_label=front-and-side |
| 6ad4279907b78bf56e0d3d2b | Deer Under Northern Lights Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Wilderness Lover Gift, Nature Ornament - Winstar4U | CLEAN | https://images.printify.com/mockup/6ad4279907b78bf56e0d3d2b/69370/100661/deer-under-northern-lights-christmas-ornament-2026-ceramic-holiday-tree-ornament-wilderness-lover-gift-nature-ornament-winstar4u.jpg?camera_label=front |
| 6a493c622964869925020b39 | Canadian Maple Leaf Phone Case | Magnetic Impact-Resistant Case | CLEAN | https://images.printify.com/mockup/6a493c622964869925020b39/96135/81354/canadian-maple-leaf-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 6a493c49e2256aa80f0b82c5 | Puerto Rico Flag Phone Case | Tough Cases | CLEAN [DUP-PAIR] | https://images.printify.com/mockup/6a493c49e2256aa80f0b82c5/61521/2494/puerto-rico-flag-phone-case-tough-cases.jpg?camera_label=front-and-side |
| 6a493c407599ea93f7080d48 | Waving Puerto Rico Flag Phone Case | Magnetic Impact-Resistant Case | CLEAN | https://images.printify.com/mockup/6a493c407599ea93f7080d48/96135/81354/waving-puerto-rico-flag-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 6ad4244e9c8f61e787078f70 | Mahjong Tiles in Santa Hats Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Game Night Gift for Mahjong Lovers - Winstar4U | CLEAN | https://images.printify.com/mockup/6ad4244e9c8f61e787078f70/69370/100661/mahjong-tiles-in-santa-hats-christmas-ornament-2026-ceramic-holiday-tree-ornament-game-night-gift-for-mahjong-lovers-winstar4u.jpg?camera_label=front |
| 6a518d144e3673bc45016ac3 | American Flag Sea Turtle Tough Magnetic Case | Patriotic Turtle Phone Cover | CLEAN | https://images.printify.com/mockup/6a518d144e3673bc45016ac3/129532/111226/american-flag-sea-turtle-tough-magnetic-case-patriotic-turtle-phone-cover.jpg?camera_label=front |
| 6ad4213a11e95e7c5f0cd488 | Construction Worker Christmas Shirt - Funny Contractor Holiday Tee, Gift for Builders & Construction Crews | CLEAN | https://images.printify.com/mockup/6ad4213a11e95e7c5f0cd488/12100/102005/construction-worker-christmas-shirt-funny-contractor-holiday-tee-gift-for-builders-construction-crews.jpg?camera_label=front-2 |
| 6ad410763af1c130250b6337 | Dog Mom Christmas Shirt - Funny Xmas Dog Lover Tee, Paw Print Holiday Gift for Dog Moms | CLEAN | https://images.printify.com/mockup/6ad410763af1c130250b6337/12100/102005/dog-mom-christmas-shirt-funny-xmas-dog-lover-tee-paw-print-holiday-gift-for-dog-moms.jpg?camera_label=front-2 |
| 6a493c8808efc981890568be | American Flag Butterfly Canvas Lunch Bag | CLEAN | https://images.printify.com/mockup/6a493c8808efc981890568be/91358/59663/american-flag-butterfly-canvas-lunch-bag.jpg?camera_label=front |
| 6a493c6a2964869925020b3d | Brazil Flag Phone Case | Magnetic Impact-Resistant Case | CLEAN | https://images.printify.com/mockup/6a493c6a2964869925020b3d/96135/81354/brazil-flag-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 6a493c7ddf721fcc700771b1 | American Flag Butterfly Muscle Tank | America the Beautiful | CLEAN | https://images.printify.com/mockup/6a493c7ddf721fcc700771b1/125340/120169/american-flag-butterfly-muscle-tank-america-the-beautiful.jpg?camera_label=front |
| 6a493c16df721fcc700771ad | Strawberry Pattern Tough Case | Cute Pink Berry Phone Case | CLEAN | https://images.printify.com/mockup/6a493c16df721fcc700771ad/61521/2494/strawberry-pattern-tough-case-cute-pink-berry-phone-case.jpg?camera_label=front-and-side |
| 6a493bffc49b3a4cb20a9fe8 | Retro Floral Pattern Phone Case | Tough Magnetic Case | CLEAN | https://images.printify.com/mockup/6a493bffc49b3a4cb20a9fe8/109328/107253/retro-floral-pattern-phone-case-tough-magnetic-case.jpg?camera_label=front |
| 6a493c6d2964869925020b3f | Mexico Flag Phone Case | Magnetic Impact-Resistant Case | CLEAN | https://images.printify.com/mockup/6a493c6d2964869925020b3f/96135/81354/mexico-flag-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 6a493c602964869925020b37 | Canadian Maple Leaf Heart phone case | Tough Magnetic Case | CLEAN | https://images.printify.com/mockup/6a493c602964869925020b37/109328/107253/canadian-maple-leaf-heart-phone-case-tough-magnetic-case.jpg?camera_label=front |
| 6a493c51e2256aa80f0b82c9 | Dominican Republic Flag Phone Case | Tough Case | CLEAN | https://images.printify.com/mockup/6a493c51e2256aa80f0b82c9/61521/2494/dominican-republic-flag-phone-case-tough-case.jpg?camera_label=front-and-side |
| 6a493ca008efc981890568c4 | Distressed American Flag Tank Top | Vintage USA Patriotic Sleeveless Tee | CLEAN | https://images.printify.com/mockup/6a493ca008efc981890568c4/105810/102834/distressed-american-flag-tank-top-vintage-usa-patriotic-sleeveless-tee.jpg?camera_label=front |
| 6a4d9ce9069947de980419b2 | Ladybug Illustration Tee | Adorable Spring Bug Shirt, Cute Insect Graphic | CLEAN | https://images.printify.com/mockup/6a4d9ce9069947de980419b2/12100/92570/ladybug-illustration-tee-adorable-spring-bug-shirt-cute-insect-graphic.jpg?camera_label=front |
| 6ad4262318e0243bd10d4b6a | 50 Years Golden Heart Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Golden Anniversary Gift for Couples - Winstar4U | CLEAN | https://images.printify.com/mockup/6ad4262318e0243bd10d4b6a/69370/100661/50-years-golden-heart-christmas-ornament-2026-ceramic-holiday-tree-ornament-golden-anniversary-gift-for-couples-winstar4u.jpg?camera_label=front |
| 6a51933d4e3673bc450171d4 | American Flag Sea Turtle Tough Case | Patriotic Ocean Phone Case | CLEAN | https://images.printify.com/mockup/6a51933d4e3673bc450171d4/112191/105690/american-flag-sea-turtle-tough-case-patriotic-ocean-phone-case.jpg?camera_label=front |
| 6a493c41e2256aa80f0b82c2 | Puerto Rico Flag Phone Case | Tough Case | CLEAN [DUP-PAIR] | https://images.printify.com/mockup/6a493c41e2256aa80f0b82c2/61521/2494/puerto-rico-flag-phone-case-tough-case.jpg?camera_label=front-and-side |
| 6ad410603af1c130250b6328 | Bah Humbug Shirt - Funny Eggnog Christmas Tee, Sarcastic Holiday Shirt, Retro Xmas Gift for the Family Grouch | CLEAN | https://images.printify.com/mockup/6ad410603af1c130250b6328/12100/102005/bah-humbug-shirt-funny-eggnog-christmas-tee-sarcastic-holiday-shirt-retro-xmas-gift-for-the-family-grouch.jpg?camera_label=front-2 |
| 6a493c22a36a12099202d048 | Jumping Bass Phone Case | Fishing Lake Water Illustration | CLEAN | https://images.printify.com/mockup/6a493c22a36a12099202d048/61521/2494/jumping-bass-phone-case-fishing-lake-water-illustration.jpg?camera_label=front-and-side |
| 6a493c0fdf721fcc700771ab | Abstract Botanical Phone Case | Modern Leaf Art, Peach & Black Shapes | CLEAN | https://images.printify.com/mockup/6a493c0fdf721fcc700771ab/62582/97458/abstract-botanical-phone-case-modern-leaf-art-peach-black-shapes.jpg?camera_label=front-and-side |
| 6a493c7edf721fcc700771b3 | Patriot 250 Eagle Flag Dad Cap | American Flag, Distressed Embroidery | CLEAN | https://images.printify.com/mockup/6a493c7edf721fcc700771b3/105381/102307/patriot-250-eagle-flag-dad-cap-american-flag-distressed-embroidery.jpg?camera_label=front |
| 6a493c5b08efc981890568ba | Union Jack Heart Phone Case | Magnetic Impact-Resistant Case | CLEAN | https://images.printify.com/mockup/6a493c5b08efc981890568ba/96135/81354/union-jack-heart-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 6ad424bcf1aeec4b590f68ff | Cozy Mahjong Game Night Christmas Ornament 2026 - Ceramic Holiday Tree Ornament, Game Night Gift for Mahjong Lovers - Winstar4U | CLEAN | https://images.printify.com/mockup/6ad424bcf1aeec4b590f68ff/69370/100661/cozy-mahjong-game-night-christmas-ornament-2026-ceramic-holiday-tree-ornament-game-night-gift-for-mahjong-lovers-winstar4u.jpg?camera_label=front |
| 6a493bfa131a5b73ff0f1d0b | American Flag Phone Case | Magnetic Impact-Resistant Case | CLEAN | https://images.printify.com/mockup/6a493bfa131a5b73ff0f1d0b/96135/81354/american-flag-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 6ac2f509bde50e6b7a0cb4a5 | Tree Rex Funny Christmas T-Shirt - Humorous Christmas Graphic Tee - Unisex Heavy Cotton Shirt | CLEAN | https://images.printify.com/mockup/6ac2f509bde50e6b7a0cb4a5/12100/102005/tree-rex-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt.jpg?camera_label=front-2 |
| 6a493c81df721fcc700771b5 | Great American Kid Youth Tee | Distressed Flag Kids Shirt, Patriotic 4th of July | CLEAN | https://images.printify.com/mockup/6a493c81df721fcc700771b5/61520/94623/great-american-kid-youth-tee-distressed-flag-kids-shirt-patriotic-4th-of-july.jpg?camera_label=front |
| 6aa59fa32f9b5f342a0f9955 | Autumn Cozy Snowman Phone Case | Fall Pumpkin Leaves Pattern Halloween Theme | CLEAN | https://images.printify.com/mockup/6aa59fa32f9b5f342a0f9955/76611/97514/autumn-cozy-snowman-phone-case-fall-pumpkin-leaves-pattern-halloween-theme.jpg?camera_label=front |

## 8e. Etsy shop (26603005) batch 3/3 — COMPLETE: 97/97 visually inspected, 0 confirmed artwork
## defects, 15 confirmed true duplicate-listing clusters (2026-11-18, this session)

**Status: final batch for the Etsy shop, following batch 1 (§8c, 97/97, 1 confirmed defect) and batch 2
(§8d, 97/97, 2 confirmed duplicate pairs, 1 IP flag).** 97/97 products in this batch visually inspected
(every default mockup downloaded and opened). 0 confirmed cropping/alignment/spelling defects and 0
content-mismatch defects (the batch-1 "gift set" pattern was checked for and not found here). 0 new
IP/trademark flags.

**This batch is the densest for true duplicates found anywhere in the five-shop recovery so far: 15
confirmed duplicate clusters (32 of the 97 products, 33%), all within a cluster of patriotic-flag and
novelty phone-case/T-shirt listings.** Every cluster below shares an identical print-area image filename,
scale, and position **and an identical Printify blueprint (same case model/shirt template)** — the bar
this register uses for a true duplicate, same standard as §8a (Amazon) and §8d (Etsy batch 2). All 15 were
additionally confirmed by direct visual comparison of both default mockups; none were false positives.

### Confirmed true duplicate clusters (14 pairs + 1 four-way cluster)

1. **American Flag Magnetic Phone Case — 4-way cluster**: `69b021b78aab92667f02b8c6`,
   `6a493bf6131a5b73ff0f1d09`, `69c9aae97f4cb7de21100207`, `69b021984fead7b1ce06b6bf` — identical image
   `Cell Phone - American Flag 2.jpg`, same scale/position, same blueprint 1273. Four separate Printify
   listings selling the same magnetic-case design.
2. **Philippine Flag Heart Phone Case**: `6a492d222e954b33910ec4b4` / `69c9a980ce78beb8610a32f3` —
   identical image, blueprint 421.
3. **Jesus Is My Best Friend T-Shirt**: `69c9ab9daf54e9c54605a0e3` / `699fd4e4f8e5c2375807797e` —
   identical front artwork and blueprint 706. (One listing's title claims an added "Back Cross" design;
   the shared front mockup is still pixel-identical, so this is still a true front-artwork duplicate.)
4. **Smiley Face / Smiley Pattern Phone Case**: `69c9ab56e5f391153001a9d3` / `69c9ab5d936256aabc04adfd`
   — identical image, blueprint 269.
5. **Puerto Rico Flag Phone Case (flat design)**: `69c9a9d54c5d410b1f0fd5dc` / `69c9a9e888e993b7d40e17c9`
   — identical image, blueprint 421.
6. **Puerto Rico Flag Heart Phone Case**: `69c9aa13c1744955170d9473` / `69c9aa1cc1744955170d9474` —
   identical image, blueprint 421.
7. **Purrrrfect Cat T-Shirt**: `69c9ab8faa266b7a800a2474` / `699fd4ddf8e5c23758077979` — identical
   image, blueprint 706.
8. **Drink Drank Drunk St Patrick's Day T-Shirt**: `69c9ab963f8316381202b054` / `699fd4d3f8e5c23758077976`
   — identical images (both the "clover" and "drink" print layers match), blueprint 706.
9. **Canadian Flag Tough Phone Case**: `69c9aa2c2f6f1849a30b5c02` / `69c9aa54aa266b7a800a2449` —
   identical image AND identical title text ("Canadian Flag Tough Phone Case Durable Maple Leaf iPhone
   Case" on both), blueprint 421. The clearest case in this batch: two listings with the same title and
   the same artwork.
10. **American Flag One-Piece Swimsuit**: `69c9a96c6cd594938803de3d` / `6a492d15895fa49f68062146` —
    identical images on both print layers, blueprint 360.
11. **Distressed American Flag Phone Case**: `69c9aad4e5f391153001a9c0` / `69b021c56d2baa18fc0b5a6e` —
    identical image, blueprint 421.
12. **Nurse Iguana Loco T-Shirt**: `69c9aab44c5d410b1f0fd5f7` / `699fd4c8f8e5c2375807796d` — identical
    image and blueprint 706. **Note:** the second listing's title field is just "Unisex Garment-Dyed
    T-shirt" — a non-descriptive, generic placeholder title with no keywords at all. This is a secondary,
    SEO-relevant finding independent of the duplicate: the listing is effectively unsearchable on its own
    title.
13. **Hummingbird Floral Phone Case (pink background)**: `69b021cbbdf0eefec20d530c` /
    `69c9aab8ce78beb8610a3320` — identical image, blueprint 1273.
14. **American Flag Phone Case (tough, stars-stripes layout)**: `69c9aacc7f4cb7de211001f8` /
    `69b021bebdf0eefec20d5309` — identical image, blueprint 421.
15. **Ruby-throated Hummingbird Phone Case (green background)**: `69c9aac47ee2f2859c09469c` /
    `69b021d38c561a36090eb202` — identical image, blueprint 1273.

### Duplicate-candidate groups checked and ruled OUT (same artwork, different blueprint/product-type — normal reuse)

Several flag-themed phone-case pairs with matching filenames were checked and ruled out because the
print-area **scale or position differs between the two records even though the filename matches** (an
artist re-cropped the same source art for a different case model), or because they use a different
Printify blueprint entirely: the two Brazil Flag phone cases (`69c9aa933f8316381202b020` magnetic
blueprint 1273 vs `69c9aa9181d880656f0b2de0` tough-case blueprint 421 — confirmed visually distinct,
different background treatment), the two Mexico Flag phone cases (different blueprints, different case
shapes), and the broader family of national-flag "heart" phone cases (India/Italy/UK/Mexico/Panama/
Venezuela/Dominican Republic hearts) that intentionally share one template design with only the flag
graphic swapped — a legitimate design-template product line, not a duplicate-listing defect, consistent
with the Amazon Cat-Lineup (§8a), TikTok Badge/Retro (§8b), and Etsy batch-2 Sea Turtle (§8d) precedent.

### Sync-mapping status (batch 3/3)

86/97 have a populated Printify `external` channel-mapping field; 11/97 show `external: null`. Standing
caveat applies (§1): Printify-side mapping evidence only, not confirmed Etsy-side buyability.

### Etsy shop — FULL CLOSE-OUT (all 297 products: 6 previously inspected + 97+97+97 across the three
### batches)

**The Etsy shop is now 100% visually inspected.** Shop-wide totals across the 1 pre-existing inspection
round plus batches 1–3:
- **1 confirmed over-scale/cropping defect** (the cribbage ornament, §2, already resolved/documented, a
  proposed owner-approval-only fix on record).
- **1 confirmed content-mismatch defect** ("Funny Ornament Gift Set of 3" advertising 3 designs with only
  1 image present, §8c).
- **17 confirmed true duplicate-listing clusters** total (2 from batch 2 + 15 from batch 3), the largest
  duplicate-listing count of any shop in this five-shop recovery (eBay had 2, Amazon had 11, TikTok had 0).
- **1 trademark/IP flag** (TEXACO branding on a framed canvas print, §8d) requiring owner/counsel review.
- **1 minor SEO finding**: one listing (cluster 12 above) has a non-descriptive placeholder title.
- Sync-mapping gap across the shop: standing caveat applies throughout — Printify-side mapping only, never
  confirmed Etsy-side buyability/inventory/reviews.

**No live writes were made anywhere in this shop.** All duplicate-cluster, defect, and IP findings are
owner-approval-only proposals; no publish/unpublish/price/inventory/delete action was taken.

## 8f. Shopify shop (26418699, Winstar4U) #361-460 — first full-visual-inspection batch: 100/100
## visually inspected, HIGH-SEVERITY finding — 30% confirmed defect rate (2026-11-18, this session)

**This is the first Shopify batch inspected at full-visual depth (every default mockup actually opened),
rather than the metadata/sync-sampling depth used for #1-360 in earlier sessions (see §7). It surfaced
the single most severe defect-rate finding of the entire five-shop recovery.**

### HEADLINE FINDING: systemic cropping defect concentrated in the "Backpack" blueprint

Of the 34 backpack-blueprint products in this batch, **20 (59%)** show a confirmed cropping defect: the
print-area artwork is scaled/positioned so that part of the design — almost always a line of text —
is cut off by the edge of the visible print window on the product mockup. This is NOT the single
mis-entered `scale` value that caused the §2 cribbage-ornament defect; most of these backpacks use the
same `scale: 1` as many *non-defective* backpacks in the same batch, so the fault is in the **source
artwork's own height/width relative to the fixed print-area window** for this blueprint, not a single
input typo. Patterns observed:
- **Top-line text cropping** (most common): the first line of a 2-3 line slogan is cut off entirely or
  reduced to illegible slivers of letters, e.g. "O Holy Night" (only the second line visible), "Joy To
  The World" (only "...ORLD" visible), "Reason For Season" (the word "REASON" entirely missing), "Savior
  Born Manger" (top line gone).
- **Complete text-element loss**: some designs lose an entire line/banner with zero pixels visible, e.g.
  "Happy Holidays Tree" (no "HAPPY HOLIDAYS" text visible at all, just the tree graphic), "Merry Christmas
  Leave Me Alone" (no text visible at all), "I Came I Saw I Bought It" ("I CAME I SAW" entirely missing).
- **Horizontal (left/right) cropping**: "Holiday Spirit Cookies" is cut on BOTH sides, with "I'M FULL OF
  HOLID[AY SPIRIT]" and "[AND] COOKI[ES]" both clipped at the margins — a different axis than the
  top/bottom pattern, confirming this is a general artwork-vs-window sizing problem, not one bug.
- **Garbled/fragmented text** (worst cases): "Jingle Bells Santa Smells" and "Morning Person Dec25
  Skeleton" show text broken into disconnected, overlapping, illegible fragments rather than a clean crop.
- **Blank text placeholder**: "Candy Cane Lane" shows an empty rectangular sign graphic where the street
  name ("Candy Cane Lane") should render, in addition to its own top-text crop — a second, independent
  defect on the same product.

A secondary, much milder version of the same root cause (artwork sized larger than its print window)
appears on the circular "Button Pin" blueprint: **5 of ~20 button pins** show the first or last line of a
multi-line design clipped by the circular edge (e.g. "Christmas Vacation Canceled," "Christmas 2026
Caffeine Panic," "Corkscrew Wine Repeat," "Christmas Open Bar," "Chic Happens Cocktail"). These are
milder — usually one word or a few letters — and are recorded as `DEFECT-MINOR`/`DEFECT` rather than
`DEFECT-SEVERE`. Sticker Packs (die-cut, scalloped-edge products) had **zero** cropping defects in this
batch — their die-cut outline follows the artwork's own contour, so there is no fixed rectangular/circular
window to crop against. This strongly suggests the die-cut Sticker Pack blueprint is inherently immune to
this defect class, while Backpack and Button Pin (both fixed-window blueprints) are not.

**Batch tally: 100/100 visually inspected — 21 DEFECT, 4 DEFECT-SEVERE, 5 DEFECT-MINOR (30 total
defect-bearing products, 30%), 2 TRUE_DUP (one pair), 64 CLEAN, 4 CLEAN-BORDERLINE (text touches the edge
but remains fully legible, not counted as a defect).**

### CONFIRMED TRUE DUPLICATE PAIR: "Naughty List Skeleton" Backpack

`6ac71804b814691321003c5c` ("Naughty List Skeleton") and `6ac717fd57b1ebbe6c0c6ee9` ("Naughty List
Skeleton V2") — same blueprint (10823), same scale (0.9) and position (x=0.5, y=0.4999...), but DIFFERENT
print-area image filenames (`naughty-list-skeleton.jpg-TRANSPARENT.png` vs
`naughty-list-skeleton-v2.png-TRANSPARENT.png`). Filename+scale/position matching alone found this pair
as merely "same blueprint, similar name" — it was confirmed as pixel-identical artwork only by directly
viewing both mockups side by side, consistent with the same filename-mismatch-hides-a-true-duplicate
pattern first documented on Amazon's "Naughty List Cat" pair and TikTok's methodology note. The "V2"
title suffix in this case does NOT indicate a genuinely revised design — it's the same image under a new
filename.

### Duplicate-candidate groups checked and ruled OUT (same main title, different sub-design)

This Shopify design collection runs two visually distinct styles under 18 shared character/phrase
concepts: a photoreal "front-facing illustrated scene" style (e.g. "Dear Santa Explain," "Christmas Eat No
January") and near-duplicate retry/"V2" pairs. Every same-product-type, same-title-prefix candidate pair
was checked via BOTH print-area filename+scale/position matching AND direct visual comparison:
- "Christmas Eat No January" vs "...V2" (Sticker Pack): different filenames AND visibly distinct art
  (different cookie/candy-cane placement) — ruled OUT, genuinely distinct renders.
- "Dear Santa Explain" vs "Dear Santa Explain Santa" (Button Pin): completely different illustrations
  (clipboard checklist vs. shushing Santa with naughty list) — ruled OUT.
- "Deck The Halls" (Button Pin) vs "Deck The Halls Sit Down" (different Button Pin product): different
  art — ruled OUT (not actually a same-title pair, listed separately for completeness).

### Sync-mapping status (batch #361-460)

0/100 show a populated `external` field via the bulk `include_full=true` list endpoint for this Shopify
shop — unlike eBay/Amazon/TikTok, Shopify's list-endpoint response does not surface the `external` object
at all in this account; it appears to require an individual `product_id` fetch per product (consistent
with why earlier Shopify batches only sync-checked a small sample). This batch did not individually
fetch sync status for all 100 — that remains a gap for a future pass, consistent with the standing
guidance (§8 item 3: direct marketplace-side verification, not just Printify's `external` field, is the
real test of buyability regardless).

### Secondary finding: one generic/unoptimized listing title

`6ac72401cacff3948b065b5d` is titled only **"Custom Pin Buttons"** — no descriptive subtitle, no keyword
phrase, unlike every other listing in this batch and shop. Its artwork duplicates the "Christmas Party
Survivor" design (normal product-type reuse, not a defect) but also shows the same circular-edge
top-text-crop defect as other button pins. Flagged as an SEO/discoverability issue for owner review
alongside the visual defect.

**No live writes were made.** All findings above are documentation only; no publish/unpublish/price/
inventory/delete action was taken on any of these 100 products.

## 8g. Shopify shop (26418699, Winstar4U) #461-560 — second full-visual-inspection batch: 100/100
## visually inspected, 46/100 confirmed defects — highest defect rate of the whole recovery (2026-11-18, this session)

**Second consecutive full-visual Shopify batch. Confirms and sharpens the §8f systemic-cropping finding:
the defect is not confined to the Backpack blueprint — it affects the Laptop Sleeve blueprint at a
comparable rate, while apparel blueprints (T-shirt, Fleece Zip-Up, Tank Top) in the same batch remain
almost entirely clean.**

### Blueprint composition this batch
47 Laptop Sleeve, 23 Backpack, 19 Fleece Zip-Up, 10 Women's T-Shirt, 1 Tank Top.

### HEADLINE FINDING: the systemic print-window-cropping defect also affects Laptop Sleeve, at a similar rate to Backpack

| Blueprint | Count this batch | Confirmed defects | Rate |
|---|---|---|---|
| Backpack (10823) | 23 | 22 | **95.7%** |
| Laptop Sleeve (429) | 47 | 21 | **44.7%** |
| Fleece Zip-Up (66) | 19 | 1 (non-cropping, see below) | 5.3% |
| Women's T-Shirt (9) | 10 | 2 (non-cropping, see below) | 20%* |
| Tank Top (39) | 1 | 0 | 0% |

*Both T-shirt flags are a recurring source-art defect (checkerboard/receipt-placeholder), not cropping —
see below.

Backpack's 95.7% rate (22/23) in this batch is markedly worse than §8f's 59% (20/34), confirming this is
not a one-off — it is the dominant outcome for this blueprint across two independent, non-overlapping
batches (42/57 Backpacks inspected across §8f+§8g = 74% combined). Laptop Sleeve, inspected here for the
first time, shows the same failure mode at nearly the same rate (44.7%), confirming the root cause is
generic to small-fixed-print-window blueprints, not specific to Backpack.

Pattern breakdown (same taxonomy as §8f):
- **Top-line text cropping** (most common on both blueprints): e.g. "Rejoice" (Laptop Sleeve — only the
  bottom half of each letter visible), "Hallelujah Angels" (Backpack — same), "Home For Christmas" ("HOME
  FOR" gone), "Merry Christmas Let's Get Lit" (Laptop Sleeve — "MERRY" almost entirely cropped).
- **Complete text-element loss** (worst cases, several on Backpack): "Glory To God," "Everyone Go Home,"
  "Eggnog Recovery Skeleton," and "Blessed Christmas" show **zero text pixels** despite each title implying
  specific wording — only the illustration remains.
- **First-word loss on left edge**: "Christ Is Born" → "CHRIST" entirely gone, only "IS BORN" visible;
  "Amazing Grace" → "AMAZING" entirely gone, only "GRACE" visible; "Dreaming Stress Free Christmas" →
  "DREAMING" gone, only "OF A STRESS-FREE" visible.
- **Bottom-line/punchline loss**: "Naughty List Resume" (Laptop Sleeve) loses its entire punchline, "AT
  THIS POINT, IT'S A RESUME" — the joke's payoff is gone; "Christmas Party Survivor" (Backpack) loses
  "SURVIVOR" entirely, leaving only a clipped "PARTY"; "90% Stress, 10% Tinsel..." (Backpack) loses its
  punchline line, "100% Done."
- **Both-edges cropping on one product**: "Prosecco Ho Ho Ho" (Laptop Sleeve) and "Christmas Open Bar"
  (Backpack) each lose text at BOTH the top and bottom simultaneously.
- **Garbled/illegible fragments**: "Christmas Mode Dnd" and "Dear Santa Explain Santa" (both Backpack)
  crop down to illegible slivers or garbled fragments rather than a clean partial line.
- **Left/right (horizontal) cropping on a non-Backpack blueprint**: "Morning Person Dec25 Skeleton" and
  the "Naughty List Skeleton" pair (both Laptop Sleeve) lose the ends of a banner ribbon on both sides —
  confirming the horizontal-axis crop pattern first seen on Backpack in §8f also occurs on Laptop Sleeve.

Sticker Pack and apparel blueprints (T-shirt, Fleece Zip-Up, Tank Top) remain effectively immune, as in
§8f — apparel print windows are proportionally far larger than the Backpack/Laptop Sleeve chest-badge
window, so the same source artwork prints with full margin on a T-shirt or hoodie while being clipped on
a Backpack or Laptop Sleeve. This was directly confirmed multiple times this batch: the identical
"Prosecco Ho Ho Ho," "Santa's Favorite [X]," and "Only Nice For Presents" designs print cleanly on
T-shirt/Fleece Zip-Up but are cropped on Laptop Sleeve/Backpack.

**Batch tally: 100/100 visually inspected — 43 confirmed crop/text-loss defects (21 Laptop Sleeve, 22
Backpack), 1 confirmed true duplicate pair (2 products), 3 recurring non-cropping source-art defects
(2 products with an unrendered-transparency checkerboard background, 2 products — one counted among the
3 — with a receipt graphic showing literal placeholder text "PRICE" instead of values), 3 products with a
truncated/cut-off listing title (SEO defect, not visual), 1 product with a blank/unfinished sign
placeholder graphic. 49 products fully clean.**

### CONFIRMED TRUE DUPLICATE PAIR: "Naughty List Skeleton" Laptop Sleeve

`6ac7156dfa3cae10170efc83` ("Naughty List Skeleton") and `6ac7156442c818a1ad0960e6` ("Naughty List
Skeleton V2") — same blueprint (429 Laptop Sleeve), same scale (0.9) and position, but different print-area
filenames (`naughty-list-skeleton.png-TRANSPARENT.png` vs `naughty-list-skeleton-v2.png-TRANSPARENT.png`).
Confirmed pixel-identical by direct visual comparison of both mockups — the exact same pattern as the
Backpack-blueprint "Naughty List Skeleton" pair found in §8f, now showing this same character design was
duplicated under a "V2" filename across at least two different blueprints. Both members also independently
show the left/right banner-text cropping defect described above.

### Recurring non-cropping source-art defects (same bad asset reused across blueprints)

- **Unrendered-transparency checkerboard artifact**: the "Santa's Favorite Distraction" design
  (`6ac71560ed135347800f9cf6` Women's T-Shirt, `6ac715da4636838bd804f5f3` Fleece Zip-Up, and the same
  design on Laptop Sleeve `6ac71662fd7ff00ded03cb96`) prints a visible gray/white checkerboard pattern as
  its background — the classic "alpha channel not flattened before upload" artifact, printed directly onto
  three different garments. Most visible on the white T-shirt. Confirmed across 3 blueprints, so this is a
  defect in the uploaded source image itself, not a per-product scale/position error.
- **Unfinished receipt-graphic placeholder text**: the "Santa's Favorite Customer VIP" design
  (`6ac71559c077332834034f19` Women's T-Shirt and `6ac7165ea4c95c48e20365fd` Laptop Sleeve) shows a mock
  receipt literally reading "ITEM — PRICE / QUANTITY — PRICE / TOTAL — PRICE" — the word "PRICE" repeated
  as placeholder text instead of real line-item values, with only the $99,999.99 total actually filled in.
  Same source-art defect, reused across 2 blueprints.
- **Truncated listing titles** (SEO defect, not a visual defect — each product's mockup image itself is
  clean): `6ac715d9fb1d11d19e0372a0` is titled "Merry Christmas Sant..." (missing "a"), `6ac71587336f8358660116d9`
  is titled "Christmas Wishes Sta..." (missing "r"), and `6ac71524ed135347800f9ccb` is titled "Thankful
  Grateful Blesse..." (missing "d" — this product also has the top-of-field "BLESSED" cropping defect
  above, so it carries both a visual and a title defect).
- **Blank sign placeholder**: `6ac7158146dd1e896e04e2de` ("Candy Cane Lane" Laptop Sleeve) shows an empty
  green rectangular street-sign graphic where the street name should render — the same placeholder-graphic
  failure mode as §8f's "Candy Cane Lane" finding on a different blueprint.

### Duplicate-candidate groups checked and ruled OUT (same main title, different sub-design — normal product-line variation)

This batch runs the same two-style pattern documented in earlier shops: a photoreal "Badge"-style design
and a flat "Retro"-style design sharing 18+ character concepts (e.g. "Santa's Favorite Distraction/Arrow/
Customer VIP," "Only Nice For Presents," "Professional Gift Returner," "Walk By Faith," "Powered By
Cookies," "Seasons Greetings," "Jingle Bells," "Home For Christmas," "Believe," "Naughty List VIP,"
"Merry Everything Happy Always," "Noel," "Merry & Bright," "Silent Night Village," "Truck Tree/Christmas
Time," "Savior Born Manger," "Here For Snacks," "Let It Snow/Joy Holly/Joy To World"). Every same-title
pair was checked by filename+scale/position matching (none matched — confirming different artwork) AND, for
the one pair that shared a title stem across identical blueprints ("Naughty List Skeleton"), by direct
visual comparison, which is where the true duplicate above was actually caught — filename mismatch alone
would have ruled it out incorrectly, same lesson as §8f and the Amazon/TikTok batches.

### Sync-mapping status (batch #461-560)

0/100 show a populated `external` field via the bulk `include_full=true` list endpoint — consistent with
§8f's finding that this Shopify account's list endpoint does not surface the `external` object at all
(it requires an individual `product_id` fetch per product). This is a tooling/API-coverage gap, not
evidence that none of these 100 products are synced to the live Shopify storefront — no claim about
actual Shopify-side sync or buyability is made from this figure, consistent with the standing
Printify-mapping-only caveat applied throughout this register.

**No live writes were made.** All findings above are documentation only; no publish/unpublish/price/
inventory/delete action was taken on any of these 100 products.

## 13. Etsy batch 3/3 full 97-row ID register (complete, per-product evidence, same format as §9/§10/§11/§12)

Format: `Printify ID | Title | Visual result | Default mockup image URL used for inspection`.
`DUP-N` labels mark the 15 confirmed true-duplicate clusters in §8e (same N = same cluster); CLEAN is a
visual-artwork judgment only, not a confirmed Etsy-side buyability/sync claim.

| 6a493bf6131a5b73ff0f1d09 | American Flag Phone Case / Magnetic Impact-Resistant Case | DUP-1 | https://images.printify.com/mockup/6a493bf6131a5b73ff0f1d09/96135/81354/american-flag-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 6a492d222e954b33910ec4b4 | Philippine Flag Heart phone case / Philippines heart phone case | DUP-2 | https://images.printify.com/mockup/6a492d222e954b33910ec4b4/61521/2494/philippine-flag-heart-phone-case-philippines-heart-phone-case.jpg?camera_label=front-and-side |
| 6a492d15895fa49f68062146 | American Flag One-Piece Swimsuit / USA Stars Stripes Patriotic Swimwear | DUP-10 | https://images.printify.com/mockup/6a492d15895fa49f68062146/44805/1055/american-flag-one-piece-swimsuit-usa-stars-stripes-patriotic-swimwear.jpg?camera_label=front |
| 6a492d089e663ab1a903886f | American Flag Butterfly Tank Top / Patriotic Fourth of July Tee | CLEAN | https://images.printify.com/mockup/6a492d089e663ab1a903886f/105810/102834/american-flag-butterfly-tank-top-patriotic-fourth-of-july-tee.jpg?camera_label=front |
| 6a492cff895fa49f68062145 | Distressed American Flag Tank Top / Patriotic USA Stars Stripes | CLEAN | https://images.printify.com/mockup/6a492cff895fa49f68062145/105810/102834/distressed-american-flag-tank-top-patriotic-usa-stars-stripes.jpg?camera_label=front |
| 6a492cf64ef55842100a60f4 | God Bless the USA T-Shirt / Patriotic Flag Text, Fireworks 4th of July Tee | CLEAN | https://images.printify.com/mockup/6a492cf64ef55842100a60f4/12100/92570/god-bless-the-usa-t-shirt-patriotic-flag-text-fireworks-4th-of-july-tee.jpg?camera_label=front |
| 6a492cc1f97d9d50320c3fd4 | Great American Kid Youth Tee / Distressed Flag Kids T-Shirt | CLEAN | https://images.printify.com/mockup/6a492cc1f97d9d50320c3fd4/61520/94623/great-american-kid-youth-tee-distressed-flag-kids-t-shirt.jpg?camera_label=front |
| 6a492cafc9e8b8c586001fa4 | American Flag Butterfly Muscle Tank / America the Beautiful Patriotic | CLEAN | https://images.printify.com/mockup/6a492cafc9e8b8c586001fa4/125340/120169/american-flag-butterfly-muscle-tank-america-the-beautiful-patriotic.jpg?camera_label=front |
| 69c9eabbe5f391153001b492 | Brazil Flag One Piece Swimsuit Brazilian Swimwear Brazil Pride Bathing Suit Green Yellow Blue Swimwear Womens Beach Outfit | CLEAN | https://images.printify.com/mockup/69c9eabbe5f391153001b492/44749/1060/brazil-flag-one-piece-swimsuit-brazilian-swimwear-brazil-pride-bathing-suit-green-yellow-blue-swimwear-womens-beach-outfit.jpg?camera_label=front |
| 69c9abc6e5f391153001a9e2 | St. Patrick's Shamrocked & Unhinged T-Shirt | CLEAN | https://images.printify.com/mockup/69c9abc6e5f391153001a9e2/38191/97992/st-patricks-shamrocked-unhinged-t-shirt.jpg?camera_label=front |
| 69c9abc12f6f1849a30b5c4f | Shamrock Shirt St Patricks Day Shirt Lucky Clover Tee Shirt Green Graphic Tee Unisex Shirt Irish Holiday Shirt Gift Idea | CLEAN | https://images.printify.com/mockup/69c9abc12f6f1849a30b5c4f/12100/92570/shamrock-shirt-st-patricks-day-shirt-lucky-clover-tee-shirt-green-graphic-tee-unisex-shirt-irish-holiday-shirt-gift-idea.jpg?camera_label=front |
| 69c9abb7374936c29b08d0a0 | Lucky But Slightly Toxic Shirt Shamrock Tee Shirt Funny St Patricks Day Shirt Cute Clover Tee Unisex Graphic Shirt Gift Idea | CLEAN | https://images.printify.com/mockup/69c9abb7374936c29b08d0a0/12100/92570/lucky-but-slightly-toxic-shirt-shamrock-tee-shirt-funny-st-patricks-day-shirt-cute-clover-tee-unisex-graphic-shirt-gift-idea.jpg?camera_label=front |
| 69c9abb2af54e9c54605a0e6 | Zero Lucks Given Shirt Funny St Patricks Day Shirt Irish Humor Tee Shamrock Shirt Sarcastic Graphic Tee Unisex Gift Idea | CLEAN | https://images.printify.com/mockup/69c9abb2af54e9c54605a0e6/18542/92547/zero-lucks-given-shirt-funny-st-patricks-day-shirt-irish-humor-tee-shamrock-shirt-sarcastic-graphic-tee-unisex-gift-idea.jpg?camera_label=front |
| 69c9abab2f6f1849a30b5c4b | Punch Love Shirt Cute Monkey Tee Shirt Valentine Shirt Kawaii Graphic Tee Cute Couple Shirt Love Gift Unisex Funny Shirt | CLEAN | https://images.printify.com/mockup/69c9abab2f6f1849a30b5c4b/61520/94623/punch-love-shirt-cute-monkey-tee-shirt-valentine-shirt-kawaii-graphic-tee-cute-couple-shirt-love-gift-unisex-funny-shirt.jpg?camera_label=front |
| 69c9aba66cd594938803df05 | Kindness Shirt Cute Monkey Tee Shirt Positive Message Tee Inspirational Graphic Shirt Cute Cartoon Tee Unisex Gift Idea | CLEAN | https://images.printify.com/mockup/69c9aba66cd594938803df05/12100/92570/kindness-shirt-cute-monkey-tee-shirt-positive-message-tee-inspirational-graphic-shirt-cute-cartoon-tee-unisex-gift-idea.jpg?camera_label=front |
| 69c9ab9daf54e9c54605a0e3 | Jesus Is My Best Friend Shirt Christian Tee Shirt Faith Based Tee Religious Shirt Inspirational Graphic Tee Church Shirt Unisex Gift | DUP-3 | https://images.printify.com/mockup/69c9ab9daf54e9c54605a0e3/73207/98445/jesus-is-my-best-friend-shirt-christian-tee-shirt-faith-based-tee-religious-shirt-inspirational-graphic-tee-church-shirt-unisex-gift.jpg?camera_label=front |
| 69c9ab963f8316381202b054 | Drink Drank Drunk Shirt Funny St Patricks Day Shirt Drinking Tee Shamrock Shirt Party Shirt Irish Holiday Tee Unisex Gift | DUP-8 | https://images.printify.com/mockup/69c9ab963f8316381202b054/73207/98445/drink-drank-drunk-shirt-funny-st-patricks-day-shirt-drinking-tee-shamrock-shirt-party-shirt-irish-holiday-tee-unisex-gift.jpg?camera_label=front |
| 69c9ab8faa266b7a800a2474 | Purrrrfect Shirt Cute Cat Tee Shirt Funny Cat Lover Tee Kawaii Kitty Shirt Cute Animal Graphic Tee Gift For Cat Lovers Unisex Shirt | DUP-7 | https://images.printify.com/mockup/69c9ab8faa266b7a800a2474/73207/98445/purrrrfect-shirt-cute-cat-tee-shirt-funny-cat-lover-tee-kawaii-kitty-shirt-cute-animal-graphic-tee-gift-for-cat-lovers-unisex-shirt.jpg?camera_label=front |
| 69c9ab8a02f914c0070d694a | Cute Monkey Shirt Baby Monkey T Shirt Cute Animal Tee Kawaii Monkey Shirt Adorable Graphic Tee Gift For Kids Girls Boys Unisex Shirt | CLEAN | https://images.printify.com/mockup/69c9ab8a02f914c0070d694a/83039/108041/cute-monkey-shirt-baby-monkey-t-shirt-cute-animal-tee-kawaii-monkey-shirt-adorable-graphic-tee-gift-for-kids-girls-boys-unisex-shirt.jpg?camera_label=front |
| 69c9ab82472862c1430c5a1c | In My Becoming Era Shirt Inspirational Quote Tee Minimalist Aesthetic Shirt Self Growth Tee Motivational Shirt Unisex Gift Idea | CLEAN | https://images.printify.com/mockup/69c9ab82472862c1430c5a1c/18542/92547/in-my-becoming-era-shirt-inspirational-quote-tee-minimalist-aesthetic-shirt-self-growth-tee-motivational-shirt-unisex-gift-idea.jpg?camera_label=front |
| 69c9ab747f4cb7de21100219 | Cute Chick Pattern Cute Cartoon Phone Case Kawaii Aesthetic iPhone Case Cute Pattern Case Soft Girl Phone Case Trendy Girly Case Gift Idea | CLEAN | https://images.printify.com/mockup/69c9ab747f4cb7de21100219/61521/2494/cute-chick-pattern-cute-cartoon-phone-case-kawaii-aesthetic-iphone-case-cute-pattern-case-soft-girl-phone-case-trendy-girly-case-gift-idea.jpg?camera_label=front-and-side |
| 69c9ab6e2f6862e2cf0a1c69 | Pink Bow Stripes Phone Case / Tough Magnetic Case | CLEAN | https://images.printify.com/mockup/69c9ab6e2f6862e2cf0a1c69/129532/111226/pink-bow-stripes-phone-case-tough-magnetic-case.jpg?camera_label=front |
| 69c9ab6781d880656f0b2e06 | Floral Phone Case Cute Flower iPhone Case Aesthetic Phone Case Colorful Floral Case Spring Summer Phone Case Girly Case Gift Idea | CLEAN | https://images.printify.com/mockup/69c9ab6781d880656f0b2e06/61521/2494/floral-phone-case-cute-flower-iphone-case-aesthetic-phone-case-colorful-floral-case-spring-summer-phone-case-girly-case-gift-idea.jpg?camera_label=front-and-side |
| 69c9ab5d936256aabc04adfd | Smiley Pattern Tough Phone Case Bright Retro Yellow & Pink Protective Cover | DUP-4 | https://images.printify.com/mockup/69c9ab5d936256aabc04adfd/130115/111285/smiley-pattern-tough-phone-case-bright-retro-yellow-pink-protective-cover.jpg?camera_label=front |
| 69c9ab56e5f391153001a9d3 | Smiley Face Phone Case Cute Emoji iPhone Case Retro Aesthetic Phone Case Yellow Happy Face Case Trendy Fun Phone Case Gift Idea | DUP-4 | https://images.printify.com/mockup/69c9ab56e5f391153001a9d3/62582/97458/smiley-face-phone-case-cute-emoji-iphone-case-retro-aesthetic-phone-case-yellow-happy-face-case-trendy-fun-phone-case-gift-idea.jpg?camera_label=front-and-side |
| 69c9ab506cd594938803decf | Checkered Floral Phone Case Retro Flower iPhone Case Cute Daisy Phone Case Aesthetic Checkerboard Case Trendy Y2K Phone Case Gift | CLEAN | https://images.printify.com/mockup/69c9ab506cd594938803decf/77016/23412/checkered-floral-phone-case-retro-flower-iphone-case-cute-daisy-phone-case-aesthetic-checkerboard-case-trendy-y2k-phone-case-gift.jpg?camera_label=front |
| 69c9ab4a472862c1430c5a04 | Dripping Purple Smiley Face Phone Case Drip Emoji iPhone Case Retro Aesthetic Phone Case Y2K Cute Phone Case Trendy Fun Case Gift Idea | CLEAN | https://images.printify.com/mockup/69c9ab4a472862c1430c5a04/61521/2494/dripping-purple-smiley-face-phone-case-drip-emoji-iphone-case-retro-aesthetic-phone-case-y2k-cute-phone-case-trendy-fun-case-gift-idea.jpg?camera_label=front-and-side |
| 69c9ab432f6862e2cf0a1c62 | Bass Fishing Phone Case Fisherman iPhone Case Fishing Lover Gift Angler Phone Case Outdoor Nature Phone Case Fish Art Case Largemouth  | CLEAN | https://images.printify.com/mockup/69c9ab432f6862e2cf0a1c62/61521/2494/bass-fishing-phone-case-fisherman-iphone-case-fishing-lover-gift-angler-phone-case-outdoor-nature-phone-case-fish-art-case-largemouth.jpg?camera_label=front-and-side |
| 69c9ab3d374936c29b08d08e | Bass Fishing Phone Case Lake Fishing iPhone Case Fisherman Gift Angler Phone Case Outdoor Nature Case Fish Art Phone Case | CLEAN | https://images.printify.com/mockup/69c9ab3d374936c29b08d08e/62582/97458/bass-fishing-phone-case-lake-fishing-iphone-case-fisherman-gift-angler-phone-case-outdoor-nature-case-fish-art-phone-case.jpg?camera_label=front-and-side |
| 69c9ab377ee2f2859c0946b0 | Strawberry Phone Case Cute Fruit iPhone Case Aesthetic Strawberry Case Girly Phone Case Summer Phone Case Cute Pattern Case Gift | CLEAN | https://images.printify.com/mockup/69c9ab377ee2f2859c0946b0/61521/2494/strawberry-phone-case-cute-fruit-iphone-case-aesthetic-strawberry-case-girly-phone-case-summer-phone-case-cute-pattern-case-gift.jpg?camera_label=front-and-side |
| 69c9ab2faf54e9c54605a0d7 | Abstract Botanical Phone Case Aesthetic iPhone Case Minimalist Floral Case Modern Art Phone Case Neutral Tone Case Trendy Case Gift | CLEAN | https://images.printify.com/mockup/69c9ab2faf54e9c54605a0d7/62582/97458/abstract-botanical-phone-case-aesthetic-iphone-case-minimalist-floral-case-modern-art-phone-case-neutral-tone-case-trendy-case-gift.jpg?camera_label=front-and-side |
| 69c9ab28aa266b7a800a2468 | Mushroom Phone Case Cute Cottagecore iPhone Case Butterfly Floral Phone Case Nature Aesthetic Case Whimsical Forest Case Gift | CLEAN | https://images.printify.com/mockup/69c9ab28aa266b7a800a2468/96135/81354/mushroom-phone-case-cute-cottagecore-iphone-case-butterfly-floral-phone-case-nature-aesthetic-case-whimsical-forest-case-gift.jpg?camera_label=front |
| 69c9ab21374936c29b08d08a | Dog Pack Golden Retriever Phone Case Dog Lover iPhone Case Cute Puppy Case Pet Lover Gift Dog Mom Case Animal Phone Case Unisex Gift | CLEAN | https://images.printify.com/mockup/69c9ab21374936c29b08d08a/62582/97458/dog-pack-golden-retriever-phone-case-dog-lover-iphone-case-cute-puppy-case-pet-lover-gift-dog-mom-case-animal-phone-case-unisex-gift.jpg?camera_label=front-and-side |
| 69c9ab1c374936c29b08d089 | American Flag Phone Case USA iPhone Case Patriotic Phone Case USA Flag Case Fourth Of July Case Military Gift Freedom Case | CLEAN | https://images.printify.com/mockup/69c9ab1c374936c29b08d089/79732/44702/american-flag-phone-case-usa-iphone-case-patriotic-phone-case-usa-flag-case-fourth-of-july-case-military-gift-freedom-case.jpg?camera_label=front |
| 69c9ab13374936c29b08d086 | Starry Night Wallet Case Card Holder Celestial Moon Phone Case Galaxy iPhone Case Astrology Aesthetic Case Cosmic Space Phone Case Gift Idea | CLEAN | https://images.printify.com/mockup/69c9ab13374936c29b08d086/79732/44702/starry-night-wallet-case-card-holder-celestial-moon-phone-case-galaxy-iphone-case-astrology-aesthetic-case-cosmic-space-phone-case-gift-idea.jpg?camera_label=front |
| 69c9ab0eaf54e9c54605a0d2 | Romantic Pink Bow Heart Phone Case Cute Girly iPhone Case Coquette Aesthetic Case Romantic Phone Case Soft Girl Case Cute Pattern Case | CLEAN | https://images.printify.com/mockup/69c9ab0eaf54e9c54605a0d2/61521/2494/romantic-pink-bow-heart-phone-case-cute-girly-iphone-case-coquette-aesthetic-case-romantic-phone-case-soft-girl-case-cute-pattern-case.jpg?camera_label=front-and-side |
| 69c9aafe81d880656f0b2df9 | Pink Bow Heart Pattern phone case / Tough Phone Cases | CLEAN | https://images.printify.com/mockup/69c9aafe81d880656f0b2df9/130115/111285/pink-bow-heart-pattern-phone-case-tough-phone-cases.jpg?camera_label=front |
| 69c9aaf8936256aabc04adee | Vintage Floral Phone Case Retro Flower iPhone Case Boho Aesthetic Phone Case Cottagecore Floral Case Cute Nature Phone Case Gift | CLEAN | https://images.printify.com/mockup/69c9aaf8936256aabc04adee/109328/107253/vintage-floral-phone-case-retro-flower-iphone-case-boho-aesthetic-phone-case-cottagecore-floral-case-cute-nature-phone-case-gift.jpg?camera_label=front |
| 69c9aaf1aa266b7a800a2464 | Bow Phone Case Cute Girly iPhone Case Coquette Aesthetic Phone Case Pink Bow Case Romantic Heart Phone Case Cute Pattern Case | CLEAN | https://images.printify.com/mockup/69c9aaf1aa266b7a800a2464/96135/81354/bow-phone-case-cute-girly-iphone-case-coquette-aesthetic-phone-case-pink-bow-case-romantic-heart-phone-case-cute-pattern-case.jpg?camera_label=front |
| 69c9aae97f4cb7de21100207 | American Flag Phone Case USA iPhone Case Patriotic Case Fourth Of July Phone Case USA Flag Cover Military Gift Freedom Case | DUP-1 | https://images.printify.com/mockup/69c9aae97f4cb7de21100207/96135/81354/american-flag-phone-case-usa-iphone-case-patriotic-case-fourth-of-july-phone-case-usa-flag-cover-military-gift-freedom-case.jpg?camera_label=front |
| 69c9aae2aa266b7a800a2461 | Phases of the Moon phone case / Tough Case | CLEAN | https://images.printify.com/mockup/69c9aae2aa266b7a800a2461/61521/2494/phases-of-the-moon-phone-case-tough-case.jpg?camera_label=front-and-side |
| 69c9aadace78beb8610a332f | American Flag Phone Case / Magnetic Impact-Resistant Case | CLEAN | https://images.printify.com/mockup/69c9aadace78beb8610a332f/130091/111262/american-flag-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 69c9aad4e5f391153001a9c0 | Distressed American Flag phone case / Tough Cases | DUP-11 | https://images.printify.com/mockup/69c9aad4e5f391153001a9c0/61521/2494/distressed-american-flag-phone-case-tough-cases.jpg?camera_label=front-and-side |
| 69c9aacc7f4cb7de211001f8 | American Flag Phone Case / Tough Protective Phone Case, Patriotic Stars Stripes | DUP-14 | https://images.printify.com/mockup/69c9aacc7f4cb7de211001f8/61521/2494/american-flag-phone-case-tough-protective-phone-case-patriotic-stars-stripes.jpg?camera_label=front-and-side |
| 69c9aac47ee2f2859c09469c | Ruby-throated Hummingbird Phone Case / Magnetic Impact-Resistant Case | DUP-15 | https://images.printify.com/mockup/69c9aac47ee2f2859c09469c/96135/81354/ruby-throated-hummingbird-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 69c9aab8ce78beb8610a3320 | Hummingbird Floral Phone Case / Magnetic Impact-Resistant Case | DUP-13 | https://images.printify.com/mockup/69c9aab8ce78beb8610a3320/130091/111262/hummingbird-floral-phone-case-magnetic-impact-resistant-case.jpg?camera_label=front |
| 69c9aab44c5d410b1f0fd5f7 | Nurse Iguana Loco Shirt Funny Iguana T Shirt Mexican Style Graphic Tee Fiesta Shirt Cute Lizard Shirt Party Shirt Unisex Gift Nurses | DUP-12 | https://images.printify.com/mockup/69c9aab44c5d410b1f0fd5f7/73207/98445/nurse-iguana-loco-shirt-funny-iguana-t-shirt-mexican-style-graphic-tee-fiesta-shirt-cute-lizard-shirt-party-shirt-unisex-gift-nurses.jpg?camera_label=front |
| 69c9aaaaa5acc0c432054222 | she is evolving script tee / Inspirational Phrase T-Shirt | CLEAN | https://images.printify.com/mockup/69c9aaaaa5acc0c432054222/18542/92547/she-is-evolving-script-tee-inspirational-phrase-t-shirt.jpg?camera_label=front |
| 69c9aa9f472862c1430c59e1 | Mexico Flag Phone Case Mexican iPhone Case Patriotic Mexico Case Mexican Pride Phone Case Tricolor Phone Case Gift Idea | CLEAN | https://images.printify.com/mockup/69c9aa9f472862c1430c59e1/130091/111262/mexico-flag-phone-case-mexican-iphone-case-patriotic-mexico-case-mexican-pride-phone-case-tricolor-phone-case-gift-idea.jpg?camera_label=front |
| 69c9aa99a5acc0c43205421a | Mexico Flag Phone Tough Case Mexican iPhone Case Patriotic Mexico Case Mexican Pride Phone Case Tricolor Case National Flag Cover | CLEAN | https://images.printify.com/mockup/69c9aa99a5acc0c43205421a/62582/97458/mexico-flag-phone-tough-case-mexican-iphone-case-patriotic-mexico-case-mexican-pride-phone-case-tricolor-case-national-flag-cover.jpg?camera_label=front-and-side |
| 69c9aa933f8316381202b020 | Brazil Flag Magnetic Impact-Resistant Phone Case Brazil Flag Phone Case Brazilian iPhone Case Brazil Pride Case National Flag Case Gift Idea | CLEAN | https://images.printify.com/mockup/69c9aa933f8316381202b020/96135/81354/brazil-flag-magnetic-impact-resistant-phone-case-brazil-flag-phone-case-brazilian-iphone-case-brazil-pride-case-national-flag-case-gift-idea.jpg?camera_label=front |
| 69c9aa9181d880656f0b2de0 | Brazil Flag Phone Case Brazilian iPhone Case Brazil Pride Case Green Yellow Blue Phone Case National Flag Case Gift Idea | CLEAN | https://images.printify.com/mockup/69c9aa9181d880656f0b2de0/61521/2494/brazil-flag-phone-case-brazilian-iphone-case-brazil-pride-case-green-yellow-blue-phone-case-national-flag-case-gift-idea.jpg?camera_label=front-and-side |
| 69c9aa88a5acc0c432054217 | Canada Flag Magnetic Impact-Resistant Canada Flag Canadian Case iPhone Case Canada Pride Case Maple Leaf Case Patriotic Phone Case Gift | CLEAN | https://images.printify.com/mockup/69c9aa88a5acc0c432054217/96135/81354/canada-flag-magnetic-impact-resistant-canada-flag-canadian-case-iphone-case-canada-pride-case-maple-leaf-case-patriotic-phone-case-gift.jpg?camera_label=front |
| 69c9aa82374936c29b08d071 | Canada Heart Tough Magnetic Phone Case | CLEAN | https://images.printify.com/mockup/69c9aa82374936c29b08d071/109328/107253/canada-heart-tough-magnetic-phone-case.jpg?camera_label=front |
| 69c9aa7bc1744955170d9482 | Patriotic Heart Phone Case American Flag Magnetic Impact Resistant Case | CLEAN | https://images.printify.com/mockup/69c9aa7bc1744955170d9482/96135/81354/patriotic-heart-phone-case-american-flag-magnetic-impact-resistant-case.jpg?camera_label=front |
| 69c9aa74a5acc0c432054215 | Italy Flag Heart Phone Case Magnetic Impact Resistant Protective Cover | CLEAN | https://images.printify.com/mockup/69c9aa74a5acc0c432054215/96135/81354/italy-flag-heart-phone-case-magnetic-impact-resistant-protective-cover.jpg?camera_label=front |
| 69c9aa6f88e993b7d40e17e2 | Union Jack Heart Phone Case Magnetic Impact Resistant UK Flag Cover | CLEAN | https://images.printify.com/mockup/69c9aa6f88e993b7d40e17e2/96135/81354/union-jack-heart-phone-case-magnetic-impact-resistant-uk-flag-cover.jpg?camera_label=front |
| 69c9aa69af54e9c54605a0a2 | India Flag Heart Magnetic Impact Resistant Phone Case | CLEAN | https://images.printify.com/mockup/69c9aa69af54e9c54605a0a2/96135/81354/india-flag-heart-magnetic-impact-resistant-phone-case.jpg?camera_label=front |
| 69c9aa623f8316381202b015 | Mexico Heart Flag Phone Case Magnetic Impact Resistant Protective Cover | CLEAN | https://images.printify.com/mockup/69c9aa623f8316381202b015/96135/81354/mexico-heart-flag-phone-case-magnetic-impact-resistant-protective-cover.jpg?camera_label=front |
| 69c9aa5d374936c29b08d068 | Union Jack Magnetic Impact Resistant Phone Case | CLEAN | https://images.printify.com/mockup/69c9aa5d374936c29b08d068/96135/81354/union-jack-magnetic-impact-resistant-phone-case.jpg?camera_label=front |
| 69c9aa54aa266b7a800a2449 | Canadian Flag Tough Phone Case Durable Maple Leaf iPhone Case | DUP-9 | https://images.printify.com/mockup/69c9aa54aa266b7a800a2449/61521/2494/canadian-flag-tough-phone-case-durable-maple-leaf-iphone-case.jpg?camera_label=front-and-side |
| 69c9aa427f4cb7de211001e3 | Dominican Flag Tough Phone Case Protective Patriotic Phone Cover | CLEAN | https://images.printify.com/mockup/69c9aa427f4cb7de211001e3/62582/97458/dominican-flag-tough-phone-case-protective-patriotic-phone-cover.jpg?camera_label=front-and-side |
| 69c9aa2c2f6f1849a30b5c02 | Canadian Flag Tough Phone Case Durable Maple Leaf iPhone Case | DUP-9 | https://images.printify.com/mockup/69c9aa2c2f6f1849a30b5c02/61521/2494/canadian-flag-tough-phone-case-durable-maple-leaf-iphone-case.jpg?camera_label=front-and-side |
| 69c9aa2488e993b7d40e17d1 | Dominican Republic Flag Tough Phone Case Protective Patriotic iPhone Cover | CLEAN | https://images.printify.com/mockup/69c9aa2488e993b7d40e17d1/61521/2494/dominican-republic-flag-tough-phone-case-protective-patriotic-iphone-cover.jpg?camera_label=front-and-side |
| 69c9aa1cc1744955170d9474 | Puerto Rico Heart Phone Case Puerto Rican iPhone Case Boricua Love Case Flag Heart Phone Case Caribbean Pride Gift Idea | DUP-5 | https://images.printify.com/mockup/69c9aa1cc1744955170d9474/61521/2494/puerto-rico-heart-phone-case-puerto-rican-iphone-case-boricua-love-case-flag-heart-phone-case-caribbean-pride-gift-idea.jpg?camera_label=front-and-side |
| 69c9aa13c1744955170d9473 | Puerto Rico Flag Heart phone case / Tough Case | DUP-5 | https://images.printify.com/mockup/69c9aa13c1744955170d9473/61521/2494/puerto-rico-flag-heart-phone-case-tough-case.jpg?camera_label=front-and-side |
| 69c9a9f8936256aabc04adcd | Dominican Republic Flag Magnetic Impact Resistant Phone Case | CLEAN | https://images.printify.com/mockup/69c9a9f8936256aabc04adcd/96135/81354/dominican-republic-flag-magnetic-impact-resistant-phone-case.jpg?camera_label=front |
| 69c9a9f07f4cb7de211001d4 | Puerto Rico Flag Tough Phone Case Patriotic Red & White Stripe Design | CLEAN | https://images.printify.com/mockup/69c9a9f07f4cb7de211001d4/61522/2495/puerto-rico-flag-tough-phone-case-patriotic-red-white-stripe-design.jpg?camera_label=front-and-side |
| 69c9a9e888e993b7d40e17c9 | Puerto Rican Flag Phone Case / Tough Case | DUP-6 | https://images.printify.com/mockup/69c9a9e888e993b7d40e17c9/67998/7970/puerto-rican-flag-phone-case-tough-case.jpg?camera_label=front-and-side |
| 69c9a9d54c5d410b1f0fd5dc | Puerto Rico Flag Phone Case Puerto Rican iPhone Case Boricua Pride Case Red White Blue Phone Case Caribbean Pride Gift Idea | DUP-6 | https://images.printify.com/mockup/69c9a9d54c5d410b1f0fd5dc/61521/2494/puerto-rico-flag-phone-case-puerto-rican-iphone-case-boricua-pride-case-red-white-blue-phone-case-caribbean-pride-gift-idea.jpg?camera_label=front-and-side |
| 69c9a9d0af54e9c54605a07e | Puerto Rico Flag Magnetic Impact Resistant Phone Case | CLEAN | https://images.printify.com/mockup/69c9a9d0af54e9c54605a07e/96135/81354/puerto-rico-flag-magnetic-impact-resistant-phone-case.jpg?camera_label=front |
| 69c9a9caaf54e9c54605a07c | Venezuela Heart Flag Phone Case Tough Protective Phone Case | CLEAN | https://images.printify.com/mockup/69c9a9caaf54e9c54605a07c/102549/99048/venezuela-heart-flag-phone-case-tough-protective-phone-case.jpg?camera_label=front-and-side |
| 69c9a9c5374936c29b08d051 | Dominican Republic Heart phone case / Tough Case | CLEAN | https://images.printify.com/mockup/69c9a9c5374936c29b08d051/112191/105690/dominican-republic-heart-phone-case-tough-case.jpg?camera_label=front |
| 69c9a9bc2f6862e2cf0a1c17 | Brazil Flag Heart Tough Case / Phone Protective Case, Brazilian Pride | CLEAN | https://images.printify.com/mockup/69c9a9bc2f6862e2cf0a1c17/112191/105690/brazil-flag-heart-tough-case-phone-protective-case-brazilian-pride.jpg?camera_label=front |
| 69c9a9b6472862c1430c59c5 | Panama Flag Heart phone case / Tough Case | CLEAN | https://images.printify.com/mockup/69c9a9b6472862c1430c59c5/112191/105690/panama-flag-heart-phone-case-tough-case.jpg?camera_label=front |
| 69c9a9ad2f6f1849a30b5bf5 | Dripping Rose T-shirt / Melting Floral Graphic Tee | CLEAN | https://images.printify.com/mockup/69c9a9ad2f6f1849a30b5bf5/73207/98445/dripping-rose-t-shirt-melting-floral-graphic-tee.jpg?camera_label=front |
| 69c9a9a77ee2f2859c094675 | Juicy Black Women's Thong - Playful Pink Puff Lettering | CLEAN | https://images.printify.com/mockup/69c9a9a77ee2f2859c094675/105606/102782/juicy-black-womens-thong-playful-pink-puff-lettering.jpg?camera_label=front |
| 69c9a9a1ce78beb8610a32ff | Retro Doodle Smiley Face Tee / Neon Stickers, Lightning Bolts, Skull Icons | CLEAN | https://images.printify.com/mockup/69c9a9a1ce78beb8610a32ff/18390/102044/retro-doodle-smiley-face-tee-neon-stickers-lightning-bolts-skull-icons.jpg?camera_label=front-2 |
| 69c9a9993f8316381202aff5 | Brazil Flag Thong Women's Brazilian Flag Bikini Underwear | CLEAN | https://images.printify.com/mockup/69c9a9993f8316381202aff5/105608/102782/brazil-flag-thong-womens-brazilian-flag-bikini-underwear.jpg?camera_label=front |
| 69c9a991374936c29b08d043 | Panama Flag Heart Underwear Womens Patriotic Panties Panama Flag Lingerie Cute Heart Underwear Comfortable Briefs Gift Idea | CLEAN | https://images.printify.com/mockup/69c9a991374936c29b08d043/61896/2608/panama-flag-heart-underwear-womens-patriotic-panties-panama-flag-lingerie-cute-heart-underwear-comfortable-briefs-gift-idea.jpg?camera_label=front |
| 69c9a98802f914c0070d68ff | American Flag Heart Underwear Womens Patriotic Panties USA Flag Lingerie Cute Fourth Of July Underwear Comfortable Briefs Gift | CLEAN | https://images.printify.com/mockup/69c9a98802f914c0070d68ff/61896/2608/american-flag-heart-underwear-womens-patriotic-panties-usa-flag-lingerie-cute-fourth-of-july-underwear-comfortable-briefs-gift.jpg?camera_label=front |
| 69c9a980ce78beb8610a32f3 | Philippine Flag Heart Phone Case / Tough Phone Case | DUP-2 | https://images.printify.com/mockup/69c9a980ce78beb8610a32f3/112191/105690/philippine-flag-heart-phone-case-tough-phone-case.jpg?camera_label=front |
| 69c9a9737f4cb7de211001c0 | American Flag Bikini USA Flag Swimsuit Patriotic Two Piece Bikini Fourth Of July Swimwear USA Bathing Suit Beachwear Gift Idea | CLEAN | https://images.printify.com/mockup/69c9a9737f4cb7de211001c0/44540/935/american-flag-bikini-usa-flag-swimsuit-patriotic-two-piece-bikini-fourth-of-july-swimwear-usa-bathing-suit-beachwear-gift-idea.jpg?camera_label=front |
| 69c9a96c6cd594938803de3d | American Flag One Piece Swimsuit USA Flag Swimwear Patriotic Bathing Suit Fourth Of July Outfit Womens Swimwear Beachwear Gift | DUP-10 | https://images.printify.com/mockup/69c9a96c6cd594938803de3d/44749/1060/american-flag-one-piece-swimsuit-usa-flag-swimwear-patriotic-bathing-suit-fourth-of-july-outfit-womens-swimwear-beachwear-gift.jpg?camera_label=front |
| 69c9a96502f914c0070d68f7 | American Flag Heart Underwear Womens Patriotic Panties USA Flag Lingerie Fourth Of July Underwear Cute Comfortable Briefs Gift | CLEAN | https://images.printify.com/mockup/69c9a96502f914c0070d68f7/61896/2608/american-flag-heart-underwear-womens-patriotic-panties-usa-flag-lingerie-fourth-of-july-underwear-cute-comfortable-briefs-gift.jpg?camera_label=front |
| 69b021d38c561a36090eb202 | Hummingbird Floral Phone Case Magnetic Impact Resistant Protection | DUP-15 | https://images.printify.com/mockup/69b021d38c561a36090eb202/130091/111262/hummingbird-floral-phone-case-magnetic-impact-resistant-protection.jpg?camera_label=front |
| 69b021cbbdf0eefec20d530c | Phone Case Pink Hummingbird Floral Magnetic Impact Resistant Case | DUP-13 | https://images.printify.com/mockup/69b021cbbdf0eefec20d530c/130091/111262/phone-case-pink-hummingbird-floral-magnetic-impact-resistant-case.jpg?camera_label=front |
| 69b021c56d2baa18fc0b5a6e | American Flag Tough Phone Case Distressed Stars & Stripes Protective Cover | DUP-11 | https://images.printify.com/mockup/69b021c56d2baa18fc0b5a6e/112191/105690/american-flag-tough-phone-case-distressed-stars-stripes-protective-cover.jpg?camera_label=front |
| 69b021bebdf0eefec20d5309 | American Flag Tough Phone Case Patriotic iPhone Protective Cover | DUP-14 | https://images.printify.com/mockup/69b021bebdf0eefec20d5309/112191/105690/american-flag-tough-phone-case-patriotic-iphone-protective-cover.jpg?camera_label=front |
| 69b021b78aab92667f02b8c6 | American Flag Magnetic Impact Resistant Phone Case | DUP-1 | https://images.printify.com/mockup/69b021b78aab92667f02b8c6/130091/111262/american-flag-magnetic-impact-resistant-phone-case.jpg?camera_label=front |
| 69b021984fead7b1ce06b6bf | American Flag Magnetic Impact Resistant Phone Case | DUP-1 | https://images.printify.com/mockup/69b021984fead7b1ce06b6bf/130091/111262/american-flag-magnetic-impact-resistant-phone-case.jpg?camera_label=front |
| 699fd4e4f8e5c2375807797e | Jesus Is My Best Friend Tee Shirt  Faith Christian Tee with Back Cross | DUP-3 | https://images.printify.com/mockup/699fd4e4f8e5c2375807797e/73207/98445/jesus-is-my-best-friend-tee-shirt-faith-christian-tee-with-back-cross.jpg?camera_label=front |
| 699fd4ddf8e5c23758077979 | Puuurrrrfect! Cute Tabby Cat Graphic T-Shirt | DUP-7 | https://images.printify.com/mockup/699fd4ddf8e5c23758077979/73207/98445/puuurrrrfect-cute-tabby-cat-graphic-t-shirt.jpg?camera_label=front |
| 699fd4d3f8e5c23758077976 | Drink Drank Drunk St Patricks Day Tee Shirt | DUP-8 | https://images.printify.com/mockup/699fd4d3f8e5c23758077976/73207/98445/drink-drank-drunk-st-patricks-day-tee-shirt.jpg?camera_label=front |
| 699fd4c8f8e5c2375807796d | Unisex Garment-Dyed T-shirt | DUP-12 | https://images.printify.com/mockup/699fd4c8f8e5c2375807796d/73207/98445/unisex-garment-dyed-t-shirt.jpg?camera_label=front |
| 699fd0bb7fd997a9d10bc1a5 | American Flag Peace Merica Tee - Patriotic Garment-Dyed T-Shirt, 4th of July USA Flag Shirt Gift | CLEAN | https://images.printify.com/mockup/699fd0bb7fd997a9d10bc1a5/73207/98445/american-flag-peace-merica-tee-patriotic-garment-dyed-t-shirt-4th-of-july-usa-flag-shirt-gift.jpg?camera_label=front |
| 699fcde6f38bdbd36701c3bc | Puppy Love Kids Tee / Cute Cartoon Puppy, Hearts, Playful Design | CLEAN | https://images.printify.com/mockup/699fcde6f38bdbd36701c3bc/42519/105377/puppy-love-kids-tee-cute-cartoon-puppy-hearts-playful-design.jpg?camera_label=front |

## 14. Shopify #361-460 full 100-row ID register (complete, per-product evidence, same format as §9/§10/§11/§12/§13)

Format: `Printify ID | Title | Visual result | Default mockup image URL used for inspection`.
`TRUE_DUP` marks the one confirmed duplicate pair (§8f); `DEFECT`/`DEFECT-SEVERE`/`DEFECT-MINOR` mark
confirmed cropping/garbling defects by severity (§8f); `CLEAN-BORDERLINE` means text touches the print
edge but remains fully legible (not counted as a defect). Sync-mapping (`external` field) was not
individually checked per-ID this batch — see §8f sync-mapping note.

| 6ac717c54ff91977d503de96 | Thankful Grateful Blesse Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac717c54ff91977d503de96/401444/145590/thankful-grateful-blesse-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac717dda5ade89b5c08148a | Jingle All Way Liquor Christmas Backpack — Cheerful Christmas Travel Pack, Gift for Students | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac717dda5ade89b5c08148a/401444/145590/jingle-all-way-liquor-christmas-backpack-cheerful-christmas-travel-pack-gift-for-students-winstar4u.jpg?camera_label=front |
| 6ac7182a4ff91977d503decc | Joy Holly Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7182a4ff91977d503decc/401444/145590/joy-holly-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac722c9b612605ab00508c2 | Winter Wonderland Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722c9b612605ab00508c2/72006/13462/winter-wonderland-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac722a8c147c939f20dbc54 | Noel Elegant Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722a8c147c939f20dbc54/72006/13462/noel-elegant-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac724463889391cc309c602 | Dear Santa Explain Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac724463889391cc309c602/62070/98417/dear-santa-explain-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac722aecaaa1d800e0db38d | Peace On Earth Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722aecaaa1d800e0db38d/72006/13462/peace-on-earth-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723adb612605ab005097c | Corkscrew Wine Repeat Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723adb612605ab005097c/72006/13462/corkscrew-wine-repeat-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac722b33889391cc309c48f | Seasons Greetings Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722b33889391cc309c48f/72006/13462/seasons-greetings-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717b764166f603b0c8932 | O Holy Night Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac717b764166f603b0c8932/401444/145590/o-holy-night-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac7232d73283b982509a1c3 | Tree Up Patience Down Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | DEFECT-MINOR | https://images.printify.com/mockup/6ac7232d73283b982509a1c3/72006/13462/tree-up-patience-down-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717ebaa7a21cb900b5066 | Merry Everything Happy Always Christmas Backpack — Cheerful Christmas Travel Pack, Gift for Students | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac717ebaa7a21cb900b5066/401444/145590/merry-everything-happy-always-christmas-backpack-cheerful-christmas-travel-pack-gift-for-students-winstar4u.jpg?camera_label=front |
| 6ac724253889391cc309c5f6 | Christmas Vacation Canceled Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | DEFECT-MINOR | https://images.printify.com/mockup/6ac724253889391cc309c5f6/62070/98417/christmas-vacation-canceled-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac722cf28a484f897041257 | Only Nice For Presents Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722cf28a484f897041257/72006/13462/only-nice-for-presents-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac72375383159aef207b9a2 | Christmas Eat No January V2 Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac72375383159aef207b9a2/72006/13462/christmas-eat-no-january-v2-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac72297082094e22a08bd87 | Let It Snow Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac72297082094e22a08bd87/72006/13462/let-it-snow-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac722df73283b982509a1b4 | Professional Gift Returner Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722df73283b982509a1b4/72006/13462/professional-gift-returner-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7237bc7d7ac2fa30f5d15 | Christmas Eat No January Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7237bc7d7ac2fa30f5d15/72006/13462/christmas-eat-no-january-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7233d383159aef207b969 | Avoiding Carolers Gnome Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | DEFECT-SEVERE | https://images.printify.com/mockup/6ac7233d383159aef207b969/72006/13462/avoiding-carolers-gnome-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7181c35cf3f6ec802eecd | Fireplace Stocking Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac7181c35cf3f6ec802eecd/401444/145590/fireplace-stocking-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac724359a4346ee1d08943a | Dear Santa Bank Account Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac724359a4346ee1d08943a/62070/98417/dear-santa-bank-account-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717f3aa7a21cb900b506c | My Elf Made Me Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac717f3aa7a21cb900b506c/401444/145590/my-elf-made-me-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac723dab814691321004159 | Christmas Calories Dont Count Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723dab814691321004159/62070/98417/christmas-calories-dont-count-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac722fabf15946c8a0d9eea | Santas Favorite Customer Vip Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722fabf15946c8a0d9eea/72006/13462/santas-favorite-customer-vip-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717cced135347800fa039 | Here For Snacks Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | CLEAN-BORDERLINE | https://images.printify.com/mockup/6ac717cced135347800fa039/401444/145590/here-for-snacks-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac71804b814691321003c5c | Naughty List Skeleton Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | TRUE_DUP | https://images.printify.com/mockup/6ac71804b814691321003c5c/401444/145590/naughty-list-skeleton-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac7229d082094e22a08bd88 | Merry Bright Lights Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7229d082094e22a08bd88/72006/13462/merry-bright-lights-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717c264166f603b0c8939 | Savior Born Manger Christmas Backpack — Cheerful Christmas Travel Pack, Gift for Students | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac717c264166f603b0c8939/401444/145590/savior-born-manger-christmas-backpack-cheerful-christmas-travel-pack-gift-for-students-winstar4u.jpg?camera_label=front |
| 6ac723e6738fa0f7e9064e00 | Christmas Eat No January Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723e6738fa0f7e9064e00/62070/98417/christmas-eat-no-january-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac722a373283b982509a1a0 | Merry Christmas Sant Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722a373283b982509a1a0/72006/13462/merry-christmas-sant-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7231c6441b9380a019120 | Sleigh All Day Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7231c6441b9380a019120/72006/13462/sleigh-all-day-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717b057b1ebbe6c0c6ebb | Joy To World Christian Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac717b057b1ebbe6c0c6ebb/401444/145590/joy-to-world-christian-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac72359738fa0f7e9064ced | Chic Happens Cocktail Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac72359738fa0f7e9064ced/72006/13462/chic-happens-cocktail-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac72281b612605ab00508b3 | Jingle Bells Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac72281b612605ab00508b3/72006/13462/jingle-bells-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717d3a5ade89b5c081487 | Holiday Spirit Cookies Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | DEFECT-SEVERE | https://images.printify.com/mockup/6ac717d3a5ade89b5c081487/401444/145590/holiday-spirit-cookies-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac723817c04b79ced0ddf16 | Christmas Excuse Eat King Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723817c04b79ced0ddf16/72006/13462/christmas-excuse-eat-king-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717fa775b6fcd2c0e906b | Naughty List Resume Christmas Backpack — Cheerful Christmas Travel Pack, Gift for Students | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac717fa775b6fcd2c0e906b/401444/145590/naughty-list-resume-christmas-backpack-cheerful-christmas-travel-pack-gift-for-students-winstar4u.jpg?camera_label=front |
| 6ac722ea76ea237d7f00fc9f | Santa I Can Explain Clipboard Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722ea76ea237d7f00fc9f/72006/13462/santa-i-can-explain-clipboard-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac72370825150f7340c109b | Christmas Calories Dont Count Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac72370825150f7340c109b/72006/13462/christmas-calories-dont-count-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7233276ea237d7f00fca7 | All I Want Nap Pillow Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7233276ea237d7f00fca7/72006/13462/all-i-want-nap-pillow-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7182364166f603b0c8971 | Home For Christmas Christmas Backpack — Cheerful Christmas Travel Pack, Gift for Students | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac7182364166f603b0c8971/401444/145590/home-for-christmas-christmas-backpack-cheerful-christmas-travel-pack-gift-for-students-winstar4u.jpg?camera_label=front |
| 6ac722e573283b982509a1b8 | Prosecco Ho Ho Ho Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722e573283b982509a1b8/72006/13462/prosecco-ho-ho-ho-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717da35cf3f6ec802eeae | Ill Be Home Christmas Probably Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac717da35cf3f6ec802eeae/401444/145590/ill-be-home-christmas-probably-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac723a8d5899f19b40133da | Christmas Wreath 2026 Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723a8d5899f19b40133da/72006/13462/christmas-wreath-2026-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717fd57b1ebbe6c0c6ee9 | Naughty List Skeleton V2 Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | TRUE_DUP | https://images.printify.com/mockup/6ac717fd57b1ebbe6c0c6ee9/401444/145590/naughty-list-skeleton-v2-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac71815a5ade89b5c0814c5 | Christmas Wishes Sta Christmas Backpack — Cheerful Christmas Travel Pack, Gift for Students | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac71815a5ade89b5c0814c5/401444/145590/christmas-wishes-sta-christmas-backpack-cheerful-christmas-travel-pack-gift-for-students-winstar4u.jpg?camera_label=front |
| 6ac722c4128c75f07103f8e7 | Vintage Santa Portra Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722c4128c75f07103f8e7/72006/13462/vintage-santa-portra-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7181fa4cff7da370fd18a | Happy Holidays Tree Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac7181fa4cff7da370fd18a/401444/145590/happy-holidays-tree-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac717d6a4c95c48e203674e | I Came I Saw I Bought It Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac717d6a4c95c48e203674e/401444/145590/i-came-i-saw-i-bought-it-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac7238c3889391cc309c4fe | Christmas Mode Dnd Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7238c3889391cc309c4fe/72006/13462/christmas-mode-dnd-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723977536ac3c5f0c3ede | Christmas Party Survivor Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723977536ac3c5f0c3ede/72006/13462/christmas-party-survivor-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7228c38dbb50d19041625 | Joy Holly Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7228c38dbb50d19041625/72006/13462/joy-holly-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723f038dbb50d1904173d | Christmas Lights Therapy Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723f038dbb50d1904173d/62070/98417/christmas-lights-therapy-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac722b931b3ce04bf05d502 | Silent Night Village Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722b931b3ce04bf05d502/72006/13462/silent-night-village-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723006441b9380a019113 | Santas Favorite Distraction Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723006441b9380a019113/72006/13462/santas-favorite-distraction-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7180ea4c95c48e2036775 | Believe Sleigh Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7180ea4c95c48e2036775/401444/145590/believe-sleigh-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac722dacbd4fbcd4a0e2289 | Powered By Cookies Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722dacbd4fbcd4a0e2289/72006/13462/powered-by-cookies-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac724409a4346ee1d08943c | Dear Santa Explain Santa Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac724409a4346ee1d08943c/62070/98417/dear-santa-explain-santa-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7235f3889391cc309c4c8 | Christmas 2026 Caffeine Panic Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7235f3889391cc309c4c8/72006/13462/christmas-2026-caffeine-panic-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723b39a4346ee1d089385 | Dear Santa Bank Account Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723b39a4346ee1d089385/72006/13462/dear-santa-bank-account-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723867c04b79ced0ddf26 | Christmas Lights Therapy Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723867c04b79ced0ddf26/72006/13462/christmas-lights-therapy-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723a2cbd4fbcd4a0e2302 | Christmas Vacation Canceled Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723a2cbd4fbcd4a0e2302/72006/13462/christmas-vacation-canceled-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717f7aa7a21cb900b5072 | Naughty Is New Nice Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac717f7aa7a21cb900b5072/401444/145590/naughty-is-new-nice-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac71819a4cff7da370fd188 | Deck The Halls Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | CLEAN-BORDERLINE | https://images.printify.com/mockup/6ac71819a4cff7da370fd188/401444/145590/deck-the-halls-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac722f56441b9380a01910f | Santas Favorite Arrow Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722f56441b9380a01910f/72006/13462/santas-favorite-arrow-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717b364166f603b0c892b | Keep Christ Christmas Christmas Backpack — Cheerful Christmas Travel Pack, Gift for Students | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac717b364166f603b0c892b/401444/145590/keep-christ-christmas-christmas-backpack-cheerful-christmas-travel-pack-gift-for-students-winstar4u.jpg?camera_label=front |
| 6ac717d046dd1e896e04e60a | Ho Ho Pour Another Christmas Backpack — Cheerful Christmas Travel Pack, Gift for Students | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac717d046dd1e896e04e60a/401444/145590/ho-ho-pour-another-christmas-backpack-cheerful-christmas-travel-pack-gift-for-students-winstar4u.jpg?camera_label=front |
| 6ac7244c7536ac3c5f0c3fd3 | Deck The Halls Sit Down Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7244c7536ac3c5f0c3fd3/62070/98417/deck-the-halls-sit-down-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7241f738fa0f7e9064e4f | Christmas Stress Tinsel Done Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | DEFECT-MINOR | https://images.printify.com/mockup/6ac7241f738fa0f7e9064e4f/62070/98417/christmas-stress-tinsel-done-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac722be383159aef207b941 | Truck Tree Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722be383159aef207b941/72006/13462/truck-tree-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723e0b81469132100416b | Christmas Eat No January V2 Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | CLEAN-BORDERLINE | https://images.printify.com/mockup/6ac723e0b81469132100416b/62070/98417/christmas-eat-no-january-v2-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7234e383159aef207b96f | Calories Dont Count Thanksgiving Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7234e383159aef207b96f/72006/13462/calories-dont-count-thanksgiving-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723381ec581a32d059623 | All I Want Nap Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723381ec581a32d059623/72006/13462/all-i-want-nap-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723c9c4090742a201b9c2 | Christmas 2026 Caffeine Panic Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | DEFECT-MINOR | https://images.printify.com/mockup/6ac723c9c4090742a201b9c2/62070/98417/christmas-2026-caffeine-panic-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac71826fa3cae10170eff96 | Jingle Bells Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac71826fa3cae10170eff96/401444/145590/jingle-bells-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac7242aa5ade89b5c08197f | Christmas Wreath 2026 Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7242aa5ade89b5c08197f/62070/98417/christmas-wreath-2026-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac72401cacff3948b065b5d | Custom Pin Buttons | DEFECT-MINOR | https://images.printify.com/mockup/6ac72401cacff3948b065b5d/62070/98417/custom-pin-buttons.jpg?camera_label=front |
| 6ac717e1ac4a665555019d40 | Jingle Bells Santa Smells Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | DEFECT-SEVERE | https://images.printify.com/mockup/6ac717e1ac4a665555019d40/401444/145590/jingle-bells-santa-smells-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac717e846dd1e896e04e617 | Merry Christmas Lets Get Lit Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac717e846dd1e896e04e617/401444/145590/merry-christmas-lets-get-lit-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac722d4caaa1d800e0db393 | Party In Holiday Party Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722d4caaa1d800e0db393/72006/13462/party-in-holiday-party-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723226441b9380a019122 | Survived Christmas Hangover Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723226441b9380a019122/72006/13462/survived-christmas-hangover-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7242fd5899f19b40134d7 | Corkscrew Wine Repeat Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac7242fd5899f19b40134d7/62070/98417/corkscrew-wine-repeat-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac71811d0a23214d80b2aec | Candy Cane Lane Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac71811d0a23214d80b2aec/401444/145590/candy-cane-lane-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac722921ec581a32d05960a | Joy To World Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac722921ec581a32d05960a/72006/13462/joy-to-world-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7232768f08843f201d050 | Too Lit Nice List Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7232768f08843f201d050/72006/13462/too-lit-nice-list-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717bea5ade89b5c08147e | Rejoice Star Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac717bea5ade89b5c08147e/401444/145590/rejoice-star-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac723f6738fa0f7e9064e14 | Christmas Mode Dnd Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723f6738fa0f7e9064e14/62070/98417/christmas-mode-dnd-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7180b775b6fcd2c0e9074 | Naughty List Vip Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7180b775b6fcd2c0e9074/401444/145590/naughty-list-vip-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac7239c28a484f8970412cc | Christmas Stress Tinsel Done Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7239c28a484f8970412cc/72006/13462/christmas-stress-tinsel-done-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7231028a484f89704126b | Silent Night Family Go Away Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7231028a484f89704126b/72006/13462/silent-night-family-go-away-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717ba64166f603b0c8935 | Reason For Season Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac717ba64166f603b0c8935/401444/145590/reason-for-season-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac72348a4c95c48e2036b6b | Bah Humbug Wine Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac72348a4c95c48e2036b6b/72006/13462/bah-humbug-wine-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723914701e7f9fa07ab21 | Christmas Open Bar Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac723914701e7f9fa07ab21/72006/13462/christmas-open-bar-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717c907e4149a0f0014b5 | Walk By Faith Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac717c907e4149a0f0014b5/401444/145590/walk-by-faith-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac717e4a4c95c48e2036750 | Merry Christmas Leave Me Alone Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac717e4a4c95c48e2036750/401444/145590/merry-christmas-leave-me-alone-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac723eb73283b982509a2bd | Christmas Excuse Eat King Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | CLEAN-BORDERLINE | https://images.printify.com/mockup/6ac723eb73283b982509a2bd/62070/98417/christmas-excuse-eat-king-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723fb1ec581a32d05974d | Christmas Open Bar Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac723fb1ec581a32d05974d/62070/98417/christmas-open-bar-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac723c37c04b79ced0ddfa3 | Chic Happens Cocktail Christmas Button Pin — Festive Pin Button, Holiday Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac723c37c04b79ced0ddfa3/62070/98417/chic-happens-cocktail-christmas-button-pin-festive-pin-button-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac717f0a5ade89b5c081491 | Morning Person Dec25 Skeleton Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | DEFECT-SEVERE | https://images.printify.com/mockup/6ac717f0a5ade89b5c081491/401444/145590/morning-person-dec25-skeleton-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac723437536ac3c5f0c3e7a | Avoiding Carolers Raccoon Christmas Sticker Pack — Die-Cut Sticker Pack, Holiday Gift | Winstar4U | DEFECT | https://images.printify.com/mockup/6ac723437536ac3c5f0c3e7a/72006/13462/avoiding-carolers-raccoon-christmas-sticker-pack-die-cut-sticker-pack-holiday-gift-winstar4u.jpg?camera_label=front |
## 15. Shopify #461-560 full 100-row ID register (complete, per-product evidence, same format as §9/§10/§11/§12/§13/§14)

| ID | Title | Result | Default mockup image URL |
|---|---|---|---|
| 6ac717aca4cff7da370fd151 | Hallelujah Angels Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | DEFECT-SEVERE (HALLELUJAH cropped top, only slivers visible) | https://images.printify.com/mockup/6ac717aca4cff7da370fd151/401444/145590/hallelujah-angels-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac717a95a14e80fa703f22f | Greatest Gift Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | DEFECT (title text clipped at top edge, gold-on-black illegible) | https://images.printify.com/mockup/6ac717a95a14e80fa703f22f/401444/145590/greatest-gift-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac717a6a4cff7da370fd145 | God Bless Christmas Christmas Backpack — Cheerful Christmas Travel Pack, Gift for Students | Winstar4U | DEFECT ("GOD BLESS" text missing, only "CHRISTMAS" visible) | https://images.printify.com/mockup/6ac717a6a4cff7da370fd145/401444/145590/god-bless-christmas-christmas-backpack-cheerful-christmas-travel-pack-gift-for-students-winstar4u.jpg?camera_label=front |
| 6ac717a24636838bd804f846 | Glory To God Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | DEFECT-SEVERE (no title text visible at all) | https://images.printify.com/mockup/6ac717a24636838bd804f846/401444/145590/glory-to-god-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac7179eb814691321003c22 | Christ Is Born Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | DEFECT-SEVERE ("CHRIST" entirely cropped off left, only "IS BORN" visible) | https://images.printify.com/mockup/6ac7179eb814691321003c22/401444/145590/christ-is-born-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac7179bac4a665555019d14 | Blessed Christmas Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | DEFECT-SEVERE (no text visible at all, title implies "BLESSED CHRISTMAS") | https://images.printify.com/mockup/6ac7179bac4a665555019d14/401444/145590/blessed-christmas-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac7179757b1ebbe6c0c6ea4 | Amazing Grace Christmas Backpack — Cheerful Christmas Travel Pack, Gift for Students | Winstar4U | DEFECT ("AMAZING" missing, only "GRACE" visible, cropped top) | https://images.printify.com/mockup/6ac7179757b1ebbe6c0c6ea4/401444/145590/amazing-grace-christmas-backpack-cheerful-christmas-travel-pack-gift-for-students-winstar4u.jpg?camera_label=front |
| 6ac717945a14e80fa703f22a | Everyone Go Home Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | DEFECT-SEVERE (no text visible at all, title implies "EVERYONE GO HOME") | https://images.printify.com/mockup/6ac717945a14e80fa703f22a/401444/145590/everyone-go-home-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac71790ed135347800fa01b | Elegantly Wasted Martini Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | DEFECT-SEVERE (only top sliver of art visible, rest cropped away) | https://images.printify.com/mockup/6ac71790ed135347800fa01b/401444/145590/elegantly-wasted-martini-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac7178daa7a21cb900b5046 | Eggnog Recovery Skeleton Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | DEFECT-SEVERE (no text visible at all, title implies "EGGNOG RECOVERY") | https://images.printify.com/mockup/6ac7178daa7a21cb900b5046/401444/145590/eggnog-recovery-skeleton-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac7178ad0a23214d80b2aa7 | Dreaming Stress Free Christmas Christmas Backpack — Cheerful Christmas Travel Pack, Gift for Students | Winstar4U | DEFECT ("DREAMING" missing, only "OF A STRESS-FREE" visible) | https://images.printify.com/mockup/6ac7178ad0a23214d80b2aa7/401444/145590/dreaming-stress-free-christmas-christmas-backpack-cheerful-christmas-travel-pack-gift-for-students-winstar4u.jpg?camera_label=front |
| 6ac71786a5ade89b5c081451 | Deck The Halls Sit Down Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | DEFECT-SEVERE ("DECK THE HALLS!" cropped to illegibility at top) | https://images.printify.com/mockup/6ac71786a5ade89b5c081451/401444/145590/deck-the-halls-sit-down-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac7178307e4149a0f001490 | Dear Santa Explain Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | DEFECT ("I CAN EXPLAIN" clipped at top edge) | https://images.printify.com/mockup/6ac7178307e4149a0f001490/401444/145590/dear-santa-explain-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac7177f46dd1e896e04e5dc | Dear Santa Explain Santa Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | DEFECT-SEVERE (banner text garbled/cropped, illegible) | https://images.printify.com/mockup/6ac7177f46dd1e896e04e5dc/401444/145590/dear-santa-explain-santa-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac7177807e4149a0f001482 | Dear Santa Bank Account Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | DEFECT-SEVERE ("BANK ACCOUNT" missing, only "SAYS...NO" visible) | https://images.printify.com/mockup/6ac7177807e4149a0f001482/401444/145590/dear-santa-bank-account-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac7177407e4149a0f00147f | Corkscrew Wine Repeat Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7177407e4149a0f00147f/401444/145590/corkscrew-wine-repeat-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac71771c0773328340351f6 | Christmas Wreath 2026 Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | DEFECT-SEVERE (top half of wreath + all text cropped away) | https://images.printify.com/mockup/6ac71771c0773328340351f6/401444/145590/christmas-wreath-2026-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac7176da4c95c48e203670d | Christmas Vacation Canceled Christmas Backpack — Cheerful Christmas Travel Pack, Gift for Students | Winstar4U | DEFECT (VACATION touches top edge) | https://images.printify.com/mockup/6ac7176da4c95c48e203670d/401444/145590/christmas-vacation-canceled-christmas-backpack-cheerful-christmas-travel-pack-gift-for-students-winstar4u.jpg?camera_label=front |
| 6ac7176a4636838bd804f82b | Christmas Stress Tinsel Done Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | DEFECT-SEVERE (bottom line "100% DONE" cropped off) | https://images.printify.com/mockup/6ac7176a4636838bd804f82b/401444/145590/christmas-stress-tinsel-done-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac7176757b1ebbe6c0c6e84 | Christmas Party Survivor Christmas Backpack — Festive Holiday Travel Bag, Christmas Gift | Winstar4U | DEFECT-SEVERE ("PARTY" clipped bottom, "SURVIVOR" entirely missing) | https://images.printify.com/mockup/6ac7176757b1ebbe6c0c6e84/401444/145590/christmas-party-survivor-christmas-backpack-festive-holiday-travel-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac71763fb1d11d19e0374b3 | Christmas Open Bar Christmas Backpack — Merry Christmas Daypack, Holiday Gift Idea | Winstar4U | DEFECT-SEVERE (top line nearly invisible, "OPEN BAR" clipped bottom) | https://images.printify.com/mockup/6ac71763fb1d11d19e0374b3/401444/145590/christmas-open-bar-christmas-backpack-merry-christmas-daypack-holiday-gift-idea-winstar4u.jpg?camera_label=front |
| 6ac71760c0773328340351f0 | Christmas Mode Dnd Christmas Backpack — Cheerful Christmas Travel Pack, Gift for Students | Winstar4U | DEFECT-SEVERE (title banner almost entirely cropped, sliver only) | https://images.printify.com/mockup/6ac71760c0773328340351f0/401444/145590/christmas-mode-dnd-christmas-backpack-cheerful-christmas-travel-pack-gift-for-students-winstar4u.jpg?camera_label=front |
| 6ac71720a4c95c48e20366ae | Christmas Lights Therapy Christmas Backpack — Holiday School Bag, Christmas Gift | Winstar4U | DEFECT (heart-shape design clipped, top text cropped) | https://images.printify.com/mockup/6ac71720a4c95c48e20366ae/401444/145590/christmas-lights-therapy-christmas-backpack-holiday-school-bag-christmas-gift-winstar4u.jpg?camera_label=front |
| 6ac71662fd7ff00ded03cb96 | Santas Favorite Distraction Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN (checkerboard noted but design otherwise intact) | https://images.printify.com/mockup/6ac71662fd7ff00ded03cb96/62037/3028/santas-favorite-distraction-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7165ea4c95c48e20365fd | Santas Favorite Customer Vip Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN image, but receipt graphic shows literal "PRICE" placeholder text | https://images.printify.com/mockup/6ac7165ea4c95c48e20365fd/62037/3028/santas-favorite-customer-vip-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7165aa5ade89b5c081347 | Santas Favorite Arrow Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7165aa5ade89b5c081347/62037/3028/santas-favorite-arrow-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac71653fd7ff00ded03cb91 | Reason For Season Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac71653fd7ff00ded03cb91/31948/110719/reason-for-season-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac71653f2868c4f0a02171a | Santa I Can Explain Clipboard Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT-MINOR (EXPLAIN touches top-right edge) | https://images.printify.com/mockup/6ac71653f2868c4f0a02171a/62037/3028/santa-i-can-explain-clipboard-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7164faa7a21cb900b4f01 | Prosecco Ho Ho Ho Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT-SEVERE (top AND bottom text both cropped) | https://images.printify.com/mockup/6ac7164faa7a21cb900b4f01/62037/3028/prosecco-ho-ho-ho-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7164cfd7ff00ded03cb8f | Professional Gift Returner Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT-MINOR (top banner touches edge) | https://images.printify.com/mockup/6ac7164cfd7ff00ded03cb8f/62037/3028/professional-gift-returner-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac716454ff91977d503dd15 | Powered By Cookies Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac716454ff91977d503dd15/62037/3028/powered-by-cookies-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7163fa4cff7da370fd032 | Party In Holiday Party Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7163fa4cff7da370fd032/62037/3028/party-in-holiday-party-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7163cac4a665555019bf4 | Only Nice For Presents Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT (top line cropped) | https://images.printify.com/mockup/6ac7163cac4a665555019bf4/62037/3028/only-nice-for-presents-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7163c4636838bd804f6f3 | O Holy Night Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7163c4636838bd804f6f3/31948/110719/o-holy-night-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac716384636838bd804f6ee | Bah Humbug Wine Christmas Tank Top — Cute Christmas Apparel, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac716384636838bd804f6ee/24828/101889/bah-humbug-wine-christmas-tank-top-cute-christmas-apparel-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7163557b1ebbe6c0c6d4c | Winter Wonderland Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7163557b1ebbe6c0c6d4c/62037/3028/winter-wonderland-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7162f336f835866011896 | Vintage Santa Portra Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT-MINOR (VINTAGE touches top edge) | https://images.printify.com/mockup/6ac7162f336f835866011896/62037/3028/vintage-santa-portra-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac716284636838bd804f6d7 | Truck Tree Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT (CHRISTMAS TIME cropped top) | https://images.printify.com/mockup/6ac716284636838bd804f6d7/62037/3028/truck-tree-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac71624fa3cae10170efe1d | Silent Night Village Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac71624fa3cae10170efe1d/62037/3028/silent-night-village-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7162207e4149a0f001371 | Tree Up Patience Down Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7162207e4149a0f001371/31950/110719/tree-up-patience-down-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac7161dac4a665555019bca | Too Lit Nice List Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7161dac4a665555019bca/31948/110719/too-lit-nice-list-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac7161ca4c95c48e20365c6 | Seasons Greetings Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7161ca4c95c48e20365c6/62037/3028/seasons-greetings-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac716175a14e80fa703f066 | Survived Christmas Hangover Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac716175a14e80fa703f066/31950/110719/survived-christmas-hangover-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac7160d5a14e80fa703f040 | Sleigh All Day Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7160d5a14e80fa703f040/31948/110719/sleigh-all-day-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac715f0ac4a665555019b29 | Peace On Earth Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715f0ac4a665555019b29/62037/3028/peace-on-earth-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac715e4b814691321003a1d | Noel Elegant Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715e4b814691321003a1d/62037/3028/noel-elegant-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac715da4636838bd804f5f3 | Santas Favorite Distraction Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | DEFECT (unrendered-transparency checkerboard background artifact) | https://images.printify.com/mockup/6ac715da4636838bd804f5f3/31950/110719/santas-favorite-distraction-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac715d9fb1d11d19e0372a0 | Merry Christmas Sant Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN image, title truncated: "Merry Christmas Sant" (missing "a") | https://images.printify.com/mockup/6ac715d9fb1d11d19e0372a0/62037/3028/merry-christmas-sant-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac715d5a4c95c48e20364e3 | Santas Favorite Customer Vip Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715d5a4c95c48e20364e3/31950/110719/santas-favorite-customer-vip-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac715d2ed135347800f9dfc | Merry Bright Lights Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715d2ed135347800f9dfc/62037/3028/merry-bright-lights-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac715cfd0a23214d80b2809 | Santas Favorite Arrow Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715cfd0a23214d80b2809/31948/110719/santas-favorite-arrow-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac715ca42c818a1ad0961af | Let It Snow Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715ca42c818a1ad0961af/62037/3028/let-it-snow-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac715c3d0a23214d80b27ed | Joy To World Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715c3d0a23214d80b27ed/62037/3028/joy-to-world-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac715c14636838bd804f5bb | Santa I Can Explain Clipboard Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715c14636838bd804f5bb/31950/110719/santa-i-can-explain-clipboard-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac715bec077332834034fa6 | Prosecco Ho Ho Ho Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715bec077332834034fa6/31950/110719/prosecco-ho-ho-ho-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac715bac077332834034f9b | Professional Gift Returner Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715bac077332834034f9b/31948/110719/professional-gift-returner-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac715baa4c95c48e20364af | Joy Holly Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715baa4c95c48e20364af/62037/3028/joy-holly-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac715b235cf3f6ec802ec57 | Jingle Bells Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715b235cf3f6ec802ec57/62037/3028/jingle-bells-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac715aced135347800f9db7 | Powered By Cookies Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715aced135347800f9db7/31948/110719/powered-by-cookies-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac715a8d0a23214d80b27d1 | Home For Christmas Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT (HOME FOR cropped top) | https://images.printify.com/mockup/6ac715a8d0a23214d80b27d1/62037/3028/home-for-christmas-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac715a7fa3cae10170efcd4 | Party In Holiday Party Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715a7fa3cae10170efcd4/31948/110719/party-in-holiday-party-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac715a4d0a23214d80b27cc | Only Nice For Presents Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715a4d0a23214d80b27cc/31948/110719/only-nice-for-presents-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac715a0a4c95c48e203647c | Happy Holidays Tree Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT (HOLIDAYS cropped top) | https://images.printify.com/mockup/6ac715a0a4c95c48e203647c/62037/3028/happy-holidays-tree-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7159746dd1e896e04e318 | Vintage Santa Portra Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7159746dd1e896e04e318/31948/110719/vintage-santa-portra-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac71593ed135347800f9d87 | Fireplace Stocking Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT (CHRISTMAS cropped top) | https://images.printify.com/mockup/6ac71593ed135347800f9d87/62037/3028/fireplace-stocking-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7158ba5ade89b5c0811c2 | Deck The Halls Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7158ba5ade89b5c0811c2/62037/3028/deck-the-halls-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7158a35cf3f6ec802ec21 | Truck Tree Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7158a35cf3f6ec802ec21/31948/110719/truck-tree-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac71587336f8358660116d9 | Christmas Wishes Sta Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN image, title truncated: "Christmas Wishes Sta" (missing "r") | https://images.printify.com/mockup/6ac71587336f8358660116d9/62037/3028/christmas-wishes-sta-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7158146dd1e896e04e2de | Candy Cane Lane Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN image, but blank/unfinished street-sign placeholder (no text) | https://images.printify.com/mockup/6ac7158146dd1e896e04e2de/62037/3028/candy-cane-lane-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7157efb1d11d19e0371b9 | Believe Sleigh Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7157efb1d11d19e0371b9/62037/3028/believe-sleigh-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7157da5ade89b5c0811ae | Silent Night Village Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7157da5ade89b5c0811ae/31948/110719/silent-night-village-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac7157a0ed8f1657605f458 | Naughty List Vip Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT (JINGLE BELLS cropped top) | https://images.printify.com/mockup/6ac7157a0ed8f1657605f458/62037/3028/naughty-list-vip-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac71579c077332834034f47 | Seasons Greetings Christmas Fleece Zip-Up — Cozy Full-Zip Holiday Hoodie, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac71579c077332834034f47/31948/110719/seasons-greetings-christmas-fleece-zip-up-cozy-full-zip-holiday-hoodie-holiday-gift-winstar4u.jpg?camera_label=front-2 |
| 6ac7156dfa3cae10170efc83 | Naughty List Skeleton Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT + TRUE_DUP (banner cropped left/right; duplicate of V2) | https://images.printify.com/mockup/6ac7156dfa3cae10170efc83/62037/3028/naughty-list-skeleton-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7156442c818a1ad0960e6 | Naughty List Skeleton V2 Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT + TRUE_DUP (banner cropped left/right; duplicate of non-V2) | https://images.printify.com/mockup/6ac7156442c818a1ad0960e6/62037/3028/naughty-list-skeleton-v2-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac71560ed135347800f9cf6 | Santas Favorite Distraction Christmas Women's T-Shirt — Festive Holiday Tee for Her, Holiday Gift | Winstar4U | DEFECT (unrendered-transparency checkerboard background artifact) | https://images.printify.com/mockup/6ac71560ed135347800f9cf6/17979/88/santas-favorite-distraction-christmas-womens-t-shirt-festive-holiday-tee-for-her-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac715600ed8f1657605f429 | Naughty List Resume Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT-SEVERE (bottom punchline "AT THIS POINT ITS A RESUME" cropped) | https://images.printify.com/mockup/6ac715600ed8f1657605f429/62037/3028/naughty-list-resume-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7155d35cf3f6ec802ebe6 | Naughty Is New Nice Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT-MINOR (NICE touches bottom edge) | https://images.printify.com/mockup/6ac7155d35cf3f6ec802ebe6/62037/3028/naughty-is-new-nice-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac71559c077332834034f19 | Santas Favorite Customer Vip Christmas Women's T-Shirt — Festive Holiday Tee for Her, Holiday Gift | Winstar4U | DEFECT (receipt graphic shows literal "PRICE" placeholder text, not values) | https://images.printify.com/mockup/6ac71559c077332834034f19/17979/88/santas-favorite-customer-vip-christmas-womens-t-shirt-festive-holiday-tee-for-her-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7155542c818a1ad0960c7 | My Elf Made Me Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT (text error: "MADE" duplicated in art) | https://images.printify.com/mockup/6ac7155542c818a1ad0960c7/62037/3028/my-elf-made-me-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac71552c077332834034f0e | Santas Favorite Arrow Christmas Women's T-Shirt — Festive Holiday Tee for Her, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac71552c077332834034f0e/17979/88/santas-favorite-arrow-christmas-womens-t-shirt-festive-holiday-tee-for-her-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7154ed0a23214d80b274d | Morning Person Dec25 Skeleton Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT (banner text cropped left/right) | https://images.printify.com/mockup/6ac7154ed0a23214d80b274d/62037/3028/morning-person-dec25-skeleton-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7154b42c818a1ad0960b5 | Santa I Can Explain Clipboard Christmas Women's T-Shirt — Festive Holiday Tee for Her, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7154b42c818a1ad0960b5/17979/88/santa-i-can-explain-clipboard-christmas-womens-t-shirt-festive-holiday-tee-for-her-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7154a42c818a1ad0960b4 | Merry Everything Happy Always Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7154a42c818a1ad0960b4/62037/3028/merry-everything-happy-always-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7154742c818a1ad0960b2 | Prosecco Ho Ho Ho Christmas Women's T-Shirt — Festive Holiday Tee for Her, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7154742c818a1ad0960b2/17979/88/prosecco-ho-ho-ho-christmas-womens-t-shirt-festive-holiday-tee-for-her-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7154742c818a1ad0960b1 | Merry Christmas Lets Get Lit Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT-SEVERE (MERRY almost entirely cropped top) | https://images.printify.com/mockup/6ac7154742c818a1ad0960b1/62037/3028/merry-christmas-lets-get-lit-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7154335cf3f6ec802ebc3 | Professional Gift Returner Christmas Women's T-Shirt — Festive Holiday Tee for Her, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7154335cf3f6ec802ebc3/17979/88/professional-gift-returner-christmas-womens-t-shirt-festive-holiday-tee-for-her-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac71540a5ade89b5c08110f | Jingle Bells Santa Smells Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac71540a5ade89b5c08110f/62037/3028/jingle-bells-santa-smells-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7153fa5ade89b5c08110e | Powered By Cookies Christmas Women's T-Shirt — Festive Holiday Tee for Her, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7153fa5ade89b5c08110e/17979/88/powered-by-cookies-christmas-womens-t-shirt-festive-holiday-tee-for-her-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7153cc077332834034e9d | Jingle All Way Liquor Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7153cc077332834034e9d/62037/3028/jingle-all-way-liquor-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7153c35cf3f6ec802ebc1 | Party In Holiday Party Christmas Women's T-Shirt — Festive Holiday Tee for Her, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7153c35cf3f6ec802ebc1/17979/88/party-in-holiday-party-christmas-womens-t-shirt-festive-holiday-tee-for-her-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac71539a5ade89b5c08110c | Ill Be Home Christmas Probably Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac71539a5ade89b5c08110c/62037/3028/ill-be-home-christmas-probably-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7153835cf3f6ec802ebbd | Only Nice For Presents Christmas Women's T-Shirt — Festive Holiday Tee for Her, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7153835cf3f6ec802ebbd/17979/88/only-nice-for-presents-christmas-womens-t-shirt-festive-holiday-tee-for-her-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7152ffa3cae10170efc50 | Ho Ho Pour Another Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT-SEVERE (HO HO HO cropped top) | https://images.printify.com/mockup/6ac7152ffa3cae10170efc50/62037/3028/ho-ho-pour-another-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7152bfa3cae10170efc4e | Here For Snacks Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7152bfa3cae10170efc4e/62037/3028/here-for-snacks-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7152807e4149a0f0011b3 | Walk By Faith Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT (WALK BY FAITH cropped top) | https://images.printify.com/mockup/6ac7152807e4149a0f0011b3/62037/3028/walk-by-faith-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac71524ed135347800f9ccb | Thankful Grateful Blesse Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT (BLESSED cropped bottom; title also truncated "Blesse") | https://images.printify.com/mockup/6ac71524ed135347800f9ccb/62037/3028/thankful-grateful-blesse-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac715217be9df884b032edf | Savior Born Manger Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac715217be9df884b032edf/62037/3028/savior-born-manger-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7151eb8146913210038ff | Vintage Santa Portra Christmas Women's T-Shirt — Festive Holiday Tee for Her, Holiday Gift | Winstar4U | CLEAN | https://images.printify.com/mockup/6ac7151eb8146913210038ff/17979/88/vintage-santa-portra-christmas-womens-t-shirt-festive-holiday-tee-for-her-holiday-gift-winstar4u.jpg?camera_label=front |
| 6ac7151ded135347800f9cb7 | Rejoice Star Christmas Laptop Sleeve — Stylish Tech Travel Gift, Holiday Gift | Winstar4U | DEFECT-SEVERE (REJOICE cropped top) | https://images.printify.com/mockup/6ac7151ded135347800f9cb7/62037/3028/rejoice-star-christmas-laptop-sleeve-stylish-tech-travel-gift-holiday-gift-winstar4u.jpg?camera_label=front |
