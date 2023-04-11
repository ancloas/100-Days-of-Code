from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_on=True

coffee_menu=Menu()
coffee_machine=CoffeeMaker()
money_machine=MoneyMachine()

while turn_on:
    req=input("What would you like? (espresso/latte/cappuccino/): ")

    if req in coffee_menu.get_items():
        drink=coffee_menu.find_drink(req)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)


    elif req.lower()=='off':
        turn_on=False
    elif req.lower()=='report':
        coffee_machine.report()
        money_machine.report()
    
