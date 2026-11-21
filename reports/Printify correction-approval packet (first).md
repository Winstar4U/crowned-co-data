# Printify Quality Recovery — First Correction-Approval Packet

**Bridge task:** T-6N0T120Q2R (Winstar Enterprises — Printify Quality Recovery, PRIORITY CRITICAL)
**Due:** within 48 hours of confirmed start (2026-11-16T19:51) → by 2026-11-18T19:51. Delivered on schedule.
**Status:** Proposals for owner decision. **Nothing has been published, unpublished, repriced, or synced. No approval in this packet has been executed.**

## 1. What's new since the first inspection packet

A second batch of 11 products was inspected across the three previously-unstarted shops (Winstar4U/Shopify, Winstardeals4U/eBay, My Tiktok Shop), using the same method as batch 1: real Printify API full-product-detail pulls, then the actual default mockup image downloaded and visually opened for every product — not metadata alone.

| # | Shop | Product ID | Title | Sync status | Visual result |
|---|---|---|---|---|---|
| 1 | Shopify | `6ae64cca54fa3d36d60bedc7` | Santa's Favorite Pilot T-Shirt | **Synced** — live at [myshopify.com](https://4juy1i-kq.myshopify.com/products/santas-favorite-pilot-t-shirt-vintage-airplane-wreath-aviation-christmas-gift-tee-for-pilots) | Clean |
| 2 | Shopify | `6ae64cb854fa3d36d60bedba` | Black Cat Christmas T-Shirt | **Synced** | Clean |
| 3 | Shopify | `6ae64c1054fa3d36d60bed6c` | Sold on Christmas T-Shirt | **Synced** | Clean |
| 4 | Shopify | `6ae64c0088325bfb8908eecd` | Librarian Christmas T-Shirt | **Synced** | Clean |
| 5 | eBay | `6a493cc4a36a12099202d054` | Brazil Heart Flag Phone Case | **external: null — not synced** | Clean artwork |
| 6 | eBay | `6a493cc0a36a12099202d052` | Panama Flag Heart Phone Case | **external: null — not synced** | Clean artwork |
| 7 | eBay | `6a493cb9a36a12099202d050` | Dripping Rose Graphic T-Shirt | **external: null — not synced** | Clean artwork |
| 8 | eBay | `6a493ca208efc981890568c5` | Distressed American Flag Tank Top | **external: null — not synced** | Clean artwork |
| 9 | TikTok | `6adf6def3a852e6fa20e6caa` | Hot Cocoa Club Christmas Sweatshirt | Has a `seller-us.tiktok.com` edit link (see caveat below) | Clean |
| 10 | TikTok | `6adf6ddcc60cddcb06010608` | Merry Catmas Christmas Sweatshirt | Has a `seller-us.tiktok.com` edit link | Clean |
| 11 | TikTok | `6adf6dc9250930614e0f3bce` | Dachshund Through the Snow Christmas Sweatshirt | Has a `seller-us.tiktok.com` edit link | Clean |

**TikTok caveat:** unlike Etsy and Shopify, Printify's `external.handle` for these TikTok products is a seller-center *edit* link (`seller-us.tiktok.com/product/edit/...`), not a public buyer-facing listing page. I can't independently confirm from this link type alone that these are actually visible to a shopper the way Etsy/Shopify listings are — it indicates a channel connection exists, but not conclusively that the listing is live and purchasable. Marked as a lower-confidence "likely synced," not a confirmed pass, pending a direct public-page check.

**No defect was found in any of the 11 images.** All are correctly centered, legible, and sharp — consistent with batch 1.

## 2. Combined finding across both batches: a confirmed, cross-marketplace sync-readiness defect

Across 21 products inspected so far (10 in the first packet + 11 here), covering all 5 shops:

| Shop | Sampled | Genuinely synced/live | Sync gap (`external: null`) |
|---|---|---|---|
| Winstar Etsy Store | 5 | 5 | 0 |
| Winstar4U (Shopify) | 4 | 4 | 0 |
| My Tiktok Shop | 3 | 3 (lower-confidence, see caveat) | 0 |
| Winstar4U Amazon | 5 | 0 | **5** |
| Winstardeals4U (eBay) | 3 | 0 | **3** |

