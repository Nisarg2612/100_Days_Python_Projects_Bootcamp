MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte":{
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
    },
}

sales = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# made a separate copy of machine resources to track ingredients
current_resources = resources.copy()

# TODO 1. Print report of all coffee machine resources
def print_report():
    for key, values in current_resources.items():
        print(f"{key} : {values}")

# TODO 2. Check the resources sufficient to make drink order.
def is_resource_sufficient(ordered_drink):
    """Return True when order can be made, False if ingredients are insufficient."""

    for item in ordered_drink["ingredients"]:
        if ordered_drink["ingredients"][item] > current_resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# TODO 3. Prompt the user to insert coins and Calculate the monetary value of the inserted coins
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

# TODO 4. Check that the user has inserted enough money to purchase the drink they selected
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received == drink_cost:
        global sales
        sales += drink_cost
        return True
    elif money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        sales += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

# TODO 5. Deduct resources, restart the code
def make_coffee(drink_name, ordered_item):
    """Deduct the required ingredients from the resources"""
    for item in ordered_item["ingredients"]:
        current_resources[item] -= ordered_item["ingredients"][item]
    print(f"Here is your {drink_name}. Enjoy! ☕")

def refill_ingredients(leftover_resources):
    for item in leftover_resources:
        if leftover_resources[item] != resources[item]:
            current_resources[item] += (resources[item] - leftover_resources[item])
        else:
            pass
    print_report()
    print("Machine has been refilled. Ready to Brew! ")

coffee_machine_is_on = True
while coffee_machine_is_on:
    try:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            coffee_machine_is_on = False
            print(f"Machine is OFF")
        elif choice == "report":
            print_report()
            print(f"Money: ${sales}")
        elif choice == "refill":
            refill_ingredients(current_resources)
        else:
            drink = MENU[choice]
            if is_resource_sufficient(drink) is True:
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink)
    except:
        print("ERROR")
