import math
def s():
    r = float(input())
    ax, ay = map(float, input().split())
    bx, by = map(float, input().split())
    dx, dy = bx - ax, by - ay
    a = dx*dx + dy*dy
    b = 2 * (ax*dx + ay*dy)
    c = ax*ax + ay*ay - r*r
    if a == 0:
        return r if ax*ax + ay*ay <= r*r else 0.0
    d = b*b - 4*a*c
    if d < 0:
        print(f"{0.0:.10f}")
        return
    t1 = (-b - math.sqrt(d)) / (2*a)
    t2 = (-b + math.sqrt(d)) / (2*a)
    t_start = max(0, min(t1, t2))
    t_end = min(1, max(t1, t2))
    if t_start > t_end:
        print(f"{0.0:.10f}")
    else:
        length = (t_end - t_start) * math.sqrt(a)
        print(f"{length:.10f}")
s()