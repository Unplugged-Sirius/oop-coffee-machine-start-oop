from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
money = MoneyMachine()
opts = Menu()
while True:
    print("what do u want to have")
    menues = opts.get_items()
    print(menues)

    choice = input("enter the drink")
    if choice == "report":
        machine.report()
        money.report()
        continue
    drink = opts.find_drink(choice)
    k = machine.is_resource_sufficient(drink)
    if k == True:
        s = money.make_payment(drink.cost)
    else:
        continue
    if s == True:
        machine.make_coffee(drink)
    else:
        continue
