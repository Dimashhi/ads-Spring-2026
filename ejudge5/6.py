import re
z = input()
p = r"\S+@\S+\.\S+"
r = re.search(p, z)
if r:
    print(r.group())
else:
    print("No email")