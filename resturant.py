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
        print(f'{"Item":<20} {"Price":>6}')
        print("=" * 28)

        with open("menu.csv", "r", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                name = row["Name"]
                cls.menu.append(name)
                price = int(row["Price"])
                print(f'{name:<21} $ {price:02}')

        print("=" * 28)



    def waiter(self):
        """ Summary """
        while True:
            try:
                print()
                item = input("What would you like to have: ")
                food, quantity = self.validate_and_ditribute(item)
                
                if food in self.order:
                    self.order[food.lower()] += quantity
                else:
                    self.order[food.lower()] = quantity
                
                if self.verfiy_re_order:
                    break

            except ValueError as e:
                print(f"Error: {str(e)}")

        for key, value in self.order.items():
            print(key,value)
    
    
    @property
    def verfiy_re_order(self):
        print()
        res = input("Would you like to order something else (y/n): ").strip()
        while True:
            try:
                if res.lower() not in ['y','n']:
                    raise ValueError("Please enter 'y' or 'n'")
                
                break
            except ValueError as e:
                print(f"Error: {str(e)}")
                
        if res.lower() == 'n':
            return True
                        

        

    def validate_and_ditribute(self, text):
        """Summary"""
        match = re.fullmatch(r"([a-zA-Z]+)\s*[xX]\s*([1-9][0-9]*)", text)
        if not match:
            raise ValueError(
                "Please write the order in the giving sequence :)")

        food, quantity = text.lower().split('x')

        return (food.strip(), int(quantity.strip()))


def main():
    rest = Resturant()
    rest.show_banner()
    rest.show_menu()
    print()
    print('=============== CAUTION: WRITE YOUR ORDER IN THIS SEQUENCE i-e ( burger X 2 ) =============== ')
    rest.waiter()


if __name__ == '__main__':
    main()
