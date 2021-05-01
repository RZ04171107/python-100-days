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
    "money": 0
}


def print_the_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def prompt_start():
    user_choice = input("What would you like?(espresso/latte/cappuccino):")

    ## Turn off the coffee machine by entering "off" to the prompt
    if user_choice == "off":
        quit()
    ## When the user enters "report" to the prompt, a report should be generated
    ## that shows the current resource
    elif user_choice == "report":
        print_the_report()
        prompt_start()
    else:

        if not check_resources(user_choice):  # when all the resources are enough
            # then ask the user to insert coins
            money_inserted = precess_coins()

            # check transaction successful?
            if check_money(user_choice, money_inserted):
                # report before purchasing the drink
                print_the_report()
                money_left = make_coffee(user_choice, money_inserted)
                if money_left > 0:
                    print(f"Here is ${money_left} dollars in change.")
                # report after purchasing the drink
                print_the_report()

                print(f"Here is your {user_choice}. Enjoy!")

                # The coffee machine will restart after the user purchasing a drink
                prompt_start()
            else:
                print("Sorry that's not enough money, Money refunded.")

        # when something is not enough
        else:
            print(f"Sorry there is not enough {check_resources(user_choice)}")

        prompt_start()


def precess_coins():
    print("Please insert coins:")
    quarters = int(input("How many quarters? :"))
    dimes = int(input("How many dimes? :"))
    nickles = int(input("How many nickles? :"))
    pennies = int(input("How many pennies? :"))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def check_money(drink, money_inserted):
    if drink == "espresso" and money_inserted >= 1.5:
        return True
    elif drink == "latte" and money_inserted >= 2.5:
        return True
    elif drink == "cappuccino" and money_inserted >= 3.0:
        return True
    return False


def check_resources(drink):
    """returns None when all the resources(water, coffee and milk) are enough"""
    what_not_enough = ""
    if drink == "espresso":
        if resources["water"] < 50:
            what_not_enough = "water"
        elif resources["coffee"] < 18:
            what_not_enough = "coffee"
    elif drink == "latte":
        if resources["water"] < 200:
            what_not_enough = "water"
        elif resources["coffee"] < 24:
            what_not_enough = "coffee"
        elif resources["milk"] < 150:
            what_not_enough = "milk"
    elif drink == "cappuccino":
        if resources["water"] < 250:
            what_not_enough = "water"
        elif resources["coffee"] < 24:
            what_not_enough = "coffee"
        elif resources["milk"] < 100:
            what_not_enough = "milk"
    return what_not_enough


def make_coffee(coffee, money_inserted):
    """ Returns the change, which should be rounded to 2 decimal places"""
    money_left = 0
    if coffee == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
        resources["money"] += 1.5
        money_left = money_inserted - 1.5
    elif coffee == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        resources["money"] += 2.5
        money_left = money_inserted - 2.5
    elif coffee == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        resources["money"] += 3.0
        money_left = money_inserted - 3.0
    else:
        print("input error")
    return round(money_left, 2)


prompt_start()
