import json
def f(v):
    if v == "<missing>": return v
    return json.dumps(v, separators=(',', ':'))
def d(a, b, p, r):
    k1 = set(a.keys()) if isinstance(a, dict) else set()
    k2 = set(b.keys()) if isinstance(b, dict) else set()
    all_k = sorted(k1 | k2)
    for k in all_k:
        v1 = a.get(k, "<missing>") if isinstance(a, dict) else "<missing>"
        v2 = b.get(k, "<missing>") if isinstance(b, dict) else "<missing>"
        cp = f"{p}.{k}" if p else k
        if isinstance(v1, dict) and isinstance(v2, dict):
            d(v1, v2, cp, r)
        elif v1 != v2:
            r.append(f"{cp} : {f(v1)} -> {f(v2)}")
x = json.loads(input())
y = json.loads(input())
res = []
d(x, y, "", res)
if not res:
    print("No differences")
else:
    for line in sorted(res):
        print(line)