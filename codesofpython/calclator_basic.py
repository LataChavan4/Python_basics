



def add (n1, n2):
    return n1 + n2

def sub (n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div (n1, n2):
    return n1 / n2

math_operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
    }

def calculator():
    num1 = float(input("Enter the 1st number: "))
    print(math_operations.keys())
    
    continue_cal = True
    while continue_cal:
        operation = input("Enter the operation which you want to perform from list: ")
        num2 = float(input("Enter the 2nd number: "))

        function = math_operations[operation]
        answer = function(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        action = input("Enter 'y' if you want to continue or 'n' to stop and 's' for new session")

        if action == "y":
            num1 = answer
        elif action == "n":
            continue_cal = False
        elif action == "s":
            continue_cal = False
            calculator()

        # operation = input("Pick another operation: ")
        # num3 = float(input("Enter the number: "))

        # function = math_operations[operation]
        # second_answer = function(first_answer, num3)

        # print(f"{first_answer} {operation} {num3} = {second_answer}")

calculator()

