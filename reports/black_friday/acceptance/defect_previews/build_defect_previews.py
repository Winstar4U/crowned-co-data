"""Task C: offline defect previews from LOCAL evidence only (no API calls, nothing applied).

Outputs (in this folder):
  <id>_proposed_art.png / <id>_proposed_placement.json
  <id>_before_after.png
  ../defect_previews.csv
"""
import csv, json, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = "/home/user/crowned-co-data"
OUT = os.path.dirname(os.path.abspath(__file__))
EV = f"{ROOT}/reports/black_friday/wave2/evidence"
SAFE = 0.05  # 5% safe-area inset, same rule as work/d6_* placement.json


def font(sz):
    for f in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if os.path.exists(f):
            return ImageFont.truetype(f, sz)
    return ImageFont.load_default()


def rel_lum(rgb):
    c = np.asarray(rgb, dtype=float) / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def contrast(a, b):
    la, lb = float(rel_lum(a)), float(rel_lum(b))
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def sample_blank(path, pts):
    im = Image.open(path).convert("RGB")
    px = np.array([im.getpixel(p) for p in pts], dtype=float)
    return tuple(int(round(v)) for v in px.mean(axis=0))


def inside_safe_frac(mask, iw, ih, pw, ph, x, y, scale):
    """Pixel-based: fraction of content pixels whose placeholder position lies inside the 5% safe rect.
    Printify convention: scale = art width / placeholder width; (x, y) = art centre, normalised."""
    aw = scale * pw
    ah = aw * ih / iw
    ys, xs = np.nonzero(mask)
    px = x * pw + (xs + 0.5) / iw * aw - aw / 2
    py = y * ph + (ys + 0.5) / ih * ah - ah / 2
    ok = (px >= SAFE * pw) & (px <= (1 - SAFE) * pw) & (py >= SAFE * ph) & (py <= (1 - SAFE) * ph)
    vis = (px >= 0) & (px <= pw) & (py >= 0) & (py <= ph)
    return float(ok.mean()), float(vis.mean()), aw, ah


def label(img, lines, h=None):
    f = font(24)
    W = max(img.width, max(int(f.getlength(t)) for t in lines) + 30)
    h = h or 34 * len(lines) + 16
    canvas = Image.new("RGB", (W, img.height + h), (255, 255, 255))
    canvas.paste(img, (0, h))
    d = ImageDraw.Draw(canvas)
    f = font(24)
    for i, t in enumerate(lines):
        d.text((12, 8 + 34 * i), t, fill=(0, 0, 0), font=f)
    return canvas


