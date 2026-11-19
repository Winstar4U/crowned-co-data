#!/usr/bin/env python3
"""D6 artwork-repair Batch 3 -- NON-LIVE placement prep (adapted from d6_batch2/build.py).

Reads read-only Printify data captured in products.jsonl (incl. each product's view-SVG id(s)) + placeholders.json,
the downloaded originals/mockups in <product_id>/, and Printify view SVGs in _svg/
(used only to extract each blueprint's own "Safe Area" / print-shape outline).
Writes per-product placement.json + previews, batch3_results.csv and contact sheets.
Nothing here talks to Printify.  Run with:  python3 -I build.py
"""
import csv, json, math, os, re, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.abspath(__file__))
Image.MAX_IMAGE_PIXELS = 80_000_000
MARGIN = 0.05
WRAP_BLUEPRINTS = {425, 854, 1245}          # mug / bottle / shot glass wraparound
WRAP_ZONE = (0.20, 0.80)                    # keep key art away from seam/handle
DARK_SUBSTRATE_METHODS = {"dtf", "dtg", "engraving"}
DECO_BY_BP = {5546: "dtf", 10796: "dtf", 10823: "dtf", 1515: "engraving", 77: "dtg", 568: "dtg", 1398: "dtg",
              2662: "direct-to-fabric"}
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
IP_TERMS = ["grinch", "disney", "marvel", "starbucks", "coca", "pepsi", "nike", "adidas",
            "harry potter", "peanuts", "snoopy", "home alone", "hallmark", "lego", "barbie",
            "pokemon", "star wars", "elf on the shelf", "rudolph", "frosty", "nfl", "nba",
            "taylor swift", "magsafe", "iphone", "samsung", "galaxy", "inxs", "elegantly wasted",
            "christmas vacation", "national lampoon", "griswold", "dr. seuss", "charlie brown"]
IP_NOTES = {"elegantly wasted": "LOW: 'Elegantly Wasted' is also an INXS song/album title (titles rarely protectable; review)",
            "iphone": "LOW: device-compatibility names (iPhone/Samsung/MagSafe) in listing; descriptive use only",
            "samsung": "LOW: device-compatibility names in listing; descriptive use only",
            "magsafe": "LOW: MagSafe(R) named in description; descriptive compatibility use",
            "christmas vacation": "LOW: 'Christmas Vacation' echoes the National Lampoon film title; here used as a generic phrase ('Christmas Vacation Canceled') - review, no film marks/characters seen"}


def font(sz, bold=False):
    try:
        return ImageFont.truetype(FONTB if bold else FONT, sz)
    except Exception:
        return ImageFont.load_default()


# ---------------------------------------------------------------- SVG safe areas
NUM = r"-?\d*\.?\d+(?:e-?\d+)?"


def _attr(tag, name):
    m = re.search(r'\b%s="([^"]*)"' % re.escape(name), tag)
    return m.group(1) if m else None


def _path_polys(d):
    from svg.path import parse_path, Move
    if not re.fullmatch(r"[0-9A-Za-z.,\-\s]+", d or ""):
        return []
    path = parse_path(d)
    polys, cur = [], []
    for seg in path:
        if isinstance(seg, Move):
            if len(cur) > 2:
                polys.append(cur)
            cur = [(seg.end.real, seg.end.imag)]
            continue
        n = 2 if seg.__class__.__name__ in ("Line", "Close") else 24
        for i in range(1, n + 1):
            p = seg.point(i / n)
            cur.append((p.real, p.imag))
    if len(cur) > 2:
        polys.append(cur)
    return polys


