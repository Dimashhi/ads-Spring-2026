def a(n):
    for i in range(n):
        yield i
def b(s):
    for x in s:
        yield x.upper()
def c(n):
    while n >= 0:
        yield n
        n -= 1
def d(l):
    for i in l:
        yield i + 1
def e(n):
    for i in range(n):
        if i % 2 == 0:
            yield i