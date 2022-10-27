"""Interactive animated dice rolling app"""

from os import system
from platform import system as operating_system
from random import randint
from time import sleep
# from typing import


def user_input():
    """Option selection"""
    dictionary_input: dict[str, str] = {
        "dice": "How many dice to roll?  ",
        "sides": "Type in the maximum number:  ",
        "confirm": """Your mode is {0}, you're rolling {1}d{2} dice.
            Is this correct? (y/n/quit)\n""",
        "mode": """Please select a number of your desired mode
1) Normal
2) Increments of 10
3) Selective (Only numbers specified by user)
4) Exclude (Do not repeat numbers)\n"""}

    mode_input: dict[int, str] = {
        1: "Normal",
        2: "Increments",
        3: "Selective",
        4: "Exclude"
    }

    choice: list[int] = [0, 0, 0]
    confirmation: str = ""
    print(choice)
    while confirmation != "Y":
        try:
            choice[2] = int(input(dictionary_input["mode"]))
            choice[0] = int(input(dictionary_input["dice"]))
            choice[1] = int(input(dictionary_input["sides"]))
            print(type(choice[0]))
            print(type(choice[1]))
            if choice[0] > 0 and choice[1] > 0:
                if choice[2] in mode_input:
                    confirmation = input(dictionary_input["confirm"].format(
                        mode_input[choice[2]],
                        choice[0], choice[1])).upper()
                    if confirmation == "QUIT":
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
    return choice[:3]


def dice_animation(face: int) -> str:
    """Printing animated dice roll"""
    return str(face)


def replace_numbers_with_dice(face: int) -> str:
    """Used to replace numbers with dice printed sideways"""
    return str(face)


def number_generator(dice: int, face: int, mode: int) -> list[int]:
    """Populating list with random numbers"""
    result: list[int] = []
    if mode == 1:
        for _ in range(dice):
            result.append(randint(1, face))
    if mode == 2:
        for _ in range(dice):
            result.append(randint(1, face))
    elif mode == 4:
        numbers = [*range(1, face+1)]
        while len(result) < dice:
            temp_result = randint(1, face)
            if temp_result in numbers:
                result.append(temp_result)
                numbers.remove(temp_result)
    return result


def clear_terminal() -> None:
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
# my_list = [1, 2, 3, 4]
# print(my_list[1])
# print(type(my_list[1]))
x: list[int] = [1, 2, 3]
if x[0] < x[2]:
    print(x)