def svg_shape(svg_path):
    """Return dict(bg=(x,y,w,h), polys=[...] in normalized placeholder coords, kind)."""
    s = open(svg_path, encoding="utf-8", errors="replace").read()
    bg = re.search(r'<rect id="color_background"[^>]*>', s)
    if not bg:
        return None
    t = bg.group(0)
    bx, by = float(_attr(t, "x") or 0), float(_attr(t, "y") or 0)
    bw, bh = float(_attr(t, "width")), float(_attr(t, "height"))
    polys, kind = [], None
    # 1) explicit Printify safe area element (not a <g>)
    for m in re.finditer(r'<(rect|circle|polygon|path) id="(safew|safe|safe area|Safe area|Safe Area)"[^>]*>', s):
        tag, el = m.group(1), m.group(0)
        if tag == "rect":
            x, y = float(_attr(el, "x") or 0), float(_attr(el, "y") or 0)
            w, h = float(_attr(el, "width")), float(_attr(el, "height"))
            polys = [[(x, y), (x + w, y), (x + w, y + h), (x, y + h)]]
        elif tag == "circle":
            cx, cy, r = float(_attr(el, "cx")), float(_attr(el, "cy")), float(_attr(el, "r"))
            polys = [[(cx + r * math.cos(a), cy + r * math.sin(a)) for a in np.linspace(0, 2 * math.pi, 180)]]
        elif tag == "polygon":
            v = [float(z) for z in re.findall(NUM, _attr(el, "points"))]
            polys = [list(zip(v[0::2], v[1::2]))]
        else:
            polys = _path_polys(_attr(el, "d"))
        kind = "printify_safe_area"
        break
    # 2) otherwise the drawn product outline (e.g. fanny-pack front face)
    if not polys:
        m = re.search(r'<g id="outlines">\s*<g id="front">\s*<path d="([^"]+)"', s)
        if m:
            polys = _path_polys(m.group(1))
            kind = "printify_print_outline"
    if not polys:
        return {"bg": (bx, by, bw, bh), "polys": [], "kind": "rect"}
    norm = [[((px - bx) / bw, (py - by) / bh) for px, py in poly] for poly in polys]
    return {"bg": (bx, by, bw, bh), "polys": norm, "kind": kind}


# ---------------------------------------------------------------- masks
def safe_mask(W, H, shape, res=600, extra=None):
    """Boolean mask (h x w) of the allowed region in normalized placeholder space."""
    k = res / max(W, H)
    mw, mh = max(8, int(round(W * k))), max(8, int(round(H * k)))
    # 5% inset rectangle always applies
    m = Image.new("L", (mw, mh), 0)
    d = ImageDraw.Draw(m)
    d.rectangle([MARGIN * mw, MARGIN * mh, (1 - MARGIN) * mw - 1, (1 - MARGIN) * mh - 1], fill=255)
    if shape and shape["polys"]:
        sm = Image.new("L", (mw, mh), 0)
        sd = ImageDraw.Draw(sm)
        for poly in shape["polys"]:
            sd.polygon([(u * mw, v * mh) for u, v in poly], fill=255)
        if shape["kind"] == "printify_print_outline":     # erode outline by 5% of short side
            r = max(1, int(MARGIN * min(mw, mh)))
            sm = sm.filter(ImageFilter.MinFilter(2 * r + 1))
        m = Image.fromarray(np.minimum(np.array(m), np.array(sm)))
    if extra:  # (u0,u1,v0,v1) extra rect constraint
        e = Image.new("L", (mw, mh), 0)
        ImageDraw.Draw(e).rectangle([extra[0] * mw, extra[2] * mh, extra[1] * mw - 1, extra[3] * mh - 1], fill=255)
        m = Image.fromarray(np.minimum(np.array(m), np.array(e)))
    return np.array(m) > 127


