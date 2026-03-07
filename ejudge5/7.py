import re
s = input()
p = input()
r = input()
n = re.sub(p, r, s)
print(n)