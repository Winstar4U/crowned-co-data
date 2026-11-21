# Winstar Five-Shop Sales-Readiness Register (SELL NOW / REPAIR FIRST / HOLD / UNKNOWN)

**Compiled:** 2026-11-19, under the owner's Direct Execution Order. It is built from existing inspection evidence plus a live, read-only Printify pull of the Amazon, TikTok, Etsy and Shopify catalogs taken today.
**Full per-product data:** `reports/Winstar_Sales_Readiness_Register.csv` has 3,008 rows. Each row has the product ID, shop ID, title, holiday flag, live channel link, price range, reason, proposed correction, flags and evidence pointer.
**Rebuild:** `python3 work/build_sales_register.py <dir with live Printify pulls>`.
**Owner decisions:** `reports/Winstar_Owner_Decision_Register.md` (D1–D7).
**No live changes were made to produce this.** No publishing, price, inventory or listing changes.

## Definitions (strict)

- **SELL NOW:** the artwork was confirmed clean on a real Printify mockup, and there are no open quality, IP, price-loss or fulfillment flags.
  - Etsy, Amazon, TikTok and Shopify rows also need a live channel link from Printify.
  - Shopify storefront links were pulled from Printify on 2026-11-19 (shop 26418699, all 51 pages, 2,508 products). A clean Shopify product with no storefront link is UNKNOWN, not SELL NOW.
- **REPAIR FIRST:** a confirmed, correctable problem: an artwork defect, the tapestry price loss, or the checkerboard platform block.
- **HOLD:** a serious compliance concern. Do not promote.
- **UNKNOWN:** the artwork is fine but listing status can't be confirmed, or there is no inspection evidence.
- **REMOVED:** already taken off sale by owner decision.

## Counts

| Bucket | Etsy | Amazon | eBay | TikTok | Shopify | Total |
|---|---|---|---|---|---|---|
| SELL NOW | 241 | 17 | 0 | 20 | 330 | 608 |
| REPAIR FIRST | 1 | 0 | 0 | 0 | 446 | 447 |
| HOLD | 1 | 0 | 0 | 0 | 0 | 1 |
| UNKNOWN | 53 | 46 | 53 | 51 | 1727 | 1930 |
| REMOVED | 3 | 0 | 0 | 0 | 19 | 22 |
| **Total** | 299 | 63 | 53 | 71 | 2522 | 3008 |

Margin was verified only on the tapestries (losing money on 2 of 4 sizes) and the duffels (45–50% cost-to-price). For every other product type, margin is **not yet computed** and is not claimed.

## Promotion-ready now: 348 holiday products with live, clickable links (for ChatGPT)

Etsy links are public listing pages. Amazon links are built from the ASIN Printify holds, in the form amazon.com/dp/ASIN. TikTok links are the seller-center product pages; get the public share link from TikTok Seller Center. Shopify links are the Winstar4U storefront product URLs Printify holds (4juy1i-kq.myshopify.com/products/...); the storefront itself cannot be opened from this environment, so the pages were not click-tested. **Margin caution:** the $11.99 Etsy ornaments cost about $6.31 to make plus about $6.29 to ship. They are profitable only if the customer pays shipping. Promote them only once that is confirmed (see D2). The Amazon "duplicate pair" products are both kept, per the owner's 2026-11-18 decision.

By shop: Shopify 219, Etsy 92, TikTok 20, Amazon 17.

