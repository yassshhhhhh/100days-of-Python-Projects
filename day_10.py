# Calculator
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
              }

while True:
    first_number = int(input("Enter the first number: "))
    is_ture = True
    while is_ture is True:
        for operation in operations:
            print(operation)
        operation = input("Pick an operation: ")
        second_number = int(input("Enter the next number: "))
        answer = operations[operation](first_number, second_number) # Calling a function using dictionary.
        print(f"{first_number} {operation} {second_number} = {answer}")
        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if cont == "y":
            print("clear")# clear()
            first_number = answer
        elif cont == "n":
            is_ture = False

