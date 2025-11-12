a = "Hello World !"
# print(a[0])

# for x in "banana":
#     print(x, end=" ")

# To get the lenth of string, use the len() function
print(len(a))

# To check if a contain phrase of character is present in a string
# we can use the keyword 'in'
b = "The best things in life are free !"
# print("free" in b)
if "free" in b:
    print("Yes, 'free' is present")

# To check if a contain phrase of character is NOT present in a string
# we can use the keyword 'not in'
c = "The best things in life are free !"
# print("expensive" not in c)
if "expensive" not in c:
    print("No, 'expensive' is NOT present.")