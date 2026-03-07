import re
a = input()
b = input()
c = re.escape(b)
d = re.findall(c, a)
print(len(d))