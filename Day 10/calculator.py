# Calculator
from art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

print(logo)

num1 = float(input("What is the first number?: "))

again = "y"
while (again == "y"):
    for x in operations:
        print(x)
    
    operation_sumbol = input("Pick an operation from the list above: ")

    num2 = float(input("What is the second number?: "))

    answer = operations[operation_sumbol](num1, num2)

    print(f"{num1} {operation_sumbol} {num2} = {answer}")

    again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    if again == "y":
        num1 = answer
print("Goodbye")
