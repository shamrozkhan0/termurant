from datetime import datetime

from restaurant import Restaurant, show_banner
from admin import Admin

class Project:
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def get_time(self):
        time = datetime.now().strftime("%H:%M")
        return time

    def greeting(self):
        greeting = "Good Morning"
        hour, min = self.get_time().split(':')
        hour = int(hour)
        if hour < 12:
            greeting = "Good Morning"
        elif hour < 18:
            greeting = "Good Afternoon"
        else:
            greeting = "Good Evening"

        return f"{greeting} ({self.get_time()})"

    def admin_controls(self):
        print("="*40, "Welcome To Admin Dashboard", "="*40)
        admin = Admin(self.restaurant)

        if not admin.authenticate_user():
            print("="*40,"Exiting Admin Dashboard...", "="*40)
            self.chooser()
        else:
            admin.admin_chooser()


    def restaurant_controls(self):
        rest = Restaurant()
        print("=" * 40, "Ordering System", "="*40)
        rest.show_menu()
        print()
        print("=" * 15, "CAUTION: WRITE YOUR ORDER IN THIS SEQUENCE i-e ( burger X 2 )", "=" * 15)
        rest.waiter()
        rest.order_confirm()
        print()
        print('=' * 50)
        print(f"Thanks for choosing us here is your total bill: ${rest.order_total()}")
        print('=' * 50)


    def chooser(self):
        commands = ["Order System", "Admin Controls"]

        print(self.greeting())
        print()
        print("Controls Options:")

        for i, command in enumerate(commands, start=1):
            print(f"{i} = {command}")

        while True:
            print()
            choice = input("Choose an Option: ").strip()

            if not choice.isdigit():
                print("Error: Enter the index number")
                continue

            match int(choice):
                case 1:
                    self.restaurant_controls()
                    return
                case 2:
                    self.admin_controls()
                    return
                case _:
                    print("Error: Enter the correct option :)")



def main():
    restaurant = Restaurant()
    main = Project(restaurant)
    show_banner()
    main.chooser()





if __name__ == '__main__':
    main()
