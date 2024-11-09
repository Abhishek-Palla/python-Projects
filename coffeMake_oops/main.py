from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    user_choice =input(f"What do you want {menu.get_items()}")
    if user_choice.lower() == "off":
        is_on = False
    if user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
        continue
    drink = menu.find_drink(user_choice)
    print(f"you have selected {drink.name}")
    print(f"The cost of {drink.name} is {drink.cost}")
    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

















