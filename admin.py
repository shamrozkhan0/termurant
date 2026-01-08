import csv

class Admin:
    def __init__(self,restaurant):
        self._password = "admin123"
        self.restaurant = restaurant


    def _check_password(self, password):
        if password != self._password:
            return False
        return True


    def authenticate_user(self):
        while True:
            password = input("(type exit to exist) Enter Password: ").strip()
            if password.lower() == "exit":
                    return False
            if self._check_password(password):
                    return True
            print()
            print("Error Incorrect Password")


    def get_csv_data(self):
        data = {}
        with open("menu.csv", "r", newline="") as file:
            for row in csv.DictReader(file):
                data[row["Name"]] = int(row["Price"])

        return data


    def add_food_in_menu(self):
        data = self.get_csv_data()

        while True:
            print()
            food_name = input("Type the food name: ").strip()

            key = next((k for k in data if k.lower() == food_name.lower()), None)

            if key:
                print(f"{food_name} in already in the menu")
                continue

            break

        while True:
            food_price = input("Enter food price: ").strip()

            if food_price.isdigit() or int(food_price) > 0:
                break

            print()
            print("Enter a valid price, and should be greater than 0 ")

        data[food_name.capitalize()] = food_price

        self.update_csv(data)



    def edit_menu(self):
        print()
        print("=" * 40, "Our Current Menu", "=" * 40)
        self.restaurant.show_menu()

        data = self.get_csv_data()

        while True:

            while True:
                print()
                name = input("Which food price would you like to edit: ").strip()

                key = next((k for k in data if k.lower() == name.lower()), None)

                if key:
                    break

                print()
                print("Error: Enter a valid food name")

            while True:
                print()
                price = input("Enter new price: ").strip()

                if price.isdigit() and int(price) > 0:
                    price = int(price)
                    break

                print()
                print("Error: Enter a valid price")

            data[key] = price

            print()
            re_edit = input("Do you want to edit again? (y/n): ").strip().lower()

            if re_edit == "n":
                self.update_csv(data)
                return
            elif re_edit == "y":
                continue
            else:
                print()
                print("Invalid response, returning to menu")
                self.update_csv(data)
                return


    def update_csv(self, data):
        header = ["Name", "Price"]
        data = [{"Name": key, "Price": int(value)} for key, value in data.items()]

        with open("menu.csv", 'w', newline='') as file:
            csv_writer = csv.DictWriter(file,fieldnames=header)

            csv_writer.writeheader()
            csv_writer.writerows(list(data))

        self.restaurant.show_menu()

        print()
        print("="*40,"Successfully Edited the price ", "="*40)



    def admin_chooser(self):
        commands = ['Editing The existing Menu', 'Add New Item In Menu']
        print("="*40, "Admin Controls", "="*40)
        print()
        print("Options:")

        for i, opt in enumerate(commands, start=1):
            print(f"{i} = {opt}")

        while True:
            print()
            option = input("Choose An Option To Continue: ").strip()
            if not option.isdigit():
                print
                print("Error: Enter a correct number")

            match int(option):
                case 1:
                    self.edit_menu()
                    return
                case 2:
                    self.add_food_in_menu()
                    return
                case _:
                    print()
                    print("Enter a correct option number")
