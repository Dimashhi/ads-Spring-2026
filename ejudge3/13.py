def p(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
s = input().split()
a = [int(x) for x in s]
f = list(filter(lambda n: p(n), a))
if not f:
    print("No primes")
else:
    print(*(f))