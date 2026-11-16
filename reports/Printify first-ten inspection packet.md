# Printify Quality Recovery — First-Ten Product Inspection Packet

**Bridge task:** T-6N0T120Q2R (Winstar Enterprises — Printify Quality Recovery, PRIORITY CRITICAL)
**Status:** INSPECTION COMPLETE for the first 10 products (5 Etsy + 5 Amazon). Submitted for independent verification — not self-marked done.
**Scope covered:** Winstar Etsy Store (shop 26603005) and Winstar4U Amazon (shop 29451844), 5 products each.
**Method:** Real Printify API product detail pulled for each of the 10 IDs below (images, variants, print_areas, external sync status) — then the actual default mockup image for every product was downloaded and visually inspected (not metadata-only). No product was published, unpublished, deleted, repriced, or had inventory altered.

## 0. Access confirmation

All 5 Printify shops reachable and authenticated read-only:

| Shop | ID | Channel |
|---|---|---|
| Winstar4U | 26418699 | Shopify |
| Winstar Etsy Store | 26603005 | Etsy |
| Winstardeals4U | 28059412 | eBay |
| My Tiktok Shop | 28122957 | TikTok |
| Winstar4U Amazon | 29451844 | Amazon |

Note: the directive's phrasing "WinstarDesigns Etsy" does not exactly match the real shop name ("Winstar Etsy Store") — flagged for the owner, not acted on as a discrepancy.

**Visual-inspection blocker and fix:** `images.printify.com` was blocked by this session's network policy (confirmed 403 on the proxy's CONNECT tunnel). Per the owner's own environment-change approval flow, I requested — and the owner approved — adding `images.printify.com`, the Printify S3 artwork host, and `www.etsy.com` to this session's network allowlist. Only after that approval did image inspection actually happen; no image was inspected from metadata alone.

## 1. Per-product inspection table

