def x(s):
    f = open("raw.txt", "a")
    f.write(s + "\n")
    f.close()

a = "milk"
b = 1.2
v = a + " " + str(b)
x(v)

c = 10
d = 5
e = c + d
v = "total " + str(e)
x(v)

c = ["pen", "bread", "bag"]
v = ""
for i in c:
    v = v + i + "/"
x(v[:-1])

c = 100
if c > 50:
    v = "big"
else:
    v = "small"
x(v)

a = "user"
b = "7"
v = a + b
x(v)