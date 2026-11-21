"""Builds manifest.csv, verification_log_shipping.csv and price_option_2499 numbers.
Inputs: local CSVs + printify_variants_etsy_amazon.csv (Printify reads, Etsy/Amazon shops only)."""
import csv, json, collections

R = "/home/user/crowned-co-data/reports/black_friday"
A = f"{R}/acceptance"

# ---------------- fee model (task brief) ----------------
TXN, PROC, PROC_FIX, LIST, RET = 0.065, 0.03, 0.25, 0.20, 0.02
SHIP_COST = {"tee": 5.35, "crewneck": 9.19, "hoodie": 9.19, "ornament": 6.29}  # Printify calculate-shipping US standard, shortlist.csv 2026-11-20
BUYER_SHIP = {"300729500105": 4.95}   # displayed "$4.95" on listing 4597737445 (scrape 2026-11-21); other profiles UNVERIFIED


def etsy_net(price, cost, ship_cost, buyer_ship=0.0, offsite=0.0):
    rev = price + buyer_ship
    fees = TXN * rev + PROC * rev + PROC_FIX + LIST + RET * price + offsite * rev
    return rev - cost - ship_cost - fees


def amazon_net(price, cost, ship_cost):
    return price - cost - ship_cost - 0.17 * price - RET * price   # 17% referral ASSUMED (unconfirmed)


# ---------------- inputs ----------------
var = collections.defaultdict(list)
meta = {}
for r in csv.DictReader(open(f"{A}/printify_variants_etsy_amazon.csv")):
    var[r["product_id"]].append((r["variant_title"], float(r["price_usd"]), float(r["cost_usd"])))
    meta[r["product_id"]] = r
tmpl = json.load(open(f"{A}/shipping_templates.json"))

prods = []
for wave, f in [("1", f"{R}/launch/candidates.csv"), ("2", f"{R}/wave2/wave2_candidates.csv")]:
    for r in csv.DictReader(open(f)):
        if r["shop"] == "Shopify" or r["rank"] == "EXCLUDED" or r["verified_status"] != "VERIFIED LIVE":
            continue
        r["wave"] = wave
        prods.append(r)
pend = list(csv.DictReader(open(f"{R}/wave2/etsy_uninspected.csv")))

vlog = {}
for f in [f"{R}/launch/verification_log.csv", f"{R}/wave2/verification_log.csv"]:
    for r in csv.DictReader(open(f)):
        vlog[r["product_id"]] = r
ship = {r["product_id"]: r for r in csv.DictReader(open(f"{A}/verification_log_shipping.csv")) if r["product_id"]}

quality = {}  # from reports/Winstar_Five_Shop_Quality_Register.md per-product verdict tables (parsed earlier, all CLEAN)
import re
for line in open("/home/user/crowned-co-data/reports/Winstar_Five_Shop_Quality_Register.md"):
    m = re.match(r"\| (\w{24}) \| .*? \| (\w[\w \-/]*?) \| (https\S+)", line)
    if m:
        quality[m.group(1)] = m.group(2)
defects = {r["product_id"] for r in csv.DictReader(open("/home/user/crowned-co-data/reports/master_register/master_defects.csv"))}

