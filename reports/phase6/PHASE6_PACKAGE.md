# Winstar Black Friday Completion Package (Phase 6)

**Prepared:** 2026-11-20, about 17:10 UTC.

**Nothing in this package has been applied to a live product, price, listing or channel.** Each live step below needs your separate, product-specific approval. Bridge posts are on task T-6N0T120Q2R. Commit hashes are cited in each section.

---

## 1. Five-store scoreboard

Source: `reports/master_register/scoreboard.md` (commit 9df09b0), updated with the warn-disposition results (commit fc18e56). Counts are unique products, each counted once at its worst open status.

| Shop | Inspected | Defective | VERIFIED READY FOR APPROVAL | REWORK REQUIRED | BLOCKED — OWNER DECISION | BLOCKED — TECHNICAL | NOT VERIFIED | Store complete? |
|---|---|---|---|---|---|---|---|---|
| Shopify Winstar4U 26418699 | 2,069 | 457 | 299 | 1 | 141 | 10 | 6 | **NO**: 1,272 clean but unlinked, 450 uninspected |
| Etsy WinstarDesigns 26603005 | 297 | 38 | 0 | 0 | 38 | 0 | 0 | **NO**: 48 unlinked, 5 uninspected |
| eBay Winstardeals4U 28059412 | 53 | 4 | 0 | 0 | 4 | 0 | 0 | **NO**: 53 of 53 unlinked (D5) |
| TikTok 28122957 | 71 | 0 | 0 | 0 | 0 | 0 | 0 | **NO**: 51 of 71 unlinked (D5) |
| Amazon Winstar4U 29451844 | 62 | 8 | 0 | 0 | 8 | 0 | 0 | **NO**: 46 have no ASIN (D5) |
| **Total** | **2,552** | **507** | **299** | **1** | **191** | **10** | **6** | **0 of 5** |

No storefront has been checked on the marketplace side. Every "linked" fact comes from Printify. `external: null` does not prove that a listing is unpublished.

## 2. Outstanding defects and blockers

| Item | Products | Status | What clears it |
|---|---|---|---|
| Duplicate listings | 63 rows | OWNER | Keep or unpublish each duplicate (`master_defects.csv`, defect_type duplicate_listing) |
| Wording groups (11) | 49 | OWNER | Section 4 |
| Tapestry pricing (D1/D2) | 48 | OWNER | D1 option A, B or C, plus D2 |
| Low resolution, AI upscale only | 15 | OWNER | Accept the upscale, use a smaller motif, or pay for regeneration (section 3) |
| Discontinued provider 99 (socks bp 376, candles bp 727) | 17 | OWNER | Recreate on another provider (new listing) or unpublish |
| Duffels with no Shopify link (D3) | 5 | OWNER | D3 |
| TEXACO IP (D7) | 1 | OWNER | D7 |
| Checkerboard legacy variants (D4) | 10 | TECHNICAL | Owner submits `reports/Printify_Support_Packet_Checkerboard_Legacy_Variants.md` |
| Santa's List scarf `6ac7112383f1a0e50d071cdf` | 1 | REWORK | Needs a clean transparent source at least 3,386 px wide (minimum 1,693 px) |
| Cribbage ornament `6ad4254232b024bb32043467` (Etsy) | 1 | OWNER | Keep the small photo, or go full-bleed (x 0.5, y 0.53, scale 1.2) |
| Open Bar tank `6ac710117be9df884b032c6c`, Black variants | 1 | OWNER | Disable the Black variants, or make a light-ink version |
| Placement defect not reproducible | 4 | NOT VERIFIED | Likely false positives: `6ac70ec09a2f0cb82508f89a`, `6ac71018e2a15b12600266b5`, `6ac7157a0ed8f1657605f458`, `6ac70231154e72164e0d8eea` |
| Blank colour not checked | 2 | NOT VERIFIED | `6ac702e21e2eac4da206fc57`, `6ac702d43fd8c86beb0f48b1` |
| Listings missing on eBay, TikTok and Amazon | 150 | OWNER ACTION | D5 exports from Seller Central, eBay and TikTok |
| Storefront host blocked here | n/a | TECHNICAL | Storefront check must be done from a browser or the crowned-co-data environment |

## 3. Independent QA evidence

