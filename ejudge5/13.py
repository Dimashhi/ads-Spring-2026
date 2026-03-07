import re
s = input()
p = r"\w+"
v = re.findall(p, s)
print(len(v))