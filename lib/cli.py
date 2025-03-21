# lib/cli.py

from helpers import (
    exit_program,
    age_checker
)

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
        print("Invalid choice, please try again")

#entering the bar
def enter_bar():
    print("\nPlease select an option:")
    print("1. Can I see your ID?")
    print("2. Leave")

    choice = get_valid_choice(["1", "2"])
    if choice == "1":
        age_checker()
    elif choice == "2":
        exit_program()
        

#main option select
def option_select():
    print("\nOptions")
    #change later to only show if tab is open
    print("1. Can I get a drink?")
    if (tab_open):
        print("2. Close Your Tab")
        print("\nhint: to leave, close your tab")
    else:
        print("2. Leave")

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
    print("\n Options:")
    print("1. Cosmo")
    print("2. Manhattan")
    print("3. Tequila Sunrise")
    print("4. Rum Runner")
    print("5. Bees Knees")
    print("6. Go Back")

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
    print(f"\n{drinks[choice]}, right up!")

    if tab_open:
        add_to_tab(drinks, choice)
    else:
        open_tab()
        

def open_tab():
    global tab_open
    print("Would you like to open a tab?")
    print("y. yes")
    print("n. no")

    choice = get_valid_choice(["y", "n"])
    if choice == "y":
        print("Opening tab!")
        tab_open = True
    elif choice == "n":
        print("Here's your total: total")
    
    print("Press enter to continue")
    user_input = input()
    option_select()

def add_to_tab(drinks, choice):
    print(f"Adding {drinks[choice]} to tab!")
    option_select()

#shows option to close tab, change later to show up if drinks are added to tab
def close_tab():
    global tab_open
    print("\nAre you sure?:")
    print("y. Yes")
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
    print("\nClosing Tab!")
    option_select()
    

def leave():
    print("Are you sure?")
    print("y. yes")
    print("n. no")

    choice = get_valid_choice(["y", "n"])
    if choice == "y":
        exit_program()
    elif choice == "n":
        option_select()

if __name__ == "__main__":
    main()
