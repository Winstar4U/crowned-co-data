"""Extract a compact product record from a saved read-only printify-get-products JSON response. Usage: python3 -I compact_from_json.py FILE"""
import json, sys, re
d = json.load(open(sys.argv[1]))
if isinstance(d, list): d = d[0]
if "text" in d and isinstance(d.get("text"), str): d = json.loads(d["text"])
en = [v["id"] for v in d["variants"] if v["is_enabled"]]
titles = {str(v["id"]): v["title"] for v in d["variants"] if v["is_enabled"]}
unav = [v["id"] for v in d["variants"] if v["is_enabled"] and not v.get("is_available", True)]
mock = next((i["src"] for i in d["images"] if i.get("is_default")), d["images"][0]["src"] if d["images"] else "")
mock = re.sub(r"/[^/]+\.jpg", "/x.jpg", mock)
# primary print area: the one covering enabled variant(s) with a non-empty image
areas = []
for pa in d["print_areas"]:
    if not set(pa["variant_ids"]) & set(en): continue
    for ph in pa["placeholders"]:
        if not ph["images"]: continue
        i = ph["images"][0]
        areas.append({"pos": ph["position"], "deco": ph.get("decoration_method"), "vids": pa["variant_ids"],
                      "img": [i["id"], i["name"], i["width"], i["height"], i["x"], i["y"], i["scale"], i.get("angle", 0),
                              i["src"].rsplit("/", 1)[1]], "nimg": len(ph["images"])})
svgs = {}
pos0 = areas[0]["pos"] if areas else None
for v in d.get("views", []):
    if v["position"] != pos0: continue
    for f in v["files"]:
        sid = f["src"].rsplit("/", 1)[1].replace(".svg", "")
        for vid in f["variant_ids"]:
            if vid in en: svgs[str(vid)] = sid
rec = {"pid": d["id"], "shop": d["shop_id"], "bp": d["blueprint_id"], "pp": d["print_provider_id"], "upd": d["updated_at"],
       "vis": d["visible"], "mock": mock, "en": en, "svgs": svgs, "areas": areas,
       "extra": {"unavailable_enabled": unav, "enabled_titles": titles, "n_areas_with_art": len(areas),
                 "title": d["title"]}}
print(json.dumps(rec))
