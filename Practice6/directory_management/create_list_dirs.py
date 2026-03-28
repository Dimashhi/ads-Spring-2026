import os
os.makedirs("a/b/c",exist_ok=True)
l=os.listdir(".")
for i in l:
    print(i)
t=[x for x in os.listdir(".") if x.endswith(".txt")]
print(t)