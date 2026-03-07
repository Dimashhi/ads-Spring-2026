import re
k = input()
g = r"[A-Z]"
v = re.findall(g, k)
print(len(v))