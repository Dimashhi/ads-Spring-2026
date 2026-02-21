#1
class A:
    def __init__(self, x): self.x = x
class B(A):
    def __init__(self, x): super().__init__(x)
#2
class C:
    def f(self): print("p")
class D(C):
    def f(self): super().f()
#3
class E:
    def __init__(self): self.a = 1
class F(E):
    def __init__(self): super().__init__()
#4
class G:
    def m(self): return 10
class H(G):
    def m(self): return super().m() + 1
#5
class I:
    def __init__(self, s): self.s = s
class J(I):
    def __init__(self, s): super().__init__(s)