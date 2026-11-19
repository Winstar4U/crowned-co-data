# Winstar Five-Shop Sales-Readiness Register (SELL NOW / REPAIR FIRST / HOLD / UNKNOWN)

**Compiled:** 2026-11-19, under the owner's Direct Execution Order. It is built from existing inspection evidence plus a live, read-only Printify pull of the Amazon, TikTok and Etsy catalogs taken today.
**Full per-product data:** `reports/Winstar_Sales_Readiness_Register.csv` has 2,558 rows. Each row has the product ID, shop ID, title, holiday flag, live channel link, price range, reason, proposed correction, flags and evidence pointer.
**Rebuild:** `python3 work/build_sales_register.py <dir with live Printify pulls>`.
**Owner decisions:** `reports/Winstar_Owner_Decision_Register.md` (D1–D7).
**No live changes were made to produce this.** No publishing, price, inventory or listing changes.

## Definitions (strict)

- **SELL NOW:** the artwork was confirmed clean on a real Printify mockup, and there are no open quality, IP, price-loss or fulfillment flags.
  - Etsy, Amazon and TikTok rows also need a live channel link from Printify.
  - Shopify rows have a clean mockup, but their storefront links have not been pulled yet. That is the next task.
- **REPAIR FIRST:** a confirmed, correctable problem: an artwork defect, the tapestry price loss, or the checkerboard platform block.
- **HOLD:** a serious compliance concern. Do not promote.
- **UNKNOWN:** the artwork is fine but listing status can't be confirmed, or there is no inspection evidence.
- **REMOVED:** already taken off sale by owner decision.

## Counts

