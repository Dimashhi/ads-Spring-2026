#1
a=["apple", "banana", "tomato"]
for x in a:
    if x=="banana":
        continue
    print(x)
#2
for i in range(5):
    if i%2==0:
        continue
    print(i)
#3
b="python"
for char in b:
    if char in "aeiou":
        continue
    print(char)
#4
c=[1,0,-1,-2,3]
for n in c:
    if n<=0:
        continue
    print(n)
#5
for word in ["hi","hello","py"]:
    if len(word)>2:
        continue
    print(word)