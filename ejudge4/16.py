from datetime import datetime
def s(x):
    p = x.split()
    t = datetime.strptime(f"{p[0]} {p[1]}", "%Y-%m-%d %H:%M:%S")
    o = p[2][3:]
    h, m = map(int, o[1:].split(':'))
    v = h * 3600 + m * 60
    return t.timestamp() - v if o[0] == '+' else t.timestamp() + v
a = s(input())
b = s(input())
print(int(round(b - a)))