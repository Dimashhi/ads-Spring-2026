import re
s = input()
p = r"Hello"
m = re.match(p, s)
if m:
    print("Yes")
else:
    print("No")