import sys
n = int(sys.stdin.read())
g = (i**2 for i in range(1, n + 1))
for x in g:
    print(x)