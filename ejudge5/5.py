import re
t = input()
p = r"^[a-zA-Z].*\d$"
m = re.search(p, t)
if m:
    print("Yes")
else:
    print("No")