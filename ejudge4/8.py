def p(m):
    for i in range(2, m + 1):
        is_p = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_p = False
                break
        if is_p:
            yield i
n = int(input())
print(*p(n))