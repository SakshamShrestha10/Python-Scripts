#function for adding two numbers
def add(num1, num2):
    return num1 + num2

# function for subtracting two numbers

def subtract(num1, num2):
    return num1 - num2

# function for multiplying two numbers

def multiply(num1, num2):
    return num1 * num2

# function for dividing two numbers

def divide(num1, num2):
    return num1 / num2

print("select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

option = float(input("select option from 1, 2, 3, 4 : "))
num1 = float(input("Enter a number :"))
num2 = float(input("Enter second number :"))

if option == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif option == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif option == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif option == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid choice")
