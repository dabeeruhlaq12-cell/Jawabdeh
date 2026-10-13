#!/usr/bin/env python3
"""Check data/ for problems that would break the app or mislead a user. Exit 1 on errors."""
import json, re, sys
from pathlib import Path
root = Path(__file__).resolve().parent.parent
errs, warns = [], []
states = json.loads((root/"data/states.json").read_text(encoding="utf-8"))
problems = json.loads((root/"data/problems.json").read_text(encoding="utf-8"))
national = json.loads((root/"data/national.json").read_text(encoding="utf-8"))
bodies = {p["body"] for p in problems["problems"]}
def check_ch(where, c):
    for k in ("type","label_en","label_hi","status"):
        if k not in c: errs.append(f"{where}: channel missing {k}: {c}")
    v = c.get("value","")
    if c.get("type")=="phone":
        if not re.fullmatch(r"\d{3,13}", v): errs.append(f"{where}: bad phone {v!r}")
        if len(v)==10 and v[0] not in "6789" and not v.startswith("0"): warns.append(f"{where}: 10-digit number not a mobile: {v}")
    if c.get("type")=="web":
        if v.startswith("http"): errs.append(f"{where}: web value should not include scheme: {v}")
        if " " in v or "." not in v: errs.append(f"{where}: bad web value {v!r}")
    if c.get("status")=="needs_verification" and not c.get("source"): warns.append(f"{where}: unverified channel without source: {v}")
    if c.get("status") not in ("verified","needs_verification"): errs.append(f"{where}: bad status {c.get('status')}")
for k, s in states.items():
    if not s["grievance"]["channels"]: errs.append(f"state {k}: no grievance channel")
    for c in s["grievance"]["channels"]+s.get("municipal_shared",[]): check_ch(f"state {k}", c)
ids=set()
for f in sorted((root/"data/cities").glob("*.json")):
    c = json.loads(f.read_text(encoding="utf-8")); w=f"city {c.get('id')}"
    if c["id"]!=f.stem: errs.append(f"{w}: id does not match file name")
    if c["id"] in ids: errs.append(f"{w}: duplicate id")
    ids.add(c["id"])
    if c["state"] not in states: errs.append(f"{w}: unknown state {c['state']}")
    lat, lon = c.get("geo",[0,0])
    if not (6<=lat<=37 and 68<=lon<=98): errs.append(f"{w}: geo outside India {c.get('geo')}")
    chans = c["municipal"]["channels"] + c.get("water",{}).get("channels",[]) + c.get("dev_authority",{}).get("channels",[])
    for ch in chans: check_ch(w, ch)
    vals=[x["value"] for x in chans if x["value"]]
    if len(vals)!=len(set(vals)): warns.append(f"{w}: duplicate channel values")
    has_phone = any(x["type"]=="phone" for x in chans) or any(x["type"]=="phone" for x in states[c["state"]].get("municipal_shared",[]))
    if not has_phone and not c.get("note_en"): warns.append(f"{w}: no city phone and no note explaining it")
    if not c["reps"]["mps"]: errs.append(f"{w}: no MP")
    for m in c["reps"]["mlas"]:
        if not m["name"] and c["reps"]["mla_status"]!="to_be_contributed": errs.append(f"{w}: empty MLA name for {m['seat']}")
    for k in ("name_en","name_hi","last_reviewed"):
        if not c.get(k): errs.append(f"{w}: missing {k}")
for p in problems["problems"]:
    for k in ("id","en","hi","body","dept_en","dept_hi"):
        if not p.get(k): errs.append(f"problem {p.get('id')}: missing {k}")
print(f"{len(ids)} cities, {len(states)} states checked")
for x in warns: print("WARN", x)
for x in errs: print("ERROR", x)
sys.exit(1 if errs else 0)
