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
    ''' check resources required'''
    coffee_type = MENU[choice]["ingredients"]
    water = coffee["water"]
    milk = coffee["milk"]
    coffee = coffee["coffee"]
    return f"Required ingredients are water = {coffee.water}, milk = {coffee.milk}, coffee = {coffee.coffee} "
    if water >= resources["water"] and milk >= resources["milk"] and coffee >= resources["coffe"]:
        resources["water"] = resources["water"] - water
        resources["milk"] = resources["milk"] - milk
        resources["coffee"] = resources["coffee"] - coffee
        print(f"Here is your {choice}. Enjoy!")



#TODO1: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

get_resourcesrequired(choice)
if choice == 'off':
    machine_sate = False
elif choice == 'report':
    print(resources)

print("Please insert coins.")
quaters = int(input("How many quaters?: "))
dimes = int(input("How many dimes?: "))
nickels = int(input("How many nickels?: "))
penny = int(input("How many penny?: "))

total_amount = ((quaters*25) + (dimes*10) + (nickels*5) + (penny))/100
cost = MENU[choice]["cost"]
if cost > total_amount:
    print("Sorry that's not enough money. Money refunded.")
if cost < total_amount:
    change = (total_amount - cost)
    print(f"Here is $ {change} in change.")



    

    
