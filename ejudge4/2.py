n = int(input())
g = (i for i in range(n + 1) if i % 2 == 0)
print(*g, sep=',')