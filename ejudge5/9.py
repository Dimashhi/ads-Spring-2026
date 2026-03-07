import re
u = input()
w = r"\b[a-zA-Z]{3}\b"
v = re.findall(w, u)
print(len(v))