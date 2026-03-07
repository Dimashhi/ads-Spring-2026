import re
x = input()
y = re.compile(r"^\d+$")
z = y.match(x)
if z:
    print("Match")
else:
    print("No match")