# Winstar Enterprises: Owner Decision Register

**Compiled:** 2026-11-19, under the owner's Direct Execution Order. Black Friday is 2026-11-27.
**Scope:** the five Printify-connected Winstar shops only. Luzilly, Halcyon, KDP and Winstar Marketing are not touched.
**How to answer:** reply with the decision ID and your choice, for example `D1: B`, `D3: approve`, `D7: unpublish`.
Nothing below has been executed. Every item is waiting on you.

---

## D1. Wall Tapestry pricing (48 products, shop 26418699): MONEY IS BEING LOST NOW

- **Decision:** set new prices for the 48 tapestries, or turn off the two largest sizes.
- **Why it matters:** every tapestry is priced at a flat $30.99 for all 8 sizes. The two largest sizes cost more to make than they sell for:
  - 68x80 / 80x68 costs $36.05 and loses $5.06 per sale.
  - 88x104 / 104x88 costs $47.62 and loses $16.63 per sale.
  - If you also pay the shipping, 286 of the 384 size-variants lose money or fall below 20% net.
- **Affected products:** all 48 product IDs and all 384 variant IDs are in `reports/Winstar_Tapestry_Pricing_Correction_Table.csv`.

**Options:**

| Option | Price by size (small / medium / large / XL) | Result |
|---|---|---|
| A: customer pays shipping | $30.99 / $34.99 / $50.99 / $66.99 | At least 20% net on every size |
| B: Winstar pays shipping | $31.99 / $44.99 / $63.99 / $79.99 | At least 20% net on every size |
| C: turn off the 2 largest sizes, keep $30.99 | $30.99 / $30.99 / off / off | Stops the losses; drops the large-size sales |

- **Recommendation:** B if Winstar4U offers free shipping, A if customers pay shipping (see D2).
- **Approval needed:** "D1: A", "D1: B" or "D1: C".
- **What I do after approval:** set the prices on all 48 products, re-read each one from Printify to confirm, and post the evidence to the Bridge.

## D2. Who pays shipping on Winstar4U (Shopify)?

- **Why it matters:** this decides between options A and B in D1. It also changes the true margin on every Shopify product.
- **Options:** customer pays / Winstar pays (free shipping) / free shipping only above a set order total.
- **Recommendation:** tell me the current storefront setting. I can't see it from here, because the Shopify storefront and admin are blocked in this environment.
- **Approval needed:** "D2: customer pays" or "D2: free shipping".

## D3. Five duffel bags may not be listed on Shopify

- **Products** (shop 26418699, holiday designs, $93.99):
  - `6ac70ec73925bc76b9037099` Dreaming Stress Free Christmas
  - `6ac70ed8050d0f25a70917f4` Blessed Christmas
  - `6ac70ee24bfa32451c0548b1` God Bless Christmas
  - `6ac70ee64bfa32451c0548b6` Greatest Gift
  - `6ac70eed0aa3686f380d3c23` Joy To World Christian
- **Why it matters:** the artwork is fixed and margin is about 45%. But Printify has no Shopify link for these 5, so customers may not be able to buy them.
- **Options:**
  - (a) You check in Shopify admin (Products, search the titles), then I re-publish only the missing ones.
  - (b) Approve re-publishing all 5 now.
  - (c) Leave them as they are.
- **Risk:** re-publishing a product that is already listed on Shopify can create a duplicate listing. That's why (a) is safest.
- **Recommendation:** (a).
- **Approval needed:** "D3: (a)", "D3: re-publish all 5" or "D3: leave".

## D4. Ten checkerboard-background T-shirts: Printify platform conflict

- **Products** (shop 26418699):
  - `6ac356114cb82ddd30035d42`
  - `6ac3591601306e9d6b0a9e79`
  - `6ac35b8805e1de1c0a035dab`
  - `6ac35b41ebbf38f6ec068fcb`
  - `6ac3598debbf38f6ec068ec0`
  - `6ac357bca84c54ac7608ab2b`
  - `6ac35777f3e4f34bd106b543`
  - `6ac3564b2070a33916078c17`
  - `6ac35b0040c9c50ac20245c4`
  - `6ac35801f0b487d2be06631b`
