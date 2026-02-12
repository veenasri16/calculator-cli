# ----------------------------------------
# Simple Calculator CLI Application
# ----------------------------------------

# Function Definitions

def add(a, b):
    """Returns addition of two numbers"""
    return a + b


def subtract(a, b):
    """Returns subtraction of two numbers"""
    return a - b


def multiply(a, b):
    """Returns multiplication of two numbers"""
    return a * b


def divide(a, b):
    """Returns division of two numbers"""
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Main Program

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        

        choice = input("Enter your choice (1-5): ")

        # Exit Condition
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        # Check if valid operation selected
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)

                print("Result:", result)

            except ValueError:
                print("Invalid input! Please enter numeric values only.")

        else:
            print("Invalid choice! Please select between 1 and 5.")


# Run the program
if __name__ == "__main__":
    main()