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
    "Money": 0
}


def coffee_maker():
    global main

    money = {"quarters": 0,
             "dimes": 0,
             "nickles": 0,
             "pennies": 0,
             }

    drink = input('What would you like?(espresso/latte/cappuccino)')
    if drink == 'off':
        main = 'off'
    if drink == 'report':
        for i in resources:
            print(f"{i.capitalize()} : {resources[i]}")

    if drink == 'expresso' or 'latte' or 'cappuccino':
        for i in MENU:
            if i == drink:
                for ing in MENU[drink]['ingredients']:
                    if MENU[drink]['ingredients'][ing] > resources[ing]:
                        print(f'Sorry there is not enough {ing}')
                        return
                for m in money:
                    coin = float(input(f"Insert {m}: "))
                    money[m] = coin
                money_inserted = money['quarters'] * 0.25 + money['dimes'] * 0.10 + money[
                    'nickles'] * 0.05 + money['pennies'] * 0.01
                if money_inserted < MENU[drink]['cost']:
                    print('Sorry that`s not enough. Money refunded.')
                else:
                    resources['Money'] += MENU[drink]['cost']
                    change = money_inserted - MENU[drink]['cost']
                    print(f"Your change is {round(change, 2)}")
                    for k in MENU[drink]['ingredients']:
                        resources[k] -= MENU[drink]['ingredients'][k]

                    print(f"Here is your {drink}.Enjoy")


main = 'on'
print('Welcome to the coffee_Machine')
while main != 'off':
    coffee_maker()
