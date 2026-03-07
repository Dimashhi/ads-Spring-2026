import re
s = input()
p = re.compile(r"\b\w+\b")
m = p.findall(s)
print(len(m))