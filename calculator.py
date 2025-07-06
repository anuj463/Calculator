# Python project to implement calculator functionality
# Author:Anuj Savant
# Date:06/07/2025

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

operator = input("Enter the opeartor:")

if operator == '+':
    print("Sum = ",num1 + num2)
elif operator == '-':
    print("Difference = ", num1 - num2)
elif operator == '*':
    print("Product = ", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Quotient = ", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
elif operator == '%':
    print("Remainder = ", num1 % num2)

else:
    print("Invalid operator")
    