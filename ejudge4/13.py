import json
import re
def q(d, s):
    p = re.findall(r'(\w+)|\[(\d+)\]', s)
    c = d
    try:
        for k, i in p:
            if k:
                c = c[k]
            else:
                c = c[int(i)]
        return json.dumps(c, separators=(',', ':'))
    except:
        return "NOT_FOUND"
v = json.loads(input())
m = int(input())
for _ in range(m):
    print(q(v, input()))