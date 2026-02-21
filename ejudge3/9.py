class C:
    def __init__(self, r):
        self.r = r
    def a(self):
        v = 3.14159
        return v * self.r * self.r
n = int(input())
o = C(n)
print("{:.2f}".format(o.a()))