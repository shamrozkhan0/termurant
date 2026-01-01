""" Summaru """
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
        while True:
            try:
                item = input("What would you like to have: ")
                food, quantity = self.validate_and_ditribute(item)
                self.order[food] = quantity
                print(f"{food} {quantity}")
                again = input("Would you like to order again (y/n):  ")
                if again.lower() == "y":
                    continue
                elif again.lower() == "n":
                    break
                else:
                    raise ValueError("")

            except ValueError as e:
                print(str(e))
            
        for i in self.order:
            print(i)
                

    def validate_and_ditribute(self, text):
        match = re.fullmatch(r"([a-zA-Z]+)\s*[xX]\s*([1-9][0-9]*)", text)
        if not match:
            raise ValueError("Please write the order in the giving sequence :)")
        
        food,quantity = text.lower().split('x')
        

        return (food.strip(),int(quantity.strip()))


def main():
    rest = Resturant()
    rest.show_banner()
    rest.show_menu()
    print()
    print('=============== CAUTION: WRITE YOUR ORDER IN THIS SEQUENCE ii-e ( burger X 2 ) =============== ')
    rest.waiter()


if __name__ == '__main__':
    main()


# import csv
# import re
# from pyfiglet import Figlet

# class Termurant:

#     @property
#     def banner(self):
#         f = Figlet(font="banner3-D")
#         return f.renderText("Welcome to Termurant")

#     @property
#     def menu(self):
#         print(f"{'Item':<15} {'Calories':<10} {'Price':<10}")
#         print("=" * 35)

#         items = []
#         with open("menu.csv", "r", encoding="utf-8") as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 items.append(row)
#                 print(f"{row['Name']:<15} {row['Calories']:<10} {row['Price']:<10}")
#                 print("-" * 35)
#         return items


# def take_order(menu_data):
#     order_list = []

#     while True:
#         order = input("\nWhat would you like to order? ").strip().lower()

#         if order == "done":
#             break

#         match = re.fullmatch(r"([a-zA-Z]+)\s*[xX]\s*([1-9][0-9]*)", order)
#         if not match:
#             print("Invalid format. Use: item x quantity")
#             continue

#         item_name = match.group(1)
#         quantity = int(match.group(2))

#         # check if item exists
#         found = False
#         for item in menu_data:
#             if item["Name"].lower() == item_name:
#                 order_list.append({
#                     "name": item_name,
#                     "qty": quantity,
#                     "price": int(item["Price"])
#                 })
#                 found = True
#                 break

#         if not found:
#             print("Item not on menu")
#             continue

#         again = input("Anything else? (y/n): ").lower()
#         if again == "n":
#             break

#     make_total(order_list)


# def make_total(order_list):
#     total = 0
#     print("\nYour Order:")
#     for item in order_list:
#         subtotal = item["qty"] * item["price"]
#         total += subtotal
#         print(f"{item['name']} x {item['qty']} = {subtotal}")

#     print(f"\nTotal bill: {total}")


# def main():
#     r = Termurant()
#     print(r.banner)
#     menu_data = menu
#     take_order(menu_data)


# if __name__ == "__main__":
#     main()
