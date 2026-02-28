def s():
    ax, ay = map(float, input().split())
    bx, by = map(float, input().split())
    by_mirror = -by
    t = ay / (ay - by_mirror)
    rx = ax + t * (bx - ax)
    ry = 0.0
    print(f"{rx:.10f} {ry:.10f}")
s()