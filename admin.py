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
            print("Error Incorrect Password")


    def edit_menu(self):
        print("="*40,"Our Current Menu", "="*40)
        self.restaurant.show_menu()

        with open("menu.csv", 'r') as file:






    def admin_chooser(self):
        commands = ['Editing The existing Menu']
        print("="*40, "Admin Controls", "="*40)
        print()
        print("Options:")

        for i, opt in enumerate(commands, start=1):
            print(f"{i} = {opt}")

        while True:
            print()
            option = input("Choose An Option To Continue: ").strip()
            if not option.isdigit():
                print("Error: Enter a correct number")

            match int(option):
                case 1:
                    self.edit_menu()
                    return
                case _:
                    print("Enter a correct option number")






