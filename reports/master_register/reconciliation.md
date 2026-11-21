# Reconciliation of Headline Numbers

Built 2026-11-20 from existing files only. The builder is read-only on every source.

**Sources, in order of authority (later wins):**
1. Quality Register
2. Sales Readiness Register (3,008 rows)
3. Decision Register D1–D7
4. D6 queue and batch results
5. `d6_new_art`
6. `winstar-recovery` @ c74849e
7. `work/d6_qa_fixes/results.csv`: 25 rows, 23 products, mtime 16:07:09 UTC. It was unchanged when re-checked at build time and covers every FAIL it was meant to fix, so no row is marked "fix in progress".

**Result:** 524 defect rows across 507 unique products.

## 1. 2,552 products inspected

- **Source:** Quality Register line 1095: eBay 53 + Amazon 62 + TikTok 71 + Etsy 297 + Shopify 2,069 (#361–2,429) = **2,552**.
- **Sales Readiness Register:** it has 3,008 rows. Of these, 455 have the reason "Not covered by an inspection row" (Shopify 450, Etsy 5), which leaves **2,553 covered**.
- **NOT EXACTLY RECONCILED (off by 1 net):** by shop, Shopify has 2,072 covered against 2,069 (+3), Etsy 294 against 297 (−3) and Amazon 63 against 62 (+1).
  - Likely cause: the Shopify pull of 2026-11-19 includes products created after the inspection, plus #1–360 rows matched to register lines. Etsy originals were replaced by the migrated briefs.
  - No ID-level list exists to settle this without a new pull. This was not done, per the rules.
- **In the master register:** 2,552 is the "inspected" column in the scoreboard. The 455 uninspected products are reported as an inspection gap, not as defects.

## 2. 553 historical finding instances

The source is Quality Register line 1096: Priority A 19 + Priority B 497 + Priority C 37. The register itself calls 553 "a conservative upper bound… not an exact deduplicated count".

### A: 19 products

| Finding | Products | Master register |
|---|---|---|
| Alcohol art on youth or baby apparel | 15 | Bucket REMOVED (owner-approved removal). Closed, no row. |
| Shopify thongs | 2 | REMOVED. Closed. |
| Etsy "Gift Set of 3" | 1 | REMOVED. Closed. |
| TEXACO | 1 | **1 IP row**, BLOCKED — OWNER DECISION (D7) |

18 are closed and 1 is open.

### B: 497 Shopify artwork instances

These map to:

| Group | Products | Master register |
|---|---|---|
| D6 queue (Shopify) | 388 | Rows below. The 389th D6 product is the Etsy cribbage ornament from §2, not Priority B. |
| Tapestries | 48 | Art already fixed live. Now **48 profitability rows** (D1/D2). |
| Duffels | 45 | Art fixed live. Closed, except **5 marketplace_sync rows** (D3). |
| Checkerboard tees | 12 | **10 BLOCKED — TECHNICAL** (D4). 2 REMOVED. |

That is 493 products. **NOT RECONCILED: 4 instances (497 − 493).** Priority B was summed from per-batch tallies, not from IDs. The register notes up to about 9 Youth Hoodie products counted under both A and B. No ID list exists for the 497.

### C: 37 duplicate pairs or clusters

| Shop | Pairs or clusters | Master register |
|---|---|---|
| Amazon | 11 pairs | 7 both-live pairs were closed by the owner ("keep all 7", D-3F2G504W3Y; 14 products, no rows). 4 pairs are open (#1, #9, #10, #11): **8 rows**. |
| Etsy | 17 clusters | **36 rows**: every member flagged DUPLICATE_LISTING. |
| eBay | 2 pairs | **4 rows** |
| Shopify | 7 pairs | **15 rows**: 9 on D6 products (8 flagged members plus the "Copy of" listing `69b0212c`) and 6 on UNKNOWN products. These also cover the pillow-size pairs that the register lists separately as YELLOW, so the Shopify row count goes beyond the 7 pairs. |

**Deduplicated:** the master register has **524 rows across 507 unique products**:

| Source | Rows | Products |
|---|---|---|
| D6 queue | 406 | 389 |
| Tapestry profitability | 48 | |
| Checkerboard | 10 | |
| D3 sync | 5 | |
| TEXACO | 1 | |
| Duplicates outside D6 | 54 | Etsy 36, Amazon 8, Shopify 6, eBay 4 |

76 historical products are closed with no row:
- REMOVED: 22
- Owner-kept Amazon pairs: 14
- Fixed-live duffels: 40 (45 minus the 5 D3 duffels)

## 3. 224 placement corrections

These are the PLACEMENT ONLY rows in `placement_qa_224.csv`: 107 PASS, 106 WARN, 11 FAIL. In the master register:

- **216 placement rows are VERIFIED READY FOR APPROVAL:**
  - 107 PASS
  - 106 WARN (warning text kept in the row)
  - 3 pillow FAILs fixed by d6_qa_fixes with per-variant print_areas (PASS)
- **1 resolution row is VERIFIED:** the napkin `6ac713526356cae0df02e40e`, smaller motif, 156 dpi, PASS.
- **7 resolution rows are BLOCKED — OWNER DECISION:** AI upscale WARN, with native-equivalent resolution of only 39–86 dpi.
- **3 extra artwork rows are NOT VERIFIED:** TRANSPARENCY-WARN, blank colour unchecked.
- **5 extra duplicate_listing rows**

Product level: 209 VERIFIED, 12 BLOCKED-OWNER, 3 NOT VERIFIED.

## 4. 81 files covering 123 products

`repaired_art_qa.csv` has 123 rows and 81 unique files:

| Source | Files | Products |
|---|---|---|
| local | 64 | |
| local_v2 | 10 | |
| local and local_v2 combined | 59 | 74 |
| text_fix | 22 | 49 |

Independent QA: 104 PASS, 5 WARN, 14 FAIL. Four of those products moved to the regeneration workstream, so 119 products remain under "REPAIRED ART" in the evidence register.

In the master register:
- 70 artwork rows and 6 resolution rows are VERIFIED.
- 43 wording rows and 6 resolution rows are BLOCKED-OWNER.

**Unique total:** 123 + 24 − 4 overlap = **143**, which matches the 143 products in `d6_new_art/inventory.csv`.

## 5. 24 regenerations

`regeneration_register_24.csv`: 15 PASS, 2 PASS-WARN, 2 REWORK, 5 BLOCKED-WORDING. In the master register:

- **16 artwork rows are VERIFIED:** the 15 PASS plus `6ac71152` (PASS-WARN, tiny engraved text, provider proof advised).
- **6 wording rows are BLOCKED-OWNER:** W6 ×4, W7, and W9 `6ac711e2`, which is PASS-WARN.
- **2 duvet resolution rows are BLOCKED-OWNER:** d6_qa_fixes gives options A and B, both WARN.

## 6. 11 placement FAILs

All 11 are fixed in d6_qa_fixes:
- **4 PASS:** the 3 throw pillows (bp 5353) and 1 napkin. All are VERIFIED READY FOR APPROVAL.
- **7 WARN, AI upscale only:** 2 duvets, 2 shower curtains and 3 tablecloths. All are BLOCKED — OWNER DECISION.

## 7. 14 repaired-art FAILs (4 superseded)

**The 4 superseded:**
- `6ac7113450fc6704d30bf944` and `6ac717a24636838bd804f846`: regenerated, PASS, VERIFIED.
- `6ac71204…` and `6ac711a4…` (duvets): REWORK, then d6_qa_fixes WARN, now BLOCKED-OWNER.

**The other 10 are all in d6_qa_fixes:**
- **PASS (4):** `6ac7149d` (TREE UP holes filled), `6ac71344`, `6ac713e2` and `6ac7232d`.
  - All 4 are in wording groups, so their status is BLOCKED — OWNER DECISION on wording, not on art.
- **WARN, upscale (6):** these carry an extra resolution row, BLOCKED-OWNER.

## 8. 106 placement WARNs

| Warning | Count | Master register |
|---|---|---|
| Non-rectangular safe area only | 92 | Rect bounds independently verified; shape fit inherited from the prior check. VERIFIED, with the WARN text in the description. |
| RESOLUTION-WARN, ratio 0.42–0.48 | 11 | VERIFIED, with the WARN text. |
| TRANSPARENCY-WARN | 3 | Placement VERIFIED, plus a separate artwork row, NOT VERIFIED. |

## 9. 11 wording groups / 49 products

- **Groups:** W1–W7 and W9 (there is no W8), plus G1–G3: 11 groups and 49 products.
  - 43 are text-fix products and 6 are regenerated.
- **Master register:** 49 wording rows, all BLOCKED — OWNER DECISION.
  - 6 also have a resolution row (BLOCKED-OWNER).
  - 2 also have a duplicate_listing row.

## Where sources disagreed (newer or more specific evidence kept)

- **Placement FAILs and repaired-art FAILs:** d6_qa_fixes (16:07 UTC) supersedes winstar-recovery QA (c74849e).
- **Throw pillows:** winstar-recovery FAIL (about 88% inside the lumbar variant) supersedes the batch-3 "verify_pass" of 1.0. That FAIL is then superseded by the d6_qa_fixes per-variant PASS.
- **Status of the 389 D6 products:** the D6 batch status (READY / NEEDS_NEW_ART / BLOCKED) is superseded by the independent winstar-recovery QA.
  - The 4 "cannot reproduce" products are still REPAIR FIRST in the Sales Readiness Register. They are recorded as **NOT VERIFIED** (likely false positives) until the owner agrees to close them.
- **Amazon duplicates:** the Quality Register "11 pairs" is narrowed by the owner's decision, which keeps only the 7 both-live pairs. 4 pairs remain open.
- **Promotion Candidates CSV (343 products):** not used for status. The independent QA and d6_qa_fixes are newer.

## Not counted as defects (noted only)

- **15 LOW IP title-echo flags in the D6 batch results:** "Elegantly Wasted" (INXS), "Christmas Vacation", "All I Want for Christmas", and MagSafe(R) on `69b0212c`. These are common phrases and none was found as an actual mark, so they are not rows.
- **Marketplace verification gap:** 1,470 inspected-clean products with no channel link (Shopify 1,272, Etsy 48, eBay 53, TikTok 51, Amazon 46). These are a gap, not defects. They are in the scoreboard and listed per ID in the Sales Readiness Register (bucket UNKNOWN).

## NOT VERIFIED (7 rows)

| Product | What is unverified | Why |
|---|---|---|
| `6ac70ec09a2f0cb82508f89a`, `6ac71018e2a15b12600266b5`, `6ac7157a0ed8f1657605f458`, `6ac70231154e72164e0d8eea` (Shopify) | The historical defect | D6 could not reproduce it. The live placement is inside the safe area and the zoomed mockup looks clean. Probably false positives, but closing them needs the owner's agreement. |
| `6ad4254232b024bb32043467` (Etsy) and `6ac702e21e2eac4da206fc57`, `6ac702d43fd8c86beb0f48b1` (Shopify) | Whether the opaque art background matches the blank colour | It was not checked in the evidence. It can be closed with one read-only `printify-get-products-9eb` call per product. This was not done because it is not a gap in the register's numbers. |

**Other unverified items:**
- **D7 replacement TEXACO art:** never downloaded or trademark-screened, because the image host is blocked. It sits inside the IP row.
- **Live status of every Amazon, eBay and TikTok listing:** awaits the D5 exports.
