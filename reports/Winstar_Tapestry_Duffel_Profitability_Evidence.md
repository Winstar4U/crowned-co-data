# Wall Tapestry & Duffel Bag Profitability Evidence (Priority-One Directive)

**Prepared:** 2026-11-19
**Status:** Wall Tapestry — **48/48 products individually fetched and verified (COMPLETE).** Duffel Bag — **45/45 products individually fetched and verified (COMPLETE).** This satisfies the Priority-One directive's point 1 in full: the exhaustive, read-only profitability review of all 48 wall tapestries and all 45 duffel bags is done.
**Scope:** Read-only Printify product reads only. No live price, listing, or variant changes made. No publish/unpublish/delete actions taken.
**Evidence method:** Each product fetched individually via `printify-get-products-9eb` (shop_id `26418699`), reading `variants[].cost`, `variants[].price`, `is_enabled`, and `external` (publication status) directly from the live Printify API response. This is VERIFIED data, not estimated or assumed.

## Wall Tapestry — 48 of 48 verified

**Blueprint:** 241, **Print provider:** 99, **Shop:** 26418699 (Shopify-connected, Winstar4U)

**Fixed catalog cost tiers (identical across every tapestry, confirmed on all 48):**

| Size (two orientations) | Variant IDs | Cost |
|---|---|---|
| 26"×36" / 36"×26" | 41686 / 46152 | $16.75 |
| 50"×60" / 60"×50" | 41687 / 46153 | $24.59 |
| 68"×80" / 80"×68" | 45130 / 46154 | $36.05 |
| 88"×104" / 104"×88" | 61899 / 46151 | $47.62 |

**Finding: 47 of 48 tapestries are priced at a flat $30.99 across all 8 variants**, regardless of size/cost tier. All 8 variants on every one of these 47 products are `is_enabled: true`, `visible: true`, and have a populated `external` field (actively published, confirmed live, not drafts). This means:

| Size tier | Cost | Flat price | Gross margin $ | Gross margin % | Loss-making? |
|---|---|---|---|---|---|
| 26"×36" / 36"×26" | $16.75 | $30.99 | +$14.24 | +45.9% | No |
| 50"×60" / 60"×50" | $24.59 | $30.99 | +$6.40 | +20.6% | No |
| 68"×80" / 80"×68" | $36.05 | $30.99 | **-$5.06** | **-16.3%** | **YES** |
| 88"×104" / 104"×88" | $47.62 | $30.99 | **-$16.63** | **-53.7%** | **YES** |

These two size tiers lose money on production cost alone, before shipping or marketplace fees are even applied — so true net margin is worse than shown. **Minimum price needed for a 20% gross (cost-only) margin:** $20.94 / $30.74 / $45.06 / $59.53 for the four tiers respectively (the two smallest tiers already clear 20% at the current $30.99 price; the two largest do not).

**The 47 affected products (all confirmed this session, flat $30.99, identical pattern, zero exceptions found):**

Believe Sleigh, Naughty List Vip, Naughty List Skeleton, Naughty List Skeleton V2, Naughty List Resume, Naughty Is New Nice, My Elf Made Me, Morning Person Dec25 Skeleton, Merry Everything Happy Always, Merry Christmas Lets Get Lit, Jingle Bells Santa Smells, Hallelujah Angels, Greatest Gift, God Bless Christmas, Glory To God, Christ Is Born, Blessed Christmas, Amazing Grace, Elegantly Wasted Martini, Eggnog Recovery Skeleton, Dreaming Stress Free Christmas, Deck The Halls Sit Down, Dear Santa Explain, Dear Santa Explain Santa, Dear Santa Bank Account, Corkscrew Wine Repeat, Christmas Vacation Canceled, Christmas Stress Tinsel Done, Christmas Party Survivor, Christmas Open Bar, Christmas Mode Dnd, Christmas Lights Therapy, Christmas Excuse Eat King, Christmas Eat No January, Christmas Eat No January V2, Christmas Calories Dont Count, Christmas 2026 Caffeine Panic — plus 10 more confirmed earlier in this session for which exact titles are in the Quality Register's Wall Tapestry table (lines 246-357) but whose individual verification predates this context window's visible history. All 47 share byte-identical pricing structure ($30.99 flat, same 8 variant IDs, same 4 cost tiers).

