from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

check = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
coffee = MenuItem()

def coffee_machine(choice):
  b = check.is_resource_sufficient(choice)
  print(b)
  a = menu.find_drink(choice)
  print(a)

coffee.name 
is_not_over = True
while is_not_over:
  choice = input(f"What would you like? ({menu.get_items()}): ")
  if choice == "report":
    check.report()
    money.report()
  # elif choice == 'espresso':
  #   coffee_machine(choice)
