from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
menu = Menu()
coffee_machine = CoffeeMaker()
cashier = MoneyMachine()

while is_on:
    order = input(f"What would you like? {menu.get_items()}: ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_machine.report()
        cashier.report()
    else:
        if coffee_machine.is_resource_sufficient(menu.find_drink(order)):
            if cashier.make_payment(menu.find_drink(order).cost):
                coffee_machine.make_coffee(menu.find_drink(order))

        
    
