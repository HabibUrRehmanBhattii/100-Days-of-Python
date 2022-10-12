from operator import imod
from art import logo

# Addition
def add(n1, n2):
    """Add Function"""
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    """Subtract Function"""
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    """Multiply Function"""
    return n1 * n2

# Division
def divide(n1, n2):
    """Divide Function"""
    return n1 / n2

# Dictionary of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for sysmbol in operations:
        print(sysmbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calulation_function = operations[operation_symbol]
        answer = calulation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or n for end the calculation.").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
            

    
""" The code above does the following, explained in English:
1. Ask the user for the first number.
2. Ask the user for the operation they want to use.
3. Ask the user for the next number.
4. Perform the calculation.
5. Print the result.
6. Ask the user if they want to use the result as the first number for the next calculation.
7. If the user types 'y', then start at step 2.
8. If the user types 'n', then exit the program. """
