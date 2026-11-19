"""Build the Winstar five-shop SELL NOW / REPAIR FIRST / HOLD / UNKNOWN register.

Inputs (read-only):
  - reports/Winstar_Five_Shop_Quality_Register.md  (visual-inspection evidence, per-ID rows)
  - reports/Winstar_Tapestry_Pricing_Correction_Table.csv (48 tapestry IDs, pricing)
  - reports/Winstar_Tapestry_Duffel_Profitability_Evidence.md (45 duffel IDs)
  - live Printify product pulls (full JSON) for Amazon, TikTok, Etsy, saved in a
    scratch directory passed as argv[1]  (amzF*.json, tt*.json, et_*.json)

Output: reports/Winstar_Sales_Readiness_Register.csv
No Printify writes are made by this script.
"""
import csv, glob, json, os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REP = os.path.join(ROOT, "reports")
LIVE = sys.argv[1]

SHOP_ID = {"Shopify": "26418699", "Etsy": "26603005", "eBay": "28059412",
           "TikTok": "28122957", "Amazon": "29451844"}

HOLIDAY = re.compile(r"christmas|xmas|holiday|santa|reindeer|\belf\b|\belves\b|snow|winter|ornament|"
                     r"stocking|naughty|nice list|noel|jingle|gingerbread|grinch|mistletoe|"
                     r"thanksgiving|new year|hanukkah|nativity|merry|festive|sleigh|candy cane", re.I)

# ---------- fixed sets from existing, owner-acknowledged evidence ----------
REMOVED = {  # not on sale any more (owner-approved removals / drafts / deleted / unpurchasable originals)
    # alcohol art on Youth Hoodie / Baby Onesie -- owner said "Remove", confirmed gone
    "6ac712026356cae0df02e31c", "6ac711e03925bc76b903727e", "6ac711fea005c19c550d898b",
    "6ac711cec077332834034d2e", "6ac711ab336f8358660114d1", "6ac7118fc077332834034cfd",
    "6ac70fecb8d5d3e71901300d", "6ac70fe9b8d5d3e71901300a", "6ac70fd0e2a15b1260026691",
    "6ac70fbf35a66ab7dc0b0e9b", "6ac70f9c35a66ab7dc0b0e86", "6ac7114807e4149a0f000fef",
    "6ac7108350fc6704d30bf899", "6ac7108007e4149a0f000f4e", "6ac7105707e4149a0f000f3b",
    # checkerboard unfixable pair -- unpublished
    "6ac358c152f41a8eba0998f5", "6ac356ae2776a7c47f00ee18",
    # Etsy ornament "set of 3" -- drafted
    "6ad42970f1aeec4b590f6d00",
    # discontinued thong blueprint originals (0 enabled variants) -- replaced by briefs
    "69c7630e3acff09c580c3072", "69c75c408ac9a0544a0ebe6d",
    "69c9a9a77ee2f2859c094675", "69c9a9993f8316381202aff5",
}
MIGRATED_BRIEFS = {"6afdabe964b943792d07d418": "Shopify", "6afdac2c1cb1d74e0a01c2d0": "Shopify",
                   "6afe010c38c1616cec0c3e4e": "Etsy", "6afe01111c59c096c3040444": "Etsy"}
CHECKERBOARD_BLOCKED = {
    "6ac356114cb82ddd30035d42", "6ac3591601306e9d6b0a9e79", "6ac35b8805e1de1c0a035dab",
    "6ac35b41ebbf38f6ec068fcb", "6ac3598debbf38f6ec068ec0", "6ac357bca84c54ac7608ab2b",
    "6ac35777f3e4f34bd106b543", "6ac3564b2070a33916078c17", "6ac35b0040c9c50ac20245c4",
    "6ac35801f0b487d2be06631b"}
UNMAPPED_DUFFELS = {"6ac70ec73925bc76b9037099", "6ac70ed8050d0f25a70917f4", "6ac70ee24bfa32451c0548b1",
                    "6ac70ee64bfa32451c0548b6", "6ac70eed0aa3686f380d3c23"}
