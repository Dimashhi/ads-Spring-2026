import re
x = input()
y = input()
z = re.findall(y, x)
print(len(z))