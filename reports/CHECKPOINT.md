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

## Waiting on owner (nothing executes until decided)

1. Tapestry repricing: choose Scenario B prices ($31.99 / $44.99 / $63.99 / $79.99), Scenario A, or disable the two large sizes.
2. Confirm whether Winstar4U customers pay shipping.
3. Shopify admin check of the 5 unmapped duffels, then approve a re-publish.
4. Submit the checkerboard support ticket.
5. The 10 checkerboard swap-ins (T-4P5P5J571N), after the support ticket resolves.

## Known blockers

- Egress to `4juy1i-kq.myshopify.com` is refused, so the Winstar4U storefront cannot be checked from here.
- The Shopify app connected in this session is "Winstar Marketing" (winstarmarketing.shop), **not** the Winstar4U store.
- Luzilly Fragrances (T-3Z2E4A4V60) is deferred by the owner. Do not claim it.

## Next action for the next session

Wait for the owner's pricing decision. Once approved, run `printify-set-product-prices` on the 48 products using the CSV, re-fetch each one to verify, update this file, and post the result to Bridge.
