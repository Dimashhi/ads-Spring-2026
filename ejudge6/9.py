n = int(input())
k = input().split()
v = input().split()
d = dict(zip(k, v))
q = input()
if q in d:
    print(d[q])
else:
    print("Not found")