def g(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
k = int(input())
print(*g(k), sep=',')