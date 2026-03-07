import re
k = input()
v = re.findall(r"\d", k)
print(" ".join(v))