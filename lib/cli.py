# lib/cli.py

from helpers import (
    exit_program,
    age_checker
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            age_checker()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Can Drink?")


if __name__ == "__main__":
    main()