| # | Shop | Product ID | Title | Price | Link |
|---|---|---|---|---|---|
| 1 | Amazon | `6ae2af10bcfc422d820a54c7` | Christmas Baking Crew T-Shirt / Cookie Baker Holiday Gift Tee | $27.99-$35.99 | https://www.amazon.com/dp/B0HPMZMQZ3 |
| 2 | Amazon | `6ae414e42e006c787106bd98` | Christmas Baking Crew T-Shirt / Cookie Baker Rolling Pin Recipe Card H | $24.20-$33.68 | https://www.amazon.com/dp/B0HPSQSMCQ |
| 3 | Amazon | `6ae2af11bcfc422d820a54c9` | Christmas Cookie Dealer Graphic T-Shirt / Funny Holiday Baking Cookie  | $27.99-$35.99 | https://www.amazon.com/dp/B0HPN23TVY |
| 4 | Amazon | `6adea7d6853b5615b805ead5` | Christmas Golden Retriever T-Shirt, Santa Hat and Ornament Design | $29.99-$35.99 | https://www.amazon.com/dp/B0HPN22XVP |
| 5 | Amazon | `6ae2af12bcfc422d820a54ca` | Construction Crew Christmas T-Shirt / Builder Tradesman Holiday Gift T | $27.99-$35.99 | https://www.amazon.com/dp/B0HPN1GRMX |
| 6 | Amazon | `6ae414e12e006c787106bd94` | Construction Crew Christmas T-Shirt / Hard Hat Caution Sign Holiday Gi | $27.99-$35.99 | https://www.amazon.com/dp/B0HPRZCZ7V |
| 7 | Amazon | `6ae414e32e006c787106bd96` | Cookie Dealer Christmas T-Shirt / Funny Holiday Baking Cookie Swap Gif | $24.20-$33.68 | https://www.amazon.com/dp/B0HPSQZ91Z |
| 8 | Amazon | `6ae2af13bcfc422d820a54cb` | Dear Santa I Was Goodish Christmas T-Shirt | $27.99-$35.99 | https://www.amazon.com/dp/B0HPN5V85T |
| 9 | Amazon | `6ae414e42e006c787106bd97` | Dear Santa I Was Goodish Christmas T-Shirt / Funny Naughty or Nice Gif | $24.20-$33.68 | https://www.amazon.com/dp/B0HPSGB5HG |
| 10 | Amazon | `6ae2af0ed0738075d402e2b2` | Dog Mom Christmas T-Shirt / Santa Hat Dog Holiday Gift Tee | $29.99-$35.99 | https://www.amazon.com/dp/B0HPMTHR4C |
| 11 | Amazon | `6ae414e52e006c787106bd99` | Dog Mom Christmas T-Shirt / Santa Hat Dog Pine & Holly Ribbon Holiday  | $23.61-$32.85 | https://www.amazon.com/dp/B0HPS4FTHJ |
| 12 | Amazon | `6ae414e0e88b7e964c0e72ee` | Naughty List Cat Christmas T-Shirt / Funny Cat Lover Gift Tee for Cat  | $24.20-$33.68 | https://www.amazon.com/dp/B0HPSD8268 |
| 13 | Amazon | `6ae2af15bcfc422d820a54cc` | Naughty or Nice Christmas Holiday T-Shirt | $27.99-$35.99 | https://www.amazon.com/dp/B0HPN82LRD |
| 14 | Amazon | `6ae414e22e006c787106bd95` | Naughty or Nice Christmas T-Shirt / Funny Santa's List Scroll Hexagon  | $27.99-$35.99 | https://www.amazon.com/dp/B0HPSJKC7R |
| 15 | Amazon | `6adea4fb17865a20ce04ea54` | Santa Cat Mom T-Shirt / Christmas Cat Design | $29.99-$35.99 | https://www.amazon.com/dp/B0HP8TDXHQ |
| 16 | Amazon | `6ae414e72e006c787106bd9b` | Santa's Favorite Hairstylist Christmas T-Shirt / Scissors & Comb Signp | $27.99-$35.99 | https://www.amazon.com/dp/B0HPSGKB5Z |
| 17 | Amazon | `6ae2af10bcfc422d820a54c8` | Santa’s Favorite Hairstylist Christmas T-Shirt / Hair Stylist Barber H | $27.99-$35.99 | https://www.amazon.com/dp/B0HPN87ZDX |
| 18 | Etsy | `6ad426a6236d14a85901dbdd` | 10th Anniversary Tin Star Christmas Ornament 2026 - Ceramic Holiday Tr | $11.99-$11.99 | https://www.etsy.com/listing/4598074968/10th-anniversary-tin-star-christmas |
| 19 | Etsy | `6ad4ed6d55fae0bc720d564b` | 25th Anniversary Silver Bauble Christmas Ornament 2026 - Ceramic Holid | $11.99-$11.99 | https://www.etsy.com/listing/4598055167/25th-anniversary-silver-bauble-christmas |
| 20 | Etsy | `6ad4262318e0243bd10d4b6a` | 50 Years Golden Heart Christmas Ornament 2026 - Ceramic Holiday Tree O | $11.99-$11.99 | https://www.etsy.com/listing/4598052721/50-years-golden-heart-christmas-ornament |
| 21 | Etsy | `6ad432a411e95e7c5f0ce1ea` | 5th Anniversary Wooden Heart Christmas Ornament 2026 - Ceramic Holiday | $11.99-$11.99 | https://www.etsy.com/listing/4597795464/5th-anniversary-wooden-heart-christmas |
| 22 | Etsy | `6ad4288511e95e7c5f0cdab2` | Accountant Santa Calculator Christmas Ornament 2026 - Ceramic Holiday  | $11.99-$11.99 | https://www.etsy.com/listing/4597798488/accountant-santa-calculator-christmas |
| 23 | Etsy | `6af8d5d4383728621d00df34` | Apres Ski Club Christmas Shirt, Skier Gift, Ski Lover Holiday T-Shirt, | $29.99-$35.99 | https://www.etsy.com/listing/4617426557/apres-ski-club-christmas-shirt-skier |
| 24 | Etsy | `6aa59fa32f9b5f342a0f9955` | Autumn Cozy Snowman Phone Case / Fall Pumpkin Leaves Pattern Halloween | $29.84-$33.82 | https://www.etsy.com/listing/4574071503/autumn-cozy-snowman-phone-case-fall |
| 25 | Etsy | `6ad410603af1c130250b6328` | Bah Humbug Shirt - Funny Eggnog Christmas Tee, Sarcastic Holiday Shirt | $24.99-$26.99 | https://www.etsy.com/listing/4597760192/bah-humbug-pass-the-eggnog-funny |
| 26 | Etsy | `6af90b36ca5d307abc0160a4` | Books Cocoa and Christmas Hoodie, Book Lover Christmas Hoodie, Reader  | $54.99-$60.99 | https://www.etsy.com/listing/4617554450/books-cocoa-and-christmas-hoodie-book |
| 27 | Etsy | `6af8c95cc745d035040e4b00` | Books Cocoa and Christmas Shirt, Book Lover Christmas Gift, Bookworm H | $29.99-$35.99 | https://www.etsy.com/listing/4617393485/books-cocoa-and-christmas-shirt-book |
| 28 | Etsy | `6af8ff3b6d67bf35520cb1af` | Books Cocoa and Christmas Sweatshirt, Book Lover Christmas Crewneck, R | $46.99-$59.99 | https://www.etsy.com/listing/4617521277/books-cocoa-and-christmas-sweatshirt |
| 29 | Etsy | `6ad456e49c8f61e78707bfa1` | Buffalo Plaid Ornament Phone Case / Magnetic Impact-Resistant Case, Ru | $29.95-$29.95 | https://www.etsy.com/listing/4598132067/buffalo-plaid-ornament-phone-case |
| 30 | Etsy | `6af8d8d2a62de2d61c0bff5d` | Cat Mom Christmas Shirt, Santa Hat Tabby Cat T-Shirt, Cat Lover Christ | $29.99-$35.99 | https://www.etsy.com/listing/4617444578/cat-mom-christmas-shirt-santa-hat-tabby |
| 31 | Etsy | `6af8ff826d67bf35520cb20f` | Cat Mom Christmas Sweatshirt, Santa Hat Tabby Cat Crewneck, Cat Lover  | $46.99-$59.99 | https://www.etsy.com/listing/4617521517/cat-mom-christmas-sweatshirt-santa-hat |
| 32 | Etsy | `6ade4b8dd51db081ef0e7d2c` | Cat Mom Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Tabby Cat Santa  | $17.99-$20.99 | https://www.etsy.com/listing/4603014978/cat-mom-fuel-christmas-mug-15oz-ceramic |
| 33 | Etsy | `6adbc573c2c3b6a62f0bc564` | Celestial Christmas Ornament, Blue and Silver Moon and Star, Winter Sn | $22.99-$22.99 | https://www.etsy.com/listing/4602628880/celestial-christmas-ornament-blue-and |
| 34 | Etsy | `6ad50c137e86416ffc09854a` | Cheers Dears Wine Tumbler 20oz / Retro Christmas Wine Tumbler, Holiday | $34.99-$34.99 | https://www.etsy.com/listing/4598234329/cheers-dears-wine-tumbler-20oz-retro |
| 35 | Etsy | `6adbc503ac1177c7f0102440` | Chocolate Lab Christmas Ornament 2026, Labrador Dog Mom Gift, Realisti | $22.99-$22.99 | https://www.etsy.com/listing/4602628730/chocolate-lab-christmas-ornament-2026 |
| 36 | Etsy | `6ad4116c3af1c130250b6447` | Christmas Calories Don't Count Shirt - Funny Foodie Holiday Tee, Xmas  | $24.99-$26.99 | https://www.etsy.com/listing/4597742327/christmas-calories-dont-count-funny |
| 37 | Etsy | `6ad42ff6f1aeec4b590f726e` | Christmas Cards and Holly Christmas Ornament 2026 - Ceramic Holiday Tr | $11.99-$11.99 | https://www.etsy.com/listing/4597769685/christmas-cards-and-holly-christmas |
| 38 | Etsy | `6adf9fb0c392daed6500ee05` | Christmas Coffee Club Mug - 15oz Ceramic Coffee Mug, Santa Hat Latte A | $17.99-$20.99 | https://www.etsy.com/listing/4603654757/christmas-coffee-club-mug-15oz-ceramic |
| 39 | Etsy | `6ad50c0be2ff8ddc0b0e6f3c` | Christmas Fox Scarf Phone Case / Magnetic Impact-Resistant Case, Cute  | $29.95-$29.95 | https://www.etsy.com/listing/4598154188/christmas-fox-scarf-phone-case-magnetic |
| 40 | Etsy | `6ad4213a11e95e7c5f0cd488` | Construction Worker Christmas Shirt - Funny Contractor Holiday Tee, Gi | $24.99-$26.99 | https://www.etsy.com/listing/4597770750/construction-workers-make-a-merry |
| 41 | Etsy | `6ac2f508368bb1b26d051cd7` | Cookie Dealer Funny Christmas T-Shirt - Humorous Christmas Graphic Tee | $24.99-$26.99 | https://www.etsy.com/listing/4597840318/cookie-dealer-funny-christmas-t-shirt |
| 42 | Etsy | `6adbc4e8ac1177c7f010242d` | Corgi Christmas Ornament 2026, Corgi Mom Gift, Realistic Santa Hat Por | $22.99-$22.99 | https://www.etsy.com/listing/4602602661/corgi-christmas-ornament-2026-corgi-mom |
| 43 | Etsy | `6ad424bcf1aeec4b590f68ff` | Cozy Mahjong Game Night Christmas Ornament 2026 - Ceramic Holiday Tree | $11.99-$11.99 | https://www.etsy.com/listing/4597790322/cozy-mahjong-game-night-christmas |
| 44 | Etsy | `6af8d5caca5d307abc0120fd` | Cozy Season Christmas Shirt, Snowy Window Hot Cocoa Books T-Shirt, Hyg | $29.99-$35.99 | https://www.etsy.com/listing/4617436048/cozy-season-christmas-shirt-snowy-window |
| 45 | Etsy | `6af8ffc7c745d035040e8965` | Cozy Season Christmas Sweatshirt, Snowy Window Hot Cocoa Crewneck, Coz | $46.99-$59.99 | https://www.etsy.com/listing/4617531284/cozy-season-christmas-sweatshirt-snowy |
| 46 | Etsy | `6ad50c0fc5bf429b0a083b1e` | Cozy Season Sunburst Phone Case / Magnetic Impact-Resistant Case, Retr | $29.95-$29.95 | https://www.etsy.com/listing/4598156016/cozy-season-sunburst-phone-case-magnetic |
| 47 | Etsy | `6ad50c0dc5bf429b0a083b1d` | Cute Reindeer Lights Phone Case / Magnetic Impact-Resistant Case, Fest | $29.95-$29.95 | https://www.etsy.com/listing/4598155282/cute-reindeer-lights-phone-case-magnetic |
| 48 | Etsy | `6adbc48c1406181c4108061e` | Dachshund Christmas Ornament 2026, Doxie Dog Mom Gift, Realistic Santa | $22.99-$22.99 | https://www.etsy.com/listing/4602043421/dachshund-christmas-ornament-2026-doxie |
| 49 | Etsy | `6ade4bbc3757c80615072b6d` | Dad Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Santa Hat and Plaid  | $17.99-$20.99 | https://www.etsy.com/listing/4603259656/dad-fuel-christmas-mug-15oz-ceramic |
| 50 | Etsy | `6ad4279907b78bf56e0d3d2b` | Deer Under Northern Lights Christmas Ornament 2026 - Ceramic Holiday T | $11.99-$11.99 | https://www.etsy.com/listing/4597797222/deer-under-northern-lights-christmas |
| 51 | Etsy | `6ad410763af1c130250b6337` | Dog Mom Christmas Shirt - Funny Xmas Dog Lover Tee, Paw Print Holiday  | $24.99-$26.99 | https://www.etsy.com/listing/4597761152/dog-mom-christmas-funny-christmas-t |
| 52 | Etsy | `6ade4b78813f94035306f51a` | Dog Mom Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Golden Retriever | $17.99-$20.99 | https://www.etsy.com/listing/4603014920/dog-mom-fuel-christmas-mug-15oz-ceramic |
| 53 | Etsy | `69c9ab963f8316381202b054` | Drink Drank Drunk Shirt Funny St Patricks Day Shirt Drinking Tee Shamr | $25.73-$38.73 | https://www.etsy.com/listing/4479868615/drink-drank-drunk-shirt-funny-st |
| 54 | Etsy | `6af8e0b4edd1928e090c8308` | Even Santa Needs a Paramedic Shirt, Paramedic Christmas Gift, EMT EMS  | $29.99-$35.99 | https://www.etsy.com/listing/4617463574/even-santa-needs-a-paramedic-shirt |
| 55 | Etsy | `6ac2f50abde50e6b7a0cb4a6` | Festive AF Funny Christmas T-Shirt - Humorous Christmas Graphic Tee -  | $24.99-$26.99 | https://www.etsy.com/listing/4597816661/festive-af-funny-christmas-t-shirt |
| 56 | Etsy | `6ad4105a9c8f61e787077ee9` | Firefighter Christmas Shirt - Funny Santa Rescue Tee, Gift for Firefig | $24.99-$26.99 | https://www.etsy.com/listing/4597737445/santa-called-for-backup-firefighter |
| 57 | Etsy | `6adbc4ce09f47187170ffd46` | French Bulldog Christmas Ornament 2026, Frenchie Mom Gift, Realistic S | $22.99-$22.99 | https://www.etsy.com/listing/4602345920/french-bulldog-christmas-ornament-2026 |
| 58 | Etsy | `6af8e15fedd1928e090c839f` | Frosted Star Christmas Shirt, Blue and Silver Star T-Shirt, Elegant Wi | $29.99-$35.99 | https://www.etsy.com/listing/4617465610/frosted-star-christmas-shirt-blue-and |
| 59 | Etsy | `6af8c4374643b0e30509119d` | Gardeners Grow Merry Christmas Shirt, Gardener Christmas Gift, Plant L | $29.99-$35.99 | https://www.etsy.com/listing/4617388336/gardeners-grow-merry-christmas-shirt |
| 60 | Etsy | `6af8ffb6b2e1366dcb03a161` | Gardeners Grow Merry Christmas Sweatshirt, Gardener Christmas Gift, Pl | $46.99-$59.99 | https://www.etsy.com/listing/4617531222/gardeners-grow-merry-christmas |
| 61 | Etsy | `6ad425b8236d14a85901db0e` | Golden 50th Anniversary Christmas Ornament 2026 - Ceramic Holiday Tree | $11.99-$11.99 | https://www.etsy.com/listing/4597771535/golden-50th-anniversary-christmas |
| 62 | Etsy | `6af90b5dca5d307abc0160e1` | Golden Retriever Christmas Hoodie, Golden Christmas Hoodie, Dog Mom Gi | $54.99-$60.99 | https://www.etsy.com/listing/4617554554/golden-retriever-christmas-hoodie-golden |
| 63 | Etsy | `6adbc4b3ac1177c7f01023f4` | Golden Retriever Christmas Ornament 2026, Golden Mom Gift, Realistic S | $22.99-$22.99 | https://www.etsy.com/listing/4602068546/golden-retriever-christmas-ornament-2026 |
| 64 | Etsy | `6af8e0c3a62de2d61c0c06c4` | Golden Retriever Christmas Shirt, Golden Christmas T-Shirt, Dog Lover  | $29.99-$35.99 | https://www.etsy.com/listing/4617454435/golden-retriever-christmas-shirt-golden |
| 65 | Etsy | `6af8ff5ea62de2d61c0c2d2d` | Golden Retriever Christmas Sweatshirt, Golden Christmas Crewneck, Dog  | $46.99-$59.99 | https://www.etsy.com/listing/4617521395/golden-retriever-christmas-sweatshirt |
| 66 | Etsy | `6ad431b65492c45147091870` | Golden Wedding Rings on Pine Christmas Ornament 2026 - Ceramic Holiday | $11.99-$11.99 | https://www.etsy.com/listing/4597794140/golden-wedding-rings-on-pine-christmas |
| 67 | Etsy | `6ade4bb4580ff194290bca02` | Grandma Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Santa Hat, Glass | $17.99-$20.99 | https://www.etsy.com/listing/4603259618/grandma-fuel-christmas-mug-15oz-ceramic |
| 68 | Etsy | `6af90b08c745d035040e94cf` | Highland Cow Christmas Hoodie, Farmhouse Christmas Hoodie, Highland Co | $54.99-$60.99 | https://www.etsy.com/listing/4617544987/highland-cow-christmas-hoodie-farmhouse |
| 69 | Etsy | `6af8c9bf626b8d7aa00147c2` | Highland Cow Christmas Shirt, Farmhouse Christmas T-Shirt, Highland Co | $29.99-$35.99 | https://www.etsy.com/listing/4617403950/highland-cow-christmas-shirt-farmhouse |
| 70 | Etsy | `6af8feaa383728621d010fc2` | Highland Cow Christmas Sweatshirt, Farmhouse Christmas Crewneck, Highl | $46.99-$59.99 | https://www.etsy.com/listing/4617521209/highland-cow-christmas-sweatshirt |
| 71 | Etsy | `6af90b6cca5d307abc0160ff` | Hooked on Christmas Hoodie, Crochet Christmas Hoodie, Crocheter Gift,  | $54.99-$60.99 | https://www.etsy.com/listing/4617545189/hooked-on-christmas-hoodie-crochet |
| 72 | Etsy | `6af8c97da2664d4016059f77` | Hooked on Christmas Shirt, Crochet Lover Christmas Gift, Yarn Knitting | $29.99-$35.99 | https://www.etsy.com/listing/4617393693/hooked-on-christmas-shirt-crochet-lover |
| 73 | Etsy | `6af8ff6bc745d035040e88f4` | Hooked on Christmas Sweatshirt, Crochet Christmas Crewneck, Crocheter  | $46.99-$59.99 | https://www.etsy.com/listing/4617521445/hooked-on-christmas-sweatshirt-crochet |
| 74 | Etsy | `6ad50c1233bc1400d808831d` | Made It Wine Tumbler 20oz / Funny Christmas Lights Wine Tumbler, Holid | $34.99-$34.99 | https://www.etsy.com/listing/4598158581/made-it-wine-tumbler-20oz-funny |
| 75 | Etsy | `6ad4244e9c8f61e787078f70` | Mahjong Tiles in Santa Hats Christmas Ornament 2026 - Ceramic Holiday  | $11.99-$11.99 | https://www.etsy.com/listing/4597766845/mahjong-tiles-in-santa-hats-christmas |
| 76 | Etsy | `6ade4bab580ff194290bc9f7` | Mama Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Santa Hat and Cooki | $17.99-$20.99 | https://www.etsy.com/listing/4603236981/mama-fuel-christmas-mug-15oz-ceramic |
| 77 | Etsy | `6af8d6309e4469c0080fb7bc` | Midnight Christmas Shirt, Stained Glass Moon and Stars T-Shirt, Celest | $29.99-$35.99 | https://www.etsy.com/listing/4617427597/midnight-christmas-shirt-stained-glass |
| 78 | Etsy | `6ad4281d07b78bf56e0d3d80` | Mountain Lake Pine Wreath Christmas Ornament 2026 - Ceramic Holiday Tr | $11.99-$11.99 | https://www.etsy.com/listing/4597775743/mountain-lake-pine-wreath-christmas |
| 79 | Etsy | `6af8d8af626b8d7aa001565b` | Naughty or Nice Christmas Shirt, Santa's List T-Shirt, Vintage Scroll  | $29.99-$35.99 | https://www.etsy.com/listing/4617434917/naughty-or-nice-christmas-shirt-santas |
| 80 | Etsy | `6af8c9df4643b0e305091678` | Nonna's Christmas Kitchen Shirt, Nonna Gift, Italian Grandma Christmas | $29.99-$35.99 | https://www.etsy.com/listing/4617394691/nonnas-christmas-kitchen-shirt-nonna |
| 81 | Etsy | `6adbc58f04ff64518d0e704e` | Nurse Christmas Ornament, Candy Cane Stethoscope Heart Nurse Gift, Cer | $22.99-$22.99 | https://www.etsy.com/listing/4602602899/nurse-christmas-ornament-candy-cane |
| 82 | Etsy | `6af8ff93383728621d0110c3` | Nurse Christmas Sweatshirt, Santa's Favorite Nurse Crewneck, Nurse Gif | $46.99-$59.99 | https://www.etsy.com/listing/4617531100/nurse-christmas-sweatshirt-santas |
| 83 | Etsy | `6ade4b96aa1ddebc870bedc0` | Nurse Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Stethoscope Santa  | $17.99-$20.99 | https://www.etsy.com/listing/4603015048/nurse-fuel-christmas-mug-15oz-ceramic |
| 84 | Etsy | `6af90b48948a470d5206d7db` | Nutcracker Christmas Hoodie, Nutcracker Season Hoodie, Ballet Christma | $54.99-$60.99 | https://www.etsy.com/listing/4617545065/nutcracker-christmas-hoodie-nutcracker |
| 85 | Etsy | `6adbc558bfae79f6740255ec` | Nutcracker Christmas Ornament, Jeweled Velvet Soldier Holiday Wreath,  | $22.99-$22.99 | https://www.etsy.com/listing/4602602819/nutcracker-christmas-ornament-jeweled |
| 86 | Etsy | `6af8ff4bc8d016720c098bf5` | Nutcracker Christmas Sweatshirt, Nutcracker Season Crewneck, Ballet Ch | $46.99-$59.99 | https://www.etsy.com/listing/4617521331/nutcracker-christmas-sweatshirt |
| 87 | Etsy | `6af8c9cec745d035040e4b79` | Nutcracker Season Christmas Shirt, Classic Nutcracker T-Shirt, Ballet  | $29.99-$35.99 | https://www.etsy.com/listing/4617404056/nutcracker-season-christmas-shirt |
| 88 | Etsy | `6af8d6034643b0e30509224f` | Opening Night Christmas Shirt, Theater Lover Gift, Broadway Fan Holida | $29.99-$35.99 | https://www.etsy.com/listing/4617427273/opening-night-christmas-shirt-theater |
| 89 | Etsy | `6adbc51dac1177c7f010245e` | Orange Tabby Cat Christmas Ornament 2026, Cat Mom Gift, Realistic Sant | $22.99-$22.99 | https://www.etsy.com/listing/4602068628/orange-tabby-cat-christmas-ornament-2026 |
| 90 | Etsy | `6add66f672b7b9abb209542a` | Our First Christmas Mr. & Mrs. Mug - 15oz Ceramic Coffee Mug, Newlywed | $17.99-$20.99 | https://www.etsy.com/listing/4603740852/our-first-christmas-mr-mrs-mug-15oz |
| 91 | Etsy | `6adbc5c5dc3e5f08af09eb7a` | Pet Memorial Christmas Ornament, Paw Print Angel Wings, Dog Cat Rememb | $22.99-$22.99 | https://www.etsy.com/listing/4602603003/pet-memorial-christmas-ornament-paw |
| 92 | Etsy | `6ade4bc3aa01a54ae306f9ad` | Read Sip Repeat Christmas Mug - 15oz Ceramic Coffee Mug, Book Lover Gi | $17.99-$20.99 | https://www.etsy.com/listing/4603259688/read-sip-repeat-christmas-mug-15oz |
| 93 | Etsy | `6ad4307c18e0243bd10d533d` | Reindeer Cribbage Peg Race Christmas Ornament 2026 - Ceramic Holiday T | $11.99-$11.99 | https://www.etsy.com/listing/4597792456/reindeer-cribbage-peg-race-christmas |
| 94 | Etsy | `6af8d8c0383728621d00e292` | Santa's Favorite Hairstylist Christmas Shirt, Hair Stylist Gift, Salon | $29.99-$35.99 | https://www.etsy.com/listing/4617444440/santas-favorite-hairstylist-christmas |
| 95 | Etsy | `6af8c96c2ffca93f7e0c6dce` | Santa's Favorite Mechanic Christmas Shirt, Auto Mechanic Gift, Car Guy | $29.99-$35.99 | https://www.etsy.com/listing/4617393569/santas-favorite-mechanic-christmas-shirt |
| 96 | Etsy | `6af8d89e626b8d7aa0015637` | Santa's Favorite Nurse Christmas Shirt, Nurse Christmas Gift, Stethosc | $29.99-$35.99 | https://www.etsy.com/listing/4617434789/santas-favorite-nurse-christmas-shirt |
| 97 | Etsy | `6af8c913a62de2d61c0befd3` | Santa's Got a Truck Driver Christmas Shirt, Funny Trucker Christmas Gi | $29.99-$35.99 | https://www.etsy.com/listing/4617392531/santas-got-a-truck-driver-christmas |
| 98 | Etsy | `69c9abc12f6f1849a30b5c4f` | Shamrock Shirt St Patricks Day Shirt Lucky Clover Tee Shirt Green Grap | $15.83-$21.98 | https://www.etsy.com/listing/4479872376/shamrocked-graphic-tee-minimalist-lucky |
| 99 | Etsy | `6ad4271084e559ec0e0b8e78` | Snowy Mountain Peaks Christmas Ornament 2026 - Ceramic Holiday Tree Or | $11.99-$11.99 | https://www.etsy.com/listing/4597796492/snowy-mountain-peaks-christmas-ornament |
| 100 | Etsy | `6adbc53bc2c3b6a62f0bc540` | Tartan Bow Christmas Ornament, Plaid Velvet Bow Evergreen Wreath, Heir | $22.99-$22.99 | https://www.etsy.com/listing/4602628780/tartan-bow-christmas-ornament-plaid |
| 101 | Etsy | `6af8d5b4a2664d401605a9fe` | Tartan and Tradition Christmas Shirt, Red Plaid Bow T-Shirt, Blue and  | $29.99-$35.99 | https://www.etsy.com/listing/4617435946/tartan-and-tradition-christmas-shirt-red |
| 102 | Etsy | `6adbc5aa04ff64518d0e7067` | Teacher Christmas Ornament, Jeweled Apple and Books Teacher Gift, Cera | $22.99-$22.99 | https://www.etsy.com/listing/4602602957/teacher-christmas-ornament-jeweled-apple |
| 103 | Etsy | `6af8d8912ffca93f7e0c7c2c` | Teacher Christmas Squad Shirt, Teacher Christmas Gift, Chalkboard Holi | $29.99-$35.99 | https://www.etsy.com/listing/4617444146/teacher-christmas-squad-shirt-teacher |
| 104 | Etsy | `6af8ffa7b2e1366dcb03a14e` | Teacher Christmas Sweatshirt, Teacher Christmas Squad Crewneck, Teache | $46.99-$59.99 | https://www.etsy.com/listing/4617521639/teacher-christmas-sweatshirt-teacher |
| 105 | Etsy | `6ade4ba0478a7d4f5f01f3c8` | Teacher Fuel Christmas Mug - 15oz Ceramic Coffee Mug, Apple and Holly, | $17.99-$20.99 | https://www.etsy.com/listing/4603015130/teacher-fuel-christmas-mug-15oz-ceramic |
| 106 | Etsy | `6af8e1506d67bf35520c8bea` | Tied with a Bow Christmas Shirt, Pink Satin Bow T-Shirt, Coquette Holi | $29.99-$35.99 | https://www.etsy.com/listing/4617456281/tied-with-a-bow-christmas-shirt-pink |
| 107 | Etsy | `6ac2f509bde50e6b7a0cb4a5` | Tree Rex Funny Christmas T-Shirt - Humorous Christmas Graphic Tee - Un | $24.99-$26.99 | https://www.etsy.com/listing/4597817213/tree-rex-funny-christmas-t-shirt |
| 108 | Etsy | `6af8e188edd1928e090c83ef` | Winter Garden Field Guide Christmas Shirt, Luna Moth Mushroom T-Shirt, | $29.99-$35.99 | https://www.etsy.com/listing/4617465458/winter-garden-field-guide-christmas |
| 109 | Etsy | `6af8c9ef4643b0e305091687` | Winter Herbarium Christmas Shirt, Vintage Botanical T-Shirt, Holly Pin | $29.99-$35.99 | https://www.etsy.com/listing/4617404266/winter-herbarium-christmas-shirt-vintage |
| 110 | Shopify | `6ac289e41993b4de4807c83d` | "Baking Spirits Bright" Funny Christmas T-Shirt — Humorous Christmas G | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/baking-spirits-bright-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 111 | Shopify | `6ac28d35d0995db35108e7bb` | "Chillin' With My Snowmies" Funny Christmas T-Shirt — Humorous Christm | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/chillin-with-my-snowmies-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 112 | Shopify | `6ac271aa1af637662201169e` | "Christmas Calories Are Seasonal" Funny Christmas T-Shirt — Humorous C | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/christmas-calories-are-seasonal-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 113 | Shopify | `6ac26286e31729a98d0b7b4b` | "Christmas Calories Don't Count" Funny Christmas T-Shirt — Humorous Ch | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/christmas-calories-dont-count-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 114 | Shopify | `6ac26c630b94268bbe003fb6` | "Christmas Chaos Coordinator" Funny Christmas T-Shirt — Humorous Chris | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/christmas-chaos-coordinator-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 115 | Shopify | `6ac2679941d435db210ddf31` | "Christmas Is My Cardio" Funny Christmas T-Shirt — Humorous Christmas  | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/christmas-is-my-cardio-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 116 | Shopify | `6ac277d7c3c73cbbdd01ecce` | "Christmas Is a Contact Sport" Funny Christmas T-Shirt — Humorous Chri | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/christmas-is-a-contact-sport-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 117 | Shopify | `6ac26fb2efdfdd3b9809fecd` | "Christmas Lights Are My Therapy" Funny Christmas T-Shirt — Humorous C | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/christmas-lights-are-my-therapy-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 118 | Shopify | `6ac29c71467b8d62650243a6` | "Christmas Mode On" Funny Christmas T-Shirt — Humorous Christmas Graph | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/christmas-mode-on-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 119 | Shopify | `6ac269ed1cb7ec701600669d` | "Christmas Shopping Survivor" Funny Christmas T-Shirt — Humorous Chris | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/christmas-shopping-survivor-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 120 | Shopify | `6ac291d7a01d351aa0030498` | "Cookie Dealer" Funny Christmas T-Shirt — Humorous Christmas Graphic T | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/cookie-dealer-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 121 | Shopify | `6ac27b598d5b60a1df0be02b` | "Dear Christmas, I'm Tired" Funny Christmas T-Shirt — Humorous Christm | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/dear-christmas-im-tired-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 122 | Shopify | `6ac26439c4300a8ab10a488d` | "Dear Santa, Define Good" Funny Christmas T-Shirt — Humorous Christmas | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/dear-santa-define-good-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 123 | Shopify | `6ac26ac3b2c2645b070bb055` | "Dear Santa, I Can Explain" Funny Christmas T-Shirt — Humorous Christm | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/dear-santa-i-can-explain-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 124 | Shopify | `6ac288c71993b4de4807c7dd` | "Eat, Drink & Repeat" Funny Thanksgiving T-Shirt — Humorous Thanksgivi | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/eat-drink-repeat-funny-thanksgiving-t-shirt-humorous-thanksgiving-graphic-tee-unisex-heavy-cotton-shirt |
| 125 | Shopify | `6ac2a475ba0b98f0eb050db3` | "Eat, Drink and Be Thankful" Funny Thanksgiving T-Shirt — Humorous Tha | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/eat-drink-and-be-thankful-funny-thanksgiving-t-shirt-humorous-thanksgiving-graphic-tee-unisex-heavy-cotton-shirt |
| 126 | Shopify | `6ac2a0a9869c73d60005d3e3` | "Feast Mode On" Funny Thanksgiving T-Shirt — Humorous Thanksgiving Gra | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/feast-mode-on-funny-thanksgiving-t-shirt-humorous-thanksgiving-graphic-tee-unisex-heavy-cotton-shirt |
| 127 | Shopify | `6ac2763cb9937780dd003a0b` | "Festive AF" Funny Christmas T-Shirt — Humorous Christmas Graphic Tee  | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/festive-af-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 128 | Shopify | `6ac2a309467b8d6265024700` | "Gobble Gang" Funny Thanksgiving T-Shirt — Humorous Thanksgiving Graph | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/gobble-gang-funny-thanksgiving-t-shirt-humorous-thanksgiving-graphic-tee-unisex-heavy-cotton-shirt |
| 129 | Shopify | `6ac2757ccd4d9d605e01facf` | "Holiday Hangover Club" Funny Christmas T-Shirt — Humorous Christmas G | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/holiday-hangover-club-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 130 | Shopify | `6ac2962117724158680056b7` | "Hot Mess Express" Funny Christmas T-Shirt — Humorous Christmas Graphi | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/hot-mess-express-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 131 | Shopify | `6ac2724ec3c73cbbdd01ea95` | "I Came, I Saw, I Drank" Funny Christmas T-Shirt — Humorous Christmas  | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/i-came-i-saw-i-drank-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 132 | Shopify | `6ac27ce3bf08fedc0308bf1c` | "I Survived Another Family Christmas" Funny Christmas T-Shirt — Humoro | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/i-survived-another-family-christmas-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 133 | Shopify | `6ac28a82c884c8e4fe0a1811` | "I'm Fine — Christmas Chaos" Funny Christmas T-Shirt — Humorous Christ | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/im-fine-christmas-chaos-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 134 | Shopify | `6ac285b1c0726c04480aef19` | "I'm Just Here for the Pie" Funny Thanksgiving T-Shirt — Humorous Than | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/im-just-here-for-the-pie-funny-thanksgiving-t-shirt-humorous-thanksgiving-graphic-tee-unisex-heavy-cotton-shirt |
| 135 | Shopify | `6ac26d3ab2c2645b070bb1ef` | "Introverted But Festive" Funny Christmas T-Shirt — Humorous Christmas | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/introverted-but-festive-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 136 | Shopify | `6ac2873a15e2192b3601d430` | "Leftovers Are the Real Prize" Funny Thanksgiving T-Shirt — Humorous T | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/leftovers-are-the-real-prize-funny-thanksgiving-t-shirt-humorous-thanksgiving-graphic-tee-unisex-heavy-cotton-shirt |
| 137 | Shopify | `6ac29bb8e9f108e4dd00ee08` | "Let's Get Elfed Up" Funny Christmas T-Shirt — Humorous Christmas Grap | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/lets-get-elfed-up-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 138 | Shopify | `6ac28c6fefdfdd3b980a0ada` | "Merry Christmas Y'all" Funny Christmas T-Shirt — Humorous Christmas G | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/merry-christmas-yall-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 139 | Shopify | `6ac273a5d5a92863eb0a5b5d` | "Merry Christmas, You Holiday Menace" Funny Christmas T-Shirt — Humoro | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/merry-christmas-you-holiday-menace-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 140 | Shopify | `6ac29afa1772415868005939` | "Merry Heifer" Funny Christmas T-Shirt — Humorous Christmas Graphic Te | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/merry-heifer-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 141 | Shopify | `6ac255251c5d5b7d1908fc77` | "Santa Freakin' Knows" Funny Christmas T-Shirt — Humorous Christmas Gr | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santa-freakin-knows-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 142 | Shopify | `6ac28ebcd0995db35108e8c0` | "Tree Rex" Funny Christmas T-Shirt — Humorous Christmas Graphic Tee /  | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/tree-rex-funny-christmas-t-shirt-humorous-christmas-graphic-tee-unisex-heavy-cotton-shirt |
| 143 | Shopify | `6ac712ab6027ad007d0e7ddd` | 2027 Fireworks Burst New Year 2027 Hoodie — Cozy Pullover Hoodie, New  | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/2027-fireworks-burst-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 144 | Shopify | `6ac35c5315789d66bf034f79` | Air Traffic Controllers 1 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/air-traffic-controllers-1-christmas-tee |
| 145 | Shopify | `6ac35cba01306e9d6b0aa0ec` | Air Traffic Controllers 2 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/air-traffic-controllers-2-christmas-tee |
| 146 | Shopify | `6ac70f40e2a15b1260026672` | All I Want Nap Christmas Duffel Bag — Tough Duffel for Gym & Getaways, | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/all-i-want-nap-christmas-duffel-bag-tough-duffel-for-gym-getaways-holiday-gift-winstar4u |
| 147 | Shopify | `6ac710b3fa3cae10170efa05` | All I Want Nap Christmas Fanny Pack — Stylish Hands-Free Waist Bag, Ho | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/all-i-want-nap-christmas-fanny-pack-stylish-hands-free-waist-bag-holiday-gift-winstar4u |
| 148 | Shopify | `6ac70f3db7d78a62480e7264` | All I Want Nap Pillow Christmas Duffel Bag — Holiday Travel Essential, | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/all-i-want-nap-pillow-christmas-duffel-bag-holiday-travel-essential-holiday-gift-winstar4u |
| 149 | Shopify | `6ac710a7b8d5d3e7190130bc` | All I Want Nap Pillow Christmas Fanny Pack — Trendy Festival Belt Bag, | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/all-i-want-nap-pillow-christmas-fanny-pack-trendy-festival-belt-bag-holiday-gift-winstar4u |
| 150 | Shopify | `6ac70f444e8c3a1ca906ec70` | Avoiding Carolers Gnome Christmas Duffel Bag — Roomy Gym & Travel Bag, | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/avoiding-carolers-gnome-christmas-duffel-bag-roomy-gym-travel-bag-holiday-gift-winstar4u |
| 151 | Shopify | `6ac70f47b7d78a62480e726b` | Avoiding Carolers Raccoon Christmas Duffel Bag — Spacious Weekend Trav | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/avoiding-carolers-raccoon-christmas-duffel-bag-spacious-weekend-travel-tote-holiday-gift-winstar4u |
| 152 | Shopify | `6ac70f6c4e8c3a1ca906ec85` | Avoiding Carolers Raccoon Christmas Fanny Pack — Stylish Hands-Free Wa | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/avoiding-carolers-raccoon-christmas-fanny-pack-stylish-hands-free-waist-bag-holiday-gift-winstar4u |
| 153 | Shopify | `6ac70f4b82fcbdd37b039f40` | Bah Humbug Wine Christmas Duffel Bag — Durable Gym Bag for Travelers,  | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/bah-humbug-wine-christmas-duffel-bag-durable-gym-bag-for-travelers-holiday-gift-winstar4u |
| 154 | Shopify | `6ac347cca84c54ac7608a158` | Bakers Make Merry Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/bakers-make-merry-christmas-tee |
| 155 | Shopify | `6ac711e0b81469132100377f` | Believe Sleigh Christmas Duffel Bag — Durable Gym Bag for Travelers, H | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/believe-sleigh-christmas-duffel-bag-durable-gym-bag-for-travelers-holiday-gift-winstar4u |
| 156 | Shopify | `6ac7125446dd1e896e04e131` | Believe Sleigh Christmas Fanny Pack — Chic Hands-Free Purse, Holiday G | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/believe-sleigh-christmas-fanny-pack-chic-hands-free-purse-holiday-gift-winstar4u |
| 157 | Shopify | `6ac712dea4c95c48e2036272` | Boss Of The Bird Thanksgiving Hoodie — Cozy Pullover Hoodie, Thanksgiv | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/boss-of-the-bird-thanksgiving-hoodie-cozy-pullover-hoodie-thanksgiving-gift-winstar4u |
| 158 | Shopify | `6ac3521aae872af0dc03608b` | Building Christmas Project Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/building-christmas-project-tee |
| 159 | Shopify | `6ac7123e6356cae0df02e33f` | Candy Cane Lane Christmas Duffel Bag — Durable Gym Bag for Travelers,  | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/candy-cane-lane-christmas-duffel-bag-durable-gym-bag-for-travelers-holiday-gift-winstar4u |
| 160 | Shopify | `6ac325717d5b871eff0a9ef7` | Candy Cane Stethoscope 2 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/candy-cane-stethoscope-2-christmas-tee |
| 161 | Shopify | `6ac7135f35a66ab7dc0b10a0` | Cardinal in Snow Winter Hoodie — Cozy Pullover Hoodie, Winter Gift / W | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/cardinal-in-snow-winter-hoodie-cozy-pullover-hoodie-winter-gift-winstar4u |
| 162 | Shopify | `6ac712b4fa3cae10170efaf5` | Cheers 2027 New Year 2027 Hoodie — Cozy Pullover Hoodie, New Year 2027 | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/cheers-2027-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 163 | Shopify | `6ac712a483f1a0e50d071d86` | Cheers To 2027 New Year 2027 Hoodie — Cozy Pullover Hoodie, New Year 2 | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/cheers-to-2027-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 164 | Shopify | `6ac35d1540c9c50ac202473d` | Chefs Make Merry 1 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/chefs-make-merry-1-christmas-tee |
| 165 | Shopify | `6ac35d713e6059a5f30ae3df` | Chefs Make Merry 2 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/chefs-make-merry-2-christmas-tee |
| 166 | Shopify | `6ac35dd42e807e6eea0a9dec` | Chefs Make Merry 3 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/chefs-make-merry-3-christmas-tee |
| 167 | Shopify | `6ac70f55fa3cae10170ef95c` | Chic Happens Cocktail Christmas Duffel Bag — Tough Duffel for Gym & Ge | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/chic-happens-cocktail-christmas-duffel-bag-tough-duffel-for-gym-getaways-holiday-gift-winstar4u |
| 168 | Shopify | `6ac70f7a0c643bdff309d4cf` | Chic Happens Cocktail Christmas Fanny Pack — Hands-Free Holiday Crossb | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/chic-happens-cocktail-christmas-fanny-pack-hands-free-holiday-crossbody-holiday-gift-winstar4u |
| 169 | Shopify | `6ac7137ad9b782898109a9d6` | Chill Penguin Winter Hoodie — Cozy Pullover Hoodie, Winter Gift / Wins | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/chill-penguin-winter-hoodie-cozy-pullover-hoodie-winter-gift-winstar4u |
| 170 | Shopify | `6ac70edc7be9df884b032bed` | Christ Is Born Christmas Duffel Bag — Roomy Gym &amp; Travel Bag, Holi | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/christ-is-born-christmas-duffel-bag-roomy-gym-amp-travel-bag-holiday-gift-winstar4u |
| 171 | Shopify | `6ac70f597be9df884b032c1b` | Christmas 2026 Caffeine Panic Christmas Duffel Bag — Roomy Gym & Trave | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/christmas-2026-caffeine-panic-christmas-duffel-bag-roomy-gym-travel-bag-holiday-gift-winstar4u |
| 172 | Shopify | `6ac70e83b8d5d3e719012f4f` | Christmas Calories Dont Count Christmas Duffel Bag — Spacious Weekend  | $85.99-$93.99 | https://4juy1i-kq.myshopify.com/products/christmas-calories-dont-count-christmas-duffel-bag-spacious-weekend-travel-tote-holiday-gift-winstar4u |
| 173 | Shopify | `6ac70e8e050d0f25a70917c2` | Christmas Eat No January Christmas Duffel Bag — Perfect Carry-On Weeke | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/christmas-eat-no-january-christmas-duffel-bag-perfect-carry-on-weekender-holiday-gift-winstar4u |
| 174 | Shopify | `6ac70e8bb8d5d3e719012f56` | Christmas Eat No January V2 Christmas Duffel Bag — Durable Gym Bag for | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/christmas-eat-no-january-v2-christmas-duffel-bag-durable-gym-bag-for-travelers-holiday-gift-winstar4u |
| 175 | Shopify | `6ac70e92e2a15b1260026614` | Christmas Excuse Eat King Christmas Duffel Bag — Holiday Travel Essent | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/christmas-excuse-eat-king-christmas-duffel-bag-holiday-travel-essential-holiday-gift-winstar4u |
| 176 | Shopify | `6ac70e96050d0f25a70917cb` | Christmas Lights Therapy Christmas Duffel Bag — Tough Duffel for Gym & | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/christmas-lights-therapy-christmas-duffel-bag-tough-duffel-for-gym-amp-getaways-holiday-gift-winstar4u |
| 177 | Shopify | `6ac70ff0f0a0ce97bc0c9079` | Christmas Lights Therapy Christmas Fanny Pack — Stylish Hands-Free Wai | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/christmas-lights-therapy-christmas-fanny-pack-stylish-hands-free-waist-bag-holiday-gift-winstar4u |
| 178 | Shopify | `6ac70e9f9a2f0cb82508f87d` | Christmas Open Bar Christmas Duffel Bag — Spacious Weekend Travel Tote | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/christmas-open-bar-christmas-duffel-bag-spacious-weekend-travel-tote-holiday-gift-winstar4u |
| 179 | Shopify | `6ac70ff77be9df884b032c51` | Christmas Open Bar Christmas Fanny Pack — Concert-Ready Waist Pack, Ho | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/christmas-open-bar-christmas-fanny-pack-concert-ready-waist-pack-holiday-gift-winstar4u |
| 180 | Shopify | `6ac33e3293e5fb657309843e` | Christmas Pajamas Woman Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/christmas-pajamas-woman-tee |
| 181 | Shopify | `6ac70ea3f0a0ce97bc0c8fe7` | Christmas Party Survivor Christmas Duffel Bag — Durable Gym Bag for Tr | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/christmas-party-survivor-christmas-duffel-bag-durable-gym-bag-for-travelers-holiday-gift-winstar4u |
| 182 | Shopify | `6ac70ea79a2f0cb82508f885` | Christmas Stress Tinsel Done Christmas Duffel Bag — Perfect Carry-On W | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/christmas-stress-tinsel-done-christmas-duffel-bag-perfect-carry-on-weekender-holiday-gift-winstar4u |
| 183 | Shopify | `6ac70eaaa4000bde5508bbd0` | Christmas Vacation Canceled Christmas Duffel Bag — Holiday Travel Esse | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/christmas-vacation-canceled-christmas-duffel-bag-holiday-travel-essential-holiday-gift-winstar4u |
| 184 | Shopify | `6ac7124246dd1e896e04e124` | Christmas Wishes Sta Christmas Duffel Bag — Perfect Carry-On Weekender | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/christmas-wishes-sta-christmas-duffel-bag-perfect-carry-on-weekender-holiday-gift-winstar4u |
| 185 | Shopify | `6ac7125b2d1baaa3fd005809` | Christmas Wishes Sta Christmas Fanny Pack — Trendy Festival Belt Bag,  | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/christmas-wishes-sta-christmas-fanny-pack-trendy-festival-belt-bag-holiday-gift-winstar4u |
| 186 | Shopify | `6ac34dabd27bb3ec4601b4dc` | Cleared Takeoff North Pole Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/cleared-takeoff-north-pole-christmas-tee |
| 187 | Shopify | `6ac34b7d6d0be71d1a0c16fb` | Cna Spreading Care Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/cna-spreading-care-christmas-tee |
| 188 | Shopify | `6ac34bc072c515c2e4074453` | Construction Crew Building Merry Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/construction-crew-building-merry-christmas-tee |
| 189 | Shopify | `6ac35e2a05e1de1c0a035f8f` | Construction Workers Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/construction-workers-christmas-tee |
| 190 | Shopify | `6ac34fdc2d0a9b485f038ea2` | Cooking Up Christmas Magic Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/cooking-up-christmas-magic-tee |
| 191 | Shopify | `6ac71362fb1d11d19e0370a7` | Cozy Cabin Winter Hoodie — Cozy Pullover Hoodie, Winter Gift / Winstar | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/cozy-cabin-winter-hoodie-cozy-pullover-hoodie-winter-gift-winstar4u |
| 192 | Shopify | `6ac713760ed8f1657605f359` | Cozy Cocoa Winter Hoodie — Cozy Pullover Hoodie, Winter Gift / Winstar | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/cozy-cocoa-winter-hoodie-cozy-pullover-hoodie-winter-gift-winstar4u |
| 193 | Shopify | `6ac346f02f513cff0f09afb1` | Cute Reindeer Lights Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/cute-reindeer-lights-christmas-tee |
| 194 | Shopify | `6ac70eb5050d0f25a70917e5` | Dear Santa Bank Account Christmas Duffel Bag — Spacious Weekend Travel | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/dear-santa-bank-account-christmas-duffel-bag-spacious-weekend-travel-tote-holiday-gift-winstar4u |
| 195 | Shopify | `6ac70ec0a4000bde5508bbde` | Dear Santa Explain Christmas Duffel Bag — Holiday Travel Essential, Ho | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/dear-santa-explain-christmas-duffel-bag-holiday-travel-essential-holiday-gift-winstar4u |
| 196 | Shopify | `6ac70ebc0a720c0b670cc5c4` | Dear Santa Explain Santa Christmas Duffel Bag — Perfect Carry-On Weeke | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/dear-santa-explain-santa-christmas-duffel-bag-perfect-carry-on-weekender-holiday-gift-winstar4u |
| 197 | Shopify | `6ac336c03ef3c129d802073a` | Dear Santa Goodish Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/dear-santa-goodish-christmas-tee |
| 198 | Shopify | `6ac712453925bc76b90372bb` | Deck The Halls Christmas Duffel Bag — Holiday Travel Essential, Holida | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/deck-the-halls-christmas-duffel-bag-holiday-travel-essential-holiday-gift-winstar4u |
| 199 | Shopify | `6ac70ec3b8d5d3e719012f93` | Deck The Halls Sit Down Christmas Duffel Bag — Tough Duffel for Gym &a | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/deck-the-halls-sit-down-christmas-duffel-bag-tough-duffel-for-gym-amp-getaways-holiday-gift-winstar4u |
| 200 | Shopify | `6ac71366fb1d11d19e0370ab` | Deer in Moonlight Winter Hoodie — Cozy Pullover Hoodie, Winter Gift /  | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/deer-in-moonlight-winter-hoodie-cozy-pullover-hoodie-winter-gift-winstar4u |
| 201 | Shopify | `6ac350242bb086484f0ecc1b` | Delivery Driver Santa Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/delivery-driver-santa-christmas-tee |
| 202 | Shopify | `6ac712a86027ad007d0e7ddc` | Disco 2027 New Year 2027 Hoodie — Cozy Pullover Hoodie, New Year 2027  | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/disco-2027-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 203 | Shopify | `6ac3273ec46d416a8b06de46` | Dog Mom Christmas Badge Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/dog-mom-christmas-badge-tee |
| 204 | Shopify | `6ac348281698f855e804f287` | Electricians Make Merry 1 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/electricians-make-merry-1-christmas-tee |
| 205 | Shopify | `6ac348765dc6b2aeda0d684c` | Electricians Make Merry 2 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/electricians-make-merry-2-christmas-tee |
| 206 | Shopify | `6ac348cab5276b73e30c5aac` | Electricians Make Merry 3 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/electricians-make-merry-3-christmas-tee |
| 207 | Shopify | `6ac3491a6d0be71d1a0c1581` | Electricians Make Merry 4 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/electricians-make-merry-4-christmas-tee |
| 208 | Shopify | `6ac349922f513cff0f09b093` | Electricians Make Merry 5 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/electricians-make-merry-5-christmas-tee |
| 209 | Shopify | `6ac7102582fcbdd37b039f7e` | Elegantly Wasted Martini Christmas Fanny Pack — Chic Hands-Free Purse, | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/elegantly-wasted-martini-christmas-fanny-pack-chic-hands-free-purse-holiday-gift-winstar4u |
| 210 | Shopify | `6ac34bfe44279671310d18d0` | Farmer Fueled Christmas Spirit Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/farmer-fueled-christmas-spirit-tee |
| 211 | Shopify | `6ac361d17b7b17b9ec0ae190` | Ferret Christmas Gifts Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/ferret-christmas-gifts-tee |
| 212 | Shopify | `6ac712e26027ad007d0e7dfb` | Friendsgiving Crew Thanksgiving Hoodie — Cozy Pullover Hoodie, Thanksg | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/friendsgiving-crew-thanksgiving-hoodie-cozy-pullover-hoodie-thanksgiving-gift-winstar4u |
| 213 | Shopify | `6ac3657760b60423bc029933` | Fur Mama Christmas Vibes Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/fur-mama-christmas-vibes-tee |
| 214 | Shopify | `6ac712e683cd0988460e927e` | Gather Together Thanksgiving Hoodie — Cozy Pullover Hoodie, Thanksgivi | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/gather-together-thanksgiving-hoodie-cozy-pullover-hoodie-thanksgiving-gift-winstar4u |
| 215 | Shopify | `6ac712ead9b782898109a95d` | Give Thanks Thanksgiving Hoodie — Cozy Pullover Hoodie, Thanksgiving G | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/give-thanks-thanksgiving-hoodie-cozy-pullover-hoodie-thanksgiving-gift-winstar4u |
| 216 | Shopify | `6ac360d87b7b17b9ec0ae0e2` | Goldfish Christmas Bowl Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/goldfish-christmas-bowl-tee |
| 217 | Shopify | `6ac712d3f0a0ce97bc0c926f` | Groovy Retro 2027 New Year 2027 Hoodie — Cozy Pullover Hoodie, New Yea | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/groovy-retro-2027-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 218 | Shopify | `6ac365b6e6aafe2ba909ffca` | Grumpy Cat Gift Box Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/grumpy-cat-gift-box-christmas-tee |
| 219 | Shopify | `6ac34c3a10261f3a950cde7f` | Hairstylists Christmas Beautiful Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/hairstylists-christmas-beautiful-tee |
| 220 | Shopify | `6ac34c7788d70ad97a0ddd3e` | Hairstylists Holidays Brighter Leopard Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/hairstylists-holidays-brighter-leopard-christmas-tee |
| 221 | Shopify | `6ac34cb1d27bb3ec4601b489` | Hairstylists Holidays Brighter Red Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/hairstylists-holidays-brighter-red-christmas-tee |
| 222 | Shopify | `6ac70ee9e2a15b1260026655` | Hallelujah Angels Christmas Duffel Bag — Holiday Travel Essential, Hol | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/hallelujah-angels-christmas-duffel-bag-holiday-travel-essential-holiday-gift-winstar4u |
| 223 | Shopify | `6ac710414bfa32451c054934` | Hallelujah Angels Christmas Fanny Pack — Trendy Festival Belt Bag, Hol | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/hallelujah-angels-christmas-fanny-pack-trendy-festival-belt-bag-holiday-gift-winstar4u |
| 224 | Shopify | `6ac712f36f976358160c47e0` | Happy Harvest Retro Thanksgiving Hoodie — Cozy Pullover Hoodie, Thanks | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/happy-harvest-retro-thanksgiving-hoodie-cozy-pullover-hoodie-thanksgiving-gift-winstar4u |
| 225 | Shopify | `6ac71265fb1d11d19e036ff0` | Happy Holidays Tree Christmas Fanny Pack — Concert-Ready Waist Pack, H | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/happy-holidays-tree-christmas-fanny-pack-concert-ready-waist-pack-holiday-gift-winstar4u |
| 226 | Shopify | `6ac712bfa005c19c550d89e8` | Happy New Year 2027 New Year 2027 Hoodie — Cozy Pullover Hoodie, New Y | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/happy-new-year-2027-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 227 | Shopify | `6ac712bb6027ad007d0e7de6` | Happy New Year 2027 Skyline New Year 2027 Hoodie — Cozy Pullover Hoodi | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/happy-new-year-2027-skyline-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 228 | Shopify | `6ac712f79ba30d41e4066075` | Harvest Blessings Thanksgiving Hoodie — Cozy Pullover Hoodie, Thanksgi | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/harvest-blessings-thanksgiving-hoodie-cozy-pullover-hoodie-thanksgiving-gift-winstar4u |
| 229 | Shopify | `6ac3629a29f83f0901071675` | Hedgehog Christmas Lights Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/hedgehog-christmas-lights-tee |
| 230 | Shopify | `6ac712afed135347800f9b86` | Hello 2027 New Year 2027 Hoodie — Cozy Pullover Hoodie, New Year 2027  | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/hello-2027-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 231 | Shopify | `6ac7137283f1a0e50d071e19` | Hello Winter Winter Hoodie — Cozy Pullover Hoodie, Winter Gift / Winst | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/hello-winter-winter-hoodie-cozy-pullover-hoodie-winter-gift-winstar4u |
| 232 | Shopify | `6ac70f1682fcbdd37b039f15` | Ill Be Home Christmas Probably Christmas Duffel Bag — Tough Duffel for | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/ill-be-home-christmas-probably-christmas-duffel-bag-tough-duffel-for-gym-getaways-holiday-gift-winstar4u |
| 233 | Shopify | `6ac710704e8c3a1ca906ecfa` | Ill Be Home Christmas Probably Christmas Fanny Pack — Stylish Hands-Fr | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/ill-be-home-christmas-probably-christmas-fanny-pack-stylish-hands-free-waist-bag-holiday-gift-winstar4u |
| 234 | Shopify | `6ac70f1a57527ce5fd019595` | Jingle All Way Liquor Christmas Duffel Bag — Roomy Gym & Travel Bag, H | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/jingle-all-way-liquor-christmas-duffel-bag-roomy-gym-travel-bag-holiday-gift-winstar4u |
| 235 | Shopify | `6ac7107335cf3f6ec802e99a` | Jingle All Way Liquor Christmas Fanny Pack — Travel-Ready Sling Bag, H | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/jingle-all-way-liquor-christmas-fanny-pack-travel-ready-sling-bag-holiday-gift-winstar4u |
| 236 | Shopify | `6ac70f1d50fc6704d30bf7f9` | Jingle Bells Santa Smells Christmas Duffel Bag — Spacious Weekend Trav | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/jingle-bells-santa-smells-christmas-duffel-bag-spacious-weekend-travel-tote-holiday-gift-winstar4u |
| 237 | Shopify | `6ac710774e8c3a1ca906ecff` | Jingle Bells Santa Smells Christmas Fanny Pack — Concert-Ready Waist P | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/jingle-bells-santa-smells-christmas-fanny-pack-concert-ready-waist-pack-holiday-gift-winstar4u |
| 238 | Shopify | `6ac70ef00aa3686f380d3c2b` | Keep Christ Christmas Christmas Duffel Bag — Roomy Gym & Travel Bag, H | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/keep-christ-christmas-christmas-duffel-bag-roomy-gym-travel-bag-holiday-gift-winstar4u |
| 239 | Shopify | `6ac712fbfa3cae10170efb1d` | Leftovers Crew Thanksgiving Hoodie — Cozy Pullover Hoodie, Thanksgivin | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/leftovers-crew-thanksgiving-hoodie-cozy-pullover-hoodie-thanksgiving-gift-winstar4u |
| 240 | Shopify | `6ac3509e38373f84c90757b9` | Location Christmas Location Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/location-christmas-location-tee |
| 241 | Shopify | `6ac350fa5dab9d4112038ade` | Making List Checking Twice Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/making-list-checking-twice-christmas-tee |
| 242 | Shopify | `6ac70f244bfa32451c0548d6` | Merry Christmas Lets Get Lit Christmas Duffel Bag — Perfect Carry-On W | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/merry-christmas-lets-get-lit-christmas-duffel-bag-perfect-carry-on-weekender-holiday-gift-winstar4u |
| 243 | Shopify | `6ac7107efa3cae10170ef9da` | Merry Christmas Lets Get Lit Christmas Fanny Pack — Hands-Free Holiday | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/merry-christmas-lets-get-lit-christmas-fanny-pack-hands-free-holiday-crossbody-holiday-gift-winstar4u |
| 244 | Shopify | `6ac7129cb32a96bbe40d0ce5` | Merry Christmas Script Christmas Hoodie — Cozy Pullover Hoodie, Christ | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/merry-christmas-script-christmas-hoodie-cozy-pullover-hoodie-christmas-gift-winstar4u |
| 245 | Shopify | `6ac3635b29f83f0901071710` | Merry Christmas Whiskers All Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/merry-christmas-whiskers-all-tee |
| 246 | Shopify | `6ac70f274e8c3a1ca906ec63` | Merry Everything Happy Always Christmas Duffel Bag — Holiday Travel Es | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/merry-everything-happy-always-christmas-duffel-bag-holiday-travel-essential-holiday-gift-winstar4u |
| 247 | Shopify | `6ac710847be9df884b032cb5` | Merry Everything Happy Always Christmas Fanny Pack — Trendy Festival B | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/merry-everything-happy-always-christmas-fanny-pack-trendy-festival-belt-bag-holiday-gift-winstar4u |
| 248 | Shopify | `6ac34e0744279671310d1a11` | Mixing Christmas Spirits Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/mixing-christmas-spirits-tee |
| 249 | Shopify | `6ac712c36027ad007d0e7dea` | My 2027 Resolution: More Naps New Year 2027 Hoodie — Cozy Pullover Hoo | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/my-2027-resolution-more-naps-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 250 | Shopify | `6ac70f2f0a720c0b670cc5f7` | My Elf Made Me Christmas Duffel Bag — Roomy Gym & Travel Bag, Holiday  | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/my-elf-made-me-christmas-duffel-bag-roomy-gym-travel-bag-holiday-gift-winstar4u |
| 251 | Shopify | `6ac7108d82fcbdd37b039fb7` | My Elf Made Me Christmas Fanny Pack — Travel-Ready Sling Bag, Holiday  | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/my-elf-made-me-christmas-fanny-pack-travel-ready-sling-bag-holiday-gift-winstar4u |
| 252 | Shopify | `6ac712c742c818a1ad095f77` | My Resolution Was To Have None New Year 2027 Hoodie — Cozy Pullover Ho | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/my-resolution-was-to-have-none-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 253 | Shopify | `6ac36700a4ac719af1080564` | Naughty Dog Nice Human Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/naughty-dog-nice-human-christmas-tee |
| 254 | Shopify | `6ac70f32050d0f25a7091825` | Naughty Is New Nice Christmas Duffel Bag — Spacious Weekend Travel Tot | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/naughty-is-new-nice-christmas-duffel-bag-spacious-weekend-travel-tote-holiday-gift-winstar4u |
| 255 | Shopify | `6ac7109250fc6704d30bf8a4` | Naughty Is New Nice Christmas Fanny Pack — Concert-Ready Waist Pack, H | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/naughty-is-new-nice-christmas-fanny-pack-concert-ready-waist-pack-holiday-gift-winstar4u |
| 256 | Shopify | `6ac70f35af40dc7cd60fb985` | Naughty List Resume Christmas Duffel Bag — Durable Gym Bag for Travele | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/naughty-list-resume-christmas-duffel-bag-durable-gym-bag-for-travelers-holiday-gift-winstar4u |
| 257 | Shopify | `6ac71096456d94f8f20ce382` | Naughty List Resume Christmas Fanny Pack — Chic Hands-Free Purse, Holi | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/naughty-list-resume-christmas-fanny-pack-chic-hands-free-purse-holiday-gift-winstar4u |
| 258 | Shopify | `6ac71356b32a96bbe40d0d77` | Naughty or Nice Christmas Hoodie — Cozy Pullover Hoodie, Christmas Gif | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/naughty-or-nice-christmas-hoodie-cozy-pullover-hoodie-christmas-gift-winstar4u |
| 259 | Shopify | `6ac712b7f0a0ce97bc0c925e` | New Year Same Me New Year 2027 Hoodie — Cozy Pullover Hoodie, New Year | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/new-year-same-me-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 260 | Shopify | `6ac34ceeefcc1caa890eeee6` | Nurses Holidays Brighter Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/nurses-holidays-brighter-christmas-tee |
| 261 | Shopify | `6ac363ad3829cc477b04aa64` | O Fish Ye Merry Gentlemen Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/o-fish-ye-merry-gentlemen-christmas-tee |
| 262 | Shopify | `6ac70ef49a2f0cb82508f8b8` | O Holy Night Christmas Duffel Bag — Spacious Weekend Travel Tote, Holi | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/o-holy-night-christmas-duffel-bag-spacious-weekend-travel-tote-holiday-gift-winstar4u |
| 263 | Shopify | `6ac33b8ca040a0dda40841ab` | Out Of Office New Year Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/out-of-office-new-year-christmas-tee |
| 264 | Shopify | `6ac35263c32146a388023abc` | Overtime Lineman Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/overtime-lineman-christmas-tee |
| 265 | Shopify | `6ac3612004778276c906e172` | Owl Be Home For Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/owl-be-home-for-christmas-tee |
| 266 | Shopify | `6ac33bd2d5f4eb4ec10e2ef2` | Paper Crown Lights Board Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/paper-crown-lights-board-christmas-tee |
| 267 | Shopify | `6ac363fea4ac719af1080435` | Parrot Santa Hat Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/parrot-santa-hat-christmas-tee |
| 268 | Shopify | `6ac712cb6356cae0df02e37c` | Party Like It's 2027 New Year 2027 Hoodie — Cozy Pullover Hoodie, New  | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/party-like-its-2027-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 269 | Shopify | `6ac33f636bc2d783ac08f2db` | Peace Earth Wine Glass Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/peace-earth-wine-glass-christmas-tee |
| 270 | Shopify | `6ac35e8e01306e9d6b0aa203` | Pilots Make Merry Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/pilots-make-merry-christmas-tee |
| 271 | Shopify | `6ac32bcce3af35e325008c70` | Plant Mom Christmas Banner Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/plant-mom-christmas-banner-tee |
| 272 | Shopify | `6ac34a2b2f513cff0f09b112` | Plumbers Make Merry Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/plumbers-make-merry-christmas-tee |
| 273 | Shopify | `6ac712cf83f1a0e50d071d96` | Pop The Bubbly 2027 New Year 2027 Hoodie — Cozy Pullover Hoodie, New Y | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/pop-the-bubbly-2027-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 274 | Shopify | `6ac70ef7b7d78a62480e724d` | Reason For Season Christmas Duffel Bag — Durable Gym Bag for Travelers | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/reason-for-season-christmas-duffel-bag-durable-gym-bag-for-travelers-holiday-gift-winstar4u |
| 275 | Shopify | `6ac710533925bc76b9037130` | Rejoice Star Christmas Fanny Pack — Hands-Free Holiday Crossbody, Holi | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/rejoice-star-christmas-fanny-pack-hands-free-holiday-crossbody-holiday-gift-winstar4u |
| 276 | Shopify | `6ac35551db7e1647760f9e6c` | Santa Called Backup 1 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santa-called-backup-1-christmas-tee |
| 277 | Shopify | `6ac3558d4cb82ddd30035cf6` | Santa Called Backup 2 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santa-called-backup-2-christmas-tee |
| 278 | Shopify | `6ac3229d696c2632950338eb` | Santa Called For Backup Firefighter Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santa-called-for-backup-firefighter-christmas-tee |
| 279 | Shopify | `6ac34ed244279671310d1a56` | Santa Delivering Christmas Driver Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santa-delivering-christmas-driver-tee |
| 280 | Shopify | `6ac3514222f5beeb1c0a6524` | Santa Flying Police 3 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santa-flying-police-3-christmas-tee |
| 281 | Shopify | `6ac352b322f5beeb1c0a65ed` | Santa Flying Police 4 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santa-flying-police-4-christmas-tee |
| 282 | Shopify | `6ac34f0f10261f3a950cdfe3` | Santa Flying Police Car Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santa-flying-police-car-christmas-tee |
| 283 | Shopify | `6ac355d1fd5c31c6ab0dd8ed` | Santa Needs Paramedic Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santa-needs-paramedic-christmas-tee |
| 284 | Shopify | `6ac3518ba84c54ac7608a80e` | Santa Paws Coming Town Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santa-paws-coming-town-christmas-tee |
| 285 | Shopify | `6ac338e513e333dc36045b55` | Santa Sleeping Zzz Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santa-sleeping-zzz-christmas-tee |
| 286 | Shopify | `6ac34d2f38373f84c9075697` | Santas Favorite Hairstylist Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santas-favorite-hairstylist-christmas-tee |
| 287 | Shopify | `6ac352fa5dab9d4112038b9e` | Santas Favorite Vet Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santas-favorite-vet-christmas-tee |
| 288 | Shopify | `6ac351d588d70ad97a0ddf20` | Santas Favorite Vet Tech Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santas-favorite-vet-tech-christmas-tee |
| 289 | Shopify | `6ac324191316d155b908c790` | Santas Got A Truck Driver 1 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santas-got-a-truck-driver-1-christmas-tee |
| 290 | Shopify | `6ac324c8dc8bc4dadc05417d` | Santas Got A Truck Driver 2 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santas-got-a-truck-driver-2-christmas-tee |
| 291 | Shopify | `6ac367883829cc477b04adac` | Santas On The Loose Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/santas-on-the-loose-christmas-tee |
| 292 | Shopify | `6ac70efe050d0f25a7091809` | Savior Born Manger Christmas Duffel Bag — Holiday Travel Essential, Ho | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/savior-born-manger-christmas-duffel-bag-holiday-travel-essential-holiday-gift-winstar4u |
| 293 | Shopify | `6ac71057f0a0ce97bc0c90d9` | Savior Born Manger Christmas Fanny Pack — Trendy Festival Belt Bag, Ho | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/savior-born-manger-christmas-fanny-pack-trendy-festival-belt-bag-holiday-gift-winstar4u |
| 294 | Shopify | `6ac33caed5f4eb4ec10e2f46` | Secret Santa Ruined Year Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/secret-santa-ruined-year-christmas-tee |
| 295 | Shopify | `6ac32c94f709d9946c08461b` | Silent Night Busy Shift 2 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/silent-night-busy-shift-2-christmas-tee |
| 296 | Shopify | `6ac332fca040a0dda4083d78` | Slay Belle Party Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/slay-belle-party-christmas-tee |
| 297 | Shopify | `6ac367d63829cc477b04ae36` | Sleigh All Day Biker Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/sleigh-all-day-biker-christmas-tee |
| 298 | Shopify | `6ac3339adec7c298800e9669` | Sleigh All Day Rocker 1 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/sleigh-all-day-rocker-1-christmas-tee |
| 299 | Shopify | `6ac3343a4b59c1258a0eabbc` | Sleigh All Day Rocker 2 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/sleigh-all-day-rocker-2-christmas-tee |
| 300 | Shopify | `6ac3534524efef54d70988a4` | Sleigh Tune Up 1 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/sleigh-tune-up-1-christmas-tee |
| 301 | Shopify | `6ac353d763d599869609f2b8` | Sleigh Tune Up 2 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/sleigh-tune-up-2-christmas-tee |
| 302 | Shopify | `6ac3541d5dab9d4112038c20` | Sleigh Tune Up 3 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/sleigh-tune-up-3-christmas-tee |
| 303 | Shopify | `6ac35476fd5c31c6ab0dd853` | Sleigh Tune Up 4 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/sleigh-tune-up-4-christmas-tee |
| 304 | Shopify | `6ac354cff3e4f34bd106b3a6` | Sleigh Tune Up 5 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/sleigh-tune-up-5-christmas-tee |
| 305 | Shopify | `6ac35510fd5c31c6ab0dd896` | Sleigh Tune Up Female Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/sleigh-tune-up-female-christmas-tee |
| 306 | Shopify | `6ac7137eb32a96bbe40d0d8d` | Snowflake Mandala Winter Hoodie — Cozy Pullover Hoodie, Winter Gift /  | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/snowflake-mandala-winter-hoodie-cozy-pullover-hoodie-winter-gift-winstar4u |
| 307 | Shopify | `6ac71382a5ade89b5c081048` | Snowman Winter Hoodie — Cozy Pullover Hoodie, Winter Gift / Winstar4U | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/snowman-winter-hoodie-cozy-pullover-hoodie-winter-gift-winstar4u |
| 308 | Shopify | `6ac712d6fb1d11d19e037022` | Sparkling Into 2027 New Year 2027 Hoodie — Cozy Pullover Hoodie, New Y | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/sparkling-into-2027-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 309 | Shopify | `6ac713039ba30d41e406608d` | Talk Turkey To Me Thanksgiving Hoodie — Cozy Pullover Hoodie, Thanksgi | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/talk-turkey-to-me-thanksgiving-hoodie-cozy-pullover-hoodie-thanksgiving-gift-winstar4u |
| 310 | Shopify | `6ac34f9688d70ad97a0dde2a` | Techy Little Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/techy-little-christmas-tee |
| 311 | Shopify | `6ac70f020aa3686f380d3c3a` | Thankful Grateful Blesse Christmas Duffel Bag — Tough Duffel for Gym & | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/thankful-grateful-blesse-christmas-duffel-bag-tough-duffel-for-gym-getaways-holiday-gift-winstar4u |
| 312 | Shopify | `6ac7105b4bfa32451c05494a` | Thankful Grateful Blesse Christmas Fanny Pack — Stylish Hands-Free Wai | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/thankful-grateful-blesse-christmas-fanny-pack-stylish-hands-free-waist-bag-holiday-gift-winstar4u |
| 313 | Shopify | `6ac71307fa3cae10170efb3c` | Thankful Grateful Blessed Thanksgiving Hoodie — Cozy Pullover Hoodie,  | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/thankful-grateful-blessed-thanksgiving-hoodie-cozy-pullover-hoodie-thanksgiving-gift-winstar4u |
| 314 | Shopify | `6ac35eee6ca06e1ed00bb3f8` | Truck Drivers Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/truck-drivers-christmas-tee |
| 315 | Shopify | `6ac7130b35a66ab7dc0b105a` | Turkey Day Squad Thanksgiving Hoodie — Cozy Pullover Hoodie, Thanksgiv | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/turkey-day-squad-thanksgiving-hoodie-cozy-pullover-hoodie-thanksgiving-gift-winstar4u |
| 316 | Shopify | `6ac7130f2d1baaa3fd00586c` | Turkey On The Run Thanksgiving Hoodie — Cozy Pullover Hoodie, Thanksgi | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/turkey-on-the-run-thanksgiving-hoodie-cozy-pullover-hoodie-thanksgiving-gift-winstar4u |
| 317 | Shopify | `6ac7131242c818a1ad095fbf` | Turkey Sunglasses Thanksgiving Hoodie — Cozy Pullover Hoodie, Thanksgi | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/turkey-sunglasses-thanksgiving-hoodie-cozy-pullover-hoodie-thanksgiving-gift-winstar4u |
| 318 | Shopify | `6ac33998a040a0dda40840a9` | Ugly Sweater Good Wine Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/ugly-sweater-good-wine-christmas-tee |
| 319 | Shopify | `6ac35f4a608846c473029b77` | Veterinarians Make Merry 1 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/veterinarians-make-merry-1-christmas-tee |
| 320 | Shopify | `6ac35fa7cf6ed3262908bedb` | Veterinarians Make Merry 2 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/veterinarians-make-merry-2-christmas-tee |
| 321 | Shopify | `6ac34ac563d599869609ec47` | Veterinarians Make Merry 3 Christmas Tee | $24.99-$26.99 | https://4juy1i-kq.myshopify.com/products/veterinarians-make-merry-3-christmas-tee |
| 322 | Shopify | `6ac712da35a66ab7dc0b1025` | Vintage Marquee 2027 New Year 2027 Hoodie — Cozy Pullover Hoodie, New  | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/vintage-marquee-2027-new-year-2027-hoodie-cozy-pullover-hoodie-new-year-2027-gift-winstar4u |
| 323 | Shopify | `6ac7135b83f1a0e50d071e08` | Vintage Santa Sleigh Ride Christmas Hoodie — Cozy Pullover Hoodie, Chr | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/vintage-santa-sleigh-ride-christmas-hoodie-cozy-pullover-hoodie-christmas-gift-winstar4u |
| 324 | Shopify | `6ac713169ba30d41e40660a5` | Vintage Turkey Thanksgiving Hoodie — Cozy Pullover Hoodie, Thanksgivin | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/vintage-turkey-thanksgiving-hoodie-cozy-pullover-hoodie-thanksgiving-gift-winstar4u |
| 325 | Shopify | `6ac70f054e8c3a1ca906ec58` | Walk By Faith Christmas Duffel Bag — Roomy Gym & Travel Bag, Holiday G | $93.99-$93.99 | https://4juy1i-kq.myshopify.com/products/walk-by-faith-christmas-duffel-bag-roomy-gym-travel-bag-holiday-gift-winstar4u |
| 326 | Shopify | `6ac7105e4bfa32451c05494e` | Walk By Faith Christmas Fanny Pack — Travel-Ready Sling Bag, Holiday G | $43.99-$43.99 | https://4juy1i-kq.myshopify.com/products/walk-by-faith-christmas-fanny-pack-travel-ready-sling-bag-holiday-gift-winstar4u |
| 327 | Shopify | `6ac7136aed135347800f9c06` | Winter Fox Winter Hoodie — Cozy Pullover Hoodie, Winter Gift / Winstar | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/winter-fox-winter-hoodie-cozy-pullover-hoodie-winter-gift-winstar4u |
| 328 | Shopify | `6ac7136efb1d11d19e0370b1` | Winter Frost Letters Winter Hoodie — Cozy Pullover Hoodie, Winter Gift | $39.99-$39.99 | https://4juy1i-kq.myshopify.com/products/winter-frost-letters-winter-hoodie-cozy-pullover-hoodie-winter-gift-winstar4u |
| 329 | TikTok | `6adecae2a02eb7366a0277e5` | Auntie Claus Christmas Sweatshirt / Santa Hat and Gift Boxes Badge Hol | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732790109517418548 |
| 330 | TikTok | `6adecb3059a53cf55f030c69` | Bah Humbug Christmas Sweatshirt / Stocking with Coal Badge Funny Holid | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732791719701942324 |
| 331 | TikTok | `6adecb086d10f640af0603a7` | Chill Penguin Winter Sweatshirt / Baby Penguin in Scarf and Beanie Bad | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732791720329318452 |
| 332 | TikTok | `6adecb5e1320136327024db7` | Cookie Season Christmas Sweatshirt / Christmas Cookies and Milk Badge  | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732791714507231284 |
| 333 | TikTok | `6adf6dc9250930614e0f3bce` | Dachshund Through the Snow Christmas Sweatshirt / Dachshund in Santa H | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732797885974745140 |
| 334 | TikTok | `6adf6d599d15ca1a990f69ba` | Everyone Go Home Christmas Sweatshirt / Cozy Slippers and Cocoa Badge  | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732792173357338676 |
| 335 | TikTok | `6adf6da49d15ca1a990f6a40` | Faith Hope Love Christmas Sweatshirt / Advent Candles and Wreath Badge | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732797862277451828 |
| 336 | TikTok | `6adecacc59a53cf55f030c1c` | Grandma Claus Christmas Sweatshirt / Santa Hat, Reading Glasses and Co | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732790098111467572 |
| 337 | TikTok | `6adf6def3a852e6fa20e6caa` | Hot Cocoa Club Christmas Sweatshirt / Cocoa Bar and Peppermint Badge H | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732797876117016628 |
| 338 | TikTok | `6adecaf559a53cf55f030c45` | Howdy Christmas Sweatshirt / Cowboy Boots and Santa Hat Western Holida | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732790098634510388 |
| 339 | TikTok | `6adf6d92c60cddcb060105af` | Joy to the World Christmas Sweatshirt / Gold Star and Brass Bell Badge | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732792186238701620 |
| 340 | TikTok | `6adf6db7250930614e0f3bba` | Let It Snow Winter Sweatshirt / Red Mittens, Scarf and Snowflake Badge | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732797870988824628 |
| 341 | TikTok | `6adecb44305999dc2d067254` | Merry 2026 Christmas Sweatshirt / Evergreen Wreath with Red Velvet Bow | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732791707047202868 |
| 342 | TikTok | `6adf6ddcc60cddcb06010608` | Merry Catmas Christmas Sweatshirt / Tabby Cat and Christmas Tree Badge | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732797872634695732 |
| 343 | TikTok | `6adf6d6b2c5edee2420ad5d8` | Morning Person Dec 25 Christmas Sweatshirt / Vintage Alarm Clock and P | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732792173436309556 |
| 344 | TikTok | `6adecab859a53cf55f030c14` | Nana Claus Christmas Sweatshirt / Santa Hat, Yarn and Cookies Badge Ho | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732790098608033844 |
| 345 | TikTok | `6adecaa51320136327024d4d` | Papa Claus Christmas Sweatshirt / Santa Hat and Plaid Flannel Badge Ho | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732790098632413236 |
| 346 | TikTok | `6adf6d46b95bee5547043b54` | Santa Called for Backup Christmas Sweatshirt / Reindeer with Jingle Be | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732792170963898420 |
| 347 | TikTok | `6adf6d7f10aa455cb00a1608` | Snack Season Christmas Sweatshirt / Holiday Snack Board Badge Funny Fo | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732792187495223348 |
| 348 | TikTok | `6adecb1c59a53cf55f030c5b` | Snowman Season Winter Sweatshirt / Snowman in Scarf and Top Hat Badge  | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732791726653083700 |

