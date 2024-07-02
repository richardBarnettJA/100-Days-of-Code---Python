from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def machine():
    is_running = True
    coffee_menu = Menu()
    menu_items = coffee_menu.get_items()
    while is_running:
        coffee_maker = CoffeeMaker()
        money_machine = MoneyMachine()
        money = 0
        coffee = (input(f"What would you like? ({menu_items}): ")).lower()
        if coffee == "report":
            coffee_maker.report()
            money_machine.report()
        elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
            item = coffee_menu.find_drink(coffee)
            if coffee_maker.is_resource_sufficient(item):
                if money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)
        elif coffee == "off":
            is_running = False
        else:
            print("Error! Invalid entry! Please try again.")
    print("Goodbye!!!")


machine()