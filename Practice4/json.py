import json
def b(x):
    return json.loads(x)
def c(x):
    return str(x)
def d(x, k):
    return x[k]
def e(x):
    print(json.dumps(x))
def m(x, k):
    return x.get(k)