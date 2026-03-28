n = int(input())
a = map(int, input().split())
b = all(x >= 0 for x in a)
if b:
    print("Yes")
else:
    print("No")