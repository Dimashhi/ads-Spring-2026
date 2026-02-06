#1
i=1
while i<=5:
    print(i)
    i+=1
#2
i=3
while i>0:
    print(i)
    i-=1
#3
fruits=["apple","banana"]
i=0
while i<len(fruits):
    print(fruits[i])
    i+=1
#4
active=True
count=0
while active:
    count+=1
    if count==3:active=False
    print("Running...")
#5
n=1
while n<20:
    print(n)
    n*=2