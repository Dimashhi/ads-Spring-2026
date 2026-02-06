#1
a=["apple","banana","tomato"]
for x in a:
    if x=="banana": break
    print(x)
#2
for i in range(1, 100):
    if i==5: 
       break
    print(i)
#3
b=[10,20,30]
for x in b:
    print(x)
    break
#4
c="Hello World"
for char in c:
    if char==" ":
        break
    print(char)
#5
for n in range(10):
    if n*n>20:
        break
    print(n)