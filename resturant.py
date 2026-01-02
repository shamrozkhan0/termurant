""" Summary """
import csv
import re
from pyfiglet import Figlet


class Resturant:
    """ Class Doc-String"""
    menu = []

    def __init__(self):
        self.order = dict({})

    def show_banner(self):
        """ SHows Banner in the terminal"""
        f = Figlet(font="rowancap")
        print(f.renderText("Welcome To Termurant"))

    @classmethod
    def show_menu(cls):
        """ Show menu """
        print(f"{'='*11} Menu {'='*11}")
        print(f'{"Item":<20} {"Price":>6}')
        print("=" * 28)

        with open("menu.csv", "r", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                name = row["Name"]
                cls.menu.append(name.lower())
                price = int(row["Price"])
                print(f'{name:<21} $ {price:02}')
        print("=" * 28)

    def waiter(self):
        """ Ask User About there order """
        while True:
            try:
                print()
                item = input("What would you like to have? ")
                food, quantity = self.validate_and_ditribute(item)

                if food in self.order:
                    self.order[food.lower()] += quantity
                else:
                    self.order[food.lower()] = quantity

                if self.verifier("Anything else"):
                    break

            except ValueError as e:
                print()
                print(f"Error: {str(e)}")

    def verifier(self,msg):
        while True:
            print()
            res = input(f"{msg}? (y/n): ").strip().lower()

            if res == 'n':
                return True
            elif res == 'y':
                return False
            else:
                print()
                print("Error: Please enter 'y' or 'n'")

    def validate_and_ditribute(self, text):
        """Summary"""
        match = re.fullmatch(r"([a-zA-Z]+)\s*[xX]\s*([1-9][0-9]*)", text)
        if not match:
            raise ValueError(
                "Please write the order in the giving sequence :)")

        food, quantity = text.lower().split('x')

        if food.strip().lower() not in self.menu:
            raise ValueError("The food is not in the menu")

        return (food.strip(), int(quantity.strip()))

    def repeat_order(self):
        print()
        print(f"{'='*15} Your Order {'='*15} ")

        for key, value in self.order.items():
            print(f"{value} {key}")
    
    def order_confirm(self):
        print()
        if self.verifier("Is this your final order"):
            self.waiter()
    


def main():
    rest = Resturant()
    rest.show_banner()
    rest.show_menu()
    print()
    print('=============== CAUTION: WRITE YOUR ORDER IN THIS SEQUENCE i-e ( burger X 2 ) =============== ')
    rest.waiter()
    rest.repeat_order()
    rest.order_confirm()
    # rest.order_total()
    print(rest.order.items())


if __name__ == '__main__':
    main()
