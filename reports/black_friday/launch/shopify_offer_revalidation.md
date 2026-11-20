# Shopify Black Friday offers: per-variant revalidation (BF-D, BF-E)

**Status: PROPOSALS ONLY. Nothing was created, scheduled or changed.** Every discount needs the owner's separate, product-specific approval before it is built in Shopify.

- Prepared 2026-11-20, about 20:25 UTC.
- Costs and prices: Printify `get-products` (read-only), shop 26418699, fetched 2026-11-20 20:13–20:15 UTC. Every **enabled** variant was checked, not just the default.
- Live price check: Firecrawl, 2026-11-20 20:19–20:21 UTC. All 10 Shopify pages returned 200, showed the Printify default price ($24.99 tees, $93.99 duffels, both duffel sizes $93.99), had Add to cart enabled and showed no sale. See `verification_log.csv`.
- Model, per unit: net = sale price − Printify cost − shipping − Shopify Payments (2.9% + $0.30 of the sale price) − 2% returns reserve. Net % is of the sale price.
- Shipping is the verified US standard quote (tee $5.35, duffel $5.35), paid by Winstar, because D2 is still open. Bigger sizes (tee 2XL/3XL, Large duffel) may cost more to ship. That is **not modelled**, so the worst-variant numbers are a best case. Each extra $1 of shipping takes about 4 points off a 3XL tee at 10% off and about 1.3 points off a Large duffel at 15% off.
- Rule: an offer is recommended only if the **worst enabled variant** stays at 18% or more. The target is 20%.
- **"% off" reference price is unproven.** The $24.99 and $93.99 prices were read today. Printify keeps no price history, so we can't show how long those prices were charged. The owner must confirm they are the real regular selling prices before any "% off" claim is published.
- A full per-variant export (every enabled variant title × discount) is in `shopify_offer_variants.csv`.

## Verdicts

| Offer | Products | Reported before | Revalidated: default | Revalidated: worst enabled variant | Verdict |
|---|---|---|---|---|---|
| **BF-D** tees 10% off | Baking Spirits Bright `6ac289e41993b4de4807c83d`, Introverted But Festive `6ac26d3ab2c2645b070bb1ef` | 26.9% | 26.9% ($6.06) | **18.7% ($4.54), 3XL** (7 of 38 variants); 2XL 23.4% | **PASSES the 18% floor, misses the 20% target.** Recommend 10% only if the owner accepts 18.7% on 3XL. Otherwise **8% off**: worst 3XL is 20.4%, so every variant meets the target. |
| BF-D extension | Santas Favorite Vet `6ac352fa5dab9d4112038b9e`, Cute Reindeer Lights `6ac346f02f513cff0f09afb1` | n/a | 26.9% | **18.7%, 3XL** | Same costs as BF-D, so the same verdict. Can join BF-D. |
| BF-D extension | Nurses Holidays Brighter `6ac34ceeefcc1caa890eeee6`, Owl Be Home For Christmas `6ac3612004778276c906e172` | n/a | 23.4% | **15.4% ($3.74), 3XL**: FAILS | Base cost is higher ($10.47 vs $9.68). **10% off across all variants is NOT recommended.** Options: (a) regular price only (default), (b) 10% off with the 7 3XL variants left out: worst is then 2XL at 20.1%, (c) 5% off everything: worst 19.6%. |
| **BF-E** duffels 15% off | Believe Sleigh `6ac711e0b81469132100377f`, Christ Is Born `6ac70edc7be9df884b032bed` | 29.0% | 29.0% ($23.17), Small | **23.4% ($18.72), Large** | **RECOMMEND.** Both sizes are above 20%. 20% off would put Large at 18.9% (just above the floor, below target), so it isn't recommended. |
| BF-E extension | O Holy Night `6ac70ef49a2f0cb82508f8b8`, Merry Everything Happy Always `6ac70f274e8c3a1ca906ec63` | n/a | 29.0% | **23.4%, Large** | Same blueprint, costs and price, so it can join BF-E. |

**Buyer-pays-shipping view (if D2 is answered "customer pays"):** tees at full price net 54.5% (Nurses/Owl 51.4%), duffels 44.4%. The Shopify fee then includes 2.9% on the shipping charged to the buyer.

## Setup rules if approved (proposal)