| Workstream | Result | Evidence (commit) |
|---|---|---|
| D6 placement-only fixes | 224 products, geometry verified | `work/d6_batch1..10/*/before_after.png`, `placement.json` (batches 1–10) |
| Placement QA rerun with B's script | 107 PASS / 106 WARN / 11 FAIL | `winstar4u/my-projects` `winstar-recovery/qa/placement_qa_224.csv` (c74849e) |
| 11 placement FAILs, 10 repaired-art FAILs, 2 duvets | 8 PASS, 15 WARN (upscale-dependent), 0 FAIL. B's script: 39 of 39 groups pass at 100% inside | `work/d6_qa_fixes/` (5f39cec), Bridge P-4P6T5C6T31 |
| 106 placement WARNs | 91 ACCEPT, 13 FIXED, 1 REWORK, 1 OWNER | `work/d6_warn_disposition/` (fc18e56), Bridge P-2Q0X721S4B |
| Local new-art fixes | 64 fixed: 45 PASS / 15 WARN / 4 FAIL. Of the 10 re-repairs: 8 PASS / 2 WARN | `work/d6_new_art/` |
| Text and blank repairs | 49 of 69 fixed locally | `work/d6_new_art/text_fix/` |

**Upscale caveat (applies to every WARN above):** Real-ESRGAN sharpens edges but invents texture. B's dpi convention also overstates large textiles: shower curtains print at about 75–95 true dpi.

## 4. Wording approval packet: recommendations

- Full packet with before/after images: https://claude.ai/artifact/CeAJdWUhNHW7XhDd6sikjq
- Source: `winstar-recovery/wording/WORDING_APPROVAL_PACKET.md`
- All 49 products are in the Shopify store (26418699).

| Group | Products | Proposed wording | **Recommendation** | Why |
|---|---|---|---|---|
| W1 | 1 | WELCOME / EST. NORTH POLE | **APPROVE** | Fills an empty sign and avoids repeating the headline |
| W2 | 12 | CANDY CANE LANE | **EDIT TO "WELCOME"** | The proposal repeats the headline at about 38 px cap height. WELCOME matches W1 and reads at small size. |
| W3 | 1 | POUR ANOTHER | **APPROVE, Shopify only** | Alcohol humour: don't cross-list to TikTok or Amazon |
| W4 | 6 | ALL THE GIFTS / UNLIMITED / PRICELESS / PAID IN COOKIES | **APPROVE** | Replaces leftover template placeholders ("PRICE", "$99,999.99") |
| W5 | 3 | BRINGING HOME THE TREE | **APPROVE** | Matches the artwork |
| W6 | 4 | TO THE LIQUOR STORE | **APPROVE, Shopify only** | Delivers the joke the titles promise. Check category rules before any cross-listing. |
| W7 | 1 | MERRY CHRISTMAS headline | **NO CHANGE (close defect)** | The intended wording was never recorded, so keeping the art avoids inventing copy |
| W9 | 1 | Remove the scripture-reference line | **APPROVE** | The line would be about 0.5 mm tall when engraved, which is illegible |
| G1 | 1 | AND, AND → AND | **APPROVE** | Typo correction |
| G2 | 10 | MY ELF MADE / MADE → MY ELF / MADE | **APPROVE** | Typo correction |
| G3 | 9 | PATITANECE → PATIENCE | **APPROVE** | Spelling correction |

**Reply format:** `W2 EDIT TO "WELCOME"; W7 NO CHANGE; all others APPROVE` (or any changes you want).

## 5. Live-application batches, ready for authorization

- Files: `reports/phase6/live_application_batches.csv` (299 products, batches LA-01 to LA-08) and `reports/phase6/held_from_live_batches.csv` (10 held because they also have an open duplicate or owner row).
- Builder: `reports/phase6/build_phase6.py`.
- Each row lists the **exact change** (Printify call, product ID, old and new x/y/scale, image file), the **risk**, the **rollback** (old image ID and x/y/scale captured before any change) and the **evidence** path.

| Batch | Products | Art swaps | AI-upscaled | Linked to a channel |
|---|---|---|---|---|
| LA-01 | 40 | 39 | 0 | 1 (`6ac712506f976358160c479a`, Naughty List fanny pack) |
| LA-02 | 40 | 40 | 0 | 0 |
| LA-03 | 40 | 5 | 0 | 0 |
| LA-04 | 40 | 0 | 1 | 0 |
| LA-05 | 40 | 0 | 8 | 0 |
| LA-06 | 40 | 0 | 1 | 0 |
| LA-07 | 40 | 0 | 1 | 0 |
| LA-08 | 19 | 8 | 0 | 0 |

