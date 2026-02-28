def s():
    g = 0
    n = 0
    k = int(input())
    for _ in range(k):
        c = input().split()
        t = c[0]
        v = int(c[1])    
        if t == 'global':
            g += v
        elif t == 'nonlocal':
            n += v       
    print(f"{g} {n}")
s()