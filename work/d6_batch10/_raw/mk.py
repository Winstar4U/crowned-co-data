"""Batch 10 shorthand -> compact records (data transcribed from read-only get-products responses).
line: kind pid upd_date upd_time img_id img_name w h x y scale uuid"""
import json, sys
T = {
 "backpack": dict(bp=10823, pp=99, pos="front_dtf", deco="dtf", en=[401444], svgs={"401444": "6a7ec23adf264c8209005322"}, mock="401444/145590", titles={"401444": "Black / One size"}, colors="Black", vids=[401444]),
 "pillow": dict(bp=5353, pp=92, pos="front", deco="dye-sublimation", en=[244224, 244226, 244227, 244228], vids=[244223,244224,244225,244226,244227,244228],
                svgs={"244228": "69946e42bd89474a4808f6a2", "244227": "69946e4130234343580f4ae3", "244226": "69946e419dcbe487bc02a352", "244224": "69946e3f595fab0ec705a662"},
                mock="244224/155844", titles={"244224": "12x18", "244226": "18x18", "244227": "20x20", "244228": "24x24"}),
 "sleeve": dict(bp=429, pp=99, pos="front", deco="dye-sublimation", en=[62037, 62038, 62039], vids=[62037, 62038, 62039],
                svgs={"62037": "5cc179989831ec000f7037d0", "62038": "5cc179999831ec013d0e5d62", "62039": "5cc179999831ec000e5b0cdc"},
                mock="62037/3028", titles={"62037": "12in", "62038": "13in", "62039": "15in"}),
}
for line in sys.stdin:
    a = line.split()
    if not a: continue
    k, pid, d1, d2, iid, name, w, h, x, y, s, uu = a[:12]
    t = T[k]
    rec = {"pid": pid, "shop": 26418699, "bp": t["bp"], "pp": t["pp"], "upd": d1 + " " + d2, "vis": True,
           "mock": "https://images.printify.com/mockup/%s/%s/x.jpg?camera_label=front" % (pid, t["mock"]), "en": t["en"], "svgs": t["svgs"],
           "areas": [{"pos": t["pos"], "deco": t["deco"], "vids": t["vids"], "img": [iid, name, int(w), int(h), float(x), float(y), float(s), 0, uu]}],
           "extra": {"unavailable_enabled": [], "enabled_titles": t["titles"]}}
    if t.get("colors"): rec["extra"]["enabled_colors"] = t["colors"]
    print(json.dumps(rec))