**All 299 are Shopify (26418699) products. Only 1 has a recorded storefront link.** For the other 298, the change is a Printify update with **no publish step**. Publishing them would create new listings, and that is a separate decision.

### How each batch would be applied (only after approval)

1. Snapshot `get-product` for each product ID. This is the rollback source.
2. If an art swap is needed, `upload-image` the staged file.
3. `upsert-product` with the new `print_areas`.
4. Re-fetch the product and compare x/y/scale/image_id with the CSV.
5. Re-render the mockup.
6. Linked product only: publish to resync, then check the storefront.

### Risks

- Mockups regenerate.
- A live listing re-syncs its images, and its title and description if Printify overwrites them. For the 1 linked product, publish with images only.
- AI-upscaled files add no real detail.

### Rollback

`upsert-product` with the `rollback` column values (old image ID plus x/y/scale/angle), then re-fetch to verify.

**Reply format:** `APPROVE LA-01` (or a list of product IDs to exclude).

## 6. Black Friday shortlist

Source: `reports/black_friday/` (commit 4390938), Bridge P-475F6P6J6A.

- **23 products:** 19 on Etsy and 4 on Shopify. All are holiday designs, marked SELL NOW, have a listing link and are not duplicates.
- **Cost and price:** read one product at a time from Printify on 2026-11-20 between 16:09 and 16:13 UTC.
- **Margins** (net, at full price, assuming Winstar pays shipping):

| Product | Net margin |
|---|---|
| Etsy tees | 36.9% |
| Etsy sweatshirts | 30.0% |
| Etsy hoodies | 31.7% |
| Shopify duffels | 38.9% |
| Shopify tees | 33.8% |
| Ornaments, single | 16.6% (offered only as 3 or more) |
| Mugs, single | 10.5% (offered only as 3 or more) |

- **Offers BF-A to BF-G:** each nets at least 18% after the discount, and they must be set up so they can't be combined. See `offers.md`.
- **Not verified:**
  - Live storefront status of the listing links.
  - That today's prices are real regular prices. Printify keeps no price history, so confirm before advertising "% off".
  - Etsy Offsite Ads fees (12–15% on orders they bring in) are not in the margins.

## 7. Promotional assets and posting schedule (drafts, nothing posted)

Files in `reports/black_friday/`:
- `copy/listing_promo_blurbs.md`
- `copy/pinterest_pins.md` (10 pins)
- `copy/instagram_facebook_captions.md` (7 captions)
- `copy/short_video_scripts.md` (5 TikTok/Shorts scripts)
- `schedule.md` (Nov 20–27)
- `tracking.md` (links and UTM tags)

No new promotional images were generated; the pins and posts use each listing's existing mockups. The copy makes no guaranteed-delivery or limited-stock claims. The holiday cutoff line is "Order by Wed Dec 2 for the best chance of arrival before Christmas", which assumes 10 days' handling plus about 5 days' US transit.

## 8. Owner decision register (only decisions that are actually needed)

| # | Decision | Affects | Options |
|---|---|---|---|
| 1 | Wording packet | 49 products | Section 4 reply line |
| 2 | Live batches LA-01 to LA-08 | 299 products | Approve batch by batch, or exclude specific IDs |
| 3 | AI-upscaled files | 15 QA-fix WARNs + 11 warn-fix upscales | Accept, use a smaller motif, or pay for native regeneration |
| 4 | Duvets `6ac71204…`, `6ac711a4…` | 2 | Option A (smaller motif) or B (4× upscale) |
| 5 | Cribbage ornament fit, and Open Bar tank Black variants | 2 | See section 2 |
| 6 | Black Friday offers BF-A to BF-G, plus confirm regular prices | 23 | Approve, change or reject each offer |
| 7 | D2: who pays shipping (Shopify), and whether the Etsy shipping profiles 318194055693 / 318270986851 charge the buyer | Margins, offers, 4 hoodies | Customer pays, or Winstar pays |
| 8 | D1 tapestry pricing | 48 | A, B or C |
| 9 | Duplicate listings | 63 rows | Keep or unpublish, per product |
| 10 | Discontinued provider 99 | 17 | Recreate on another provider, or unpublish |
| 11 | D3 duffels, D7 TEXACO | 6 | See `Winstar_Owner_Decision_Register.md` |
| 12 | Owner actions: D4 support ticket, D5 exports | 10 + 150 | You submit or export |