The other 260 linked SELL NOW products, which are not holiday designs (149 Etsy, 111 Shopify), are in the CSV.

## REPAIR FIRST: 447 products

| Group | Count | Fix | Decision |
|---|---|---|---|
| Wall Tapestry pricing (artwork already fixed) | 48 | Reprice or turn off the large sizes | D1 |
| Checkerboard T-shirts (fix staged, Printify blocks it) | 10 | Support ticket, then swap in | D4 |
| Artwork defects, live (cropping, wraparound, white-box, text color, bad source files) | 389 | Batch repair, each batch approved | D6 |

The biggest artwork-defect groups are backpacks (42), throw pillows (36), water bottles (31), fanny packs (24), hoodies (23), laptop sleeves (22), wine tumblers (21), onesies (19), scarves (17), lunch boxes (16) and socks (10). 427 of the 447 REPAIR FIRST products are holiday designs. That is why D6 matters before Nov 27.

## HOLD: 1 product

`6a53ee979296b919210641d5`: TEXACO-branded canvas (Etsy). The owner chose to keep it live, but it is excluded from promotion. Revisit under D7.

## UNKNOWN: 1,930 products

| Group | Count | What resolves it |
|---|---|---|
| eBay, artwork clean, no eBay link in Printify | 53 | Owner exports eBay listings (D5) |
| Amazon, artwork clean, no ASIN in Printify | 46 | Owner exports Seller Central inventory (D5) |
| TikTok, artwork clean, no TikTok product link | 51 | Owner exports TikTok products (D5) |
| Etsy, no live listing link, or not covered by an inspection row | 53 | Check status; visual-inspect any newer items |
| Duffels with no Shopify link | 5 | D3 |
| Shopify, artwork clean, no storefront link in Printify | 1,272 | Confirm in Shopify admin; re-publish only with owner approval |
| Shopify, in the live pull but not covered by an inspection row (incl. 54 staged repair drafts) | 450 | Visual inspection batch (read-only, no approval needed) |

## Verified vs. not verified

- **Verified:** visual-inspection results, all taken from real mockup images in earlier sessions with line-level evidence in the quality register. Today's live Printify pull confirmed the channel links: 247 of 299 Etsy products have a public listing URL, 17 of 62 Amazon products have an ASIN, and 20 of 71 TikTok products have a product link. The Shopify pull (2,508 products) found 486 with a storefront URL; 330 of the 1,602 Shopify products previously marked SELL NOW have one; the other 1,272 moved to UNKNOWN.
- **Not verified:** whether customers can actually buy each product right now. Storefront pages are blocked from this environment, so no link was click-tested. Net margin is unknown outside tapestries and duffels.
