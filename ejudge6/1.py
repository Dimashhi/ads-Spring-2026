n = int(input())
a = list(map(int, input().split()))
b = sum(map(lambda x: x**2, a))
print(b)