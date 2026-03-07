import re
s = input()
p = r"\d"
f = lambda m: m.group() * 2
r = re.sub(p, f, s)
print(r)