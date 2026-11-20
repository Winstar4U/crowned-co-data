"""Build compact records from shorthand (data transcribed from read-only get-products responses).
line: kind pid upd_date upd_time img_id img_name w h x y scale uuid [en=comma] [mockvid/cam]"""
import json, sys
T = {
 "fanny": dict(bp=468, pp=99, pos="front", deco="dye-sublimation", en=[65045], svgs={"65045": "5e2560ba0cbde50a0854fc06"}, mock="65045/6109", titles={"65045": "One size"}),
 "pillow": dict(bp=5353, pp=92, pos="front", deco="dye-sublimation", en=[244224, 244226, 244227, 244228],
                svgs={"244228": "69946e42bd89474a4808f6a2", "244227": "69946e4130234343580f4ae3", "244226": "69946e419dcbe487bc02a352",
                      "244224": "69946e3f595fab0ec705a662", "244225": "69946e406ec3fdf2e20f5db2", "244223": "69946e363695216e2f0597d2"},
                mock="244224/155844", titles={"244223": "12x12", "244224": "12x18", "244225": "16x16", "244226": "18x18", "244227": "20x20", "244228": "24x24"}),
 "backpack": dict(bp=10823, pp=99, pos="front_dtf", deco="dtf", en=[401444], svgs={"401444": "6a7ec23adf264c8209005322"}, mock="401444/145590",
                  titles={"401444": "Black / One size"}, colors="Black"),
}
for line in sys.stdin:
    a = line.split()
    if not a: continue
    k, pid, d1, d2, iid, name, w, h, x, y, s, uu = a[:12]
    t = T[k]; en = t["en"]; mock = t["mock"]
    for o in a[12:]:
        if o.startswith("en="): en = [int(v) for v in o[3:].split(",")]
        elif o.startswith("mock="): mock = o[5:]
    rec = {"pid": pid, "shop": 26418699, "bp": t["bp"], "pp": t["pp"], "upd": d1 + " " + d2, "vis": True,
           "mock": "https://images.printify.com/mockup/%s/%s/x.jpg?camera_label=front" % (pid, mock), "en": en,
           "svgs": {v: t["svgs"][v] for v in map(str, en)},
           "areas": [{"pos": t["pos"], "deco": t["deco"], "vids": en, "img": [iid, name, int(w), int(h), float(x), float(y), float(s), 0, uu]}],
           "extra": {"unavailable_enabled": [], "enabled_titles": {str(v): t["titles"][str(v)] for v in en}}}
    if t.get("colors"): rec["extra"]["enabled_colors"] = t["colors"]
    print(json.dumps(rec))
