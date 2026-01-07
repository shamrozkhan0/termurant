""" A Simple Restaurant order program made in OOP using python for CS50 python course """
import csv
import re
from pyfiglet import Figlet

def verifier(msg):
    while True:
        print()
        res = input(f"{msg}? (y/n): ").strip().lower()

        if res == 'y':
            return True
        elif res == 'n':
            return False
        else:
            print()
            print("Error: Please enter 'y' or 'n'")


def show_banner():
    """ SHows Banner in the terminal"""
    f = Figlet(font="rowancap")
    print(f.renderText("Welcome To Termurant"))


class Restaurant:

    def __init__(self):
        self.menu = dict({})
        self.order = dict({})


    def show_menu(self):
        """ Show menu """
        print(f"{'='*11} Menu {'='*11}")
        print(f'{"Item":<20} {"Price":>6}')
        print("=" * 28)

        with open("menu.csv", "r", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                name = row["Name"]
                price = int(row["Price"])
                self.menu[name.lower()] = price
                print(f'{name:<21} $ {price:02}')
        print("=" * 28)


    def waiter(self):
        """ Ask User About there order """
        while True:
            try:
                print()
                item = input("What would you like to have? ")
                food, quantity = self.validate_and_distribute(item)

                if food in self.order:
                    self.order[food.lower()] += quantity
                else:
                    self.order[food.lower()] = quantity

                if not verifier("Anything else"):
                    break

            except ValueError as e:
                print()
                print(f"Error: {str(e)}")

        self.repeat_order()


    def validate_and_distribute(self, text):
        """Summary"""
        match = re.fullmatch(r"([a-zA-Z ]+)\s*[xX]\s*([1-9][0-9]*)", text)
        if not match:
            raise ValueError(
                "Please write the order in the giving sequence :)")

        food = match.group(1).strip().lower()
        quantity = int(match.group(2))

        if food.strip() not in list(self.menu.keys()):
            raise ValueError("The food is not in the menu")

        return food, quantity


    def repeat_order(self):
        print()
        print(f"{'='*15} Your Order {'='*15} ")

        for key, value in self.order.items():
            print(f"{key} x {value}")
        print('='*42)


    def order_confirm(self):
        if not verifier("Is this your final order"):
            self.waiter()


    def order_total(self):
        total = 0
        for name, quantity in self.order.items():
            total += self.menu[name] * quantity
        return total


def main():
    rest = Restaurant()
    show_banner()
    rest.show_menu()
    print()
    print('=============== CAUTION: WRITE YOUR ORDER IN THIS SEQUENCE i-e ( burger X 2 ) =============== ')
    rest.waiter()
    rest.order_confirm()
    print()
    print('=' * 50)
    print(f"Thanks for choosing us here is your total bill: ${rest.order_total()}")
    print('=' * 50)


if __name__ == '__main__':
    main()
