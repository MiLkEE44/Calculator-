import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-" :subtract,
    "*": multiply,
    "/": division,
}

def calculator():
    first = float(input("What's the first number?: "))

    calculating = True
    while calculating:

        sign = input(
            "+ \n"
            "_ \n"
            "* \n"
            "/ \n"
            "Pick an operation: ")

        second = float(input("What's the next number?: "))

        if sign == "+":
            function = operations["+"]
            result = function(first, second)
        if sign == "-":
            function = operations["-"]
            result = function(first, second)
        if sign == "*":
            function = operations["*"]
            result = function(first, second)
        if sign == "/":
            function = operations["/"]
            result = function(first, second)

        print(f"{first} {sign} {second} = {result}")

        end = input(f"Type 'y' to continue calculating with {result}, "
                f"or type 'n' to start a new calculation: ")

        if end == 'y':
            first = result
        else:
            calculating = False
            calculator()

calculator()
