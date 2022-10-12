# Calculator

from art  import logo

# Dictionary of operations
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}



# Add
def add(x, y):
    """Add Function"""
    return x + y

# Subtract

def subtract(x, y):
    """Subtract Function"""
    return x - y

# Multiply

def multiply(x, y):
    """Multiply Function"""
    return x * y

# Divide

def divide(x, y):
    """Divide Function"""
    return x / y



# Print the logo
print(logo)
# Ask the user if they want to continue
should_continue = False
while not should_continue:
        should_continue = True
        num1 = float(input("What's the first number?: "))
        num2 = float(input("What's the second number?: "))
        operation = input("Pick an operation from the line above: ")
        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or n for end the calculation.").lower == "n":
            should_continue = False
            print("Goodbye!")
        else:
            num1 = answer
            