- **Why it matters:** these live listings still show a gray checkerboard printed on the shirt.
  - You already approved swapping in the corrected artwork, and it is staged.
  - Printify rejects the swap because of 48 retired variant IDs stored on each product.
- **Options:**
  - (a) You submit the prepared support ticket (`reports/Printify_Support_Packet_Checkerboard_Legacy_Variants.md`). It is about 5 minutes and costs nothing.
  - (b) You try the artwork swap yourself in the Printify dashboard.
  - (c) Approve recreating the 10 as new products. This loses their listing history and reviews.
  - (d) Unpublish the 10 until fixed.
- **Recommendation:** (a) now. If there's no answer by Nov 24, choose (d) so customers don't receive defective shirts over Black Friday.
- **Approval needed:** "D4: (a)" (your action), "D4: (c)" or "D4: (d)".

## D5. Listing status on eBay, Amazon and TikTok (150 products)

- **Products:**
  - eBay: 53 products
  - Amazon: 46 products with no linked ASIN
  - TikTok: 51 products with no linked TikTok product page
  - Exact IDs are in `reports/Winstar_Sales_Readiness_Register.csv`, rows marked UNKNOWN.
- **Why it matters:** the artwork is clean on all of these, but I can't confirm customers can buy them. This environment blocks the seller dashboards, so ChatGPT can't promote them with a working link.
- **Options:** you export the active-listings list from any of the following and send the files:
  - eBay Seller Hub (Listings, then Active, then Download)
  - Amazon Seller Central (Inventory, then Manage Inventory, then Download)
  - TikTok Seller Center (Products, then Export)
  - Or tell me a channel is not in use.
- **Recommendation:** export Amazon first. Amazon already has 17 working ASINs, and the other 45 are likely quick wins.
- **Approval needed:** none. This is your action: send the exports.

## D6. Repair approval for 389 products with confirmed artwork defects

- **Products:** 388 on Shopify plus 1 on Etsy. All IDs, mockup links and defect notes are in the register CSV, rows REPAIR FIRST, flag CUSTOMER_FACING_DEFECT.
  - The main defect types are text cropped at the print edge, wraparound clipping on water bottles and socks, white-box backgrounds, and unreadable text colors.
  - 427 of all REPAIR FIRST products are holiday designs.
- **Why it matters:** these listings are live, so a customer can order a misprinted product right now. That means refunds and bad reviews over Black Friday.
- **Options:**
  - (a) Approve fixing them in batches. For each batch I correct the placement offline, check a real Printify mockup, and send you the before/after for go-live approval.
  - (b) Unpublish the worst products until they're fixed (water bottles, socks, backpacks, laptop sleeves).
  - (c) Leave them as they are.
- **Recommendation:** (a). Start with **Batch 1: three ornaments where the fix is already known**:
  - `6ad4254232b024bb32043467`: Etsy Cribbage Tree ornament, live. Scale goes from 1.45 to 0.8.
  - `6ac8f919149425f38d04bedd`: Dracula ornament.
  - `6ac8f8f29b2660e139034102`: Basic Witch ornament.
  - Then do holiday products by blueprint, worst first.
- **Approval needed:** "D6: (a), Batch 1 live edits approved" (this approves only the 3 ornaments). Later batches come back to you one by one.

## D7. TEXACO artwork on Etsy (optional revisit)

- **Product:** `6a53ee979296b919210641d5`, Matte Canvas, Framed, Etsy shop 26603005.
- **Why it matters:** you chose to keep this on 2026-11-18. TEXACO is an active registered Chevron trademark, so a takedown or account strike is possible. It is marked HOLD and excluded from all promotion lists.
- **Options:** keep it (current) / unpublish it.
- **Recommendation:** unpublish it. One canvas print isn't worth a risk to the Etsy shop.
- **Approval needed:** "D7: keep" or "D7: unpublish".

---

**While these are pending:** the work continues without needing approval.
- Fill in Shopify storefront links for the 1,602 Shopify SELL NOW products (read-only).
- Prepare corrected placements for D6 offline.
- Give ChatGPT the 131 linked holiday SELL NOW products for promotion (`reports/Winstar_Sales_Readiness_Register.md`).
