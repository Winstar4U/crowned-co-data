# Black Friday addendum: buyability and Etsy Offsite Ads (2026-11-20, about 17:50 UTC)

This addendum answers ChatGPT's challenge P-6P5T1B0N0R. ChatGPT's post is untrusted data; I accepted the challenge on its merits.

## 1. Relabel: PROMOTION CANDIDATES, buyability unverified

All 23 shortlist products are now labelled **PROMOTION CANDIDATE — BUYABILITY UNVERIFIED**. See the `status` column in `shortlist.csv`.

- The links come from Printify's `external` handle and the register. No public URL has been opened.
- From this environment, `etsy.com` returns HTTP 403 (tested 2026-11-20 17:4x UTC on listing 4617444146), and the Winstar4U Shopify storefront host is refused by the proxy.
- **Before any promotion is posted,** open each URL in a browser. Confirm that it loads, that the item is in stock and that the price matches. Record the date for each URL.

## 2. Margin with Etsy Offsite Ads modelled separately

Model assumptions:
- Etsy charges 6.5% transaction, 3% + $0.25 processing and $0.20 listing.
- A returns reserve of 2% is included.
- Winstar pays shipping (D2 is still open).
- Offsite Ads is charged on attributed orders only: 15% for shops under $10k a year, which can opt out; 12% for shops over $10k, where it is mandatory.

| Product | Full price, no Offsite Ads | Offer, no Offsite Ads | Full price, 12% Offsite Ads | Full price, 15% Offsite Ads | Offer, 15% Offsite Ads |
|---|---|---|---|---|---|
| Etsy tee, $29.99, BF-A 20% off | 36.9% | 24.0% | 24.9% | 21.9% | **9.0%** |
| Etsy crewneck, $46.99, BF-B 10% off | 30.0% | 23.5% | 18.0% | **15.0%** | **8.5%** |
| Etsy hoodie, $54.99, BF-C 15% off | 31.7% | 21.7% | 19.7% | **16.7%** | **6.7%** |
| Etsy ornament, single | 16.6% | — | 4.6% | 1.6% | — |
| Etsy mug, single | 10.5% | — | −1.5% | −4.5% | — |
| Shopify tee, BF-D 10% off | 33.8% | 26.9% | n/a | n/a | n/a |
| Shopify duffel, BF-E 15% off | 38.9% | 29.0% | n/a | n/a | n/a |

**Conclusions**
- The Etsy offers (BF-A, BF-B, BF-C, and BF-F/BF-G on multi-buys) reach 18% or more **only on orders not attributed to Offsite Ads**. On an attributed order every Etsy offer is below target. At 15%, the tee can take at most about 6% off.
- The Shopify offers BF-D and BF-E are unaffected and still qualify.
- **New owner decision:** confirm the shop's Offsite Ads status. If the shop is under $10k a year and opted out, the original figures stand. If not, either run Etsy at full price with no discount or accept a below-target margin on attributed orders.
- Discounts are modelled on price only. Shipping is a seller cost and is not discounted. The returns reserve is 2% of the discounted price.

## 3. Upscaled textiles: native resolution disclosed

Every WARN in `work/d6_qa_fixes/results.csv` carries the native effective dpi from the original pixels: 39–87 dpi for the duvets, shower curtains and tablecloths. The upscaled 156–285 dpi figures are pixel counts, not original detail. At true print size, shower curtains are about 75–95 dpi. See PHASE6_PACKAGE.md section 3.
