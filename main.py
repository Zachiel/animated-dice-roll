"""Interactive animated dice rolling app"""

from os import system
from platform import system as operating_system
from random import randint
from time import sleep


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
                continue
        except ValueError:
            print("Only numbers accepted\n\n")
            continue
    choice[1] += 1
    return choice[:3]


def dice_animation(face):
    """Printing animated dice roll"""
    return face


def replace_numbers_with_dice(face):
    """Used to replace numbers with dice printed sideways"""
    return face


def number_generator(dice, face, mode):
    """Populating list with random numbers"""
    result = []
    if mode == "Normal":
        for _ in range(dice):
            result.append(randint(1, face))
    elif mode == "Exclude":
        numbers = [*range(1, face)]
        while len(result) < dice:
            temp_result = randint(1, face)
            if temp_result in numbers:
                result.append(temp_result)
                numbers.remove(temp_result)
    return result


def clear_terminal():
    """Terminal cleaning for proper animation display"""
    if operating_system() == "Windows":
        def clear():
            return system("cls")
        clear()  # on Windows System
    else:
        system("clear")  # on Linux System


def roll_dice(dice, face, mode):
    """Rolling the dice"""
    timer = 0.001
    while timer < 1:
        all_dice = []
        for _ in range(dice):
            all_dice = number_generator(dice, face, mode)
        sleep(timer)
        timer *= 1.5
        clear_terminal()
        print(str(all_dice))


def run():
    """Main function wrapping everything"""
    choice = user_input()
    roll_dice(*choice)


run()
