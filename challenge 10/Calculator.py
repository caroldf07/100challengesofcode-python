logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def division(x, y):
    if(y == 0):
        print("It can't divide per 0'")
    else:
        return x/y


def multiply(x, y):
    return x*y


operators = {
    "+": add,
    "-": subtract,
    "/": division,
    "*": multiply
}


def calculator():
    x = float(input("Please enter a number: "))

    keep_going = "y"

    while(keep_going == "y"):
        operator_chosen = input("Please enter the desired operation: ")
        y = float(input("Please enter a number: "))
        calculation = operators[operator_chosen]
        answer = calculation(x, y)
        print(f"{x} {operator_chosen} {y} = {answer}")
        keep_going = input(
            f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ").lower()
        if(keep_going == "y"):
            x = answer
            """Here we have a recursion when the user does not want to use the same answer before and it want to start a new iteration"""
        else:
            calculator()


calculator()
