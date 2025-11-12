fruits = ["apple", "banana", "cherry"]
adj = ["red", "big", "tasty"]

for item in fruits:
    print(item, end = " ")

print()

for x in range(1, 20, 3):
    print(x, end = " ")
else:
    print("\nFinally finished !")

# nested loops
for x in fruits:
    for y in adj:
        print(x, y)

for x in [1, 0, 2]:
    pass