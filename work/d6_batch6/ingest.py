#!/usr/bin/env python3
"""Batch 6: convert saved read-only printify-get-products responses (full JSON, possibly wrapped) into compact records for add6.py."""
import json, re, sys
def load(fn):
    s = open(fn, encoding="utf-8").read()
    try:
        d = json.loads(s)
    except Exception:
        d = json.loads(s[s.index("{"):s.rindex("}") + 1])
    if isinstance(d, list):
        d = json.loads(d[0]["text"])
    return d
for fn in sys.argv[1:]:
    p = load(fn)
    en = [v["id"] for v in p["variants"] if v["is_enabled"]]
    unav = [v["id"] for v in p["variants"] if v["is_enabled"] and not v["is_available"]]
    titles = {v["id"]: v["title"] for v in p["variants"] if v["is_enabled"]}
    areas = []
    for pa in p["print_areas"]:
        for ph in pa["placeholders"]:
            if not ph["images"]:
                continue
            i = ph["images"][0]
            areas.append(dict(pos=ph["position"], deco=ph.get("decoration_method"), vids=pa["variant_ids"],
                              img=[i["id"], i["name"], i["width"], i["height"], i["x"], i["y"], i["scale"], i.get("angle", 0),
                                   i["src"].rsplit("/", 1)[1]], n_images=len(ph["images"])))
    # primary area = front-ish one covering enabled variants
    pos0 = areas[0]["pos"] if areas else None
    svgs = {}
    for vw in p.get("views", []):
        if vw["position"] != pos0:
            continue
        for f in vw["files"]:
            sid = f["src"].rsplit("/", 1)[1].replace(".svg", "")
            for v in f["variant_ids"]:
                if v in en:
                    svgs.setdefault(str(v), sid)
        if not svgs and vw["files"]:
            sid = vw["files"][0]["src"].rsplit("/", 1)[1].replace(".svg", "")
            svgs = {str(v): sid for v in en}
    mock = next((im["src"] for im in p["images"] if im.get("is_default") and set(im["variant_ids"]) & set(en)), p["images"][0]["src"] if p["images"] else "")
    mock = re.sub(r"/[^/?]+\.jpg", "/x.jpg", mock)
    rec = dict(pid=p["id"], shop=p["shop_id"], bp=p["blueprint_id"], pp=p["print_provider_id"], upd=p["updated_at"], vis=p.get("visible"),
               mock=mock, en=en, svgs=svgs, areas=areas,
               extra=dict(unavailable_enabled=unav, enabled_titles=titles, n_print_areas=len(p["print_areas"]),
                          positions=[a["pos"] for a in areas], external=p.get("external"), is_locked=p.get("is_locked")))
    print(json.dumps(rec))