def on_blank(art_rgba, blank, size=700):
    a = art_rgba.copy()
    a.thumbnail((size - 80, size - 80))
    bg = Image.new("RGBA", (size, size), blank + (255,))
    bg.alpha_composite(a, ((size - a.width) // 2, (size - a.height) // 2))
    return bg.convert("RGB")


def side_by_side(left, right, ltxt, rtxt):
    f = font(26)
    W = left.width + right.width + 30
    H = max(left.height, right.height) + 50
    c = Image.new("RGB", (W, H), (255, 255, 255))
    c.paste(left, (0, 50)); c.paste(right, (left.width + 30, 50))
    d = ImageDraw.Draw(c)
    d.text((10, 10), ltxt, fill=(160, 0, 0), font=f)
    d.text((left.width + 40, 10), rtxt, fill=(0, 110, 0), font=f)
    return c


rows = []

# ---------------------------------------------------------------- 1. Dear Santa shorts
pid = "6ac70ec09a2f0cb82508f89a"
src = f"{ROOT}/work/d6_batch1/{pid}"
pl = json.load(open(f"{src}/placement.json"))
art = Image.open(f"{src}/original.png").convert("RGBA")
A = np.array(art).astype(int)
iw, ih = art.size
r, g, b, al = A[..., 0], A[..., 1], A[..., 2], A[..., 3]
mx, mn = np.maximum(np.maximum(r, g), b), np.minimum(np.minimum(r, g), b)
dark = (al > 0) & (mx < 90) & ((mx - mn) < 40)            # near-black neutral ink
band = np.zeros_like(dark); band[: int(0.40 * ih), :] = True   # text band (SAYS + underline strokes)
band[int(0.33 * ih):, int(0.42 * iw):] = False                  # keep Santa-hat outline untouched
recol = dark & band
says_box = (slice(int(0.27 * ih), int(0.40 * ih)), slice(int(0.12 * iw), int(0.45 * iw)))
says_mask = dark[says_box]
says_rgb = tuple(int(v) for v in A[says_box][..., :3][says_mask].mean(axis=0))
CREAM = (245, 240, 228)
B = A.copy()
B[recol, 0], B[recol, 1], B[recol, 2] = CREAM
# 3 px soft cream halo around SAYS-band strokes so the word separates from any dark blank
from PIL import ImageFilter
halo = Image.fromarray((recol * 255).astype("uint8")).filter(ImageFilter.MaxFilter(7))
halo = np.array(halo) > 0
add = halo & ~recol & (B[..., 3] < 255)
B[add, 0], B[add, 1], B[add, 2], B[add, 3] = CREAM[0], CREAM[1], CREAM[2], 255
prop = Image.fromarray(B.astype("uint8"), "RGBA")
prop.save(f"{OUT}/{pid}_proposed_art_dark_blanks.png")
blank_black = sample_blank(f"{EV}/{pid}_live_front-left-leg_Black.jpg", [(400, 400), (600, 300), (300, 800), (450, 600)])
cr_before = contrast(says_rgb, blank_black)
cr_after = contrast(CREAM, blank_black)
mask = A[..., 3] > 0
pw, ph = pl["placeholders"]["*"]
safe, vis, aw, ah = inside_safe_frac(mask, iw, ih, pw, ph, 0.5, 0.5, 0.7)
ratio = iw / aw
img = side_by_side(on_blank(art, blank_black), on_blank(prop, blank_black),
                   "BEFORE: live art on Black", "AFTER (proposal): cream SAYS + halo")
img = label(img, [f"{pid}  Dear Santa shorts (Shopify shop 26418699) - LOCAL EVIDENCE ONLY, NOT APPLIED",
                  f"'SAYS' contrast vs Black blank {blank_black}: before {cr_before:.2f}:1 -> after {cr_after:.2f}:1 (WCAG large-text min 3:1)",
                  f"placement unchanged x0.5 y0.5 scale0.7 | inside 5% safe area {safe*100:.1f}% | art px per placeholder px {ratio:.2f}"])
img.save(f"{OUT}/{pid}_before_after.png")
rows.append(dict(product_id=pid, product="Dear Santa Bank Account shorts", shop_id="26418699",
                 issue="black 'SAYS' + underline strokes invisible on dark blanks (Black/Shadow/Ink Blue)",
                 proposal="dark-blank art variant: near-black neutral ink in the top text band recoloured to cream #F5F0E4 with a 3 px cream halo; pig/holly line art untouched; placement unchanged",
                 proposal_file=f"defect_previews/{pid}_proposed_art_dark_blanks.png",
                 before_after_png=f"defect_previews/{pid}_before_after.png",
                 text_colour_before=str(says_rgb), text_colour_after=str(CREAM),
                 blank_colour=f"Black {blank_black} sampled from live mockup; Shadow and Ink Blue NOT measured (no local hex)",
                 contrast_before=f"{cr_before:.2f}", contrast_after=f"{cr_after:.2f}",
                 inside_safe_before_pct=f"{safe*100:.1f}", inside_safe_after_pct=f"{safe*100:.1f}",
                 effective_dpi=f"{ratio*300:.0f} (assumes Printify 300 px/in placeholder convention; UNVERIFIED for blueprint 10796) | art:placeholder px {ratio:.2f}",
                 native_dpi="not embedded in PNG (1679x1898 px)",
                 status="WARN",
                 status_reason="Contrast fixed on Black (measured). Shadow/Ink Blue blank colours unmeasured; recoloured art must be assigned only to dark variants (light variants not enabled). Needs owner approval to replace live art."))

# ---------------------------------------------------------------- 2. Stress/Tinsel tank
pid = "6ac71018e2a15b12600266b5"
src = f"{ROOT}/work/d6_batch2/{pid}"
pl = json.load(open(f"{src}/placement.json"))
art = Image.open(f"{src}/original.png").convert("RGBA")
A = np.array(art).astype(float)
iw, ih = art.size
alpha = A[..., 3] > 0
blank_black = sample_blank(f"{EV}/{pid}_live_front_Black.jpg", [(450, 850), (750, 850), (600, 300), (300, 700)])
# line bands measured on the art (top->bottom): CHRISTMAS/2026 plum, 90%/10% green, 100% DONE dark green
bands = {"'CHRISTMAS 2026:' (plum)": (0.13, 0.33), "'90% STRESS, 10% TINSEL,' (green)": (0.33, 0.62),
         "'100% DONE.' (dark green)": (0.62, 0.72)}
K = 0.62  # lighten toward white, hue kept
B = A.copy()
B[..., :3] = np.where(alpha[..., None], A[..., :3] + (255 - A[..., :3]) * K, A[..., :3])
prop = Image.fromarray(B.astype("uint8"), "RGBA")
prop.save(f"{OUT}/{pid}_proposed_art_light_ink.png")
cr = []
for name, (y0, y1) in bands.items():
    sl = (slice(int(y0 * ih), int(y1 * ih)), slice(0, iw))
    m = alpha[sl] & (A[sl][..., 3] > 200)
    c0 = tuple(int(v) for v in A[sl][..., :3][m].mean(axis=0))
    c1 = tuple(int(v) for v in B[sl][..., :3][m].mean(axis=0))
    cr.append((name, c0, c1, contrast(c0, blank_black), contrast(c1, blank_black)))
worst_b = min(c[3] for c in cr); worst_a = min(c[4] for c in cr)
mask = A[..., 3] > 0
res = []
for vid, (pw, ph) in pl["placeholders"].items():
    s, v, aw, ah = inside_safe_frac(mask, iw, ih, pw, ph, 0.5, 0.38, 0.9)
    res.append((vid, s, iw / aw))
safe = min(r_[1] for r_ in res); ratio = min(r_[2] for r_ in res)
img = side_by_side(on_blank(art, blank_black), on_blank(prop, blank_black),
                   "BEFORE: live art on Black", "AFTER (proposal): light-ink variant")
img = label(img, [f"{pid}  Stress/Tinsel tank (Shopify shop 26418699) - LOCAL EVIDENCE ONLY, NOT APPLIED",
                  "worst line contrast vs Black " + f"{blank_black}: before {worst_b:.2f}:1 -> after {worst_a:.2f}:1",
                  " | ".join(f"{n.split(' (')[0]} {b:.1f}->{a:.1f}" for n, _, _, b, a in cr),
                  f"placement unchanged x0.5 y0.38 scale0.9 | inside safe (worst of 3 sizes) {safe*100:.1f}% | art px per placeholder px {ratio:.2f}",
                  "NOTE: art shows a wine glass (alcohol) - excluded from promo creative regardless of fix"])
img.save(f"{OUT}/{pid}_before_after.png")
rows.append(dict(product_id=pid, product="Christmas Stress Tinsel Done tank", shop_id="26418699",
                 issue="dark plum/green text low contrast on the 4 enabled Black variants",
                 proposal="light-ink art variant for Black: every ink pixel lightened 62% toward white (hue kept); placement unchanged; optional: fix stray opening quote mark",
                 proposal_file=f"defect_previews/{pid}_proposed_art_light_ink.png",
                 before_after_png=f"defect_previews/{pid}_before_after.png",
                 text_colour_before="; ".join(f"{n}:{c0}" for n, c0, _, _, _ in cr),
                 text_colour_after="; ".join(f"{n}:{c1}" for n, _, c1, _, _ in cr),
                 blank_colour=f"Black {blank_black} sampled from live mockup",
                 contrast_before=f"{worst_b:.2f} (worst line)", contrast_after=f"{worst_a:.2f} (worst line)",
                 inside_safe_before_pct=f"{safe*100:.1f}", inside_safe_after_pct=f"{safe*100:.1f}",
                 effective_dpi=f"{ratio*300:.0f} worst size (assumes 300 px/in placeholder convention; UNVERIFIED for blueprint 39) | art:placeholder px {ratio:.2f}",
                 native_dpi="not embedded in PNG (1702x2048 px)",
                 status="PASS" if worst_a >= 4.5 else "WARN",
                 status_reason="Contrast >= 4.5:1 on Black for every line after fix (measured). White variants keep original art. Alcohol motif: do not promote. Needs owner approval to replace live art."))

# ---------------------------------------------------------------- 3/4. canvases
for pid, d, name in [("6ac702e21e2eac4da206fc57", "d6_batch2", "Christ Is Born canvas 16x12"),
                     ("6ac702d43fd8c86beb0f48b1", "d6_batch3", "Keep Christ Christmas canvas 16x12")]:
    src = f"{ROOT}/work/{d}/{pid}"
    pl = json.load(open(f"{src}/placement.json"))
    art = Image.open(f"{src}/original.png").convert("RGB")
    A = np.array(art).astype(int)
    iw, ih = art.size
    mask = A.min(axis=2) < 235                   # content = non-white pixels (art bg is white)
    pw, ph = pl["placeholders"]["82220"]
    cur = pl["current"]; pro = pl["proposed"]
    s0, v0, aw0, _ = inside_safe_frac(mask, iw, ih, pw, ph, cur["x"], cur["y"], cur["scale"])
    s1, v1, aw1, _ = inside_safe_frac(mask, iw, ih, pw, ph, pro["x"], pro["y"], pro["scale"])
    dpi0 = iw / (aw0 / 300.0); dpi1 = iw / (aw1 / 300.0)   # 4800x3600 placeholder = 16x12 in -> 300 px/in

    def render(p):
        S = 0.125
        cw, chh = int(pw * S), int(ph * S)
        c = Image.new("RGB", (cw, chh), (255, 255, 255))
        aw = p["scale"] * pw * S; ah = aw * ih / iw
        a = art.resize((int(aw), int(ah)))
        c.paste(a, (int(p["x"] * cw - aw / 2), int(p["y"] * chh - ah / 2)))
        dr = ImageDraw.Draw(c)
        dr.rectangle([0, 0, cw - 1, chh - 1], outline=(0, 0, 0), width=3)
        dr.rectangle([SAFE * cw, SAFE * chh, (1 - SAFE) * cw, (1 - SAFE) * chh], outline=(0, 160, 255), width=2)
        return c
    img = side_by_side(render(cur), render(pro), f"BEFORE: scale {cur['scale']} (print window)",
                       f"AFTER (proposal): x{pro['x']} y{pro['y']} scale{pro['scale']}")
    img = label(img, [f"{pid}  {name} (Shopify shop 26418699) - LOCAL EVIDENCE ONLY, NOT APPLIED",
                      f"content inside 5% safe area (blue): {s0*100:.1f}% -> {s1*100:.1f}% | content visible in print window: {v0*100:.1f}% -> {v1*100:.1f}%",
                      f"effective dpi at 16x12 in: {dpi0:.0f} -> {dpi1:.0f} (native: not embedded; 2048x2048 px) | white side bands blend with white canvas"])
    img.save(f"{OUT}/{pid}_before_after.png")
    json.dump({"product_id": pid, "variant": 82220, "current": cur, "proposed": pro,
               "source": f"work/{d}/{pid}/placement.json", "applied": False},
              open(f"{OUT}/{pid}_proposed_placement.json", "w"), indent=1)
    rows.append(dict(product_id=pid, product=name, shop_id="26418699",
                     issue=f"art cropped at scale 1.0 ({', '.join(pl['clip_edges_current'])})",
                     proposal=f"re-scale x{pro['x']} y{pro['y']} scale{pro['scale']} (from placement.json)",
                     proposal_file=f"defect_previews/{pid}_proposed_placement.json",
                     before_after_png=f"defect_previews/{pid}_before_after.png",
                     text_colour_before="n/a", text_colour_after="n/a",
                     blank_colour="white canvas; art background #FFFFFF (white on white)",
                     contrast_before="n/a", contrast_after="n/a",
                     inside_safe_before_pct=f"{s0*100:.1f}", inside_safe_after_pct=f"{s1*100:.1f}",
                     effective_dpi=f"{dpi0:.0f} -> {dpi1:.0f} (16x12 in; 4800 px placeholder = 300 px/in)",
                     native_dpi="not embedded in PNG (2048x2048 px)",
                     status="PASS" if s1 >= 0.999 and dpi1 >= 150 else "WARN",
                     status_reason=("Proposed placement 100% inside safe area and >=150 dpi effective. " if s1 >= 0.999 and dpi1 >= 150 else "Inside safe area but effective dpi below 150; consider 4:3 re-export / upscale. ")
                     + "Leaves white side bands (square art on 4:3 canvas). Needs owner approval before applying."))

with open(f"{OUT}/../defect_previews.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) + ["applied"])
    w.writeheader()
    for r_ in rows:
        r_["applied"] = "NO (preview only)"
        w.writerow(r_)
for r_ in rows:
    print(r_["product_id"], r_["status"], r_["contrast_before"], r_["contrast_after"], r_["inside_safe_before_pct"], r_["inside_safe_after_pct"], r_["effective_dpi"][:40])
