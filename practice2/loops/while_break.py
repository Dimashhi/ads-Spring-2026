#1
i=2
while i<10:
    if i==4:
        break
    print(i)
    i+=1
#2
n=1
while n<100:
    if n%10==0:
        break
    n+=1
#3
s="Python"
i=0
while i<len(s):
    if s[i]=='h':
        break
    print(s[i])
    i+=1
#4
while True:
    print("One time")
    break
#5
n = 1
while n < 50:
    print(n)
    n *= 2