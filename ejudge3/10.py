class P:
    def __init__(self, n):
        self.n = n
class S(P):
    def __init__(self, n, g):
        super().__init__(n)
        self.g = g
    def d(self):
        print(f"Student: {self.n}, GPA: {self.g}")
i = input().split()
a = i[0]
b = float(i[1])
o = S(a, b)
o.d()