class S:
    def a(self):
        return 0
class Q(S):
    def __init__(self, n):
        self.n = n
    def a(self):
        return self.n * self.n
x = int(input())
o = Q(x)
print(o.a())