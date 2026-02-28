def c(l, m):
    for _ in range(m):
        for x in l:
            yield x
s = input().split()
k = int(input())
print(*(c(s, k)))