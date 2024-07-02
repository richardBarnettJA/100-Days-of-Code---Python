from coffee_data import MENU, resources

def get_resources():
    """Gets the data to return all the resources"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = round(resources["money"], 2)
    return water, milk, coffee, money

def report():
    """Prints the report of the coffee machine"""
    water, milk, coffee, money = get_resources()
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def get_coins():
    """Gets coins from user and returns the total"""
    print("Please insert coins")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)


def update_resources(water, milk, coffee, money):
    """Takes water, milk, coffee and money to update the resources in the machine"""
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee
    resources["money"] += money


def get_coffee(drink, money):
    """Takes the drink and the money given in order to give user their drink or not"""
    coffee = MENU[drink]
    ingredients = coffee["ingredients"]
    water, milk, coffee, total = get_resources()
    cost = MENU[drink]["cost"]
    if cost > money:
        print(f"You do not have enough money to pay for your {drink}.")
        print(f"Here is your ${money} back.")
    elif water < ingredients["water"]:
        if milk < ingredients["milk"]:
            if coffee < ingredients["coffee"]:
                print(f"There is not enough water, milk or coffee to make your {drink}.")
                return 0 
            print(f"There is not enough water or milk to make your {drink}.")
            return 0 
        print(f"There is not enough water to make your {drink}.")
    elif milk < ingredients["milk"]:
        if coffee < ingredients["coffee"]:
            print(f"There is not enough milk or coffee to make your {drink}.")
            return 0 
        print(f"There is not enough milk to make your {drink}.")
    elif coffee < ingredients["coffee"]:
        print(f"There is not enough coffee to make your {drink}.")
    else:
        change = round(money - cost, 2)
        update_resources(ingredients["water"], ingredients["milk"], ingredients["coffee"], cost)
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink} 😁 Enjoy!")



def machine():
    is_running = True
    while is_running:
        money = 0
        coffee = (input("What would you like? (espresso/latte/cappuccino): ")).lower()
        if coffee == "report":
            report()
        elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
            money = get_coins()
            get_coffee(coffee, money)
        elif coffee == "off":
            is_running = False
        else:
            print("Error! Invalid entry! Please try again.")
    print("Goodbye!!!")


machine()