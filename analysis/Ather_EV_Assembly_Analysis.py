import csv, json
from collections import defaultdict

CSV_PATH = "../data/Production_Data.csv"
OUT_JSON = "metrics_rerun.json"

with open(CSV_PATH, newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

num = lambda x: float(x) if x not in (None, "") else 0.0
by_station = defaultdict(list)
for r in rows:
    by_station[r["Station ID"]].append(r)

metrics = {}
for sid, rr in by_station.items():
    planned=sum(num(r["Planned Qty"]) for r in rr)
    processed=sum(num(r["Units Processed (units)"]) for r in rr)
    good=sum(num(r["Good Units"]) for r in rr)
    ppt=sum(num(r["Planned Production Time (min)"]) for r in rr)
    op=sum(num(r["Operating Time (min)"]) for r in rr)
    ideal=num(rr[0]["Ideal Cycle Time (sec)"])
    actual_ct=sum(num(r["Actual Cycle Time (sec)"]) for r in rr)/len(rr)
    availability=op/ppt
    performance=ideal*processed/(op*60)
    quality=good/processed
    oee=availability*performance*quality
    metrics[sid]={"station":rr[0]["Station"],"planned":planned,"processed":processed,"good":good,"actual_ct":actual_ct,"availability":availability,"performance":performance,"quality":quality,"oee":oee}

with open(OUT_JSON,'w',encoding='utf-8') as f:
    json.dump(metrics,f,indent=2)

print("Rerun complete. See", OUT_JSON)
