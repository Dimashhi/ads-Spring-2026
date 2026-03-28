s = input().lower()
v = "aeiou"
a = any(c in v for c in s)
if a:
    print("Yes")
else:
    print("No")