| Bucket | Etsy | Amazon | eBay | TikTok | Shopify | Total |
|---|---|---|---|---|---|---|
| SELL NOW | 241 | 17 | 0 | 20 | 1602 | 1880 |
| REPAIR FIRST | 1 | 0 | 0 | 0 | 446 | 447 |
| HOLD | 1 | 0 | 0 | 0 | 0 | 1 |
| UNKNOWN | 53 | 46 | 53 | 51 | 5 | 208 |
| REMOVED | 3 | 0 | 0 | 0 | 19 | 22 |
| Not yet classified (no per-ID evidence: Shopify #1-360) | 0 | 0 | 0 | 0 | ~357 | ~357 |

Margin was verified only on the tapestries (losing money on 2 of 4 sizes) and the duffels (45–50% cost-to-price). For every other product type, margin is **not yet computed** and is not claimed.

## Promotion-ready now: 129 holiday products with live, clickable links (for ChatGPT)

Etsy links are public listing pages. Amazon links are built from the ASIN Printify holds, in the form amazon.com/dp/ASIN. TikTok links are the seller-center product pages; get the public share link from TikTok Seller Center. **Margin caution:** the $11.99 Etsy ornaments cost about $6.31 to make plus about $6.29 to ship. They are profitable only if the customer pays shipping. Promote them only once that is confirmed (see D2). The Amazon "duplicate pair" products are both kept, per the owner's 2026-11-18 decision.

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
| 110 | TikTok | `6adecae2a02eb7366a0277e5` | Auntie Claus Christmas Sweatshirt / Santa Hat and Gift Boxes Badge Hol | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732790109517418548 |
| 111 | TikTok | `6adecb3059a53cf55f030c69` | Bah Humbug Christmas Sweatshirt / Stocking with Coal Badge Funny Holid | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732791719701942324 |
| 112 | TikTok | `6adecb086d10f640af0603a7` | Chill Penguin Winter Sweatshirt / Baby Penguin in Scarf and Beanie Bad | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732791720329318452 |
| 113 | TikTok | `6adecb5e1320136327024db7` | Cookie Season Christmas Sweatshirt / Christmas Cookies and Milk Badge  | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732791714507231284 |
| 114 | TikTok | `6adf6dc9250930614e0f3bce` | Dachshund Through the Snow Christmas Sweatshirt / Dachshund in Santa H | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732797885974745140 |
| 115 | TikTok | `6adf6d599d15ca1a990f69ba` | Everyone Go Home Christmas Sweatshirt / Cozy Slippers and Cocoa Badge  | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732792173357338676 |
| 116 | TikTok | `6adf6da49d15ca1a990f6a40` | Faith Hope Love Christmas Sweatshirt / Advent Candles and Wreath Badge | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732797862277451828 |
| 117 | TikTok | `6adecacc59a53cf55f030c1c` | Grandma Claus Christmas Sweatshirt / Santa Hat, Reading Glasses and Co | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732790098111467572 |
| 118 | TikTok | `6adf6def3a852e6fa20e6caa` | Hot Cocoa Club Christmas Sweatshirt / Cocoa Bar and Peppermint Badge H | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732797876117016628 |
| 119 | TikTok | `6adecaf559a53cf55f030c45` | Howdy Christmas Sweatshirt / Cowboy Boots and Santa Hat Western Holida | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732790098634510388 |
| 120 | TikTok | `6adf6d92c60cddcb060105af` | Joy to the World Christmas Sweatshirt / Gold Star and Brass Bell Badge | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732792186238701620 |
| 121 | TikTok | `6adf6db7250930614e0f3bba` | Let It Snow Winter Sweatshirt / Red Mittens, Scarf and Snowflake Badge | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732797870988824628 |
| 122 | TikTok | `6adecb44305999dc2d067254` | Merry 2026 Christmas Sweatshirt / Evergreen Wreath with Red Velvet Bow | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732791707047202868 |
| 123 | TikTok | `6adf6ddcc60cddcb06010608` | Merry Catmas Christmas Sweatshirt / Tabby Cat and Christmas Tree Badge | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732797872634695732 |
| 124 | TikTok | `6adf6d6b2c5edee2420ad5d8` | Morning Person Dec 25 Christmas Sweatshirt / Vintage Alarm Clock and P | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732792173436309556 |
| 125 | TikTok | `6adecab859a53cf55f030c14` | Nana Claus Christmas Sweatshirt / Santa Hat, Yarn and Cookies Badge Ho | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732790098608033844 |
| 126 | TikTok | `6adecaa51320136327024d4d` | Papa Claus Christmas Sweatshirt / Santa Hat and Plaid Flannel Badge Ho | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732790098632413236 |
| 127 | TikTok | `6adf6d46b95bee5547043b54` | Santa Called for Backup Christmas Sweatshirt / Reindeer with Jingle Be | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732792170963898420 |
| 128 | TikTok | `6adf6d7f10aa455cb00a1608` | Snack Season Christmas Sweatshirt / Holiday Snack Board Badge Funny Fo | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732792187495223348 |
| 129 | TikTok | `6adecb1c59a53cf55f030c5b` | Snowman Season Winter Sweatshirt / Snowman in Scarf and Top Hat Badge  | $44.99-$50.99 | https://seller-us.tiktok.com/product/edit/1732791726653083700 |

The other 149 linked SELL NOW Etsy products, which are not holiday designs, are in the CSV.

## REPAIR FIRST: 447 products

| Group | Count | Fix | Decision |
|---|---|---|---|
| Wall Tapestry pricing (artwork already fixed) | 48 | Reprice or turn off the large sizes | D1 |
| Checkerboard T-shirts (fix staged, Printify blocks it) | 10 | Support ticket, then swap in | D4 |
| Artwork defects, live (cropping, wraparound, white-box, text color, bad source files) | 389 | Batch repair, each batch approved | D6 |

The biggest artwork-defect groups are backpacks (42), throw pillows (36), water bottles (31), fanny packs (24), hoodies (23), laptop sleeves (22), wine tumblers (21), onesies (19), scarves (17), lunch boxes (16) and socks (10). 427 of the 447 REPAIR FIRST products are holiday designs. That is why D6 matters before Nov 27.

## HOLD: 1 product

`6a53ee979296b919210641d5`: TEXACO-branded canvas (Etsy). The owner chose to keep it live, but it is excluded from promotion. Revisit under D7.

## UNKNOWN: 208 products, plus about 357 not yet classified

| Group | Count | What resolves it |
|---|---|---|
| eBay, artwork clean, no eBay link in Printify | 53 | Owner exports eBay listings (D5) |
| Amazon, artwork clean, no ASIN in Printify | 46 | Owner exports Seller Central inventory (D5) |
| TikTok, artwork clean, no TikTok product link | 51 | Owner exports TikTok products (D5) |
| Etsy, no live listing link, or not covered by an inspection row | 53 | Check status; visual-inspect any newer items |
| Duffels with no Shopify link | 5 | D3 |
| Shopify #1–360, metadata-sampled only and never visually inspected | ~357 | Visual inspection batch (read-only, no approval needed) |

## Verified vs. not verified

- **Verified:** visual-inspection results, all taken from real mockup images in earlier sessions with line-level evidence in the quality register. Today's live Printify pull confirmed the channel links: 247 of 299 Etsy products have a public listing URL, 17 of 62 Amazon products have an ASIN, and 20 of 71 TikTok products have a product link.
- **Not verified:** whether customers can actually buy each product right now. Storefront pages are blocked from this environment. Shopify links have not been pulled yet. Net margin is unknown outside tapestries and duffels.
