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
profit=0

def is_resource_sufficient(order_ingredients):
    # Checks if enough ingredients are available to make the coffee
    for item in order_ingredients:
        if order_ingredients[item]> resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    # Return the total calculated from the coins inserted
    print("Please insert coins")
    total=0
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.1
    nickles= int(input("how many nickles?: ")) * 0.05
    pennies= int(input("how many pennies?: ")) * 0.01
    total=quarters+dimes+nickles+pennies
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        profit+=drink_cost
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def resource_deduction(drink_name,requirements):
    for item in requirements:
        resources[item]-=requirements[item]
    print(f"Here is your {drink_name}!")

def add_resources():
    resources["water"]+=int(input("How much water you wanna add?: "))
    resources["milk"]+=int(input("How much milk you wanna add?: "))
    resources["coffee"]+=int(input("How much coffee you wanna add?: "))
    
    
while True:
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="off":
        break
    elif choice=="report":
        print(f"""Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${profit}""")
    elif choice=="add resources":
        add_resources()
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                resource_deduction(choice,drink["ingredients"])
