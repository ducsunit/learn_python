# x = 5
# myName = "DucSunIT"

# a = 5
# A = 10
# print(a)
# print(A)

#assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print()

a = b = c = "Orange"
print("a = " + a)
print("b = " + b)
print("c = " + c)

print()

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)
# print(y)
# print(z)

# Global variables
d = "awesome"

def myfunc(): 
    d = "fantastic"
    print("Python is " + d)

myfunc()

print("Python is " + d)

print()

print("-----KEYWORD GLOBAL-------")
# keyword global
def myfunc2():
    global e 
    e = "Hello World"
    print(e)

myfunc2()
print("Ngoài func2: " + e)