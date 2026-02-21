#1
a = [5, 2, 8]
b = sorted(a, key=lambda x: x)
#2
x = ["school", "easy", "cat"]
y = sorted(x, key=lambda s: s[-1])
#3
n = [[1, 9], [2, 1]]
m = sorted(n, key=lambda i: i[1])
#4
s = ["W", "S", "C"]
r = sorted(s, key=lambda i: i.lower())
#5
k = [10, -5, 2]
v = sorted(k, key=lambda x: abs(x))