q=["company","bed","closet"]
p=[10,20,30]
for i,v in enumerate(q):
    print(i,v)
for x,y in zip(q,p):
    print(x,y)
z="777"
if isinstance(z,str):
    res=int(z)
    print(type(res),res)