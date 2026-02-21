n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    s = input().split()
    op = s[0]
    if op == "add":
        v = int(s[1])
        a = list(map(lambda x: x + v, a))
    elif op == "multiply":
        v = int(s[1])
        a = list(map(lambda x: x * v, a))
    elif op == "power":
        v = int(s[1])
        a = list(map(lambda x: x ** v, a))
    elif op == "abs":
        a = list(map(lambda x: abs(x), a))
print(*(a))