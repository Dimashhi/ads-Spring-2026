class P:
    def __init__(self, x, y):
        self.v1 = x
        self.v2 = y
    def m(self, o):
        r1 = self.v1 + o.v1
        r2 = self.v2 + o.v2
        return r1, r2
s = input().split()
a1 = int(s[0])
b1 = int(s[1])
a2 = int(s[2])
b2 = int(s[3])
p1 = P(a1, b1)
p2 = P(a2, b2)
x, y = p1.m(p2)
print(f"Result: {x} {y}")