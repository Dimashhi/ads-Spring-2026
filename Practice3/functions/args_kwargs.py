#1
def p(*a):
    print(a)
#2
def q(**b):
    print(b)
#3
def r(x, *y):
    print(x, y)
#4
def s(*n):
    return sum(n)
#5
def t(**m):
    return m.keys()