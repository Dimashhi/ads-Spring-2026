class A:
    def __init__(self, x):
        self.x = x
    def d(self, v):
        self.x += v
    def w(self, v):
        if v > self.x:
            print("Insufficient Funds")
        else:
            self.x -= v
            print(self.x)
s = input().split()
b = int(s[0])
m = int(s[1])
o = A(b)
o.w(m)