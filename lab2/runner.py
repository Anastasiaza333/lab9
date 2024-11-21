from configs import app_settings
from lab2.calculator import Calculator
from lib import functions


def run():
    calculator = Calculator()
    while True:
        functions.show_menu()
        choice = input('Enter your choice: ').strip()

        match choice:
            case '1':
                calculator.run()
            case '2':
                app_settings.setting()
                
                
            case '0':
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


