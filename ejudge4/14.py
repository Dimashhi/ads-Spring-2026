from datetime import datetime, timedelta
def t(s):
    p = s.split()
    d = datetime.strptime(p[0], "%Y-%m-%d")
    o = p[1][3:]
    h, m = map(int, o[1:].split(':'))
    v = timedelta(hours=h, minutes=m)
    return d - v if o[0] == '+' else d + v
a = t(input())
b = t(input())
print(int(abs((a - b).total_seconds()) // 86400))