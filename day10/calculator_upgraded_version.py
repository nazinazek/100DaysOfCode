import os
import art

print(art.logo)

def add(n1, n2):
    """Returns sum of two numbers."""
    return n1 + n2
    
def subtract(n1, n2):
    """Returns subtraction of two numbers."""
    return n1 - n2
    
def multiply(n1, n2):
    """Returns multiplication of two numbers."""
    return n1 * n2
    
def devide(n1, n2):
    """Returns devision of two numbers."""
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : devide
}

while True: 
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operations_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operations_symbol]
    output = calculation_function(num1, num2)
    want_to_continue = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
    while want_to_continue == 'y':
        operations_symbol = input("Pick an operation: ")
        num3 = float(input("What's the next number?: "))
        calculation_function = operations[operations_symbol]
        output = calculation_function(output, num3)
        want_to_continue = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
    os.system('cls||clear')

