#1
class A: pass
class B: pass
class C(A, B): pass
#2
class X: a = 1
class Y: b = 2
class Z(X, Y): pass
#3
class M1:
    def f(self): print(1)
class M2:
    def g(self): print(2)
class N(M1, M2): pass
#4
class P1: pass
class P2: pass
class Q(P1, P2): pass
#5
class S1: x = "a"
class S2: y = "b"
class T(S1, S2): pass