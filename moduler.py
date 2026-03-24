
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b != 0:
    result = a % b
    print("Remainder is:", result)
else:
    print("Error: Cannot divide by zero")