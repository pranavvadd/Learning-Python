#Below is a simple calculator program that performs basic arithmetic operations.
operator = input("Enter the operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator."
print(f"The result is: {result}")
# Example usage:
# Enter the operator (+, -, *, /): +
# Enter the first number: 10
# Enter the second number: 5
# The result is: 15.0