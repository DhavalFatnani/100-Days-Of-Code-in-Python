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
    "coffee": 100
}
profit = 0


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(_drink, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {_drink} ☕️. Enjoy!")


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    elif money_received == drink_cost:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def serve_order(_drink):
    ingredients = drink_name["ingredients"]
    if is_resource_sufficient(ingredients):
        payment = process_coins()
        if is_transaction_successful(payment, _drink["cost"]):
            make_coffee(drink, ingredients)


global drink
while True:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == "off":
        break
    elif drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif drink == "refill":
        resources["water"] += int(input("How many ml of water?: "))
        resources["milk"] += int(input("How many ml of milk?: "))
        resources["coffee"] += int(input("How many grams of coffee?: "))
    else:
        drink_name = MENU[drink.lower()]
        serve_order(drink_name)
