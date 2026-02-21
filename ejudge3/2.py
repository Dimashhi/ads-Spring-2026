def f(n):
    if n < 1:
        return False 
    for x in [2, 3, 5]:
        while n % x == 0:
            n //= x
    return n == 1
a = int(input())
if f(a):
    print("Yes")
else:
    print("No")