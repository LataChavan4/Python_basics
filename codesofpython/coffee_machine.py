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
machine_state = True
profit = 0

def resource_check(order_ingredients, resorces):
    for item in order_ingredients:
        if order_ingredients[item] > resorces[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quaters = int(input("How many quaters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    penny = int(input("How many penny?: "))
    total_amount = ((quaters*25) + (dimes*10) + (nickels*5) + (penny))/100
    return total_amount


def check_trascation(coins_received, drink_cost):
    if coins_received >= drink_cost:
        change = round(drink_cost - coins_received, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")   



#TODO1: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while machine_state:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        machine_state = False
    elif choice == 'report':
        print(resources)
        print(f"profit: {profit}")
    else:
        drink = MENU[choice]
        if resource_check(drink["ingredients"], resources):
            payment = process_coins()
            if check_trascation(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])






    

    