def content_info(img):
    """Content mask (bool, downsampled), bbox in normalized image coords, transparency verdict."""
    rgba = img.convert("RGBA")
    a = np.array(rgba.getchannel("A"))
    has_alpha = img.mode in ("RGBA", "LA", "PA") or "transparency" in img.info
    transp_frac = float((a < 16).mean())
    if has_alpha and transp_frac > 0.01:
        mask_full = a > 24
        verdict = "OK (transparent background)"
        opaque_kind = None
    else:
        rgb = np.array(rgba.convert("RGB")).astype(int)
        border = np.concatenate([rgb[0], rgb[-1], rgb[:, 0], rgb[:, -1]])
        bmean = border.mean(0)
        if (bmean > 235).all():
            mask_full = (255 - rgb).max(2) > 30
            verdict = "FLAG: opaque white background (no alpha)"
            opaque_kind = "white"
        else:
            mask_full = np.ones(a.shape, bool)
            verdict = "FLAG: opaque full-bleed image (no alpha; bg rgb~%d,%d,%d)" % tuple(int(c) for c in bmean)
            opaque_kind = "fullbleed"
    ys, xs = np.nonzero(mask_full)
    H, W = a.shape
    bbox = (xs.min() / W, ys.min() / H, (xs.max() + 1) / W, (ys.max() + 1) / H)
    # downsample mask for geometry
    k = 160 / max(W, H)
    small = Image.fromarray((mask_full * 255).astype(np.uint8)).resize(
        (max(4, int(W * k)), max(4, int(H * k))), Image.BOX)
    sm = np.array(small) > 20
    return dict(mask=sm, bbox=bbox, verdict=verdict, opaque=opaque_kind, transp_frac=transp_frac)


def boundary_points(sm):
    er = np.array(Image.fromarray((sm * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3))) > 127
    b = sm & ~er
    ys, xs = np.nonzero(b if b.any() else sm)
    h, w = sm.shape
    # pixel corners to be conservative
    px = np.concatenate([xs / w, (xs + 1) / w, xs / w, (xs + 1) / w])
    py = np.concatenate([ys / h, ys / h, (ys + 1) / h, (ys + 1) / h])
    return px, py


def all_points(sm):
    ys, xs = np.nonzero(sm)
    h, w = sm.shape
    return (xs + 0.5) / w, (ys + 0.5) / h


def map_pts(px, py, x, y, s, ar, pa):
    """image-normalized -> placeholder-normalized (u,v). Printify: x,y centre; scale = width/W."""
    return x + s * (px - 0.5), y + s * ar * pa * (py - 0.5)


def inside(mask, u, v):
    h, w = mask.shape
    ok = (u >= 0) & (u < 1) & (v >= 0) & (v < 1)
    iu = np.clip((u * w).astype(int), 0, w - 1)
    iv = np.clip((v * h).astype(int), 0, h - 1)
    return ok & mask[iv, iu]


def clip_report(px, py, x, y, s, ar, pa, bbox):
    """How far content bbox crosses each placeholder edge, as % of content size."""
    l, t, r, b = bbox
    u0, v0 = map_pts(np.array([l]), np.array([t]), x, y, s, ar, pa)
    u1, v1 = map_pts(np.array([r]), np.array([b]), x, y, s, ar, pa)
    u0, v0, u1, v1 = float(u0[0]), float(v0[0]), float(u1[0]), float(v1[0])
    cw, ch = u1 - u0, v1 - v0
    out = []
    if u0 < 0: out.append("left %.0f%%" % (100 * -u0 / cw))
    if u1 > 1: out.append("right %.0f%%" % (100 * (u1 - 1) / cw))
    if v0 < 0: out.append("top %.0f%%" % (100 * -v0 / ch))
    if v1 > 1: out.append("bottom %.0f%%" % (100 * (v1 - 1) / ch))
    return out, (u0, v0, u1, v1)


