def greet():
    print("Helo from a function")
greet()

def my_funciton(name):
    print("Hello: " + name)

my_funciton("Alex")
my_funciton("Peter")

def my_function2(first_name, last_name):
    print(first_name + ' ' + last_name)

my_function2("Emil", "Fukuda")
my_function2("Pham", "Duc")

def default_value(name = "Alex"):
    print("Hello:",name)

default_value()

# *args -> tuple
print("------DOI SO-------")
def my_sum(*args):
    print(args)
    return sum(args)

print(my_sum(1, 2, 3, 4))
print(my_sum(10, 20, 30, 40))

#**kwargs -> dictionary
def print_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_info(name = "An", age = "21", my_class = "CNTT")

def unpacking_arg(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = unpacking_arg(*numbers) # same as: unpacking_arg(1, 2, 3)
print(result)