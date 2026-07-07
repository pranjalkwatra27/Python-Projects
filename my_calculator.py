def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

Flag = True

while Flag:

    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    choice = input("Choose operation (+,-,*,/): ")

    result = operations[choice](n1, n2)

    print(result)

    again = input("Do you want to continue? (y/n): ")

    if again == "n":
        Flag = False
