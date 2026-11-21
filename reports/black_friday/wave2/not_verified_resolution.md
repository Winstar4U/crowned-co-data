# NOT VERIFIED rows: resolution (read-only, 2026-11-20/21 UTC)

Source: `reports/master_register/master_defects.csv`, rows with final_status NOT VERIFIED. Each product was re-read with Printify get-products (shop 26418699) and compared with the stored D6 evidence (`work/d6_batch*/<id>/`, `work/d6_warn_disposition/`). Nothing was written to Printify, Shopify or Etsy. Per-row detail is in `not_verified_resolution.csv`.

| Product | Register defect | Verdict | Why |
|---|---|---|---|
| 6ac70ec09a2f0cb82508f89a Dear Santa shorts | final word cropped | **FALSE POSITIVE** (close) + new contrast issue | The placement hasn't changed since 2026-10-09 (x 0.5, y 0.5, scale 0.7) and sits 100% inside the safe area. The live Black mockup shows "NO" in full. **But** the black "SAYS" lettering can't be seen on Black and is barely visible on Shadow and Ink Blue, which are the only enabled colours. |
| 6ac71018e2a15b12600266b5 Stress/Tinsel tank | top line cropped | **FALSE POSITIVE** (close) + new contrast issue | The placement hasn't changed (y 0.38, scale 0.9). The top line shows in full on both the White and the live Black mockups. The dark plum and green text has low contrast on the 4 enabled Black variants. The art also includes a wine glass. |
| 6ac7157a0ed8f1657605f458 Naughty List laptop sleeve | "JINGLE BELLS" cropped | **FALSE POSITIVE** (close) | The live art has no "JINGLE BELLS" text. The design sits 100% inside on all 3 sizes. The white background is fine because the print background is #ffffff on a white sleeve. |
| 6ac70231154e72164e0d8eea Elegantly Wasted tumbler | text clipped at seam | **FALSE POSITIVE** (close); **exclude from promos** (alcohol) | The art spans 0.30 to 0.70 of the wrap and never reaches the seam. The edge letters only curve with the cylinder; nothing is cut off. |
| 6ac702e21e2eac4da206fc57 Christ Is Born canvas | opaque white background | **FALSE POSITIVE** (close the artwork row) | Only one variant is enabled: 82220, 16x12 canvas. The print background is #ffffff and the art background is white, so no box shows. Its **placement row (275) stays open**: at scale 1.0 the top 7% and bottom 9% are cropped. Fix from placement.json: x 0.4996, y 0.488, scale 0.747. |
| 6ac702d43fd8c86beb0f48b1 Keep Christ canvas | opaque white background | **FALSE POSITIVE** (close the artwork row) | Same as above, white on white. Its **placement row (274) stays open**: the top 10% and bottom 11% are cropped. Fix from placement.json: x 0.5001, y 0.5, scale 0.708. |
| 6ad4254232b024bb32043467 Cribbage ornament | opaque background | SKIPPED | This is already an owner decision. |

**DEFECT CONFIRMED:** none of the 6 reported defects.
**STILL UNVERIFIABLE:** none.
**New items for the owner:**
1. Dear Santa shorts: the "SAYS" text is invisible on all 3 dark blanks.
2. Stress/Tinsel tank: low contrast on Black.

Both fixes would change live products (an art swap or disabling variants), so each needs product-specific approval first.
**Owner action:** confirm closing the 6 rows. The canvas placement fixes in rows 274/275 are separate and still need approval before they're applied.
Evidence images: `evidence/6ac70ec09a2f0cb82508f89a_live_front-left-leg_Black.jpg`, `evidence/6ac71018e2a15b12600266b5_live_front_Black.jpg`.