1. Build a Shopify **automatic discount scoped to these product IDs only**, never store-wide. For Nurses/Owl option (b), choose the non-3XL variants explicitly. If the discount tool can't select variants, use option (a) or (c).
2. **No stacking.** Do not combine with any other code or automatic discount, so BF-D and BF-E cannot apply to the same line.
3. Window: Fri 11/27 00:01 to Mon 11/30 23:59 (store local time), as already proposed in `offers.md`.
4. Before going live: owner confirms (i) the regular-price basis, (ii) D2 shipping, (iii) that `winstarmarketing.shop` (where `4juy1i-kq.myshopify.com` redirects, page title suffix "Winstar Marketing", duffel pages show "Winstar4U") is the Winstar4U store and **not** the developer-managed Winstar Marketing store, which is out of scope.

## Data issue found (no action taken)

The Printify description for **Baking Spirits Bright** and **Introverted But Festive** was copied from another product ("Santa Freakin' Knows"). The **live** Shopify descriptions are correct (scraped first sentences mention the right phrase). **Do not republish these two products from Printify,** because a republish would overwrite the correct live description with the wrong one. Fixing the Printify text is a separate write and needs approval.

## Per-variant tables (net $ / net % of sale price, seller pays shipping)

### BF-D (original 2 tees)


**"Baking Spirits Bright" Funny Christmas T-Shirt — Humorous Christmas Graphic Tee** `6ac289e41993b4de4807c83d` (enabled variants: 38; shipping $5.35 seller-paid)

| Size tier | Variants (enabled) | Price | Cost | Net 0% off | Net 10% off | Net 8% off | Net 5% off |
|---|---|---|---|---|---|---|---|
| L/M/S/XL | 25 | $24.99 | $9.68 | $8.44 / 33.8% | $6.06 / 26.9% | $6.53 / 28.4% | $7.25 / 30.5% |
| 2XL | 6 | $26.99 | $11.77 | $8.25 / 30.6% | $5.68 / 23.4% | $6.19 / 24.9% | $6.96 / 27.2% |
| 3XL | 7 | $26.99 | $12.91 | $7.11 / 26.3% | $4.54 / 18.7% | $5.05 / 20.4% | $5.82 / 22.7% |

**"Introverted But Festive" Funny Christmas T-Shirt — Humorous Christmas Graphic T** `6ac26d3ab2c2645b070bb1ef` (enabled variants: 38; shipping $5.35 seller-paid)

| Size tier | Variants (enabled) | Price | Cost | Net 0% off | Net 10% off | Net 8% off | Net 5% off |
|---|---|---|---|---|---|---|---|
| L/M/S/XL | 25 | $24.99 | $9.68 | $8.44 / 33.8% | $6.06 / 26.9% | $6.53 / 28.4% | $7.25 / 30.5% |
| 2XL | 6 | $26.99 | $11.77 | $8.25 / 30.6% | $5.68 / 23.4% | $6.19 / 24.9% | $6.96 / 27.2% |
| 3XL | 7 | $26.99 | $12.91 | $7.11 / 26.3% | $4.54 / 18.7% | $5.05 / 20.4% | $5.82 / 22.7% |

### BF-D candidates: Vet / Reindeer tees (same costs)


**Santas Favorite Vet Christmas Tee** `6ac352fa5dab9d4112038b9e` (enabled variants: 42; shipping $5.35 seller-paid)

| Size tier | Variants (enabled) | Price | Cost | Net 0% off | Net 10% off | Net 8% off | Net 5% off |
|---|---|---|---|---|---|---|---|
| L/M/S/XL | 28 | $24.99 | $9.68 | $8.44 / 33.8% | $6.06 / 26.9% | $6.53 / 28.4% | $7.25 / 30.5% |
| 2XL | 7 | $26.99 | $11.77 | $8.25 / 30.6% | $5.68 / 23.4% | $6.19 / 24.9% | $6.96 / 27.2% |
| 3XL | 7 | $26.99 | $12.91 | $7.11 / 26.3% | $4.54 / 18.7% | $5.05 / 20.4% | $5.82 / 22.7% |

**Cute Reindeer Lights Christmas Tee** `6ac346f02f513cff0f09afb1` (enabled variants: 42; shipping $5.35 seller-paid)

| Size tier | Variants (enabled) | Price | Cost | Net 0% off | Net 10% off | Net 8% off | Net 5% off |
|---|---|---|---|---|---|---|---|
| L/M/S/XL | 28 | $24.99 | $9.68 | $8.44 / 33.8% | $6.06 / 26.9% | $6.53 / 28.4% | $7.25 / 30.5% |
| 2XL | 7 | $26.99 | $11.77 | $8.25 / 30.6% | $5.68 / 23.4% | $6.19 / 24.9% | $6.96 / 27.2% |
| 3XL | 7 | $26.99 | $12.91 | $7.11 / 26.3% | $4.54 / 18.7% | $5.05 / 20.4% | $5.82 / 22.7% |

