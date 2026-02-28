import sys
n = int(sys.stdin.read())
g = (i for i in range(n, -1, -1))
for x in g:
    print(x)