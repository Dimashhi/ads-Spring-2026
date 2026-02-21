class E:
    def __init__(self, n, s):
        self.n = n
        self.s = s
    def t(self):
        return float(self.s)
class M(E):
    def __init__(self, n, s, b):
        super().__init__(n, s)
        self.b = b
    def t(self):
        return self.s * (1 + self.b / 100)
class D(E):
    def __init__(self, n, s, p):
        super().__init__(n, s)
        self.p = p
    def t(self):
        return float(self.s + self.p * 500)
class I(E):
    pass
x = input().split()
v = x[0]
n = x[1]
s = int(x[2])
if v == "Manager":
    o = M(n, s, int(x[3]))
elif v == "Developer":
    o = D(n, s, int(x[3]))
else:
    o = I(n, s)

print(f"Name: {o.n}, Total: {o.t():.2f}")