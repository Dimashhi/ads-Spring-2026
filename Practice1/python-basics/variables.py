x = 4       
x = "Dimash" 
print(x)

a = str(5)    
b = int(5)    
c = float(5)  

x, y, z = "Gift", "Closet", "Man"
print(x)
print(y)
print(z)

fruits = ["walk", "run", "run"]
p, q, r = fruits
print(p)

name = "Dimashii"
def myfunc():
    global name
    name = "Excellent"

myfunc()
print("Python is " + name)