def s(a, b):
    for i in range(a, b + 1):
        yield i * i
x, y = map(int, input().split())
for v in s(x, y):
    print(v)