### BF-D candidates: Nurses Holidays Brighter / Owl tees (higher costs)


**Nurses Holidays Brighter Christmas Tee** `6ac34ceeefcc1caa890eeee6` (enabled variants: 38; shipping $5.35 seller-paid)

| Size tier | Variants (enabled) | Price | Cost | Net 0% off | Net 10% off | Net 8% off | Net 5% off |
|---|---|---|---|---|---|---|---|
| L/M/S/XL | 25 | $24.99 | $10.47 | $7.65 / 30.6% | $5.27 / 23.4% | $5.74 / 25.0% | $6.46 / 27.2% |
| 2XL | 6 | $26.99 | $12.57 | $7.45 / 27.6% | $4.88 / 20.1% | $5.39 / 21.7% | $6.16 / 24.0% |
| 3XL | 7 | $26.99 | $13.71 | $6.31 / 23.4% | $3.74 / 15.4% | $4.25 / 17.1% | $5.02 / 19.6% |

**Owl Be Home For Christmas Tee** `6ac3612004778276c906e172` (enabled variants: 38; shipping $5.35 seller-paid)

| Size tier | Variants (enabled) | Price | Cost | Net 0% off | Net 10% off | Net 8% off | Net 5% off |
|---|---|---|---|---|---|---|---|
| L/M/S/XL | 25 | $24.99 | $10.47 | $7.65 / 30.6% | $5.27 / 23.4% | $5.74 / 25.0% | $6.46 / 27.2% |
| 2XL | 6 | $26.99 | $12.57 | $7.45 / 27.6% | $4.88 / 20.1% | $5.39 / 21.7% | $6.16 / 24.0% |
| 3XL | 7 | $26.99 | $13.71 | $6.31 / 23.4% | $3.74 / 15.4% | $4.25 / 17.1% | $5.02 / 19.6% |

### BF-E (original 2 duffels)


**Believe Sleigh Christmas Duffel Bag** `6ac711e0b81469132100377f` (enabled variants: 2; shipping $5.35 seller-paid)

| Size tier | Variants (enabled) | Price | Cost | Net 0% off | Net 15% off | Net 20% off | Net 10% off |
|---|---|---|---|---|---|---|---|
| Small | 1 | $93.99 | $47.16 | $36.57 / 38.9% | $23.17 / 29.0% | $18.70 / 24.9% | $27.64 / 32.7% |
| Large | 1 | $93.99 | $51.61 | $32.12 / 34.2% | $18.72 / 23.4% | $14.25 / 18.9% | $23.19 / 27.4% |

**Christ Is Born Christmas Duffel Bag** `6ac70edc7be9df884b032bed` (enabled variants: 2; shipping $5.35 seller-paid)

| Size tier | Variants (enabled) | Price | Cost | Net 0% off | Net 15% off | Net 20% off | Net 10% off |
|---|---|---|---|---|---|---|---|
| Small | 1 | $93.99 | $47.16 | $36.57 / 38.9% | $23.17 / 29.0% | $18.70 / 24.9% | $27.64 / 32.7% |
| Large | 1 | $93.99 | $51.61 | $32.12 / 34.2% | $18.72 / 23.4% | $14.25 / 18.9% | $23.19 / 27.4% |

### BF-E candidates: O Holy Night / Merry Everything duffels


**O Holy Night Christmas Duffel Bag** `6ac70ef49a2f0cb82508f8b8` (enabled variants: 2; shipping $5.35 seller-paid)

| Size tier | Variants (enabled) | Price | Cost | Net 0% off | Net 15% off | Net 20% off | Net 10% off |
|---|---|---|---|---|---|---|---|
| Small | 1 | $93.99 | $47.16 | $36.57 / 38.9% | $23.17 / 29.0% | $18.70 / 24.9% | $27.64 / 32.7% |
| Large | 1 | $93.99 | $51.61 | $32.12 / 34.2% | $18.72 / 23.4% | $14.25 / 18.9% | $23.19 / 27.4% |

**Merry Everything Happy Always Christmas Duffel Bag** `6ac70f274e8c3a1ca906ec63` (enabled variants: 2; shipping $5.35 seller-paid)

| Size tier | Variants (enabled) | Price | Cost | Net 0% off | Net 15% off | Net 20% off | Net 10% off |
|---|---|---|---|---|---|---|---|
| Small | 1 | $93.99 | $47.16 | $36.57 / 38.9% | $23.17 / 29.0% | $18.70 / 24.9% | $27.64 / 32.7% |
| Large | 1 | $93.99 | $51.61 | $32.12 / 34.2% | $18.72 / 23.4% | $14.25 / 18.9% | $23.19 / 27.4% |