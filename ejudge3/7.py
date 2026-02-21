class P:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def s(self):
        print(f"({self.a}, {self.b})")
    def m(self, x, y):
        self.a = x
        self.b = y
    def d(self, o):
        r = ((self.a - o.a)**2 + (self.b - o.b)**2)**0.5
        return r
i = input().split()
p1 = P(int(i[0]), int(i[1]))
p1.s()
n = input().split()
p1.m(int(n[0]), int(n[1]))
p1.s()
o = input().split()
p2 = P(int(o[0]), int(o[1]))
res = p1.d(p2)
print(f"{res:.2f}")