TEXACO = "6a53ee979296b919210641d5"
EXTRA_DEFECTS = {  # confirmed in register §3 but not tagged "DEFECT" in a table row
    "6ad4254232b024bb32043467": ("Etsy", "Cribbage Board Christmas Tree Ornament",
                                 "Photo over-scaled 1.45x: star topper and board edges cropped; fix = scale 0.8 (matches clean Shopify copy)"),
    "6ac8f919149425f38d04bedd": ("Shopify", "Dracula With A Drink Halloween Ornament",
                                 "Illustration cropped at left/bottom edge"),
    "6ac8f8f29b2660e139034102": ("Shopify", "Basic Witch Halloween Ornament",
                                 "'B' and 'C' of text clipped by circular edge"),
}
AMAZON_DUP_IDS = {  # 7 both-live pairs, owner decision 11-18: keep all
    "6ae414e52e006c787106bd99", "6ae2af0ed0738075d402e2b2", "6ae414e42e006c787106bd98",
    "6ae2af10bcfc422d820a54c7", "6ae414e42e006c787106bd97", "6ae2af13bcfc422d820a54cb",
    "6ae414e12e006c787106bd94", "6ae2af12bcfc422d820a54ca", "6ae414e72e006c787106bd9b",
    "6ae2af10bcfc422d820a54c8", "6ae414e22e006c787106bd95", "6ae2af15bcfc422d820a54cc",
    "6ae414e32e006c787106bd96", "6ae2af11bcfc422d820a54c9"}

tapestry = {}
with open(os.path.join(REP, "Winstar_Tapestry_Pricing_Correction_Table.csv")) as f:
    for r in csv.DictReader(f):
        tapestry.setdefault(r["product_id"], r["design"])
evid = open(os.path.join(REP, "Winstar_Tapestry_Duffel_Profitability_Evidence.md")).read().splitlines()
duffels = set(re.findall(r"[0-9a-f]{24}", "\n".join(evid[48:110])))

# ---------- parse visual-inspection evidence rows from the register ----------
def shop_of(h):
    hl = h.lower()
    for k, v in (("amazon", "Amazon"), ("## 8a", "Amazon"), ("tiktok", "TikTok"), ("ebay", "eBay"),
                 ("etsy", "Etsy"), ("shopify", "Shopify")):
        if k in hl:
            return v
    return None

recs = {}
cur = None
for i, line in enumerate(open(os.path.join(REP, "Winstar_Five_Shop_Quality_Register.md")), 1):
    if line.startswith("## "):
        cur = shop_of(line)
        continue
    m = re.match(r"^\|?\s*`?([0-9a-f]{24})`?\s*\|", line)
    if not m:
        continue
    cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
    status = title = url = None
    for x in cells[1:]:
        k = x.lstrip("*")
        if status is None and re.match(r"^(CLEAN|DEFECT|MINOR|BRAND|TRUE_DUP|DUP)", k):
            status = x.strip("*")
        elif url is None and x.startswith("http"):
            url = x
        elif title is None and not x.startswith("http"):
            title = x
    if status is None:
        continue
    shop = cur or ("Shopify" if "Winstar4U" in line else None)
    recs.setdefault(cells[0], []).append(dict(line=i, shop=shop, title=title, status=status, url=url))

# ---------- live Printify pulls ----------
live = {}
for pat, shop in (("amzF*.json", "Amazon"), ("tt*.json", "TikTok"), ("et_*.json", "Etsy")):
    for fn in glob.glob(os.path.join(LIVE, pat)):
        for p in json.load(open(fn))["data"]:
            e = p.get("external") or {}
            en = [v for v in p["variants"] if v.get("is_enabled")]
            prices = sorted({v["price"] for v in en})
            live[p["id"]] = dict(shop=shop, title=p["title"], handle=e.get("handle") or "",
                                 ext_id=e.get("id") or "", visible=p.get("visible"),
                                 enabled=len(en), price_min=prices[0] / 100 if prices else None,
                                 price_max=prices[-1] / 100 if prices else None)