def optimise(variants, cinfo, ar, center_hint, cur):
    """Find max scale + (x,y) so content boundary is inside every variant's safe mask."""
    px, py = boundary_points(cinfo["mask"])
    l, t, r, b = cinfo["bbox"]
    cxi, cyi = (l + r) / 2, (t + b) / 2
    # minimal-change: prefer content centre near its current u, but inside the safe zone
    uc_cur = cur["x"] + cur["scale"] * (cxi - 0.5)
    uc0 = uc_cur if abs(uc_cur - center_hint) < 0.06 else center_hint
    ucs = np.unique(np.concatenate([uc0 + np.linspace(-0.06, 0.06, 9), [center_hint]]))
    vcs = np.linspace(-0.4, 1.4, 451)   # candidate y (image centre) values

    def feasible(s):
        best = None
        for uc in sorted(ucs, key=lambda q: abs(q - uc0)):
            x = uc - s * (cxi - 0.5)
            okv = np.ones(len(vcs), bool)
            for V in variants:
                u = x + s * (px - 0.5)
                h, w = V["mask"].shape
                if (u < 0).any() or (u >= 1).any():
                    okv[:] = False
                    break
                iu = (u * w).astype(int)
                # v for every candidate vc at once: vc + s*ar*pa*(py-cyi)
                vv = vcs[:, None] + s * ar * V["pa"] * (py[None, :] - 0.5)
                bad = (vv < 0) | (vv >= 1)
                iv = np.clip((vv * h).astype(int), 0, h - 1)
                okv &= ~(bad | ~V["mask"][iv, iu[None, :]]).any(1)
                if not okv.any():
                    break
            if okv.any():
                idx = np.nonzero(okv)[0]
                # minimal change: feasible y closest to the live y; but step 2 grid points
                # inward from the edge of the feasible run so rounding cannot push it out
                j = idx[np.argmin(np.abs(vcs[idx] - cur["y"]))]
                run = [k for k in idx if abs(k - j) <= 3]
                if len(run) >= 5:
                    j = min(max(j, min(run) + 2), max(run) - 2)
                vc = vcs[j]
                best = (x, vc, uc)
                break
        return best

    lo, hi = 0.0, float(cur["scale"])          # never enlarge beyond the live scale
    best = None
    f = feasible(hi)
    if f:
        return dict(x=round(f[0], 4), y=round(f[1], 4), scale=round(hi, 4), angle=0)
    for _ in range(16):
        mid = (lo + hi) / 2
        f = feasible(mid)
        if f:
            lo, best = mid, (mid, f)
        else:
            hi = mid
    if not best:
        return None
    s = math.floor(best[0] * 1000) / 1000          # round down = stays inside
    x, vc, uc = best[1]
    x = round(uc - s * (cxi - 0.5), 4)
    y = round(vc, 4)
    return dict(x=x, y=y, scale=s, angle=0)


def verify(variants, cinfo, ar, pl):
    """Dense check: every content pixel inside every variant's safe mask."""
    px, py = all_points(cinfo["mask"])
    res = []
    for V in variants:
        u, v = map_pts(px, py, pl["x"], pl["y"], pl["scale"], ar, V["pa"])
        ins = inside(V["mask"], u, v)
        res.append((V["vid"], float(ins.mean())))
    return res


