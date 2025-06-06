#This program calculates the total amount after applying compound interest.
principal = 0
rate = 0
time = 0
while True:
    principal = float(input("Enter the principal amount (greater than 0): "))
    if principal <= 0:
        print("Please enter a valid principal amount greater than 0.")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest (greater than 0): "))
    if rate <= 0:
        print("Please enter a valid rate of interest greater than 0.")
    else:
        break

while True:
    time = float(input("Enter the time period in years (greater than 0): "))
    if time <= 0:
        print("Please enter a valid time period greater than 0.")
    else:
        break

total = principal * pow((1 + rate / 100), time)
print(f"Balance after {time:.1f} year/s: ${total:.2f}")

# Example usage:
# Enter the principal amount (greater than 0): 1000
# Enter the rate of interest (greater than 0): 5
# Enter the time period in years (greater than 0): 2
# Balance after 2.0 year/s: $1102.50