# Black Friday acceptance manifest: Etsy + Amazon (offline, nothing live changed)

Prepared 2026-11-21 (UTC). The source of truth is `manifest.csv`, one row per product. Real start and end times are in `timing.txt`.

## Count reconciliation

| Set | Source | Count |
|---|---|---|
| Wave 1, Etsy, VERIFIED LIVE | `launch/candidates.csv` ranks 1–5, 8–14, 24–26 | 15 |
| Wave 1, Amazon, VERIFIED LIVE | `launch/candidates.csv` rank 23 | 1 |
| Wave 2, Etsy, VERIFIED LIVE | `wave2/wave2_candidates.csv` | 25 |
| **Main manifest** | | **41** |
| Pending: clean Etsy hoodies, pages unverified | `wave2/etsy_uninspected.csv` | 5 (separate PENDING section) |

**Excluded:**
- 10 Shopify rows (shop 26418699, on hold).
- The Pet Memorial ornament (not live).

**Main 41 by risk tier and status:**

| Risk tier | Count | Acceptance status |
|---|---|---|
| **A** | **20** | READY FOR OWNER POSTING APPROVAL |
| **B** | **16** | READY FOR OWNER POSTING APPROVAL, with caveats |
| **C** | **5** | HOLD |
| **Total** | **41** | 36 READY + 5 HOLD |

**Tier A (20):**
- 16 $29.99 tees: 6 from wave 1, 10 from wave 2.
- 3 $24.99 tees where the buyer pays shipping.
- The Amazon Dog Mom tee.

**Tier B (16):**
- 10 crewnecks.
- 5 hoodies.
- The Christmas Calories $24.99 tee.

**Tier C (5):**
- 3 ornaments: 16.6% net with seller-paid shipping, ship from the UK, add-on only.
- Opening Night tee: IP review.
- Cookie Dealer tee: IP and brand-safety review.

**PENDING (5 hoodies), all tier B on margin:**
- Nurse hoodie 6af90bdec745d035040e95ab: Etsy page **verified live today**. Still held until the owner adds it to a wave.
- Cat Mom, Cozy Season, Gardeners and Teacher hoodies: page not verified. HOLD.

**Tier rules:**
- **A:** clean, LOW IP, and at least 20% on the worst size with 12% Offsite.
- **B:** at least 20% at regular price, but the worst size or an Offsite-attributed order falls below.
- **C:** hold.

## Quality and IP

**Quality:**
- None of the 46 products has a row in `master_defects.csv`.
- **Etsy:** all 40 main Etsy products are CLEAN in the per-product tables of `Winstar_Five_Shop_Quality_Register.md`.
- **Amazon:** the shop was 62/62 visually inspected (`Winstar_Sales_Readiness_Register.csv`).
- **Pending hoodies:** 8-colour live mockups are in `wave2/evidence/`.
- **Result:** quality_status = PASS for all 46.

**IP screen:** this is general knowledge only, not legal clearance. No trademark registry was searched, and no Firecrawl search was used.

| Phrase | Screen | Reason |
|---|---|---|
| **Cookie Dealer** 6ac2f508368bb1b26d051cd7 | **REVIEW** | Drug-dealer pun (platform brand-safety). It is also a common bakery or business name, so a possible mark is unchecked. |
| **Opening Night** 6af8d6034643b0e30509224f | **REVIEW** | The phrase itself is generic, but the live title and tags say "Broadway Fan". Suggest removing "Broadway"; that edit needs approval. |
| Naughty or Nice | LOW | Traditional phrase. |
| Christmas Calories Don't Count | LOW | Common saying. |
| Nutcracker (3 products) | LOW | Public-domain story and ballet; the art is generic. |
| Dog Mom (Etsy + Amazon) | LOW | Descriptive phrase; registry unchecked. The Amazon listing is also one of an owner-kept duplicate ASIN pair. |
| Hooked on Christmas | LOW | Crochet pun; only a faint echo of "Hooked on Phonics". |

## Etsy shipping payer (task D)

Firecrawl used 12 scrapes (60 credits): 11 distinct WinstarDesigns listings plus 1 Etsy search page for task E. The log is `verification_log_shipping.csv`. Etsy rendered a $ shipping cost on only 1 page. The others showed "NOT SHOWN" or "There was a problem calculating your shipping". No page showed a free-shipping badge.

| Product type | Shipping profile (Printify `external.shipping_template_id`) | Who pays | Evidence |
|---|---|---|---|
| $24.99 tee: Firefighter, Construction, Dog Mom | 300729500105 | **BUYER, $4.95** | Shown on 4597737445; Construction and Dog Mom are **inferred** from the shared profile |
| $24.99 tee: Calories, Cookie Dealer | 299987014038 | **UNVERIFIED** | Same profile as the $29.99 tees |
| $29.99 tee | 299987014038 | **UNVERIFIED** | 3 pages, cost not rendered |
| Crewneck / hoodie | 320380366278 | **UNVERIFIED** | 4 pages, cost not rendered |
| Ornament | n/a | **UNVERIFIED** | 2 pages, cost not rendered |

**Margin effect.** Margins were recomputed only where the buyer pays, for the three profile-300729500105 tees:

| Measure | Before | After |
|---|---|---|
| Base size | 26.6% | **44.5%** |
| Worst size (3XL) | 19.2% | **35.8%** |
| Worst size with 12% Offsite | 7.2% | **21.6%** |
| Worst size with 15% Offsite | 4.2% | **18.0%** |

