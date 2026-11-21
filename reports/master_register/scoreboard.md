# Five-Shop Defect Scoreboard

Built 2026-11-20 ~16:10 UTC from existing evidence only. No new inspections, no Printify calls, no writes.
Product-level detail: `master_defects.csv` (524 rows = 507 unique products). Number mapping: `reconciliation.md`.

## Scoreboard

Status columns count **unique products** at their worst open status. The order is NOT VERIFIED, then REWORK, then BLOCKED-TECH, then BLOCKED-OWNER, then VERIFIED. Row counts follow in brackets.

| Shop | Products inspected (register) | Unique defective products | VERIFIED READY FOR APPROVAL | REWORK REQUIRED | BLOCKED — OWNER DECISION | BLOCKED — TECHNICAL | NOT VERIFIED | Marketplace verification gap | Store complete? |
|---|---|---|---|---|---|---|---|---|---|
| Shopify Winstar4U 26418699 | 2,069 (#361–2,429 full visual; #1–360 metadata only) | **457** | 300 [308] | 0 | 141 [149] | 10 [10] | 6 [6] | 1,272 clean but no storefront link + 450 products in the 2026-11-19 pull with no inspection row; storefront host blocked | **NO** |
| Etsy WinstarDesigns 26603005 | 297 | **38** | 0 [1] | 0 | 37 [37] | 0 | 1 [1] | 48 clean but unlinked + 5 never inspected | **NO** |
| eBay Winstardeals4U 28059412 | 53 | **4** | 0 | 0 | 4 [4] | 0 | 0 | **53 of 53 unlinked**, awaiting the D5 eBay export | **NO** |
| TikTok My TikTok Shop 28122957 | 71 | **0** | 0 | 0 | 0 | 0 | 0 | **51 of 71 unlinked**, awaiting the D5 TikTok export | **NO** (gap only) |
| Amazon Winstar4U 29451844 | 62 | **8** | 0 | 0 | 8 [8] | 0 | 0 | **46 of 63 unlinked** (no ASIN), awaiting the D5 Seller Central export | **NO** |
| **Total** | **2,552** | **507** | **300 [309]** | **0** | **190 [198]** | **10 [10]** | **7 [7]** | 1,470 unlinked + 455 uninspected | **0 of 5** |

No marketplace-side storefront check has been done for any shop (Quality Register line 1002). Every "linked" or "live" fact comes from Printify alone. `external: null` does not prove a listing is unpublished.

## Totals by final_status (rows)

| final_status | Rows | Unique products (worst status) |
|---|---|---|
| VERIFIED READY FOR APPROVAL | 309 | 300 |
| REWORK REQUIRED | 0 | 0 |
| BLOCKED — OWNER DECISION | 198 | 190 |
| BLOCKED — TECHNICAL | 10 | 10 |
| NOT VERIFIED | 7 | 7 |
| **Total** | **524** | **507** |

## Rows by defect_type

| defect_type | Rows | Main status |
|---|---|---|
| placement | 220 | 216 VERIFIED; 4 NOT VERIFIED (defect could not be reproduced) |
| artwork | 99 | 86 VERIFIED; 10 BLOCKED-TECH (checkerboard D4); 3 NOT VERIFIED (blank colour unchecked) |
| duplicate_listing | 63 | BLOCKED-OWNER (Etsy 36, Shopify 15, Amazon 8, eBay 4) |
| wording | 49 | BLOCKED-OWNER (11 wording groups) |
| profitability | 48 | BLOCKED-OWNER (D1/D2 tapestry pricing) |
| resolution | 22 | 7 VERIFIED; 15 BLOCKED-OWNER (accept AI upscale, shrink the motif, or regenerate) |
| availability_discontinued | 17 | BLOCKED-OWNER (10 socks bp 376 + 7 candles bp 727; provider 99 discontinued) |
| marketplace_sync | 5 | BLOCKED-OWNER (D3 duffels) |
| IP | 1 | BLOCKED-OWNER (D7 TEXACO) |
| shipping, other | 0 | D2 (who pays shipping) is a store-level decision and appears inside the profitability rows |

## What "VERIFIED READY FOR APPROVAL" means here

The row has a fix file or placement values, a geometry or resolution QA result of PASS (or a WARN noted in the row), and a before/after or render. Nothing is live. Every row still needs the owner's separate, product-specific go-live approval before the `live_action_needed` write runs.