IP = {
    "6ac2f508368bb1b26d051cd7": ("REVIEW", "'Cookie Dealer' is a drug-dealer pun (platform brand-safety) and is a common bakery/business name; possible existing marks NOT checked (no registry search run)."),
    "6af8d6034643b0e30509224f": ("REVIEW", "'Opening Night' is generic, but the live title/tags say 'Broadway Fan'; 'Broadway' is closely tied to theatre-industry brands. Suggest dropping 'Broadway' from title/tags (live edit needs approval). Registry NOT checked."),
    "6af8d8af626b8d7aa001565b": ("LOW", "'Naughty or Nice' is a traditional Christmas phrase; short phrases are not copyrightable. Registry NOT checked."),
    "6ad4116c3af1c130250b6447": ("LOW", "'Christmas Calories Don't Count' is a common holiday saying. Registry NOT checked."),
    "6af90b48948a470d5206d7db": ("LOW", "Nutcracker is a public-domain story/ballet; register shows art CLEAN (generic nutcracker, no film/ballet-company branding seen). Registry NOT checked."),
    "6af8ff4bc8d016720c098bf5": ("LOW", "Nutcracker: public-domain story/ballet; generic art. Registry NOT checked."),
    "6af8c9cec745d035040e4b79": ("LOW", "Nutcracker: public-domain story/ballet; generic art. Registry NOT checked."),
    "6ad410763af1c130250b6337": ("LOW", "'Dog Mom' is a widely used descriptive phrase. Whether any Class 25 word mark exists is NOT checked."),
    "6ae2af0ed0738075d402e2b2": ("LOW", "'Dog Mom' descriptive phrase (Amazon enforces brand claims more aggressively; registry NOT checked). Also one of an owner-kept duplicate ASIN pair (B0HPS4FTHJ / B0HPMTHR4C)."),
    "6af90b6cca5d307abc0160ff": ("LOW", "'Hooked on Christmas' is a crochet pun; faint echo of 'Hooked on Phonics' but different goods and wording. Registry NOT checked."),
    "6af8ff6bc745d035040e88f4": ("LOW", "'Hooked on Christmas' crochet pun (see hoodie). Registry NOT checked."),
    "6af8c97da2664d4016059f77": ("LOW", "'Hooked on Christmas' crochet pun (see hoodie). Registry NOT checked."),
}
DEFAULT_IP = ("LOW", "Generic occupational/pet/seasonal wording; no brand, celebrity or film reference seen in title. Registry NOT checked.")


def kind(r):
    t = r.get("type") or "hoodie"
    if t == "tee" and r.get("printify_price", "").startswith("24.99"):
        return "tee_2499"
    return t


def calc(pid, k, shop):
    vs = var.get(pid)
    if k == "ornament":   # no variant pull cached; shortlist.csv values (Printify get-product + calculate-shipping 2026-11-20)
        p, c = 22.99, 9.79
        n = etsy_net(p, c, 6.29)
        return dict(base=n / p, base_usd=n, worst=n / p, worst_v="Circle / One size", off12=etsy_net(p, c, 6.29, offsite=.12) / p,
                    off15=etsy_net(p, c, 6.29, offsite=.15) / p, worst12=etsy_net(p, c, 6.29, offsite=.12) / p,
                    worst15=etsy_net(p, c, 6.29, offsite=.15) / p, bship=0, basis="shortlist.csv cost 9.79 + ship 6.29")
    sc = SHIP_COST["tee" if k.startswith("tee") else k]
    if shop == "Amazon":
        nets = [(amazon_net(p, c, sc) / p, t, p, c) for t, p, c in vs]
        b = min(vs, key=lambda x: x[1])
        bn = amazon_net(b[1], b[2], sc)
        w = min(nets)
        return dict(base=bn / b[1], base_usd=bn, worst=w[0], worst_v=w[1], off12=None, off15=None, worst12=None, worst15=None, bship=0,
                    basis="Amazon 17% referral ASSUMED; seller pays $5.35")
    bs = BUYER_SHIP.get(tmpl.get(pid, ""), 0.0)
    b = min(vs, key=lambda x: (x[1], x[2]))
    f = lambda p, c, o=0: etsy_net(p, c, sc, bs, o) / p
    w = min(((f(p, c), t) for t, p, c in vs))
    return dict(base=f(b[1], b[2]), base_usd=etsy_net(b[1], b[2], sc, bs), worst=w[0], worst_v=w[1],
                off12=f(b[1], b[2], .12), off15=f(b[1], b[2], .15),
                worst12=min(f(p, c, .12) for _, p, c in vs), worst15=min(f(p, c, .15) for _, p, c in vs), bship=bs,
                basis=("buyer pays $4.95 shipping (profile 300729500105)" if bs else "seller pays shipping (payer UNVERIFIED)"))


