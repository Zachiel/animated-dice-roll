"""Interactive animated dice rolling app"""

from os import system
import sys
from platform import system as operating_system
from time import sleep
from random import randint


def user_input():
    """Option selection"""
    dictionary_input = {
        "dice": "How many dice to roll?  ",
        "sides": "Type in the maximum number:  ",
        "mode": """Please select a number of your desired mode
1) Normal
2) Exclude (Do not repeat numbers)\n""",
        "confirm": """Your mode is {0}, you're rolling {1}d{2} dice.
            Is this correct? (y/n/quit)\n"""
    }
    choice = [*"0000"]
    while choice[3] != "Y":
        try:
            choice[0] = int(input(dictionary_input["dice"]))
            choice[1] = int(input(dictionary_input["sides"]))
            choice[2] = int(input(dictionary_input["mode"]))
        except ValueError:
            print("Only numbers accepted\n\n")
            continue
        if choice[0] > 0 and choice[1] > 0:
            if choice[2] in [1, 2]:
                if choice[2] == 1:
                    choice[2] = "Normal"
                elif choice[2] == 2:
                    choice[2] = "Exclude"
                choice[3] = input(dictionary_input["confirm"].format(
                    choice[2], choice[0], choice[1])).upper()
                if choice[3] == "QUIT":
                    break
            else:
                print("Mode accepts only 1 or 2\n\n")
                continue
        else:
            print("Only positive numbers\n\n")
    print(choice)


def rolling(dice, face):
    """Populating list with random numbers"""
    result = []
    for _ in range(dice):
        result.append(randint(1, face))
    return result


def clear_terminal():
    """Terminal cleaning for proper animation display"""
    if operating_system() == "Windows":
        def clear():
            return system("cls")
        clear()  # on Windows System
    else:
        system("clear")  # on Linux System


def rolldice(dice, face):
    """Main function for rolling the dice"""
    timer = 0.001
    while timer < 1:
        all_dice = []
        for _ in range(dice):
            all_dice = rolling(dice, face)
        sleep(timer)
        timer *= 1.5
        clear_terminal()
        sys.stdout.write(str(all_dice))
        sys.stdout.flush()


# rolldice(10, 20)
user_input()
# print(*[1, 2, 3, 4])
