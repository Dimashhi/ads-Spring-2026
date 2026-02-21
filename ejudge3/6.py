class S:
    def a(self):
        return 0
class R(S):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def a(self):
        return self.l * self.w
i = input().split()
x = int(i[0])
y = int(i[1])
o = R(x, y)
print(o.a())