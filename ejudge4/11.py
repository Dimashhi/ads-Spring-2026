import json
def r(s, p):
    for k, v in p.items():
        if v is None:
            if k in s:
                del s[k]
        elif isinstance(v, dict) and isinstance(s.get(k), dict):
            r(s[k], v)
        else:
            s[k] = v
    return s
a = json.loads(input())
b = json.loads(input())
print(json.dumps(r(a, b), sort_keys=True, separators=(',', ':')))