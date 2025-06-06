#*args allows you to pass a variable number of arguments to a function.
#**kwargs allows you to pass a variable number of keyword arguments to a function.
'''
def add(a, b):
    return a + b

add(1, 2)  #This will return 3
'''
def add(*args):
    #Adds an arbitrary number of arguments.
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2))  # This will return 3
print(add(1, 2, 3, 4, 5))  # This will return 15

#kwargs
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street = "123 Fake St.", 
              city = "Fakeville", 
              state = "Fake", 
              zip = "56789")