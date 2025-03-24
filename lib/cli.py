# lib/cli.py
from colorama import Fore, Style, init
from helpers import (
    exit_program,
    age_checker,
    customer_name,
    customer_age
)
from models.Customer import Customer

init()

tab_open = False

def main():
    while True:
        enter_bar()
        option_select()
        
#verifies valid choice
def get_valid_choice(valid_options):
    #keep asking until a valid choice is entered
    while True:
        choice = input("> ")
        if choice in valid_options:
            return choice
        print(Style.BRIGHT + Fore.RED + "Invalid choice, please try again" + Style.RESET_ALL)

#entering the bar
def enter_bar():
    print(Style.BRIGHT + Fore.CYAN + "\nPlease select an option:" + Style.RESET_ALL)
    print("1. Can I see your ID?")
    print(Fore.RED + "2. Leave" + Style.RESET_ALL)

    choice = get_valid_choice(["1", "2"])
    if choice == "1":
        customer = customer_name()
        customer_age(customer)

    elif choice == "2":
        exit_program()
        

#main option select
def option_select():
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
        select_drink()
    elif choice == "2":
        if (tab_open):
            close_tab()
        else:
            leave()

#drink selection options
def select_drink():
    print(Style.BRIGHT + Fore.CYAN + "\n Options:" + Style.RESET_ALL)
    print("1. Cosmo")
    print("2. Manhattan")
    print("3. Tequila Sunrise")
    print("4. Rum Runner")
    print("5. Bees Knees")
    print(Fore.RED + "6. Go Back" + Style.RESET_ALL)

    choice = get_valid_choice(["1", "2", "3", "4", "5", "6"])
    if choice == "6":
        option_select()
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
        add_to_tab(drinks, choice)
    else:
        open_tab()
        

def open_tab():
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
    option_select()

def add_to_tab(drinks, choice):
    print(Fore.GREEN + f"Adding {drinks[choice]} to tab!" + Style. RESET_ALL)
    option_select()

#shows option to close tab, change later to show up if drinks are added to tab
def close_tab():
    global tab_open
    print(Style.BRIGHT + Fore.CYAN + "\nAre you sure?:" + Style.RESET_ALL)
    print(Fore.RED + "y. yes" + Style.RESET_ALL)
    print("n. No")

    choice = get_valid_choice(["y", "n"])
    if choice == "y":
        tab_open = False
        leave_bar()
    elif choice == "n":
        option_select()

#leaving the bar
def leave_bar():
    #show this if just closing tab
    print(Fore.GREEN + "\nClosing Tab!" + Style.RESET_ALL)
    option_select()
    

def leave():
    print(Style.BRIGHT + Fore.CYAN + "\nAre you sure?" + Style.RESET_ALL)
    print(Fore.RED + "y. yes" + Style.RESET_ALL)
    print("n. no")

    choice = get_valid_choice(["y", "n"])
    if choice == "y":
        exit_program()
    elif choice == "n":
        option_select()

if __name__ == "__main__":
    main()
