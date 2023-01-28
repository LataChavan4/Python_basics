from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"select the drink required {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()

    else:
        drink = menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink):
        
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            
        else:
            print(f"Sorry there isn't enough ingredients for {drink}")
            is_on = False





