import re
s = input()
p = r"\d{2}/\d{2}/\d{4}"
m = re.findall(p, s)
print(len(m))