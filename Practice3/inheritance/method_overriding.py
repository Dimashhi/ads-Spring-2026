#1
class A:
    def f(self): print(1)
class B(A):
    def f(self): print(2)
#2
class C:
    def g(self): return "a"
class D(C):
    def g(self): return "b"
#3
class E:
    def __init__(self): self.v = 0
class F(E):
    def __init__(self): self.v = 100
#4
class G:
    def x(self): pass
class H(G):
    def x(self): print("hi")
#5
class I:
    def val(self): return 5
class J(I):
    def val(self): return 10