#1
i=1
while i<10:
    if i==3:break
    print(i)
    i+=1
#2
while True:
    print("One time")
    break
#3
s="Python"
i=0
while i<len(s):
    if s[i]=='h':break
    print(s[i])
    i+=1
#4
n=1
while n<100:
    if n%7==0:break
    n+=1
#5
vals=[10,20,30]
i=0
while i<len(vals):
    if vals[i]==20:break
    i+=1