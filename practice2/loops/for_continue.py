#1
a=["magazin","bed","closet"]
for x in a:
    if x=="banana":
        continue
    print(x)
#2
for n in range(10):
    if n*n>20:
        continue
    print(n)
#3
b="snake"
for char in b:
    if char in "ake":
        continue
    print(char)
#4
c=[5,1,6,3,1]
for n in c:
    if n<=0:
        continue
    print(n)
#5
for word in ["hi","hello","py"]:
    if len(word)>4:
        continue
    print(word)