from functools import reduce
a=[8,7,6,5,4,3,2,1]
b=list(map(lambda x:x*5,a))
print(b)
c=list(filter(lambda x:x>6,a))
print(c)
d=reduce(lambda x,y:x+y,a)
print(d)