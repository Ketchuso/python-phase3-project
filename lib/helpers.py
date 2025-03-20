# lib/helpers.py
from debug import Jay
from debug import Victoria
from debug import Kerissa
from debug import Madison
from debug import Johnathan

def age_checker():
    if Johnathan.age > 21:
        print("Can Drink")
    else:
        print("Sorry gotta go")
        exit()

def exit_program():
    print("Goodbye!")
    exit()
