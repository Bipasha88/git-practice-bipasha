print("Bipasha Saha")

from datetime import date
print(date.today())

from utils import add,subtract,multiply

# main.py

import utils

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Add:", utils.add(num1, num2))
    print("Subtract:", utils.subtract(num1, num2))
    print("Multiply:", utils.multiply(num1, num2))

except ValueError:
    print("Error: Please enter valid numbers.")

except Exception as e:
    print("Unexpected error:", e)