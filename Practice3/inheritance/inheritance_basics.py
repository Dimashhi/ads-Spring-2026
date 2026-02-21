#1
class A: pass
class B(A): pass
#2
class X:
    def f(self): print(1)
class Y(X): pass
#3
class M: pass
class N(M): pass
#4
class P:
    a = 1
class Q(P): pass
#5
class C1: pass
class C2(C1): pass