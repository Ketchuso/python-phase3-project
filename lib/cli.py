# lib/cli.py
from colorama import Fore, Style, init
from helpers import (
    exit_program,
    age_checker,
    customer_name,
    customer_age
)
from models.Customer import Customer
import os

init()

tab_open = False

if not os.path.exists("company.db"):
    import seed

def main():
    customer = None
    while True:
        enter_bar(customer)
        option_select(customer)
        
#verifies valid choice
def get_valid_choice(valid_options):
    #keep asking until a valid choice is entered
    while True:
        choice = input("> ")
        if choice in valid_options:
            return choice
        print(Style.BRIGHT + Fore.RED + "Invalid choice, please try again" + Style.RESET_ALL)

#entering the bar
def enter_bar(customer):
    print(Style.BRIGHT + Fore.CYAN + "\nPlease select an option:" + Style.RESET_ALL)
    print("1. Can I see your ID?")
    print(Fore.RED + "2. Leave" + Style.RESET_ALL)

    choice = get_valid_choice(["1", "2"])
    if choice == "1":
        customer = customer_name()  # Re-assign the customer object returned by customer_name()
        customer_age(customer)
        age_checker(customer)
    elif choice == "2":
        exit_program(customer)

        

#main option select
def option_select(customer):
    print(Style.BRIGHT + Fore.CYAN + "\nOptions" + Style.RESET_ALL)
    #change later to only show if tab is open
    print("1. Can I get a drink?")
    if (tab_open):
        print(Fore.RED + "2. Close Your Tab" + Style.RESET_ALL)
        print(Fore.CYAN + "\nhint: to leave, close your tab" + Style.RESET_ALL)
    else:
        print(Fore.RED + "2. Leave" + Style.RESET_ALL)

    choice = get_valid_choice(["1", "2"])
    if choice == "1":
        select_drink(customer)
    elif choice == "2":
        if (tab_open):
            close_tab(customer)
        else:
            leave(customer)

#drink selection options
def select_drink(customer):
    print(Style.BRIGHT + Fore.CYAN + "\n Options:" + Style.RESET_ALL)
    print("1. Cosmo")
    print("2. Manhattan")
    print("3. Tequila Sunrise")
    print("4. Rum Runner")
    print("5. Bees Knees")
    print(Fore.RED + "6. Go Back" + Style.RESET_ALL)

    choice = get_valid_choice(["1", "2", "3", "4", "5", "6"])
    if choice == "6":
        option_select(customer)
    else:
        drinks = {
            "1": "Cosmo",
            "2": "Manhattan",
            "3": "Tequila Sunrise",
            "4": "Rum Runner",
            "5": "Bees Knees"
        }
    print(Fore.GREEN + f"\n{drinks[choice]}, right up!" + Style.RESET_ALL)

    if tab_open:
        add_to_tab(drinks, choice, customer)
    else:
        open_tab(customer)
        

def open_tab(customer):
    global tab_open
    print(Style.BRIGHT + Fore.CYAN + "\nWould you like to open a tab?" + Style.RESET_ALL)
    print("y. yes")
    print("n. no")

    choice = get_valid_choice(["y", "n"])
    if choice == "y":
        print(Fore.GREEN + "Opening tab!" + Style.RESET_ALL)
        tab_open = True
    elif choice == "n":
        print(Fore.GREEN + "Here's your total: total" + Style.RESET_ALL)
    
    print(Fore.CYAN + "\nPress enter to continue" + Style.RESET_ALL)
    user_input = input()
    option_select(customer)

def add_to_tab(drinks, choice, customer):
    print(Fore.GREEN + f"Adding {drinks[choice]} to tab!" + Style. RESET_ALL)
    option_select(customer)

#shows option to close tab, change later to show up if drinks are added to tab
def close_tab(customer):
    global tab_open
    print(Style.BRIGHT + Fore.CYAN + "\nAre you sure?:" + Style.RESET_ALL)
    print(Fore.RED + "y. yes" + Style.RESET_ALL)
    print("n. No")

    choice = get_valid_choice(["y", "n"])
    if choice == "y":
        tab_open = False
        leave_bar(customer)
    elif choice == "n":
        option_select(customer)

#leaving the bar
def leave_bar(customer):
    #show this if just closing tab
    print(Fore.GREEN + "\nClosing Tab!" + Style.RESET_ALL)
    option_select(customer)
    

def leave(customer):
    print(Style.BRIGHT + Fore.CYAN + "\nAre you sure?" + Style.RESET_ALL)
    print(Fore.RED + "y. yes" + Style.RESET_ALL)
    print("n. no")

    choice = get_valid_choice(["y", "n"])
    if choice == "y":
        exit_program(customer)
    elif choice == "n":
        option_select(customer)

if __name__ == "__main__":
    main()