**This is no longer an Amazon-only anomaly.** The identical signature — `visible: true` inside Printify, but `external: null`, meaning Printify has never actually pushed the product to the sales channel — now shows up consistently on **both** of the two marketplaces sampled (Amazon and eBay), at a rate of 8/8 so far, while it shows up on **none** of the three storefront-style channels sampled (Etsy, Shopify, TikTok). That pattern (marketplace-type channels affected, storefront-type channels not) is itself informative and worth the owner's attention when deciding how to investigate: it points toward something structural in how Printify's Amazon and eBay channel connections are configured, rather than per-product mistakes.

**I have not attempted to diagnose or fix the underlying connection** — that would mean touching live channel configuration, which is outside read-only scope without specific approval.

## 3. Correction-approval requests (owner decision needed — nothing executed)

### Request A — Investigate and resolve the Amazon channel connection
**Affected:** at least 5 of 5 sampled Amazon-shop products (62 products total in that shop; full scope unknown).
**Proposed action (pending approval):** Either (a) I investigate further, read-only, why Printify→Amazon isn't propagating listings (check shop connection status via Printify's shop-level data, if the API exposes it), or (b) the owner checks the Amazon channel connection directly in Printify's dashboard. I am **not** proposing to publish/sync any product without a separate, specific go-ahead once the root cause is known — publishing after a sync fix would be exactly the kind of live write the execution rules require approval for.

### Request B — Investigate and resolve the eBay channel connection
**Affected:** at least 3 of 3 sampled eBay-shop products (53 products total in that shop; full scope unknown).
**Proposed action (pending approval):** Same as Request A, applied to the eBay shop.

### Request C — Confirm a sampling approach for the remaining ~2,881 products
**Why this needs a decision:** the five shops hold **2,902 products combined** (Shopify 2,429 + Etsy 287 + TikTok 71 + Amazon 62 + eBay 53). At the pace used so far (real image download + visual inspection, ~1–2 minutes of work per product including evidence capture), literally inspecting every product by hand inside the 7-day window is not achievable — this is a scale fact, not a shortfall in effort. 21 of 2,902 products (0.7%) have been genuinely visually inspected so far.

I'm not proposing to quietly do a small fraction and call the catalog "inspected" — flagging this now so the owner can set direction. Options, for the owner to choose (or combine):
1. **Stratified random sampling** — a fixed number of products per shop per day (e.g., 10–20), continuing until the 7-day window closes, to build a statistically meaningful defect-rate estimate per shop rather than full coverage.
2. **Metadata-only triage across the full catalog, image inspection only on flagged items** — pull `external`/`visible`/sync status for all ~2,900 products (fast, no image fetch needed) to find every sync-gap product like the Amazon/eBay pattern above, then prioritize actual visual inspection on products that show other risk signals (recently edited, flagged tags, etc.). This would directly answer "how many products are affected by the sync gap" far faster than continuing 10-at-a-time image batches.
3. **Owner-directed priority list** — the owner names specific products/categories (e.g., best-sellers, recently-launched) to inspect first.

My default recommendation, if the owner has no preference, is **option 2 first** (it's the fastest way to size the real scope of Requests A and B — right now "5 of 5" and "3 of 3" are honest but small samples), followed by continued visual-inspection batches on a rotating schedule across all 5 shops per option 1. I have not started option 2 without confirmation, since even a metadata-only full-catalog pull is a meaningfully larger API/time cost than this packet's scope and I'd rather have the owner's steer before committing to it.

## 4. What this packet does not claim

- Does not claim the catalog is fully inspected — 21/2,902 products (0.7%) have had real images opened.
- Does not claim to know the Amazon/eBay sync gap's root cause, only that it exists and is consistent across every sample taken so far.
- No live product was changed in the course of producing this packet.