def link_for(pid, shop):
    lv = live.get(pid)
    if not lv or not lv["handle"]:
        return ""
    h = lv["handle"]
    if shop == "Amazon":
        return f"https://www.amazon.com/dp/{h}"
    return h  # Etsy: public listing URL; TikTok: seller-center product URL

rows = []
seen = set()

def add(pid, shop, title, bucket, reason, action, evidence, flags=""):
    if pid in seen:
        return
    seen.add(pid)
    lv = live.get(pid, {})
    rows.append(dict(
        bucket=bucket, product_id=pid, shop=shop, shop_id=SHOP_ID.get(shop, ""),
        title=(lv.get("title") or title or "")[:140],
        holiday="Y" if HOLIDAY.search((lv.get("title") or title or "")) else "",
        channel_link=link_for(pid, shop),
        price_range=(f"${lv['price_min']:.2f}-${lv['price_max']:.2f}" if lv.get("price_min") is not None else ""),
        reason=reason, proposed_correction=action, flags=flags, evidence=evidence))

# 1. special, owner-known items first
for pid in REMOVED:
    add(pid, recs.get(pid, [{}])[-1].get("shop") or ("Etsy" if pid.startswith(("69c9a9", "6ad429")) else "Shopify"),
        (recs.get(pid, [{}])[-1].get("title")), "REMOVED",
        "Already off sale per owner decision (removed, unpublished, drafted, or unpurchasable original)",
        "None", "Register: OWNER DECISIONS / LIVE POLICY ACTION / Thong migration sections")
for pid, shop in MIGRATED_BRIEFS.items():
    add(pid, shop, "Women's Panties (migrated from discontinued thong blueprint)", "SELL NOW",
        "Migrated to Women's Briefs AOP, mockup verified clean, published 2026-11-18",
        "None", "Register: THONG LISTINGS FIXED / ETSY THONG PAIR MIGRATED")
for pid, design in tapestry.items():
    add(pid, "Shopify", f"{design} Wall Tapestry", "REPAIR FIRST",
        "Artwork fixed and live, but 68x80 and 88x104 sizes sell below cost (lose $5.06 and $16.63/unit before shipping)",
        "Reprice per owner choice (Scenario A or B) or disable large sizes -- DECISION D1",
        "Winstar_Tapestry_Pricing_Correction_Table.csv", "PRICE_LOSS")
for pid in duffels:
    if pid in UNMAPPED_DUFFELS:
        add(pid, "Shopify", "Duffel Bag", "UNKNOWN",
            "Artwork fixed; Printify record has no sales-channel link -- may not be listed on Shopify",
            "Owner checks Shopify admin; then approve re-publish/re-link -- DECISION D3",
            "Winstar_Tapestry_Duffel_Profitability_Evidence.md", "NO_CHANNEL_LINK")
    else:
        add(pid, "Shopify", "Duffel Bag", "SELL NOW",
            "Artwork fixed + verified live (45/45); margin 45-50% cost-vs-price",
            "None", "Winstar_Tapestry_Duffel_Profitability_Evidence.md; register DUFFEL BAG FINAL CLOSURE")
for pid in CHECKERBOARD_BLOCKED:
    add(pid, "Shopify", (recs.get(pid, [{}])[-1].get("title")) or "Checkerboard-background T-shirt", "REPAIR FIRST",
        "Live listing still shows checkerboard background; corrected art staged but Printify rejects the swap (48 retired variant IDs)",
        "Owner files Printify support ticket (packet ready) -- DECISION D4; then approved swap-in runs",
        "Printify_Support_Packet_Checkerboard_Legacy_Variants.md", "PLATFORM_BLOCKED")
add(TEXACO, "Etsy", "Matte Canvas, Framed (TEXACO gas station art)", "HOLD",
    "Live TEXACO (Chevron-registered) trademark artwork; owner chose to keep listing on 2026-11-18",
    "Do not promote. Owner may revisit: unpublish or replace art -- DECISION D7 (optional)",
    "Register: POLICY VIOLATION REVIEW Item 2", "IP_RISK_OWNER_ACCEPTED")
