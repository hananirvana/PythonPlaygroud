fruits = ["apple", "banana", "cherry"]  # this is a list
for x in fruits:  # this iterates through each item in the list
    print(x)
    for b in fruits[1]:  # this iterates through each letter in the string
        print(b)
    if x == "banana":
        break
    print(x)
    print("\n")
    if x == "apple":
        continue
    print(x)


