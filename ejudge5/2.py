import re
a = input()
b = input()
c = re.search(b, a)
if c:
    print("Yes")
else:
    print("No")