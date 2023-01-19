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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
machine_sate = True

def get_resourcesrequired(choice):
    coffee = MENU[choice]["ingredients"]
    water = coffee["water"]
    milk = coffee["milk"]
    coffee = coffee["coffee"]
    return f"Required ingredients are water = {coffee.water}, milk = {coffee.milk}, coffee = {coffee.coffee} "
    print(coffee)

#TODO1: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

get_resourcesrequired(choice)
if choice == 'off':
    machine_sate = False
elif choice == 'report':
    print(resources)

