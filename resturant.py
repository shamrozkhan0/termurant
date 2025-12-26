import csv
import re
from pyfiglet import Figlet


def main():
    show_banner()
    menu_data = show_menu()
    take_order(menu_data)


def show_banner():
    f = Figlet(font="banner3-D")
    print(f.renderText("Welcome to Termurant"))


def show_menu():
    print(f"{'Item':<15} {'Calories':<10} {'Price':<10}")
    print("=" * 35)

    items = []
    with open("menu.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(row)
            print(f"{row['Name']:<15} {row['Calories']:<10} {row['Price']:<10}")
            print("-" * 35)
    return items


def take_order(menu_data):
    order_list = []

    while True:
        order = input("\nWhat would you like to order? ").strip().lower()

        if order == "done":
            break

        match = re.fullmatch(r"([a-zA-Z]+)\s*[xX]\s*([1-9][0-9]*)", order)
        if not match:
            print("Invalid format. Use: item x quantity")
            continue

        item_name = match.group(1)
        quantity = int(match.group(2))

        # check if item exists
        found = False
        for item in menu_data:
            if item["Name"].lower() == item_name:
                order_list.append({
                    "name": item_name,
                    "qty": quantity,
                    "price": int(item["Price"])
                })
                found = True
                break

        if not found:
            print("Item not on menu")
            continue

        again = input("Anything else? (y/n): ").lower()
        if again == "n":
            break

    make_total(order_list)


def make_total(order_list):
    total = 0
    print("\nYour Order:")
    for item in order_list:
        subtotal = item["qty"] * item["price"]
        total += subtotal
        print(f"{item['name']} x {item['qty']} = {subtotal}")

    print(f"\nTotal bill: {total}")


if __name__ == "__main__":
    main()
