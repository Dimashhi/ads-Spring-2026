import math
from datetime import datetime, timezone, timedelta
def p(s):
    d, z = s.split(' '); o = z[3:]
    h, m = map(int, o[1:].split(':')); t = timedelta(hours=h, minutes=m)
    if o[0] == '-': t = -t
    return datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=timezone(t))
b, c = p(input()), p(input())
y = c.year
while 1:
    try:
        t = b.replace(year=y)
        if t.timestamp() < c.timestamp(): raise ValueError
        break
    except ValueError:
        try:
            t = b.replace(year=y, month=2, day=28 if b.day == 29 else b.day)
            if t.timestamp() >= c.timestamp(): break
        except: pass
        y += 1
print(math.ceil(max(0, t.timestamp() - c.timestamp()) / 86400))