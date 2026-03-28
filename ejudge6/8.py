n = int(input())
a = map(int, input().split())
b = sorted(set(a))
print(*(b))