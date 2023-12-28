import os
import art

print(art.logo)

def addition(num1, num2):
    """Returns sum of two number."""
    result = num1 + num2
    return result

def subtraction(num1, num2):
    """Returns subtraction of two numbers."""
    result = num1 - num2
    return result

def multiplication(num1, num2):
    """Returns multiplication of two numbers."""
    result = num1 * num2
    return result

def devision(num1, num2):
    """Returns devision of two numbers."""
    result = num1 / num2
    return result

def calculator(num1, num2, operation):

    if operation == "+":
       output = addition(num1, num2)
    elif operation == "-":
        output = subtraction(num1, num2)
    elif operation == "*":
        output = multiplication(num1, num2)
    elif operation == "/":
        output = devision(num1, num2)
    return output
while True:
    fist_num = int(input("What's the first number?: ")) 
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    second_num = int(input("What's the next number?: "))
    output = calculator(fist_num, second_num, operation)
    want_to_continue = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
    if want_to_continue == 'y':
        operation = input("Pick an operation: ")
        second_num = int(input("What's the next number?: "))
        output = calculator(output, second_num, operation)
        want_to_continue = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
        if want_to_continue == 'n':
            os.system('cls||clear')
    elif want_to_continue == 'n':
        os.system('cls||clear')
        fist_num = int(input("What's the first number?: ")) 
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        second_num = int(input("What's the next number?: "))
        output = calculator(fist_num, second_num, operation)
        want_to_continue = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
