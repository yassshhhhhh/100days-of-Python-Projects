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


def report(quantities):
    print(f'Water: {quantities["water"]}ml \nMilk: {quantities["milk"]}ml \nCoffee: {quantities["coffee"]}g \nMoney: ${money}')


def insert_coins():
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    cents = float(input("How many cents?: "))
    total_cost = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (cents * 0.01)
    return total_cost


money = 0
game = True
while game:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        report(resources)
    elif user_input == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            cost = float(MENU["espresso"]["cost"])
            print(f"Espresso costs ${cost}, Please insert coins.")
            coins = insert_coins()
            if coins < cost:
                print("Sorry that's not enough money. Money refunded.")
            # elif insert_coins() == cost:
            #     print("Here is your espresso ☕. Enjoy!")
            else:
                change = round(coins - cost, 2)
                print(f"Here is ${change} in change.")
                print("Here is your espresso ☕. Enjoy!")
                resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                # resources["milk"] = resources["milk"] - 0
                resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
                money += cost
    elif user_input == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            cost = float(MENU["latte"]["cost"])
            print(f"Latte costs ${cost}, Please insert coins.")
            coins = insert_coins()
            change = round(coins - cost, 2)
            if coins < cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is ${change} in change.")
                print("Here is your latte ☕. Enjoy!")
                resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                money += cost
    elif user_input == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            cost = float(MENU["cappuccino"]["cost"])
            print(f"Cappuccino costs ${cost}, Please insert coins.")
            coins = insert_coins()
            change = round(coins - cost, 2)
            if coins < cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is ${change} in change.")
                print("Here is your cappuccino ☕. Enjoy!")
                resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                money += cost
    elif user_input == "off":
        game = False
# Update above project - Coffee machine with OOPs.

