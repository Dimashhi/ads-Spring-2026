import re
n = input()
p = r"Name: (.+), Age: (.+)"
m = re.search(p, n)
if m:
    print(m.group(1), m.group(2))