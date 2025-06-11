#Strings
first_name = "Bro"
food = "pizza"

print(f"Hello {first_name}, would you like some {food}")

#Integers
age = 25
print(f"{first_name} is {age} years old.")

#Floats
price = 19.99
print(f"The price of the pizza is ${price:}")

#Booleans
is_student = True
if is_student:
    print(f"{first_name} is a student.")
else:
    print(f"{first_name} is not a student.")

#Casting
name = "BroBro"
age = 30;
print(type(name))  # This will return <class 'str'>
age = float(age)  # Casting integer to float
print(age)  # This will print 30.0
print(type(age))  # This will return <class 'float'>

#User input
name = input("Enter your name: ")
print(f"Hello, {name}!")

age = input("Enter your age: ")
age = int(age)  # Convert input to integer
print(f"You are {age} years old.")

age = int(input("Enter your age: ")) #Even easier
print(f"You are {age} years old.")

#Python Functions
x = 3.14
y = -4
z = 5
result = round(x)
result = abs(y)
result = pow(z, 2)  # z raised to the power of 2
result = max(x, y, z)  # Maximum of x, y, z
result = min(x, y, z)  # Minimum of x, y, z

import math
print(math.pi) # Print the value of pi
result = math.sqrt(16)  # Square root of 16
math.ceil(4.2)  # Round up to the nearest integer
math.floor(4.8)  # Round down to the nearest integer

#If statements
temperature = 30
if temperature > 25:
    print("It's a hot day.")
elif temperature < 15:
    print("It's a cold day.")
else:
    print("It's a pleasant day.")

#While loops
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

#For loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

#Range function
for i in range(5):  # Prints numbers from 0 to 4
    print(i)
for i in range(1, 6):
    print(i)  # Prints numbers from 1 to 5
for i in range(0, 10, 2):  # Prints even numbers from 0 to 8
    print(i)
#Shortcut
i = 2
result = "EVEN" if i % 2 == 0 else "ODD"
print(f"{i} is {result}") #Print "2 is EVEN"

