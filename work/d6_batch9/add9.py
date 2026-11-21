#!/usr/bin/env python3
"""Batch 9: append compact product records (transcribed from read-only printify-get-products responses) to products.jsonl.
stdin: one compact JSON per line:
 {"pid","bp","pp","upd","vis","mock","en":[..],"svgs":{vid:svgid},
  "areas":[{"pos","deco","vids":[..],"img":[id,name,w,h,x,y,scale,angle,src_uuid]}], "extra":{...}}"""
import json, os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
fn = os.path.join(ROOT, "products.jsonl")
have = {}
if os.path.exists(fn):
    for l in open(fn):
        r = json.loads(l); have[r["product_id"]] = r
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    c = json.loads(line)
    areas = []
    for a in c["areas"]:
        i = a["img"]
        areas.append(dict(position=a["pos"], decoration=a.get("deco"), variant_ids=a.get("vids", []),
                          images=[dict(id=i[0], name=i[1], width=int(i[2]), height=int(i[3]), x=float(i[4]), y=float(i[5]),
                                       scale=float(i[6]), angle=float(i[7]),
                                       src="https://pfy-prod-image-storage.s3.us-east-2.amazonaws.com/26317439/" + i[8])]))
    svgs = {str(k): v for k, v in c.get("svgs", {}).items()}
    en = [int(v) for v in c["en"]]
    rec = dict(product_id=c["pid"], shop_id=str(c.get("shop", "26418699")), blueprint_id=int(c["bp"]), print_provider_id=int(c["pp"]),
               visible=c.get("vis", True), updated_at=c["upd"], mockup_default=c["mock"], enabled_variants=en,
               svg=svgs.get(str(en[0])) or (list(svgs.values())[0] if svgs else None), svgs=svgs, areas=areas,
               extra=c.get("extra", {}))
    have[c["pid"]] = rec
with open(fn, "w") as f:
    for r in have.values():
        f.write(json.dumps(r) + "\n")
print(len(have), "records")
