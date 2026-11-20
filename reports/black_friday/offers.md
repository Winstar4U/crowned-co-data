# Winstar Black Friday 2026: Proposed Offers (Wave 1)

**Status: every offer below is a PROPOSAL. Nothing has been created, scheduled, or changed.** Each one needs the owner's separate, explicit approval before anyone creates a sale, coupon, or automatic discount in Etsy or Shopify.

- Prepared: 2026-11-20. Black Friday: 2026-11-27.
- Products: the 23 rows in `shortlist.csv`.
- Costs and prices: read-only Printify `get-products` reads, 2026-11-20 16:09–16:13 UTC.
- Shipping: Printify `calculate-shipping`, US standard, default variant, 2026-11-20.

## How net margin is computed

Net = sale price − production cost − shipping − fees − 2% returns allowance.

- **Shipping:** counted at full Printify cost, as if Winstar absorbs it. This is the conservative case, because we don't know who pays shipping on either channel (see D2 in the Owner Decision Register).
- **Etsy fees:** 6.5% transaction + 3% + $0.25 processing + $0.20 listing per unit sold. The generic payment fee is not added again, because Etsy processing replaces it.
  - Not included: Etsy Offsite Ads, 12–15% on any attributed order. One Offsite Ads order would cut an Etsy tee from 36.9% to about 22%.
- **Shopify fees:** Shopify Payments 2.9% + $0.30. This assumes no extra Shopify transaction fee and no app fees.
- **Worst variant:** the margin of the least profitable enabled size or colour, at the same discount.
  - Larger sizes may cost more to ship. That is not modelled.
- **Floor:** an offer is proposed only if the default variant stays at 18% net or more. Where the worst variant drops below 18%, it is flagged.

## Offer table

| ID | Products (shortlist ranks) | Proposed offer | Net before (default) | Net after: default | Net after: worst variant | Verdict |
|---|---|---|---|---|---|---|
| A | Etsy Christmas tees ×6 (1–6) | 20% off sale price | $11.06 / 36.9% | $5.75 / 24.0% | $6.21 / 21.6% | Proposed |
| B | Etsy Christmas crewneck sweatshirts ×4 (7–10) | 10% off | $14.08 / 30.0% | $9.92 / 23.4% | 23.4% | Proposed. 15% would be 19.6%, so it's not proposed |
| C | Etsy Christmas hoodies ×2 (11–12) | 15% off | $17.45 / 31.7% | $10.14 / 21.7% | $10.15 / 19.9% | Proposed |
| D | Shopify funny Christmas tees ×2 (15–16) | 10% off (automatic discount on these 2 products only) | $8.44 / 33.8% | $6.06 / 26.9% | $4.54 / 18.7% (2XL+) | Proposed. 15% would put 2XL+ at 14.2%, so it's not proposed |
| E | Shopify Christmas duffel bags ×2 (13–14) | 15% off | $36.57 / 38.9% (Small) | $23.17 / 29.0% | $18.72 / 23.4% (Large) | Proposed. Largest net $ per order in the wave |
| F | Etsy Christmas ornaments ×4 (17–20) | No single-item discount. Multi-buy: **10% off 3+ ornaments** | 1 ornament: $3.82 / 16.6% (Winstar ships). 2 at full price: $13.48 / 29.3% | 3 at 10% off: $17.04 / 27.5% | Same (one variant) | Proposed as multi-buy only |
| G | Etsy "Fuel" Christmas mugs ×3 (21–23) | No single-item discount. Multi-buy: **10% off 3+ mugs** | 1 mug: $2.21 / 10.5% (Winstar ships). 2 at full price: $10.46 / 24.9% | 3 at 10% off: $13.15 / 23.2% | 11oz not modelled | Proposed as multi-buy only. "2 mugs at 10% off" would be 17.9%, so it's rejected |

### Why the ornaments and mugs are multi-buy only

At one unit, with Winstar paying shipping, an ornament nets 16.6% and a mug 10.5%. Both are below the 18% floor. If Etsy's shipping profile charges the buyer the shipping cost, they net 44.0% and 57.2%.

