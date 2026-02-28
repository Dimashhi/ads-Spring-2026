import datetime
def a(s):
    return datetime.datetime.fromisoformat(s)
def b(x):
    return x.date()
def c(x, y):
    return (x - y).days
def d():
    return datetime.datetime.now().year
def e(x):
    return str(x)