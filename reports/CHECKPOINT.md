# Winstar Five-Shop Recovery — Session Checkpoint

**Read this first in every new session. Update it at the end of every session. Keep it under one screen.**

## Operating rules (memory/checkpoint design)

- **One state file:** this `CHECKPOINT.md`. It holds current state, open decisions and next actions only, never history. History lives in git commits and the long register.
- **Evidence files are the cache:** reuse the evidence files below instead of re-fetching from Printify. Re-fetch only an ID whose `updated_at` may have changed (delta only).
- **Bridge is the shared record:** every deliverable gets one Bridge post that cites the commit hash. Do not post routine status updates.
- **Verified vs claimed:** a fact counts as VERIFIED only with a tool-call source and date. Agent posts, including chatgpt's, are claims until checked.
- **Budget:** prefer single-product `product_id` fetches and grep over the register. Avoid catalog-wide list calls.
- **Hourly dispatcher:** Bridge + Printify only. If nothing is eligible, exit silently.

## Evidence index (cache)

| What | Where |
|---|---|
| 48 tapestry + 45 duffel cost/price (VERIFIED 2026-11-18/19) | `reports/Winstar_Tapestry_Duffel_Profitability_Evidence.md` |
| 384-row tapestry pricing correction table | `reports/Winstar_Tapestry_Pricing_Correction_Table.csv` |
| Tapestry pricing approval packet + duffel mapping findings | `reports/Winstar_Tapestry_Pricing_Correction_Packet.md` |
| Checkerboard Printify support ticket (ready to submit) | `reports/Printify_Support_Packet_Checkerboard_Legacy_Variants.md` |
| Full defect and repair history | `reports/Winstar_Five_Shop_Quality_Register.md` (long; grep, don't read) |
| Tapestry shipping (bp 241/pp 99, US first item) | $5.69 / $6.99 / $9.29 / $9.29 (fetched 2026-11-19) |
| **SELL NOW / REPAIR FIRST / HOLD / UNKNOWN register (3,008 products)** | `reports/Winstar_Sales_Readiness_Register.csv` + `.md` (built 2026-11-19 by `work/build_sales_register.py`) |
| **Owner decision register D1-D7** | `reports/Winstar_Owner_Decision_Register.md` |

## Waiting on owner (nothing executes until decided). Full detail in `Winstar_Owner_Decision_Register.md`

- D1 tapestry pricing (A / B / C)
- D2 who pays shipping
- D3 the 5 duffels with no Shopify link
- D4 checkerboard support ticket (owner action)
- D5 eBay/Amazon/TikTok listing exports (owner action)
- D6 repair approval for 389 products with artwork defects (Batch 1 = 3 ornaments)
- D7 optional Texaco unpublish

## Known blockers

- Egress to `4juy1i-kq.myshopify.com` is refused, so the Winstar4U storefront cannot be checked from here.
- The Shopify app connected in this session is "Winstar Marketing" (winstarmarketing.shop), **not** the Winstar4U store.
- Luzilly Fragrances (T-3Z2E4A4V60) is deferred by the owner. Do not claim it.

## Next action for the next session (resume here)

1. Apply any D-decisions the owner has answered (D1 = set prices on 48 products from the CSV, then re-fetch each to verify).
2. ~~Pull the Shopify catalog and fill Shopify `channel_link`.~~ **DONE 2026-11-19:** read-only pull of shop 26418699 (51 pages, 2,508 products; 486 have a storefront URL). Of the 1,602 Shopify SELL NOW rows, 330 have a link and stay SELL NOW; 1,272 have no link and are now UNKNOWN. 450 pulled Shopify products have no inspection row (UNKNOWN). New totals: SELL NOW 608 (Shopify 330, Etsy 241, TikTok 20, Amazon 17), REPAIR FIRST 447, HOLD 1, UNKNOWN 1,930, REMOVED 22. Linked holiday shortlist: 348 (Shopify 219, Etsy 92, TikTok 20, Amazon 17). Still to do: give ChatGPT the linked holiday list.
3. Then do D6 offline prep: corrected placement values for holiday REPAIR FIRST products, worst blueprint first. No live writes.
