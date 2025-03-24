# lib/helpers.py
from debug import Jay
from debug import Victoria
from debug import Kerissa
from debug import Madison
from debug import Johnathan

from colorama import Fore, Style, init
from models.Customer import Customer

init()

def customer_name():
    while True:
        name = input("Enter name (1-10 characters): ").strip()
        print(f"Raw input: {repr(name)}") 
        try:
            customer = Customer(name=name, age=25)
            return customer
        except (ValueError, TypeError) as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)
            print(Fore.CYAN + "Please enter a valid name." + Style.RESET_ALL)

def customer_age(customer):
    while True:
        age = input("Enter your age: ")
        try:
            customer.age = int(age)
            customer.save()
            return customer.age
        except(ValueError, TypeError) as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)
            print(Fore.CYAN + "Please enter a valid age." + Style.RESET_ALL)

def age_checker():
    if Jay.age > 21:
        print(Fore.GREEN + "\nWelcome in!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nSorry gotta go!" + Style.RESET_ALL)
        exit()


def exit_program():
    print(Fore.GREEN + "\n See ya later!" + Style.RESET_ALL)
    exit()
