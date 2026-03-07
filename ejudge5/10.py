import re
q = input()
p = r"cat|dog"
f = re.search(p, q)
if f:
    print("Yes")
else:
    print("No")