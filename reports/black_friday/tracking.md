# Winstar4U Black Friday 2026: UTM tracking scheme. DRAFT.

These are links only. No link shortener, analytics tool or ad account was created or touched.

## Parameters

| Parameter | Rule | Values |
|---|---|---|
| `utm_source` | The platform the click comes from | `pinterest`, `instagram`, `facebook`, `tiktok`, `youtube` |
| `utm_medium` | The type of placement | `pin` (Pinterest), `social` (organic feed post), `story` (IG/FB story), `bio` (link in bio), `short_video` (TikTok/YT Shorts) |
| `utm_campaign` | One campaign for the whole wave | `bf2026_wave1` |
| `utm_content` | Product slug, then `_`, then the asset ID from the copy files | for example `teacher-christmas-squad-shirt_pin01`, `_ig06`, `_vid05` |
| `utm_term` | Not used. Organic only, no paid keywords | none |

**Rules:**
- Lowercase only. Use hyphens inside values and underscores between the slug and the asset ID.
- Don't put personal data or customer details in parameters.

## Where the data shows up (and its limits)

- **Shopify (Winstar4U):** Analytics shows sessions and sales by UTM (Reports, then sessions/sales by referrer and UTM). This is the most reliable channel to measure.
- **Etsy:** listing URLs accept these parameters, but Etsy Stats reports traffic sources only roughly (for example "Social media", "Pinterest"). It does not report a full `utm_campaign` breakdown.
  - Use `utm_content` mainly to compare assets where Etsy exposes it.
  - Otherwise rely on Etsy Stats per listing, comparing Nov 20–30 with the prior period.
- **Etsy Offsite Ads:** do not use Etsy-generated ad links. Organic social clicks to Etsy are not Offsite Ads charges, but Etsy's own off-site advertising is (12–15% fee; not in the margin model).
- **Link-in-bio:** if one link-in-bio page is used, tag it once with `utm_source=instagram&utm_medium=bio&utm_content=linkinbio`. Then tag each product link on that page as below.

## Example tagged links

All links are built from the `channel_link` column in `shortlist.csv`, which comes from the register. They were not re-checked live.

