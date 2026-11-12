
class Calculator:

    def __init__(self):
        print("Calculator Initialized!")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero is not allowed."
        return a / b

    def modulus(self, a, b):
        if b == 0:
            return "Error! Division by zero is not allowed."
        return a % b

    def power(self, a, b):
        return a ** b


# Creating an object
calc = Calculator()

while True:

    print("\n===== OOP CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "7":
        print("Thank you for using Calculator!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice!")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        result = calc.add(a, b)

    elif choice == "2":
        result = calc.subtract(a, b)

    elif choice == "3":
        result = calc.multiply(a, b)

    elif choice == "4":
        result = calc.divide(a, b)

    elif choice == "5":
        result = calc.modulus(a, b)

    elif choice == "6":
        result = calc.power(a, b)

    print("Result:", result)