# ---------------------------------------------------------------- rendering
def render(img, W, H, pl, smask, title, sub, color, size=560):
    pad = 0.18
    k = size / max(W, H)
    cw, ch = int(W * k), int(H * k)
    PX, PY = int(cw * pad) + 10, int(ch * pad) + 10
    canvas = Image.new("RGB", (cw + 2 * PX, ch + 2 * PY + 54), "white")
    d = ImageDraw.Draw(canvas)
    oy = 54
    # placeholder fill + outside-safe shading
    ph = Image.new("RGB", (cw, ch), (236, 236, 236))
    sm = Image.fromarray((smask * 255).astype(np.uint8)).resize((cw, ch), Image.NEAREST)
    ph.paste((246, 246, 246), mask=sm)
    canvas.paste(ph, (PX, PY + oy))
    # art
    rw = pl["scale"] * W * k
    rh = rw * img.height / img.width
    if rw >= 1 and rh >= 1:
        art = img.convert("RGBA").resize((max(1, int(rw)), max(1, int(rh))), Image.LANCZOS)
        ax = PX + pl["x"] * cw - art.width / 2
        ay = PY + oy + pl["y"] * ch - art.height / 2
        ghost = art.copy()
        ga = np.array(ghost.getchannel("A")).astype(float) * 0.22
        ghost.putalpha(Image.fromarray(ga.astype(np.uint8)))
        layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        layer.alpha_composite(ghost, (int(ax), int(ay)))
        clip = Image.new("L", canvas.size, 0)
        ImageDraw.Draw(clip).rectangle([PX, PY + oy, PX + cw - 1, PY + oy + ch - 1], fill=255)
        full = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        full.alpha_composite(art, (int(ax), int(ay)))
        fa = np.minimum(np.array(full.getchannel("A")), np.array(clip))
        full.putalpha(Image.fromarray(fa))
        base = canvas.convert("RGBA")
        base.alpha_composite(layer)
        base.alpha_composite(full)
        canvas = base.convert("RGB")
        d = ImageDraw.Draw(canvas)
    # dashed safe boundary
    smb = np.array(sm) > 127
    er = np.array(Image.fromarray(np.array(sm)).filter(ImageFilter.MinFilter(3))) > 127
    edge = smb & ~er
    ys, xs = np.nonzero(edge)
    dash = ((xs + ys) // 7) % 2 == 0
    arr = np.array(canvas)
    arr[ys[dash] + PY + oy, xs[dash] + PX] = (30, 90, 220)
    canvas = Image.fromarray(arr)
    d = ImageDraw.Draw(canvas)
    d.rectangle([PX - 1, PY + oy - 1, PX + cw, PY + oy + ch], outline=(220, 20, 20), width=3)
    d.rectangle([0, 0, canvas.width, 50], fill=color)
    d.text((8, 4), title, fill="white", font=font(18, True))
    d.text((8, 28), sub, fill="white", font=font(13))
    return canvas


def fit_h(im, h):
    return im.resize((max(1, int(im.width * h / im.height)), h), Image.LANCZOS)


# ---------------------------------------------------------------- main
def main():
    products = [json.loads(l) for l in open(os.path.join(ROOT, "products.jsonl"))]
    PH = json.load(open(os.path.join(ROOT, "placeholders.json")))
    rows = {r["product_id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "..", "artwork_redesign_batches.csv")))
            if r.get("batch") == "3"}
    shapes = {}
    for fn in os.listdir(os.path.join(ROOT, "_svg")):
        if fn.endswith(".svg"):
            shapes[fn[:-4]] = svg_shape(os.path.join(ROOT, "_svg", fn))

    out_rows, thumbs = [], []
    for p in products:
        pid = p["product_id"]
        row = rows.get(pid, {})
        title = row.get("title", "")
        seq = row.get("seq", "")
        cause = row.get("defect_cause", "")
        bp, pp = p["blueprint_id"], p["print_provider_id"]
        area = p["areas"][0]
        pos = area["position"]
        im0 = area["images"][0]
        deco = area.get("decoration") or p.get("decoration") or DECO_BY_BP.get(bp, "dye-sublimation")
        pdir = os.path.join(ROOT, pid)
        notes, status = [], None
        cur = dict(x=im0["x"], y=im0["y"], scale=im0["scale"], angle=im0.get("angle", 0))

        # ---- variants + placeholders
        pair = PH.get("%s/%s" % (bp, pp), {})
        keys = [k for k in pair if not k.startswith("_")]
        en = [str(v) for v in p.get("enabled_variants", [])]
        vids = [k for k in keys if k in en] if en and any(k in en for k in keys) else keys
        mock_vid = re.search(r"/mockup/[^/]+/(\d+)/", p.get("mockup_default", ""))
        mock_vid = mock_vid.group(1) if mock_vid else None
        if mock_vid in vids:
            vids.remove(mock_vid); vids.insert(0, mock_vid)
        variants, dup_vids = [], {}
        for vid in vids:
            dims = pair[vid].get(pos)
            if not dims:
                continue
            W, H = dims
            sid = (p.get("svgs") or {}).get(vid) or p.get("svg")
            shape = shapes.get(sid) if sid else None
            extra = None
            if bp in WRAP_BLUEPRINTS:
                extra = (WRAP_ZONE[0], WRAP_ZONE[1], 0, 1)
            if bp == 220 and shape and shape["polys"]:
                # two-face pillow sheet: keep design on the face it was placed on (x<0.5 -> left face)
                face = [pl_ for pl_ in shape["polys"] if (min(u for u, _ in pl_) < 0.5) == (cur["x"] < 0.5)]
                shape = dict(shape, polys=face[:1] if face else shape["polys"])
            if any(V["W"] == W and V["H"] == H and V["sid"] == sid for V in variants):
                dup_vids.setdefault((W, H, sid), []).append(vid)
                continue
            variants.append(dict(vid=vid, sid=sid, W=W, H=H, pa=W / H, shape=shape,
                                 mask=safe_mask(W, H, shape, extra=extra),
                                 safe_kind=(shape or {}).get("kind", "rect") if shape else "rect"))
        if not variants:
            status = "BLOCKED"; notes.append("no placeholder dims for %s" % pos)
        nchk = len(variants) + sum(len(v) for v in dup_vids.values())
        if nchk > 1:
            notes.append("geometry checked for %d enabled variants (%d distinct placeholder geometries)" % (nchk, len(variants)))

        # ---- original art
        orig = os.path.join(pdir, "original.png")
        img = None
        if os.path.exists(orig) and os.path.getsize(orig) > 0:
            try:
                img = Image.open(orig); img.load()
            except Exception as e:
                notes.append("original unreadable: %s" % e)
        else:
            notes.append("original not downloaded")
        if img is None:
            status = "BLOCKED"
        if img is not None and (img.width, img.height) != (im0["width"], im0["height"]):
            notes.append("downloaded size %sx%s != printify %sx%s" % (img.width, img.height, im0["width"], im0["height"]))

        rec = dict(product_id=pid, shop_id=p["shop_id"], title=title, blueprint_id=bp, print_provider_id=pp,
                   position=pos, image_id=im0["id"], image_name=im0["name"], image_src=im0["src"],
                   image_px=[im0["width"], im0["height"]], decoration_method=deco,
                   visible=p.get("visible"), updated_at=p.get("updated_at"), defect_cause=cause,
                   defect_note=row.get("defect_note", ""), current=cur)
        proposed, vres, clips, cinfo, transparency = None, [], [], None, ""
        if status != "BLOCKED":
            cinfo = content_info(img)
            transparency = cinfo["verdict"]
            ar = img.height / img.width
            V0 = variants[0]
            px, py = all_points(cinfo["mask"])
            clips, cur_box = clip_report(px, py, cur["x"], cur["y"], cur["scale"], ar, V0["pa"], cinfo["bbox"])
            cur_ver = verify(variants, cinfo, ar, cur)
            rec["content_bbox_norm"] = [round(z, 4) for z in cinfo["bbox"]]
            rec["current_content_box_in_placeholder"] = [round(z, 4) for z in cur_box]
            rec["current_inside_safe_frac"] = {v: round(f, 4) for v, f in cur_ver}
            # centre hint: safe-mask horizontal centre of primary variant
            cols = np.nonzero(V0["mask"].any(0))[0]
            hint = (cols.min() + cols.max() + 1) / 2 / V0["mask"].shape[1] if len(cols) else 0.5
            proposed = None if OVR.get(pid, {}).get("no_proposal") else optimise(variants, cinfo, ar, hint, cur)
            if proposed is None and OVR.get(pid, {}).get("no_proposal"):
                pass
            elif proposed is None:
                status = "BLOCKED"; notes.append("optimiser found no feasible placement")
            else:
                vres = verify(variants, cinfo, ar, proposed)
                # effective resolution: source px per placeholder px
                eff = min(img.width / (proposed["scale"] * V["W"]) for V in variants)
                rec["effective_px_ratio_after"] = round(eff, 3)
                if eff < 0.5:
                    notes.append("LOW-RES: art upscaled %.1fx on largest variant (src px/print px=%.2f)" % (1 / eff, eff))
            rec["proposed"] = proposed
            rec["placeholders"] = {V["vid"]: [V["W"], V["H"]] for V in variants}
            rec["safe_area_source"] = {V["vid"]: V["safe_kind"] for V in variants}
            rec["verify_inside_safe_frac"] = {v: round(f, 4) for v, f in vres}
            if any(cur_f < 0.999 for _, cur_f in cur_ver):
                worst = min(cur_ver, key=lambda q: q[1])
                notes.append("current: %.1f%% of visible content outside safe area (variant %s)" % (100 * (1 - worst[1]), worst[0]))
            else:
                notes.append("current placement already inside safe area on all checked variants")

        verify_pass = bool(vres) and all(f >= 0.999 for _, f in vres)
        if proposed is None:
            vres, verify_pass = [], False
        # ---- IP scan
        low = (title + " " + im0["name"]).lower()
        ip = sorted({IP_NOTES.get(t, "CHECK: '%s' in title/art name" % t) for t in IP_TERMS if re.search(r"\b%s\b" % re.escape(t), low)})
        ip_flag = "; ".join(ip) if ip else "none found (title/filename scan + visual check)"

        transparency_ok = "YES" if transparency.startswith("OK") else ("NO" if transparency else "")
        dark_substrate = deco in DARK_SUBSTRATE_METHODS

        # ---- status decisions
        if status != "BLOCKED":
            if cinfo and cinfo["opaque"] == "white" and dark_substrate:
                status = "NEEDS_NEW_ART"
                notes.insert(0, "art has opaque WHITE background on %s print over coloured blank -> visible white patch; "
                                "needs transparent re-export of same design (placement computed+verified, apply together)" % deco)
            elif not verify_pass:
                status = "BLOCKED"; notes.insert(0, "proposed placement failed geometry verify")
            else:
                status = "READY_FOR_REVIEW"
        if pid in OVR:
            notes.insert(0, OVR[pid]["note"])
            status = OVR[pid].get("status", status)
            if OVR[pid].get("no_proposal"):
                proposed = None

        rec.update(status=status, verify_pass=verify_pass, transparency=transparency,
                   ip_flag=ip_flag, clip_edges_current=clips, notes=notes,
                   live_change_made=False)
        with open(os.path.join(pdir, "placement.json"), "w") as f:
            json.dump(rec, f, indent=1)

        # ---- previews
        if status != "BLOCKED" or (img is not None and variants):
            V0 = variants[0]
            sub_b = "x=%.3f y=%.3f scale=%.3f | %s %sx%s | clip: %s" % (
                cur["x"], cur["y"], cur["scale"], pos, V0["W"], V0["H"], ", ".join(clips) or "none")
            bimg = render(img, V0["W"], V0["H"], cur, V0["mask"], "BEFORE (live)", sub_b, (150, 30, 30))
            bimg.save(os.path.join(pdir, "before_preview.png"))
            panels = [bimg]
            if proposed:
                sub_a = "x=%.3f y=%.3f scale=%.3f | verify %s" % (
                    proposed["x"], proposed["y"], proposed["scale"], "PASS" if verify_pass else "FAIL")
                aimg = render(img, V0["W"], V0["H"], proposed, V0["mask"], "AFTER (proposed, not live)", sub_a, (25, 110, 50))
                aimg.save(os.path.join(pdir, "after_preview.png"))
                panels.append(aimg)
            mk = os.path.join(pdir, "mockup_before.jpg")
            if os.path.exists(mk):
                try:
                    m = Image.open(mk).convert("RGB")
                    mh = panels[0].height
                    m = fit_h(m, mh - 54)
                    mp = Image.new("RGB", (m.width, mh), "white")
                    mp.paste(m, (0, 54))
                    ImageDraw.Draw(mp).rectangle([0, 0, mp.width, 50], fill=(70, 70, 70))
                    ImageDraw.Draw(mp).text((8, 14), "Live mockup (before)", fill="white", font=font(18, True))
                    panels.append(mp)
                except Exception as e:
                    notes.append("mockup unreadable: %s" % e)
            Hh = max(pn.height for pn in panels)
            panels = [pn if pn.height == Hh else fit_h(pn, Hh) for pn in panels]
            Wt = sum(pn.width for pn in panels) + 10 * (len(panels) - 1)
            sheet = Image.new("RGB", (Wt, Hh + 70), "white")
            dd = ImageDraw.Draw(sheet)
            dd.text((10, 6), "%s  [%s]  seq %s  bp %s/pp %s  %s" % (pid, status, seq, bp, pp, pos), fill="black", font=font(20, True))
            dd.text((10, 36), (title[:150]), fill=(60, 60, 60), font=font(15))
            xo = 0
            for pn in panels:
                sheet.paste(pn, (xo, 70)); xo += pn.width + 10
            sheet.save(os.path.join(pdir, "before_after.png"))
            thumbs.append((seq, pid, status, sheet))

        def fmt(pl):
            return "" if not pl else "x=%.4f;y=%.4f;scale=%.3f;angle=%s" % (pl["x"], pl["y"], pl["scale"], pl["angle"])
        out_rows.append(dict(
            seq=seq, product_id=pid, shop_id=p["shop_id"], title=title, blueprint_id=bp, position=pos,
            placeholder_wh=" | ".join("%s:%sx%s" % (V["vid"], V["W"], V["H"]) for V in variants),
            current_xyscale=fmt(cur), proposed_xyscale=fmt(proposed) if status != "BLOCKED" else "",
            clip_edges=", ".join(clips) or ("none (rect)" if cinfo else ""),
            verify_pass="PASS" if verify_pass else ("FAIL" if proposed else "N/A"),
            transparency_ok=transparency_ok + (" - " + transparency if transparency_ok == "NO" else ""),
            ip_flag=ip_flag, status=status, notes=" | ".join(n for n in notes if n)))
        print(pid, status, fmt(cur), "->", fmt(proposed), "verify", verify_pass, "|", "; ".join(clips))

    return out_rows, thumbs


OVR = json.load(open(os.path.join(ROOT, "overrides.json"))) if os.path.exists(os.path.join(ROOT, "overrides.json")) else {}


def write_outputs(out_rows, thumbs, start, end):
    fn = os.path.join(ROOT, "batch3_results.csv")
    with open(fn, "w", newline="") as f:
        f.write("# D6 artwork-repair Batch 3 - NON-LIVE prep. start_utc=%s end_utc=%s. No Printify writes performed.\n" % (start, end))
        w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        for r in sorted(out_rows, key=lambda r: int(r["seq"] or 0)):
            w.writerow(r)
    thumbs.sort(key=lambda t: int(t[0] or 0))
    TW, cols, per = 760, 3, 21
    for si in range(0, len(thumbs), per):
        chunk = thumbs[si:si + per]
        tiles = []
        for seq, pid, st, sh in chunk:
            t = sh.copy(); t.thumbnail((TW, 420))
            tile = Image.new("RGB", (TW, 450), "white")
            tile.paste(t, (0, 30))
            col = {"READY_FOR_REVIEW": (25, 110, 50), "NEEDS_NEW_ART": (190, 120, 0), "BLOCKED": (150, 30, 30)}.get(st, (0, 0, 0))
            ImageDraw.Draw(tile).rectangle([0, 0, TW, 26], fill=col)
            ImageDraw.Draw(tile).text((6, 3), "#%s %s  %s" % (seq, pid, st), fill="white", font=font(16, True))
            tiles.append(tile)
        rows_n = math.ceil(len(tiles) / cols)
        cs = Image.new("RGB", (cols * TW + (cols + 1) * 8, rows_n * 458 + 50), (225, 225, 225))
        ImageDraw.Draw(cs).text((10, 12), "D6 Batch 3 artwork repair - BEFORE (live) / AFTER (proposed, NOT live) / live mockup  - sheet %d" % (si // per + 1),
                                fill="black", font=font(20, True))
        for i, tile in enumerate(tiles):
            cs.paste(tile, (8 + (i % cols) * (TW + 8), 50 + (i // cols) * 458))
        cs.save(os.path.join(ROOT, "contact_sheet_%d.png" % (si // per + 1)))


if __name__ == "__main__":
    start = sys.argv[1] if len(sys.argv) > 1 else ""
    rows_, thumbs_ = main()
    import datetime
    end = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    write_outputs(rows_, thumbs_, start, end)
    print("wrote", len(rows_), "rows")
