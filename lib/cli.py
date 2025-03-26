# lib/cli.py
from colorama import Fore, Style, init
from helpers import (
    exit_program,
    age_checker,
    customer_name,
    customer_age
)
from models.Customer import Customer
from models.Drink_Orders import Drink_Orders
from models.Drinks import Drinks
import os
import subprocess

def run_seed():
    subprocess.run(["python", "lib/models/seed.py"])
run_seed()

init()

tab_open = False
birthday = False
birthday_toggle = False
drink_count = 0

if not os.path.exists("company.db"):
    import seed
def main():
    customer = None
    while True:
        enter_bar(customer)
        
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
        option_select(customer)
    elif choice == "2":
        exit_program(customer)

#main option select
def option_select(customer):
    global drink_count
    global birthday
    emotion_state()
    if drink_count <= 6:
        print(Style.BRIGHT + Fore.CYAN + "Options" + Style.RESET_ALL)
    else:
        print(Style.BRIGHT + Fore.CYAN + "\nCut Off" + Style.RESET_ALL)
    #change later to only show if tab is open
    if drink_count <= 6:
        print("1. Can I get a drink?")
    else:
        print("Nope, no more")

    print("2. View Open Tabs")

    if tab_open:
        if not birthday:
            print("3. It's my birthday!")
            print(Fore.RED + "4. Close Your Tab" + Style.RESET_ALL)
        else:
            print(Fore.RED + "3. Close Your Tab" + Style.RESET_ALL)
        print(Fore.CYAN + "\nhint: to leave, close your tab" + Style.RESET_ALL)
    else:
        if not birthday:
            print("3. It's my birthday!")
            print(Fore.RED + "4. Leave" + Style.RESET_ALL)
        else:
            print(Fore.RED + "3. Leave" + Style.RESET_ALL)
    
    if drink_count <= 6 and not birthday:
        choice = get_valid_choice(["1", "2", "3", "4"])
    elif not birthday:
        choice = get_valid_choice(["2", "3", "4"])

    if drink_count <= 6 and birthday:
        choice = get_valid_choice(["1", "2", "3"])
    elif birthday:
        choice = get_valid_choice(["2", "3"])

    if drink_count <= 6:
        if choice == "1":
            select_drink(customer)
        
    if choice == "2":
        view_tab(customer)
    elif choice == "3" and birthday:
        if (tab_open):
            close_tab(customer)
        else:
            leave(customer)

    elif choice == "3":
        update_birthday(customer)
    elif choice == "4" and not birthday:
        if (tab_open):
            close_tab(customer)
        else:
            leave(customer)

def update_birthday(customer):
    global birthday, birthday_toggle

    birthday = True
    birthday_toggle = True
    

    customer.age += 1
    customer.update()

    option_select(customer)


def rainbow_text(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    return "".join(colors[i % len(colors)] + char for i, char in enumerate(text)) + Style.RESET_ALL

def emotion_state():
    global birthday_toggle

    if birthday_toggle:
        print(Style.BRIGHT + "\n" + rainbow_text("HAPPY BIRTHDAY!!!"))
        print(Fore.GREEN + Style.BRIGHT + "(☞ﾟヮﾟ)☞\n" + Style.RESET_ALL)
        birthday_toggle = False
    else:
        states = {
            0: Fore.GREEN + Style.BRIGHT + "\n<" + "(￣︶￣)>\n" + Style.RESET_ALL,
            1: Fore.GREEN + Style.BRIGHT + "\n(๑>ᴗ<๑)\n" + Style.RESET_ALL,
            2: Fore.GREEN + Style.BRIGHT + "\n(ﾉ> ◇ <)ﾉ\n" + Style.RESET_ALL,
            3: Fore.GREEN + Style.BRIGHT + "\n┗(＾0＾)┓\n" + Style.RESET_ALL,
            4: Fore.GREEN + Style.BRIGHT + "\n─=≡Σ((( つ•̀ω•́)つ\n" + Style.RESET_ALL,
            5: Fore.RED + Style.BRIGHT + "\nヾ(￣□￣;)ﾉ\n" + Style.RESET_ALL,
            6: Fore.RED + Style.BRIGHT + "\n(╯°□°）╯︵ ┻━┻" + Style.RESET_ALL
        }
        print(states[drink_count])

def select_drink(customer):
    global drink_count

    print(Style.BRIGHT + Fore.CYAN + "\nOptions:" + Style.RESET_ALL)
    drinks_list = Drinks.get_all()
    print(Fore.GREEN + "Please select drink number:" + Style.RESET_ALL)

    ids = []  
    for i, drink in enumerate(drinks_list):
        print(f"{i + 1}. {drink.name}")  
        ids.append(str(i + 1))  

    print(f"{Fore.YELLOW}{len(drinks_list) + 1}. Specialty Drink {Style.RESET_ALL}")
    ids.append(str(len(drinks_list) + 1)) 

    print(f"{Fore.RED}{len(drinks_list) + 2}. Go Back {Style.RESET_ALL}")
    ids.append(str(len(drinks_list) + 2)) 

    
    choice = get_valid_choice(ids)
    choice = int(choice) 
    
    if choice == (len(drinks_list) + 2):
        option_select(customer)  
    elif choice == (len(drinks_list) + 1):
        create_specialty_drink(customer)
    else:
        drink_count += 1
        drink_index = (choice) - 1  
        selected_drink = drinks_list[drink_index]
        print(Fore.GREEN + f"\n{selected_drink}, right up!" + Style.RESET_ALL)
        Drink_Orders.create_order(customer.name, customer.id, selected_drink.name, choice)

        if tab_open:
            add_to_tab(drinks_list, drink_index, customer)  
        else:
            open_tab(customer)

def create_specialty_drink(customer):
    print(Fore.CYAN + "Enter the name for your specialty drink:" + Style.RESET_ALL)
    drink_name = input("> ").strip()

    if not drink_name:
        print(Fore.RED + "You must enter a drink name!" + Style.RESET_ALL)
        return

    # Create a new specialty drink and save it to the database
    try:
        new_drink = Drinks.create(drink_name)  
        print(Fore.GREEN + f"Your specialty drink '{new_drink.name}' has been created and added!" + Style.RESET_ALL)
    # Optionally, you could add this drink to the tab right away, or return it for later
        Drink_Orders.create_order(customer.name, customer.id, new_drink.name, new_drink._id)
        if tab_open:
            add_to_tab([new_drink], 0, customer)  
        else:
            open_tab(customer)
    
    except Exception as e:
        print(Fore.RED + f"Error creating the drink: {e}" + Style.RESET_ALL)

    option_select(customer)


def view_tab(customer):
    customer_list = customer.get_all()
    print(Fore.GREEN + "Please select tab number:" + Style.RESET_ALL)
    ids = []
    for i in customer_list:
        print(f"{i.id}. {i.name}", end=" | ")
        ids.append(str(i.id))
    print()

    choice = get_valid_choice(ids)
    select_tab(choice, customer)

def select_tab(choice, customer):
    customer = Customer.find_by_id(choice)
    if customer:
        customer_drinks = Drink_Orders.find_by_customer(customer.id)
        print(customer_drinks)
    else:
        print("Customer not found.")
    print(Fore.CYAN + "\nPress enter to continue" + Style.RESET_ALL)
    user_input = input()
    option_select(customer)


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
    Drink_Orders.insert_drink_order(customer.name, customer.id, choice)
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