| Rank | Asset | Tagged link |
|---|---|---|
| 1 | pinterest/pin01 | https://www.etsy.com/listing/4617444146/teacher-christmas-squad-shirt-teacher?utm_source=pinterest&utm_medium=pin&utm_campaign=bf2026_wave1&utm_content=teacher-christmas-squad-shirt_pin01 |
| 2 | pinterest/pin02 | https://www.etsy.com/listing/4617434789/santas-favorite-nurse-christmas-shirt?utm_source=pinterest&utm_medium=pin&utm_campaign=bf2026_wave1&utm_content=santa-s-favorite-nurse-christmas-shirt_pin02 |
| 2 | instagram/ig01 | https://www.etsy.com/listing/4617434789/santas-favorite-nurse-christmas-shirt?utm_source=instagram&utm_medium=social&utm_campaign=bf2026_wave1&utm_content=santa-s-favorite-nurse-christmas-shirt_ig01 |
| 3 | instagram/ig02 | https://www.etsy.com/listing/4617454435/golden-retriever-christmas-shirt-golden?utm_source=instagram&utm_medium=social&utm_campaign=bf2026_wave1&utm_content=golden-retriever-christmas-shirt_ig02 |
| 3 | tiktok/vid03 | https://www.etsy.com/listing/4617454435/golden-retriever-christmas-shirt-golden?utm_source=tiktok&utm_medium=short_video&utm_campaign=bf2026_wave1&utm_content=golden-retriever-christmas-shirt_vid03 |
| 5 | facebook/ig03 | https://www.etsy.com/listing/4617403950/highland-cow-christmas-shirt-farmhouse?utm_source=facebook&utm_medium=social&utm_campaign=bf2026_wave1&utm_content=highland-cow-christmas-shirt_ig03 |
| 5 | tiktok/vid04 | https://www.etsy.com/listing/4617403950/highland-cow-christmas-shirt-farmhouse?utm_source=tiktok&utm_medium=short_video&utm_campaign=bf2026_wave1&utm_content=highland-cow-christmas-shirt_vid04 |
| 6 | instagram/ig04 | https://www.etsy.com/listing/4617393485/books-cocoa-and-christmas-shirt-book?utm_source=instagram&utm_medium=story&utm_campaign=bf2026_wave1&utm_content=books-cocoa-and-christmas-shirt_ig04 |
| 8 | tiktok/vid02 | https://www.etsy.com/listing/4617521639/teacher-christmas-sweatshirt-teacher?utm_source=tiktok&utm_medium=short_video&utm_campaign=bf2026_wave1&utm_content=teacher-christmas-sweatshirt_vid02 |
| 9 | pinterest/pin04 | https://www.etsy.com/listing/4617521209/highland-cow-christmas-sweatshirt?utm_source=pinterest&utm_medium=pin&utm_campaign=bf2026_wave1&utm_content=highland-cow-christmas-sweatshirt_pin04 |
| 10 | pinterest/pin05 | https://www.etsy.com/listing/4617531284/cozy-season-christmas-sweatshirt-snowy?utm_source=pinterest&utm_medium=pin&utm_campaign=bf2026_wave1&utm_content=cozy-season-christmas-sweatshirt_pin05 |
| 11 | pinterest/pin03 | https://www.etsy.com/listing/4617554554/golden-retriever-christmas-hoodie-golden?utm_source=pinterest&utm_medium=pin&utm_campaign=bf2026_wave1&utm_content=golden-retriever-christmas-hoodie_pin03 |
| 13 | pinterest/pin09 | https://4juy1i-kq.myshopify.com/products/believe-sleigh-christmas-duffel-bag-durable-gym-bag-for-travelers-holiday-gift-winstar4u?utm_source=pinterest&utm_medium=pin&utm_campaign=bf2026_wave1&utm_content=believe-sleigh-christmas-duffel-bag_pin09 |
| 13 | instagram/ig07 | https://4juy1i-kq.myshopify.com/products/believe-sleigh-christmas-duffel-bag-durable-gym-bag-for-travelers-holiday-gift-winstar4u?utm_source=instagram&utm_medium=social&utm_campaign=bf2026_wave1&utm_content=believe-sleigh-christmas-duffel-bag_ig07 |
| 13 | tiktok/vid05 | https://4juy1i-kq.myshopify.com/products/believe-sleigh-christmas-duffel-bag-durable-gym-bag-for-travelers-holiday-gift-winstar4u?utm_source=tiktok&utm_medium=short_video&utm_campaign=bf2026_wave1&utm_content=believe-sleigh-christmas-duffel-bag_vid05 |
| 13 | youtube/vid05 | https://4juy1i-kq.myshopify.com/products/believe-sleigh-christmas-duffel-bag-durable-gym-bag-for-travelers-holiday-gift-winstar4u?utm_source=youtube&utm_medium=short_video&utm_campaign=bf2026_wave1&utm_content=believe-sleigh-christmas-duffel-bag_vid05 |
| 15 | instagram/ig06 | https://4juy1i-kq.myshopify.com/products/baking-spirits-bright-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt?utm_source=instagram&utm_medium=social&utm_campaign=bf2026_wave1&utm_content=baking-spirits-bright-funny-christmas-t_ig06 |
| 16 | pinterest/pin10 | https://4juy1i-kq.myshopify.com/products/introverted-but-festive-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt?utm_source=pinterest&utm_medium=pin&utm_campaign=bf2026_wave1&utm_content=introverted-but-festive-funny-christmas_pin10 |
| 17 | pinterest/pin07 | https://www.etsy.com/listing/4602602899/nurse-christmas-ornament-candy-cane?utm_source=pinterest&utm_medium=pin&utm_campaign=bf2026_wave1&utm_content=nurse-christmas-ornament_pin07 |
| 20 | pinterest/pin06 | https://www.etsy.com/listing/4602603003/pet-memorial-christmas-ornament-paw?utm_source=pinterest&utm_medium=pin&utm_campaign=bf2026_wave1&utm_content=pet-memorial-christmas-ornament_pin06 |
| 21 | pinterest/pin08 | https://www.etsy.com/listing/4603015048/nurse-fuel-christmas-mug-15oz-ceramic?utm_source=pinterest&utm_medium=pin&utm_campaign=bf2026_wave1&utm_content=nurse-fuel-christmas-mug-15oz-ceramic-co_pin08 |
| 21 | tiktok/vid01 | https://www.etsy.com/listing/4603015048/nurse-fuel-christmas-mug-15oz-ceramic?utm_source=tiktok&utm_medium=short_video&utm_campaign=bf2026_wave1&utm_content=nurse-fuel-christmas-mug-15oz-ceramic-co_vid01 |
| 22 | facebook/ig05 | https://www.etsy.com/listing/4603259618/grandma-fuel-christmas-mug-15oz-ceramic?utm_source=facebook&utm_medium=social&utm_campaign=bf2026_wave1&utm_content=grandma-fuel-christmas-mug-15oz-ceramic_ig05 |

**Template for any other shortlisted product:**
`<channel_link>?utm_source=<source>&utm_medium=<medium>&utm_campaign=bf2026_wave1&utm_content=<product-slug>_<asset-id>`

## What to read after the wave (read-only)

- Clicks, sessions and orders per `utm_content`.
- Revenue and net $ per shortlist rank, using `net_$` after the approved discount from `offers.md`.
- Which Etsy listings had sales from social sources (Etsy Stats).
