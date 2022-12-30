menu = {
    'espresso' : {
        'ingredients': {
            'water':50,
            'coffee':18
        },
        'cost':1.5
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'coffee':24,
            'milk':150
        },
        'cost': 2.5
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'coffee': 24,
            'milk': 100
        },
        'cost': 3.0
    }
}
resources = {
    'water': 300,
    'coffee': 100,
    'milk': 200
}
total = 0
bank = 0


def calculate_money():
    global total
    quarter = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    total = (quarter*0.25)+(dimes*0.1)+(nickels*0.05)+(pennies*0.01)
    return total


def check_enough_material(user_chosen):
    contains = (menu[user_chosen]['ingredients'])

    # print(contains)
    controller = True
    for i in contains:
        resources[i] = resources[i] - contains[i]
        if resources[i] < 0:
            print(f"Sorry there is not enough {i}.")
            controller = False
    if controller:
        print("Please insert coins.")
    return controller


def money_check():
    global total, bank
    price = menu[user_choice]['cost']
    if total >= price:
        change = round(total-price, 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {user_choice} ☕️. Enjoy!")
        bank += price
    else:
        print(" Sorry that's not enough money. Money refunded.")


while True:
    user_choice = input("    What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'report':
        print(f"Water: {resources['water']}mL")
        print(f"Milk: {resources['milk']}mL")
        print(f"Coffee: {resources['coffee']}gr ")
        print(f"Money: ${bank}")
    elif user_choice == 'off':
        break
    else:
        # check_enough_material(user_choice)
        control_material = check_enough_material(user_choice)
        if control_material:
            calculate_money()
            money_check()
