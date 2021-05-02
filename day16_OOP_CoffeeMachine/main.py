from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()

while is_on:
    choice = input("What would you like?(espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()

    #when the user chooses a drink
    else:
        drink = my_menu.find_drink(choice)
        can_make_main = my_coffee_maker.is_resource_sufficient(drink)

        if can_make_main:
            payment_accepted = my_money_machine.make_payment(drink.cost)

            if payment_accepted:
                my_coffee_maker.make_coffee(drink)











