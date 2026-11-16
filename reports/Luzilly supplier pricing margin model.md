# Luzilly Bridal — SKU-level pricing & margin model

Covers the **only three suppliers with a VERIFIED (directly published) wholesale cost** found in
the supplier verification research: BrydealoFactory, 1stopbridal, and UCALLA (plus-size line only).
Every other researched supplier's pricing is login-gated, tiered as an undisclosed percentage off
MSRP, or simply not published — no number is invented for them here.

**Modeling assumptions, stated explicitly (none of this is supplier-specific sourced data):**
- Payment processing: 2.9% + $0.30 per transaction — the standard published Shopify Payments US
  rate, not something any of these suppliers publish or control.
- Return-rate stress test uses 10% and 25% of orders returned, as bracketing assumptions for a
  bridal/formalwear category (fit-sensitive goods are commonly cited as having above-average return
  rates versus general apparel) — **not a sourced figure for any of these three suppliers specifically**.
- **Advertising/customer-acquisition cost (CAC) is deliberately NOT included** — no real Luzilly ad-spend
  data exists to draw from. Whatever CAC turns out to be in practice subtracts directly from every
  margin figure below. These numbers are a ceiling, not a forecast.
- **Fixed operating costs** (software, any staff time, etc.) are a business-level question, not a
  per-SKU one, and are likewise not included — see the approval packet's business-level note.
- Shipping cost is included in "landed cost" where the supplier publishes one; where it doesn't
  (UCALLA), that is called out explicitly rather than guessed.

## 1. BrydealoFactory — landed cost $169 (low) / $304 (mid) / $439 (high)
Wholesale $129–$399 (VERIFIED) + ~$40 shipping (mid of the $35–50/style VERIFIED range).

| Retail strategy | Price (mid-cost SKU) | Payment fee | Contribution | Margin % (before returns/CAC) | ≥20% net-margin gate? |
|---|---|---|---|---|---|
| 3.0× full price | $912.00 | $26.75 | $581.25 | 63.7% | Pass |
| 10% off | $820.80 | $24.10 | $492.70 | 60.0% | Pass |
| 20% off | $729.60 | $21.46 | $404.14 | 55.4% | Pass |
| 25% off | $684.00 | $20.14 | $359.86 | 52.6% | Pass |
| 30% off | $638.40 | $18.81 | $315.59 | 49.4% | Pass |
| 2.75× full price (for comparison) | $836.00 | $24.55 | $507.45 | 60.7% | Pass |

**Return stress test (the actual gating issue, per the research's documented terms):** BrydealoFactory's
own wholesale return policy is **store-credit-only, 35% restocking fee, all freight charged to the
buyer** (VERIFIED). Modeling a worst case where Luzilly refunds its own customer in cash and sends the
gown back: cash lost ≈ sunk landed cost ($304) + sunk payment fee (~$27, not refunded by the processor)
+ return freight (~$40) ≈ **$371 cash-negative per returned unit**, offset only by ~$198 in **non-cash**
store credit (65% of $304) usable solely on a future Brydealo order — i.e., a returned order and a kept
order are roughly a **$952 swing** in outcome ($581 contribution vs. −$371 cash) at full price.
- At a 10% return rate: blended contribution ≈ $486/order ≈ **53.3%** of sale price — still clears 20%.
- At a 25% return rate: blended contribution ≈ $343/order ≈ **37.6%** of sale price — still clears 20%.
- The margin math clears the gate even under stress; **the real problem is qualitative, not
  arithmetic**: every return converts a customer's cash expectation into Luzilly eating a documented,
  quantifiable loss with no cash recovery path — which is exactly why Section 5 of the main report
  flags this as a YELLOW, not GREEN, supplier regardless of how the numbers run.

## 2. 1stopbridal — landed cost $155 (low) / $295 (mid) / $435 (high)
Wholesale $120–$400 (VERIFIED) + $20–50/dress shipping (mid ~$35, VERIFIED).

| Retail strategy | Price (mid-cost SKU) | Payment fee | Contribution | Margin % (before returns/CAC) | ≥20% net-margin gate? |
|---|---|---|---|---|---|
| 3.0× full price | $885.00 | $26.07 | $563.93 | 63.7% | Pass |
| 10% off | $796.50 | $23.40 | $478.10 | 60.0% | Pass |
| 20% off | $708.00 | $20.83 | $392.17 | 55.4% | Pass |
| 25% off | $663.75 | $19.55 | $349.20 | 52.6% | Pass |
| 30% off | $619.50 | $18.27 | $306.23 | 49.4% | Pass |

**Return stress test — disqualifying, not just risky.** 1stopbridal **publishes no return, refund, or
defect policy of any kind** (VERIFIED absence). Modeled worst case: a return gives Luzilly **$0 recovery
of any kind** — no store credit, no stated refund path, nothing — meaning a returned order costs the
full landed cost ($295) plus the full customer refund plus the sunk payment fee, with **no documented
ceiling on the loss**. Even a single-digit return rate erodes the otherwise-healthy margins above
quickly, and because there is no written mechanism, Luzilly cannot even bound the exposure the way it
can for BrydealoFactory. **This is independent confirmation of the main report's RED classification —
the pricing looks fine in isolation, but the undocumented return path makes the SKU un-model-able, not
just unfavorable.**

## 3. UCALLA (plus-size line only) — wholesale $200–$350 (mid)–$500; shipping UNKNOWN
**Shipping cost to the US was not published anywhere on UCALLA's site (UNKNOWN)** — the figures below
use wholesale cost alone and therefore overstate the true margin; subtract actual shipping once known.

| Retail strategy | Price (mid wholesale $350) | Payment fee | Contribution (wholesale-only) | Margin % (before shipping/returns/CAC) |
|---|---|---|---|---|
| 3.0× full price | $1,050.00 | $30.75 | $669.25 | 63.7% |
| 30% off | $735.00 | $21.62 | $363.38 | 49.4% |

**Return stress test — bounded but wide.** UCALLA's return policy (30 days, buyer's remorse accepted,
refund to original payment method — VERIFIED) is the most customer-friendly *wording* of the three, but
**restocking fee and who pays return shipping are both unpublished (UNKNOWN)**. Two bounding scenarios:
- **Best case** (no restocking fee, UCALLA absorbs return shipping): a return costs Luzilly little beyond
  the original payment-processing fee — genuinely workable.
- **Conservative case** (Luzilly pays return freight on a gown shipped back to Suzhou, China, plausibly
  $40–80 given the outbound-shipping pattern of comparable China-based suppliers, plus an unknown
  restocking fee): exposure could resemble BrydealoFactory's, or worse, depending on the actual fee.
Because this is a **genuine unknown, not a documented bad term**, UCALLA is rated YELLOW rather than RED
— but the true margin cannot be finalized until both the shipping cost and the restocking-fee/return-
shipping-payer questions (already listed in the main report's Section 6 gaps) come back in writing.

## Bottom line for the approval packet
All three suppliers' **pricing** supports a 3.0x (or discounted-down-to-30%-off) strategy well above
the 20% net-margin floor **before** returns, advertising, and fixed costs are layered in. The gating
issue for every single one is **documented or undocumented return-cost recovery**, not the headline
markup — which is exactly why none of them clears GREEN. Resolving the Section 6 follow-up questions
(restocking fee, who pays return shipping, UCALLA's shipping cost) would let this model collapse from
a "best case / worst case" range into a single real number per supplier.
