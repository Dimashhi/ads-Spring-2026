d = {'ZER':'0', 
     'ONE':'1', 
     'TWO':'2', 
     'THR':'3', 
     'FOU':'4', 
     'FIV':'5', 
     'SIX':'6', 
     'SEV':'7', 
     'EIG':'8', 
     'NIN':'9'}
s = input()
op = ''
if '+' in s: op = '+'
if '-' in s: op = '-'
if '*' in s: op = '*'
p = s.split(op)
w1 = p[0]
w2 = p[1]
n1 = ''
while len(w1) > 0:
    t = w1[:3]
    n1 += d[t]
    w1 = w1[3:]
a = int(n1)
n2 = ''
while len(w2) > 0:
    t = w2[:3]
    n2 += d[t]
    w2 = w2[3:]
b = int(n2)
if op == '+': v = a + b
elif op == '-': v = a - b
else: v = a * b
res = ''
for x in str(v):
    for k in d:
        if d[k] == x:
            res += k
print(res)