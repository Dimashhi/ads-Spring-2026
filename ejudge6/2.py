n = int(input())
a = map(int, input().split())
b = list(filter(lambda x: x % 2 == 0, a))
print(len(b))