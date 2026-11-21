# $24.99 Etsy tees: price options for 2XL and 3XL (analysis only, NO price changes)

## Sources
- **Costs:** fresh Printify read-only pulls (`printify-get-products`, Etsy shop 26603005 only) on 2026-11-21 between 00:43 and 00:45 UTC. Per-variant rows are in `printify_variants_etsy_amazon.csv`.
- **Shipping:** Printify US standard quote of $5.35 per tee, from `shortlist.csv` (calculate-shipping, 2026-11-20).
- **Buyer-paid shipping:** Etsy listing 4597737445 displayed "$4.95" (`verification_log_shipping.csv`, call 9).

## The five products

All five are blueprint 6 / provider 99 and every enabled colour costs the same within a size.

| Product | ID | Enabled variants | 2XL / 3XL count | Etsy shipping profile | Who pays shipping |
|---|---|---|---|---|---|
| Firefighter "Santa Called for Backup" | 6ad4105a9c8f61e787077ee9 | 60 | 10 / 10 | 300729500105 | **Buyer, $4.95 (verified on the page)** |
| Construction Workers | 6ad4213a11e95e7c5f0cd488 | 60 | 10 / 10 | 300729500105 | Buyer, $4.95 (**inferred**: same profile) |
| Dog Mom | 6ad410763af1c130250b6337 | 100 | 16 / 16 | 300729500105 | Buyer, $4.95 (**inferred**; the page did not render a cost) |
| Christmas Calories Don't Count | 6ad4116c3af1c130250b6447 | 36 | 6 / 6 | 299987014038 | **UNVERIFIED**, modelled as seller pays |
| Cookie Dealer | 6ac2f508368bb1b26d051cd7 | 42 | 7 / 7 | 299987014038 | **UNVERIFIED**, modelled as seller pays. Product is on HOLD (IP/brand-safety REVIEW) |

**Costs (all five tees):**

| Size | Price | Printify cost |
|---|---|---|
| S–XL | $24.99 | $9.68 |
| 2XL | $26.99 | $11.77 |
| 3XL | $26.99 | $12.91 |

## Margin model

- **Seller pays shipping:** net = P − cost − $5.35 − (6.5% + 3%)·P − $0.25 − $0.20 − 2% returns·P − Offsite·P
- **Buyer pays $4.95:** revenue = P + $4.95. Etsy's 6.5% and 3% also apply to the shipping charged. Offsite Ads are charged on the order total including shipping (Etsy's published rule, not re-verified in this run).
- Net % is of the item price P.

## Per-variant results (net $ / net %)

### A. Buyer pays $4.95 (Firefighter, Construction, Dog Mom)

| Size | Option | Price | No Offsite | 15% Offsite |
|---|---|---|---|---|
| 2XL | current | $26.99 | $10.80 / 40.0% | $6.00 / 22.2% |
| 2XL | +$1 | $27.99 | $11.68 / 41.7% | $6.74 / 24.1% |
| 2XL | +$2 | $28.99 | $12.57 / 43.3% | $7.47 / 25.8% |
| 3XL | current | $26.99 | $9.66 / 35.8% | $4.86 / **18.0%** |
| 3XL | +$1 | $27.99 | $10.54 / 37.7% | $5.60 / 20.0% |
| 3XL | +$2 | $28.99 | $11.43 / 39.4% | $6.33 / 21.9% |

### B. Seller pays shipping (Calories, Cookie Dealer; payer unverified)

| Size | Option | Price | No Offsite | 15% Offsite |
|---|---|---|---|---|
| 2XL | current | $26.99 | $6.32 / 23.4% | $2.27 / 8.4% |
| 2XL | +$1 | $27.99 | $7.20 / 25.7% | $3.00 / 10.7% |
| 2XL | +$2 | $28.99 | $8.09 / 27.9% | $3.74 / 12.9% |
| 3XL | current | $26.99 | $5.18 / **19.2%** | $1.13 / 4.2% |
| 3XL | +$1 | $27.99 | $6.06 / 21.7% | $1.86 / 6.7% |
| 3XL | +$2 | $28.99 | $6.95 / 24.0% | $2.60 / 9.0% |

## Competitiveness

**Same shop.** The $29.99 tees (for example 6af8d89e626b8d7aa0015637) are on the same blank, with the same costs ($11.77 for 2XL, $12.91 for 3XL).

| Size | $24.99 tees today | $29.99 tees | $24.99 tees at +$2 |
|---|---|---|---|
| 2XL | $26.99 | $32.99 | $28.99 |
| 3XL | $26.99 | $34.99 | $28.99 |

Even +$2 leaves the $24.99 line $4–6 below its own siblings, so cannibalisation or confusion risk is low.

**Public Etsy sample.** This is a sample, not a market study. It is one Etsy search page, "funny christmas t shirt unisex", scraped 2026-11-21 00:57 UTC (scrape 01a1fb9b-45e1-700a-850c-43f17d036048) and showing 20 results:
- **Displayed price:** $5.95 to $20.26, median $13.58. These are base sizes; the search page doesn't show 2XL/3XL prices.
- **Sale pricing:** 19 of 20 show a struck-through original ($8.69–$35.72), so most competitors run permanent "sale" pricing.
- **Free shipping:** 6 of 20 show "FREE shipping".

Our $24.99 base is already above every displayed price in this sample, so a $1 change on the largest size won't change our position much. The sample can't tell us how size-specific shoppers react. That is **UNVERIFIED**.

## Recommendation (owner decision; nothing changed)

1. **Raise 3XL only by +$1, to $27.99, on all five tees. Leave 2XL at $26.99.**
   - **Calories and Cookie Dealer (seller pays):** lifts 3XL from 19.2% to 21.7% at regular price, which clears the 20% target.
   - **Firefighter, Construction and Dog Mom (buyer pays):** lifts 3XL with 15% Offsite from 18.0% to 20.0%.
   - 2XL already clears 20% at regular price in both models.
   - The writes are 49 variant prices: 10 + 10 + 16 + 6 + 7 3XL variants. They need explicit approval for each product.
2. **Don't go to +$2.** It adds only about 2 points. And with seller-paid shipping, no option here gets a 15%-Offsite order to target (best case 12.9%). Offsite exposure is a fee-structure problem, not a 3XL price problem.
3. **Before acting:** confirm the shipping profiles for Calories and Cookie Dealer (profile 299987014038). If the buyer pays there too, those two tees join model A and no change is strictly needed for regular-price orders.
4. **Cookie Dealer** stays on HOLD for the IP/brand-safety review whatever the price decision.
