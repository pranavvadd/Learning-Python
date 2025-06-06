# This code demonstrates the use of a 2D collection (list of lists) in Python.
fruits =     ["apple", "banana", "cherry", "date", "elderberry"]
vegetables = ["carrot", "broccoli", "spinach"]
meats =      ["chicken", "beef", "pork"]

groceries = [fruits, vegetables, meats]

print(groceries[1]) # Accessing the second collection (vegetables)
print(groceries[2][0]) # Accessing the first item in the third collection (meats)
print(groceries[0][2]) # Accessing the third item in the first collection (fruits)

print("----- ALL ITEMS -----")

for entireList in groceries:
    for food in entireList:
        print(food, end=' ') # Print all items in the nested collections on the same line
    print()

print()
print("----- ON TO TUPLES -----")
# This code demonstrates the use of a tuple to represent a keypad layout.
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()