| # | Shop | Product ID | Title | Listing link | Price / Cost | Visual inspection result | Severity |
|---|---|---|---|---|---|---|---|
| 1 | Etsy | `6af90c15626b8d7aa001936c` | Cozy Season Christmas Hoodie | [Etsy listing 4617545521](https://www.etsy.com/listing/4617545521/cozy-season-christmas-hoodie-snowy) | $54.99 / $21.58 | Clean: centered print, legible "Cozy Season" text, no cropping/alignment/pixelation issues. | OK |
| 2 | Etsy | `6af90c02383728621d011dd8` | Gardeners Grow Merry Christmas Hoodie | [Etsy listing 4617554898](https://www.etsy.com/listing/4617554898/gardeners-grow-merry-christmas-hoodie) | $54.99 / $21.58 | Clean: print sharp, correctly placed, text legible. | OK |
| 3 | Etsy | `6af90bdec745d035040e95ab` | Santa's Favorite Nurse Hoodie | [Etsy listing 4617545297](https://www.etsy.com/listing/4617545297/nurse-christmas-hoodie-santas-favorite) | $54.99 / $21.58 | Clean: no defects observed. | OK |
| 4 | Etsy | `6af90bf06d67bf35520cbead` | Teacher Christmas Squad Hoodie | [Etsy listing 4617545369](https://www.etsy.com/listing/4617545369/teacher-christmas-hoodie-teacher) | $54.99 / $21.58 | Clean: no defects observed. | OK |
| 5 | Etsy | `6af90b7eca5d307abc016117` | Cat Mom Christmas Hoodie | [Etsy listing 4617554646](https://www.etsy.com/listing/4617554646/cat-mom-christmas-hoodie-santa-hat-tabby) | $54.99 / $21.58 | Clean: no defects observed. | OK |
| 6 | Amazon | `6af1072a421fd94ad304e54b` | Winter Garden Field Guide Christmas T-Shirt | **Not synced — see §2** | $26.99 / $9.68 | Artwork clean in mockup; print itself has no issues. | **HIGH — not live** |
| 7 | Amazon | `6af1073ce16bc2f471089f76` | Opening Night Christmas T-Shirt | **Not synced — see §2** | $26.99 / $9.68 | Artwork clean in mockup. | **HIGH — not live** |
| 8 | Amazon | `6af10718421fd94ad304e53e` | Apres Ski Club Christmas T-Shirt | **Not synced — see §2** | $26.99 / $9.68 | Artwork clean in mockup. | **HIGH — not live** |
| 9 | Amazon | `6af1070681fb6450380f0dda` | Tied with a Bow Christmas T-Shirt | **Not synced — see §2** | $26.99 / $9.68 | Artwork clean in mockup. | **HIGH — not live** |
| 10 | Amazon | `6af106f4421fd94ad304e520` | Cozy Season Christmas T-Shirt | **Not synced — see §2** | $26.99 / $9.68 | Artwork clean in mockup; shares identical graphic with product #1 — see §3. | **HIGH — not live** / informational |

All 10 mockup images were opened and viewed directly (saved locally first); none were judged from the "hint"/metadata fields alone.

## 2. Highest-severity finding: Amazon shop is not actually publishing anything

**All 5 inspected Amazon-shop products show `external: null`** in Printify, despite `visible: true`. In Printify's data model, `external.handle` is the live marketplace listing URL; `null` means the product has never actually been pushed to Amazon's catalog, regardless of how it displays inside Printify's own dashboard.

Practical effect: these 5 products (and very plausibly more of the Amazon shop's catalog — this was only the first 10) are **not purchasable on Amazon today**. No customer can find or buy them. This is not a cosmetic defect; it's a sync/connection failure between Printify and the Amazon sales channel, and it means any revenue assumption based on Amazon-shop "live" product count is currently wrong.

**No action taken on this without owner approval**, per the execution rules (no publish/unpublish without specific owner sign-off). Flagging for the correction-approval packet: the owner needs to decide whether to (a) investigate why the Printify↔Amazon channel connection isn't propagating these listings, or (b) manually publish them from Printify once reviewed. I have not attempted either — this is a decision, not something to self-execute.

By contrast, **all 5 Etsy-shop products are genuinely live** — each resolves to a real `etsy.com/listing/...` URL (confirmed above), so the Etsy side of the two priority shops is functioning as expected.

## 3. Informational, not a defect: one design reused across channels/garment types

Product #1 (Etsy hoodie, "Cozy Season") and product #10 (Amazon tee, "Cozy Season") use the **identical print artwork** — same window/mug/books graphic, same "Cozy Season" wordmark — placed on two different blueprint types (hoodie vs. t-shirt) in two different shops. This is ordinary print-on-demand practice (one design, multiple product types/channels) and is **not** the kind of "duplicate creation" the execution rules warn against (that rule is about not re-creating the *same* listing twice, not about reusing one piece of artwork across garment types). Noting it only so the owner has visibility, not flagging it as an error.

## 4. Margin check (fully burdened, per unit, before returns/CAC)

**Etsy hoodies** — price $54.99, Printify cost $21.58:
- Etsy fees: 6.5% transaction fee ($3.57) + payment processing 3%+$0.25 ($1.90) + $0.20 listing fee ≈ $5.67
- Net contribution: $54.99 − $21.58 − $5.67 ≈ **$27.74/unit, ≈ 50.4% net margin** — healthy, clears any reasonable floor.
- Not included: Etsy Offsite Ads fee (12–15%), which only applies if a sale is attributed to an Offsite Ad click — unknown without order-level attribution data, not fabricated here.

**Amazon tees** — price $26.99, Printify cost $9.68:
- Amazon apparel referral fee is typically ~17% on items under $20 (tiered above that) — but **this math is moot right now**: since these 5 products are not actually synced to Amazon (§2), there is no real order stream to compute a margin against. Computing a theoretical margin on listings that don't exist live would be exactly the "claim completion from metadata" error the directive warned against — so I'm reporting the blocker instead of a number.

## 5. What this packet does and doesn't claim

- **Does claim:** 10 real products' actual images were downloaded and visually inspected; all 10 are artwork-clean; the Amazon shop has a real, actionable sync problem affecting all 5 inspected products.
- **Does not claim:** shipping-profile correctness, variant-level color/size completeness, or compliance screening (trademark/IP) beyond visual read — none of the 10 designs appeared to reference copyrighted characters or brands, but that was not a dedicated IP-clearance pass.
- **No live product was changed.** No publish, unpublish, price change, or inventory change was made.

## 6. Next steps (pending owner direction)

1. Owner decision needed on the Amazon sync gap (§2) before any correction is attempted.
2. Continue toward full five-shop inventory (Winstar4U/Shopify, Winstardeals4U/eBay, My Tiktok Shop still unstarted) within the 7-day window, marking inaccessible products UNKNOWN as directed.
3. Prepare the first correction-approval packet (due within 48 hours of the 2026-11-16T19:51 confirmed start) — this packet's §2 finding is the primary candidate for that packet, pending owner input on which remedy to pursue.
