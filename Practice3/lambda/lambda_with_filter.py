#1
a = [0, 2, 10, 14]
b = list(filter(lambda x: x > 5, a))
#2
x = ["goo", "sixseven", "okkk"]
y = list(filter(lambda s: len(s) > 1, x))
#3
n = [0, 1, 2, 3]
m = list(filter(lambda i: i % 2 == 0, n))
#4
s = [True, False, True]
r = list(filter(lambda i: i == True, s))
#5
k = [-1, 0, 5]
v = list(filter(lambda x: x >= 0, k))