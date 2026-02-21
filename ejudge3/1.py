def f(n):
    s = str(n)
    for x in s:
        if int(x) % 2 != 0:
            print("Not valid")
            return
    print("Valid")
v = input()
f(v)