TYPE_SHIP = {  # Etsy page evidence 2026-11-21 (verification_log_shipping.csv); used for siblings not scraped today
    "tee": ("Hialeah, FL", "Etsy est. Nov 27-30 / Nov 27-Dec 1 if ordered 2026-11-21 (3 tee pages). Promo: 'Order by Wed Dec 2 for the best chance of arrival before Christmas' (estimate)"),
    "tee_2499": ("Hialeah, FL", "Etsy est. Nov 27-Dec 2 / Nov 27-30 if ordered 2026-11-21 (2 pages). Promo: 'Order by Wed Dec 2 for the best chance of arrival before Christmas' (estimate)"),
    "crewneck": ("Hialeah, FL", "Etsy est. Nov 24-30 if ordered 2026-11-21 (2 pages). Promo: 'Order by Wed Dec 2 for the best chance of arrival before Christmas' (estimate)"),
    "hoodie": ("Hialeah, FL", "Etsy est. Nov 24-30 if ordered 2026-11-21 (2 pages). Promo: 'Order by Wed Dec 2 for the best chance of arrival before Christmas' (estimate)"),
    "ornament": ("United Kingdom", "Etsy est. Nov 25-Dec 5 if ordered 2026-11-21 (2 pages). Promo: 'Ships from the UK, please allow extra time' (no order-by date)"),
}
PAYER = {
    "tee": "UNVERIFIED (cost not rendered on 3 pages; profile 299987014038)",
    "crewneck": "UNVERIFIED (cost not rendered on 2 pages; profile 320380366278)",
    "hoodie": "UNVERIFIED (cost not rendered on 2 pages; profile 320380366278)",
    "ornament": "UNVERIFIED (cost not rendered on 2 pages)",
}


def pct(x):
    return "" if x is None else f"{x*100:.1f}"