- Etsy shipping profiles 318194055693 (ornaments) and 318270986851 (mugs) exist on the Printify records. Their rates are not visible from Printify.
- **Owner check:** in Etsy, open Settings, then Shipping settings, and confirm whether these profiles charge the buyer.
- If they do, F and G could become simple 10–15% single-item discounts. That would be a separate PROPOSAL.

### Rules every offer must follow (also PROPOSALS)

1. **No stacking.** Set the promotions up so one buyer can't combine A–E with F or G.
   - Example: a 20%-off tee plus "10% off 3+ items" pushes the tee below 18%.
   - Verify this in Etsy (Marketing, then Sales and discounts) and in Shopify Discounts before going live.
2. **Scope to the listed products only.** Never apply an offer shop-wide.
   - The excluded lines are not cleared at a discount: tapestries (D1), the checkerboard tees (D4), and the REPAIR FIRST products.
3. **Honest reference prices.** "X% off" must be taken off the current regular price.
   - That price was read from Printify on 2026-11-20. Printify has no price history, so we can't prove how long that price was charged.
   - The owner should confirm these were the real selling prices before advertising a percentage.
4. **No scarcity or delivery claims.** Don't say "limited stock" (everything is print-on-demand) or "guaranteed by Christmas".

## Suggested offer window (PROPOSAL)

- **Start:** Fri 2026-11-27 00:01 local.
- **End:** Mon 2026-11-30 23:59 local (Cyber Monday).
- **Teaser posts Nov 20–26:** promote the products at regular price. Mention an offer only in the form "Black Friday deals coming", and only once the owner has approved the offers.

## Order-by guidance for the copy (not a guarantee)

**Wording to use:** "Order by Wednesday, December 2 for the best chance of arrival before Christmas (US standard shipping)."

How the date was worked out:
- **Handling time: verified.** Printify shipping profiles give a 10-day handling time for all six product types: ornament 1599/48, mug 478/99, tee 6/99, crewneck 49/99, hoodie 77/99, duffel 372/99.
- **Transit time: assumed.** About 5 business days for US standard. Printify returned no transit-time data.
- **Calculation:** Dec 2, plus 10 business days of handling, gives Dec 16. Plus 5 business days of transit gives Dec 23.

Never write "guaranteed", "arrives by", or "in time for Christmas" as a promise.

## Candidates fetched but excluded

| Product | Reason |
|---|---|
| Shopify hoodies `6ac7135f35a66ab7dc0b10a0` Cardinal in Snow, `6ac71362fb1d11d19e0370a7` Cozy Cabin, `6ac7135b83f1a0e50d071e08` Vintage Santa Sleigh Ride, `6ac7137ad9b782898109a9d6` Chill Penguin | $39.99 vs $21.58 cost: net 17.4% if Winstar pays the $9.19 shipping, below the 18% floor. Net is 40.4% if the buyer pays. Can be added once D2 is answered "customer pays", at full price only |
| Shopify duffel `6ac7123e6356cae0df02e33f` Candy Cane Lane | IP/trademark: "Candy Cane Lane" is also the title of a 2023 feature film. Excluded as a precaution, even though the phrase is generic |
| Shopify tee `6ac28d35d0995db35108e7bb` "Chillin' With My Snowmies" | IP/trademark: popular slogan with possible trademark filings (not checked against USPTO). Excluded as a precaution |
| Standing exclusions (not considered) | All tapestries (D1); TEXACO canvas `6a53ee979296b919210641d5` (D7/HOLD); 10 checkerboard tees (D4); every REPAIR FIRST and HOLD product; Luzilly and adult-category items; alcohol and profanity-themed designs (for example "Festive AF", "Holiday Hangover Club", wine tumblers), kept out for brand safety |

## Approvals needed (reply per ID)

- `BF-A: approve` / `BF-A: change to N%` / `BF-A: reject`
- The same for BF-B, BF-C, BF-D, BF-E, BF-F and BF-G.
- `D2` and the Etsy shipping-profile check: these settle whether F and G can become single-item discounts.