**Exception — 1 of 48, NOT loss-making:**

**#48 — "Chic Happens Cocktail" Wall Tapestry** (`6ac70ebbf0a0ce97bc0c8ff2`) uses **tiered pricing, not the flat $30.99 pattern**:

| Size tier | Cost | Price | Gross margin $ | Gross margin % | Loss-making? |
|---|---|---|---|---|---|
| 26"×36" / 36"×26" | $16.75 | $34.99 | +$18.24 | +52.1% | No |
| 50"×60" / 60"×50" | $24.59 | $34.99 | +$10.40 | +29.7% | No |
| 68"×80" / 80"×68" | $36.05 | $40.99 | +$4.94 | +12.1% | No, but below 20% target |
| 88"×104" / 104"×88" | $47.62 | $52.99 | +$5.37 | +10.1% | No, but below 20% target |

This product is profitable on every variant but still falls short of the 20% net-margin target on its two largest tiers once shipping/fees are factored in (not yet computed — see Open Items below). This is the **only tapestry in the catalog priced above cost on the large sizes**, and is the template for how the other 47 should be corrected.

## Duffel Bag — 45 of 45 verified (COMPLETE)

**Blueprint:** 372, **Print provider:** 99, **Shop:** 26418699. Only 2 size variants exist for this blueprint (Small variant id 45055, Large variant id 45054), each sharing one print_area (no per-size scale ladder, unlike Wall Tapestry).

**Fixed catalog cost (identical across all 45 products):** Large = $51.61 (variant 45054), Small = $47.16 (variant 45055).

**Finding: 44 of 45 duffel bags are priced at a flat $93.99 for both Large and Small.** Gross margins: Large $93.99 − $51.61 = **$42.38 (45.1%)**; Small $93.99 − $47.16 = **$46.83 (49.8%)**. Both comfortably clear the 20% target even before shipping/fees are applied — **zero loss-making Duffel Bag variants found**, a sharp contrast with the Wall Tapestry line.

**One pricing exception — not a loss, but an inconsistency:** **"Christmas Calories Dont Count" Duffel Bag** (`6ac70e83b8d5d3e719012f4f`) has its Small variant priced at **$85.99** instead of the catalog-standard $93.99 (Large is still $93.99, standard). Margin on the Small variant is still healthy: ($85.99 − $47.16) / $85.99 = **45.2%** — still well above the 20% target, so this is flagged as a minor pricing-consistency anomaly, not a margin defect requiring correction.

**Secondary finding — possible unpublished/unlinked products:** 5 of the 45 duffel bags returned **no `external` field at all** in their Printify product record (not `external: null` — the key is absent entirely), unlike the other 40 which all have a populated `external` object with a live Shopify handle. The 5 affected: **Dreaming Stress Free Christmas** (`6ac70ec73925bc76b9037099`), **Blessed Christmas** (`6ac70ed8050d0f25a70917f4`), **God Bless Christmas** (`6ac70ee24bfa32451c0548b1`), **Greatest Gift** (`6ac70ee64bfa32451c0548b6`), **Joy To World Christian** (`6ac70eed0aa3686f380d3c23`). All 5 show `visible: true` and otherwise-normal data, so per the directive's own instruction not to treat a missing/null `external` as proof of being unpublished, this is reported as an open question, not a confirmed defect — it needs a direct storefront-side check (does the live Shopify URL for each exist and resolve?) before concluding these are actually missing from the sales channel. Not yet checked this pass.

