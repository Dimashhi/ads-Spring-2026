n = int(input())
s = input().split()
a = []
for i, w in enumerate(s):
    a.append(f"{i}:{w}")
print(" ".join(a))