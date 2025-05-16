from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create the Objects from Classes
item_list = Menu()
machine = CoffeeMaker()
transaction = MoneyMachine()

coffee_machine_is_on = True
while coffee_machine_is_on:
    user_choice = input(f"What would you like? ({item_list.get_items()}): ").lower()
    if user_choice == "off":
        coffee_machine_is_on = False
        print(f"Machine is OFF")
    elif user_choice == "report":
        machine.report()
        transaction.report()
    else:
        ordered_drink = item_list.find_drink(user_choice)
        if machine.is_resource_sufficient(ordered_drink) and transaction.make_payment(ordered_drink.cost):
            machine.make_coffee(ordered_drink)
