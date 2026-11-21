#!/usr/bin/env python3
"""Append a compact product record (from a read-only printify-get-products response) to products.jsonl.
usage: add.py pid bp pp updated enabled_csv mock_vid mock_suffix position deco img_id name w h x y scale src_uuid [visible] [svg_csv vid=svg,...]"""
import json, sys
SVGS = {854: {"76801": "61bb0923bff1585dbb2a3d5c", "76802": "61bb09358ef59d061161aa1d", "76803": "61bb09458ef59d061161aa20"},
        376: {"45132": "690bedb6cab78a517b010cd2", "45133": "690bec3235668572ae069c73", "45134": "690beeebdcfe8d8b4e07e5f2"}}
a = sys.argv[1:]
pid, bp, pp, upd, en, mv, ms, pos, deco, iid, name, w, h, x, y, sc, src = a[:17]
vis = (a[17] if len(a) > 17 else "true") == "true"
bp, pp = int(bp), int(pp)
svgs = SVGS.get(bp, {})
if len(a) > 18 and a[18]:
    svgs = dict(kv.split("=") for kv in a[18].split(","))
ev = [int(v) for v in en.split(",")]
rec = dict(product_id=pid, shop_id="26418699", blueprint_id=bp, print_provider_id=pp, visible=vis, updated_at=upd,
           mockup_default="https://images.printify.com/mockup/%s/%s/%s.jpg" % (pid, mv, ms),
           enabled_variants=ev, svg=svgs.get(str(ev[0])) or (list(svgs.values())[0] if svgs else None), svgs=svgs,
           areas=[dict(position=pos, decoration=deco, images=[dict(id=iid, name=name, width=int(w), height=int(h),
                  x=float(x), y=float(y), scale=float(sc), angle=0,
                  src="https://pfy-prod-image-storage.s3.us-east-2.amazonaws.com/26317439/" + src)])])
lines = [l for l in open("products.jsonl")] if __import__("os").path.exists("products.jsonl") else []
lines = [l for l in lines if json.loads(l)["product_id"] != pid]
lines.append(json.dumps(rec) + "\n")
open("products.jsonl", "w").writelines(lines)
print(len(lines), pid)
