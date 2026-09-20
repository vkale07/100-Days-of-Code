from art import calculator_logo


def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(calculator_logo)
    num1 = float(input("What's the first number?: "))
    calculation_continue = True

    while calculation_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if to_continue == "y":
            num1 = result
        else:
            calculation_continue = False
            print("\n" * 20)
            calculator()

calculator()