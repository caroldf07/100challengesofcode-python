MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_enough(order):
    for item in order:
        if order[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins: ")
    total = int(input("How many quartes?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


is_on = True


def is_transaction_successul(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += payment
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(choice, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]

    print(f"Here is your {choice} ")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_enough(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successul(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