out = []
for r in prods + [dict(p, shop="Etsy", wave="PENDING", type="hoodie", public_url=p["etsy_listing (Printify external handle; page not scraped)"]) for p in pend]:
    pid = r["product_id"]; shop = r["shop"]; k = kind(r)
    m = calc(pid, k, shop)
    ipv, ipr = IP.get(pid, DEFAULT_IP)
    q = quality.get(pid)
    if pid in defects:
        qs = "UNVERIFIED (open defect in master_defects)"
    elif q == "CLEAN":
        qs = "PASS (no open defect in master_defects; mockup CLEAN in Winstar_Five_Shop_Quality_Register.md per-product table)"
    elif shop == "Amazon":
        qs = "PASS (no open defect; Amazon shop 62/62 visually inspected per Winstar_Sales_Readiness_Register.csv)"
    elif r["wave"] == "PENDING":
        qs = f"PASS (no open defect; live 8-colour front mockup inspected: wave2/evidence/{pid}_front_8colours.jpg)"
    else:
        qs = "UNVERIFIED (no mockup inspection record found)"
    s = ship.get(pid)
    if shop == "Amazon":
        ships_from, est = "UNVERIFIED on Amazon page (Printify provider 99, US)", "UNVERIFIED (not captured); apparel order-by wording applies as an estimate only"
        payer = "n/a (Amazon; seller-paid $5.35 modelled)"
    else:
        ships_from, est = TYPE_SHIP[k]
        if s:
            ships_from = s["ships_from"] + " (page, 2026-11-21)"
            est = f"Etsy page: {s['est_delivery']} if ordered 2026-11-21. " + est.split(". ", 1)[1]
        elif r["wave"] == "2":
            ships_from = vlog[pid].get("ships_from", ships_from) + " (page, wave2 check)"
        else:
            ships_from += " (type-level: same provider 99 + same Etsy profile; this page not re-scraped)"
        if k == "tee_2499":
            t = tmpl.get(pid)
            payer = ("BUYER ($4.95 displayed on this page)" if pid == "6ad4105a9c8f61e787077ee9" else
                     "BUYER - INFERRED ($4.95; same Etsy shipping profile 300729500105 as verified listing 4597737445)" if t == "300729500105" else
                     "UNVERIFIED (profile 299987014038, same as $29.99 tees; cost not rendered)")
        else:
            payer = PAYER[k]
    if r["wave"] == "PENDING":
        ts = s["ts_utc"] if s else "NOT CHECKED (page never scraped)"
    else:
        ts = (s["ts_utc"] + " (re-checked)") if s else vlog[pid]["ts_utc"]
    # ---- tier
    reasons = []
    if ipv == "REVIEW":
        tier = "C"; reasons.append("IP/brand-safety REVIEW: " + ipr.split(";")[0])
    elif k == "ornament":
        tier = "C"; reasons.append(f"net {pct(m['base'])}% < 20% at regular price with seller-paid shipping (payer UNVERIFIED); ships from UK; add-on only per OWNER DECISION")
    elif not qs.startswith("PASS"):
        tier = "C"; reasons.append("quality not verified")
    elif shop == "Amazon":
        tier = "A" if m["worst"] >= .20 else "B"
    elif m["worst12"] >= .20:
        tier = "A"
    elif m["base"] >= .20:
        tier = "B"
    else:
        tier = "C"; reasons.append("below 20% at regular price")
    caveat = []
    if tier == "B":
        if m["worst"] < .20: caveat.append(f"worst size {m['worst_v']} {pct(m['worst'])}%")
        if m["worst12"] is not None and m["worst12"] < .20: caveat.append(f"worst with 12% Offsite {pct(m['worst12'])}%")
    if r["wave"] == "PENDING":
        if s:
            status = "PENDING - page verified live 2026-11-21; HOLD until owner adds it to a wave (tier " + tier + ")"
        else:
            status = "PENDING - HOLD: Etsy page not verified (buyability unknown)"
    elif tier == "C":
        status = "HOLD + " + "; ".join(reasons)
    else:
        status = "READY FOR OWNER POSTING APPROVAL" + (" (caveat: " + "; ".join(caveat) + ")" if caveat else "")
        if shop == "Amazon":
            status += " (caveat: Amazon 17% fee assumed; duplicate ASIN pair kept by owner)"
        if "INFERRED" in payer:
            status += " (caveat: buyer-paid shipping inferred from shared profile)"
    out.append(dict(section="PENDING" if r["wave"] == "PENDING" else "MAIN", product_id=pid, shop=shop, shop_id=r["shop_id"], wave=r["wave"],
                    type=k, title=r["title"], public_url=r["public_url"], buyability_check_ts=ts, quality_status=qs,
                    ip_screen=f"{ipv}: {ipr}", margin_regular_pct=pct(m["base"]), net_regular_usd=f"{m['base_usd']:.2f}",
                    margin_worst_variant_pct=f"{pct(m['worst'])} ({m['worst_v']})",
                    margin_offsite12_worst_pct=pct(m["worst12"]) or "n/a", margin_offsite15_pct=(pct(m["off15"]) or "n/a") + ("" if m["off15"] is None else f" (worst {pct(m['worst15'])})"),
                    margin_basis=m["basis"], shipping_payer=payer, ships_from=ships_from, est_delivery_wording=est,
                    risk_tier=tier, acceptance_status=status))

with open(f"{A}/manifest.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
    w.writeheader(); [w.writerow(o) for o in out if o["section"] == "MAIN"]; [w.writerow(o) for o in out if o["section"] == "PENDING"]

c = collections.Counter((o["section"], o["shop"], o["wave"]) for o in out)
print(c)
print(collections.Counter((o["section"], o["risk_tier"]) for o in out))
print(collections.Counter((o["section"], o["acceptance_status"].split(" (")[0].split(" +")[0][:40]) for o in out))
for o in out:
    print(o["risk_tier"], o["type"], o["product_id"], o["margin_regular_pct"], o["margin_worst_variant_pct"], o["margin_offsite12_worst_pct"], o["margin_offsite15_pct"], o["ip_screen"][:6], o["acceptance_status"][:60])