for pid, (shop, title, why) in EXTRA_DEFECTS.items():
    add(pid, shop, title, "REPAIR FIRST", why, "Rescale print area; regenerate mockup; owner approves live edit -- DECISION D6",
        "Register §2-§3 (mockup viewed)", "CUSTOMER_FACING_DEFECT")

# 2. everything else with inspection evidence
for pid, occ in recs.items():
    last = occ[-1]
    shop = last["shop"] or "Shopify"
    statuses = [o["status"] for o in occ]
    defect = next((s for s in statuses if s.startswith(("DEFECT", "MINOR", "BRAND"))), None)
    ev = f"Quality register line {last['line']}" + (f"; mockup {last['url']}" if last.get("url") else "")
    dup = any("DUP" in s for s in statuses)
    flags = "DUPLICATE_LISTING" if dup else ""
    if defect:
        add(pid, shop, last["title"], "REPAIR FIRST", defect[:160],
            "Correct artwork placement/source file, re-verify mockup, owner approves live edit -- DECISION D6",
            ev, (flags + " CUSTOMER_FACING_DEFECT").strip())
        continue
    # clean on visual inspection
    if shop == "eBay":
        add(pid, shop, last["title"], "UNKNOWN",
            "Artwork clean, but Printify has no eBay listing link (53/53); listing status unconfirmed",
            "Owner exports eBay active listings (or confirms none) -- DECISION D5", ev, flags)
    elif shop in ("Etsy", "TikTok", "Amazon"):
        if link_for(pid, shop):
            add(pid, shop, last["title"], "SELL NOW", "Artwork clean on real mockup; live channel link present",
                "None", ev, flags)
        else:
            add(pid, shop, last["title"], "UNKNOWN",
                "Artwork clean, but no channel link in Printify; listing status unconfirmed",
                "Confirm in channel dashboard; re-publish only with owner approval", ev, flags)
    else:  # Shopify
        add(pid, shop, last["title"], "SELL NOW",
            "Artwork clean on real mockup (full-visual sweep #361-2,429)",
            "None (storefront link pull pending -- next task)", ev, flags)

# 3. live-pull products not in register evidence (Amazon has no per-ID table; new Etsy items)
for pid, lv in live.items():
    if pid in seen:
        continue
    shop = lv["shop"]
    flags = "AMAZON_DUP_PAIR_OWNER_KEPT" if pid in AMAZON_DUP_IDS else ""
    if shop == "Amazon":
        if lv["handle"]:
            add(pid, shop, lv["title"], "SELL NOW",
                "Amazon shop 62/62 visually inspected, 0 artwork defects (register §8a); ASIN linked",
                "None", "Register §8a + live Printify pull 2026-11-19", flags)
        else:
            add(pid, shop, lv["title"], "UNKNOWN",
                "Artwork clean (register §8a) but no ASIN linked in Printify; listing status unconfirmed",
                "Owner exports Seller Central inventory -- DECISION D5", "Register §8a + live Printify pull 2026-11-19", flags)
    else:
        add(pid, shop, lv["title"], "UNKNOWN", "Not covered by an inspection row in the register",
            "Visual-inspect before promoting", "live Printify pull 2026-11-19")

order = {"SELL NOW": 0, "REPAIR FIRST": 1, "HOLD": 2, "UNKNOWN": 3, "REMOVED": 4}
rows.sort(key=lambda r: (order[r["bucket"]], r["shop"], r["holiday"] != "Y", r["title"]))
out = os.path.join(REP, "Winstar_Sales_Readiness_Register.csv")
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

tab = collections.Counter((r["bucket"], r["shop"]) for r in rows)
print("rows", len(rows))
for b in order:
    print(b, sum(v for (bb, _), v in tab.items() if bb == b),
          {s: tab[(b, s)] for s in SHOP_ID if tab[(b, s)]})
print("SELL NOW with channel link:", sum(1 for r in rows if r["bucket"] == "SELL NOW" and r["channel_link"]))
print("SELL NOW holiday:", sum(1 for r in rows if r["bucket"] == "SELL NOW" and r["holiday"]))
