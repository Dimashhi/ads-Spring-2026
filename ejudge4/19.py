import math
def s():
    r = float(input())
    ax, ay = map(float, input().split())
    bx, by = map(float, input().split())
    d_ab = math.sqrt((ax-bx)**2 + (ay-by)**2)
    oa = math.sqrt(ax**2 + ay**2)
    ob = math.sqrt(bx**2 + by**2)
    cos_gamma = (ax*bx + ay*by) / (oa * ob)
    cos_gamma = max(-1.0, min(1.0, cos_gamma))
    gamma = math.acos(cos_gamma)
    h = abs(ax*by - ay*bx) / d_ab if d_ab > 0 else oa
    dot_a = (bx-ax)*(-ax) + (by-ay)*(-ay)
    dot_b = (ax-bx)*(-bx) + (ay-by)*(-by)
    if h >= r or dot_a <= 0 or dot_b <= 0:
        print(f"{d_ab:.10f}")
    else:
        alpha = math.acos(r / oa)
        beta = math.acos(r / ob)
        ta = math.sqrt(oa**2 - r**2)
        tb = math.sqrt(ob**2 - r**2)     
        arc_angle = gamma - alpha - beta
        arc_len = max(0.0, arc_angle * r)    
        print(f"{ta + tb + arc_len:.10f}")
s()