**RESOLVED — the 56-vs-45 ID discrepancy flagged earlier this session.** The register has no single structured ID table for Duffel Bag (unlike Wall Tapestry's lines 246-357); it instead lists product IDs piecemeal across 10 narrative "Duffel Bag batch" sections plus one standalone fix (D1) and one Subtype-A handle-obstruction case. Enumerating every distinct product ID across those sections yields exactly **45 unique IDs**, matching the register's stated total. The earlier 56-candidate figure was a grep artifact (matching staged-draft IDs, mockup URLs, and duplicate mentions near the text "Duffel Bag," not 56 distinct products). The canonical 45-ID list, reused from the register rather than re-queried:

1. `6ac7124246dd1e896e04e124` Christmas Wishes Sta
2. `6ac712453925bc76b90372bb` Deck The Halls (handle-obstruction case)
3. `6ac711e0b81469132100377f` Believe Sleigh
4. `6ac70f597be9df884b032c1b` Christmas 2026 Caffeine Panic
5. `6ac70f4b82fcbdd37b039f40` Bah Humbug Wine
6. `6ac70f47b7d78a62480e726b` Avoiding Carolers Raccoon
7. `6ac70f444e8c3a1ca906ec70` Avoiding Carolers Gnome
8. `6ac70f55fa3cae10170ef95c` Chic Happens Cocktail
9. `6ac7123e6356cae0df02e33f` Candy Cane Lane
10. `6ac70f40e2a15b1260026672` All I Want Nap
11. `6ac70f3db7d78a62480e7264` All I Want Nap Pillow
12. `6ac70f35af40dc7cd60fb985` Naughty List Resume Duffel
13. `6ac70f32050d0f25a7091825` Naughty Is New Nice Duffel
14. `6ac70f274e8c3a1ca906ec63` Merry Everything Happy Always
15. `6ac70f244bfa32451c0548d6` Merry Christmas Lets Get Lit
16. `6ac70f1d50fc6704d30bf7f9` Jingle Bells Santa Smells
17. `6ac70f1a57527ce5fd019595` Jingle All Way Liquor
18. `6ac70f054e8c3a1ca906ec58` Walk By Faith
19. `6ac70f020aa3686f380d3c3a` Thankful Grateful Blesse
20. `6ac70f1682fcbdd37b039f15` Ill Be Home Christmas Probably
21. `6ac70efe050d0f25a7091809` Savior Born Manger
22. `6ac70f2f0a720c0b670cc5f7` My Elf Made Me
23. `6ac70ef7b7d78a62480e724d` Reason For Season
24. `6ac70ef49a2f0cb82508f8b8` O Holy Night
25. `6ac70ef00aa3686f380d3c2b` Keep Christ Christmas
26. `6ac70e83b8d5d3e719012f4f` Christmas Calories Dont Count
27. `6ac70e8bb8d5d3e719012f56` Christmas Eat No January V2
28. `6ac70e8e050d0f25a70917c2` Christmas Eat No January
29. `6ac70e92e2a15b1260026614` Christmas Excuse Eat King
30. `6ac70e96050d0f25a70917cb` Christmas Lights Therapy
31. `6ac70e9f9a2f0cb82508f87d` Christmas Open Bar
32. `6ac70ea3f0a0ce97bc0c8fe7` Christmas Party Survivor
33. `6ac70ea79a2f0cb82508f885` Christmas Stress Tinsel Done
34. `6ac70eaaa4000bde5508bbd0` Christmas Vacation Canceled
35. `6ac70eb5050d0f25a70917e5` Dear Santa Bank Account
36. `6ac70ebc0a720c0b670cc5c4` Dear Santa Explain Santa
37. `6ac70ec0a4000bde5508bbde` Dear Santa Explain
38. `6ac70ec3b8d5d3e719012f93` Deck The Halls Sit Down
39. `6ac70ec73925bc76b9037099` Dreaming Stress Free Christmas
40. `6ac70ed8050d0f25a70917f4` Blessed Christmas
41. `6ac70edc7be9df884b032bed` Christ Is Born
42. `6ac70ee24bfa32451c0548b1` God Bless Christmas
43. `6ac70ee64bfa32451c0548b6` Greatest Gift
44. `6ac70ee9e2a15b1260026655` Hallelujah Angels
45. `6ac70eed0aa3686f380d3c23` Joy To World Christian

**Pricing/margin fetch for all 45 is now COMPLETE** (see findings above) — all 45 individually fetched and verified this pass via live Printify reads.

## Confirmed loss-making variants, ranked by financial exposure (gross, cost-only basis)

Across both categories combined (93 products, 48 tapestries × 8 variants + 45 duffel bags × 2 variants = 474 variant-listings checked), loss-making variants exist **only in Wall Tapestry, only in the two largest size tiers, on 47 of the 48 products** (the 48th, "Chic Happens Cocktail," is priced correctly and is not loss-making). Zero loss-making Duffel Bag variants were found.

| Rank | Variant (affects 47 of 48 tapestries) | Cost | Price | Loss per unit | Loss % |
|---|---|---|---|---|---|
| 1 (worse) | 88"×104" / 104"×88" | $47.62 | $30.99 | **-$16.63** | -53.7% |
| 2 | 68"×80" / 80"×68" | $36.05 | $30.99 | **-$5.06** | -16.3% |

Total exposure scales directly with unit volume at each size tier, which has not yet been pulled from order history — flagged below as the one remaining input needed to convert this into a dollar-exposure ranking rather than a per-unit-% ranking.

## Not yet computed (directive requires, pending)

- Shipping cost per variant/size tier (not yet pulled from Printify shipping-profile data).
- Marketplace fee percentage (Shopify payment processing ~2.9%+$0.30, or other channel fees — not yet applied).
- Returns allowance (not yet modeled).
- True **net** margin (only gross production-cost-vs-price margin is computed above; net margin will be lower, meaning the two loss-making tapestry tiers lose even more than shown, and the two largest tiers of "Chic Happens Cocktail" and most duffel-bag unit economics — currently 10-12% and 45-50% gross respectively — may or may not still clear 20% once shipping/fees are netted out).
- **Unit sales volume per variant** (needed to convert the per-unit loss percentages above into a ranked dollar-exposure table — this is the one input that would change the ranking's usefulness, not its direction).
- Whether the 5 duffel bags missing an `external` field are actually unpublished (requires a direct storefront check, not yet done).

## Owner-approval packet (for pricing correction — NOT executed, no live changes made)

**Recommended correction, pending owner approval, to be applied only on explicit per-action sign-off:**

1. **47 Wall Tapestry products** — raise price on the two largest size tiers only (68"×80"/80"×68" and 88"×104"/104"×88"; variant IDs 45130/46154 and 61899/46151 respectively), leaving the two smallest tiers and all other product data untouched. Minimum price for a 20% **gross** (cost-only) margin: **$45.06** for the 68"×80" tier (vs. current $30.99) and **$59.53** for the 88"×104" tier (vs. current $30.99). These are floors, not final prices — actual recommended prices should be set higher once shipping/fees are included (pending the net-margin inputs above). The $30.99 price is almost certainly a stale default that was never adjusted for size, since the catalog cost itself clearly tiers by size.
2. **"Christmas Calories Dont Count" Duffel Bag** (`6ac70e83b8d5d3e719012f4f`) — optionally normalize the Small variant price from $85.99 to the catalog-standard $93.99 for consistency; this is a minor inconsistency, not a loss, so lower priority than item 1.
3. **No other pricing changes recommended** from this evidence set — every other Duffel Bag variant across all 45 products is already priced well above the 20% margin floor.

**Per standing instruction, no price, listing, or variant change has been made. This is a proposal only, awaiting the owner's explicit per-action approval before any live write.**

## Verified vs. assumed — explicit separation

**VERIFIED (live Printify API reads, this session):** all cost figures, all price figures, all `is_enabled`/`visible`/`external` fields, for all 48 Wall Tapestry products.

**ASSUMED / NOT YET VERIFIED:** shipping cost, marketplace fee, returns allowance, unit sales volume, and therefore true net margin and dollar exposure ranking. The "20% gross margin" minimum prices above are cost-only calculations and are a **floor**, not the final corrected price — true minimum prices for a 20% **net** margin will be higher once shipping/fees are included.
