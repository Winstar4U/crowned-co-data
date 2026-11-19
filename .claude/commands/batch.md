---
description: Run the next D6 artwork batch of 40 (non-live prep only)
argument-hint: [batch number]
---
Take batch $ARGUMENTS (or the first batch not marked DONE) from work/artwork_redesign_batches.csv. For each product: fetch the Printify product (read-only), download the source artwork, diagnose, produce corrected art/placement, render a geometry-checked preview and a before/after image labeled with the product ID. No live writes. Post the batch to the Bridge immediately, update the CSV status, then start the next batch.
