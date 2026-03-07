import re
k = input()
p = r"\d{2,}"
v = re.findall(p, k)
print(" ".join(v))