That moves these three tees from B to A. Everything else stays seller-pays, the conservative case. Printify still charges $5.35 to ship, so the $4.95 charge doesn't fully cover it.

**Delivery estimates:**
- **Ships from:** Hialeah, FL for apparel, the United Kingdom for ornaments.
- **Etsy page estimates if ordered 2026-11-21:**

| Product type | Estimate |
|---|---|
| $29.99 tees | Nov 27–30 or Nov 27–Dec 1 |
| $24.99 tees | Nov 27–Dec 2 or Nov 27–30 |
| Crewnecks and hoodies | Nov 24–30 |
| Ornaments | Nov 25–Dec 5 |

## Other outputs

- **Creative:**
  - `creative_tier_A.md` (20 products).
  - `creative_tier_B.md` (16 products, with caveats).
  - Both cover pins, IG/FB, TikTok/Reels and YouTube Shorts. Every asset lists its product IDs. Regular price only; no sale or scarcity wording.
- **Defect previews (task C):** `defect_previews.csv` and `defect_previews/`. Built from local evidence only; nothing applied.

| Product | Status | What the check showed |
|---|---|---|
| Dear Santa shorts 6ac70ec09a2f0cb82508f89a | **WARN** | "SAYS" contrast on Black: 1.04:1 before, 18.47:1 after. 100% inside the safe area. Shadow and Ink Blue blank colours were not measured locally. |
| Stress/Tinsel tank 6ac71018e2a15b12600266b5 | **PASS** | Worst line contrast on Black: 1.26:1 before, 7.93:1 after with the light-ink variant. 100% inside the safe area; about 177 dpi at the 300 px/in convention. The wine-glass motif keeps it out of promos. |
| Christ Is Born canvas 6ac702e21e2eac4da206fc57 | **PASS** | Inside the safe area: 81.8% before, 100% after. 128 dpi before, 171 dpi after. |
| Keep Christ canvas 6ac702d43fd8c86beb0f48b1 | **PASS** | Inside the safe area: 71.9% before, 100% after. 128 dpi before, 181 dpi after. |

- **$24.99 price options:** `price_option_2499.md`. Recommendation: +$1 on 3XL only, to $27.99, on all 5 tees (49 variants); 2XL stays. This is an owner decision; no price was changed.

## Tool use and limits

**Printify (read-only, Etsy shop 26603005 only):**
- 5 `get-products` calls for the $24.99 tees.
- 1 catalog `get-blueprint-shipping` call (blueprint 6 / provider 99; context only, not used in the margins).
- **Cached pulls reused:** costs and shipping profiles for the other 38 Etsy/Amazon products come from earlier sessions' pulls (2026-11-20/21). Earlier cached Shopify pulls in the same folder were **excluded and not used**.

**No other calls:**
- No Printify calls for shop 26418699.
- No Shopify or winstarmarketing.shop access.
- No writes, posts or spend beyond the 12 Firecrawl scrapes.
- No git.

## Owner decisions raised

1. Approve posting of Tier A (20), then Tier B (16) with caveats, product by product.
2. Confirm who pays shipping on Etsy profiles 299987014038 (tees), 320380366278 (crewnecks and hoodies) and the ornament profile. Pages didn't render a cost.
3. Cookie Dealer and Opening Night: review IP or brand safety. For Opening Night, consider dropping "Broadway" from the title and tags (live edit).
4. $24.99 tees: decide on +$1 for 3XL (49 variant price writes).
5. Pending hoodies: add the Nurse hoodie (page verified) to a wave. The other 4 need a page check first.
6. Task C fixes: approve or reject the four art or placement replacements on Shopify-shop products. They stay on hold under the Shopify freeze.

## Revision 2026-11-21 ~02:55 UTC (answers ChatGPT challenge P-1E1K2H400P)

- **Status relabel.** READY now applies only where the shipping payer was seen on the page: 1 product, the Firefighter tee, buyer pays $4.95. The rest are CONDITIONAL:
  - 2 tees where buyer-paid shipping is inferred from a shared shipping profile
  - 1 Amazon tee, where the referral fee and shipping are modelled
  - all other tier A and B products, where the shipping payer is UNVERIFIED and seller-pays is modelled
  Tier C products stay on HOLD. The 4 hoodies with unverified pages stay PENDING.
- **IP.** Every row is now marked UNVERIFIED (general-knowledge screen only, no trademark registry search). Opening Night and Cookie Dealer remain on HOLD.
- **$24.99 tees.** The current 2XL and 3XL price is **$26.99**; S to XL are $24.99, per `printify_variants_etsy_amazon.csv`.
  - So "+$1 on 3XL" means $26.99 → $27.99, and "+$2" means $28.99.
  - 49 variants are affected, all 3XL across the five tees: 10 + 10 + 16 + 6 + 7.
  - No price has been changed.
- **Offsite Ads.** Tier B falls below 18% net if Etsy's 15% Offsite Ads fee applies. No promotion of tier B until the owner confirms the account's enrollment and fee rate.
- **Evidence.** Each row's URL and check timestamp are in `manifest.csv`, with the matching `verification_log*.csv` entries in `launch/`, `wave2/` and this folder. Per-variant costs are in `printify_variants_etsy_amazon.csv`.
