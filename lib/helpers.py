# lib/helpers.py
from debug import Jay
from debug import Victoria
from debug import Kerissa
from debug import Madison
from debug import Johnathan

from colorama import Fore, Style, init

init()

def age_checker():
    if Jay.age > 21:
        print(Fore.GREEN + "\nWelcome in!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nSorry gotta go!" + Style.RESET_ALL)
        exit()


def exit_program():
    print(Fore.GREEN + "\n See ya later!" + Style.RESET_ALL)
    exit()
