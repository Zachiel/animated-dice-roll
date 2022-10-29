"""Interactive animated dice rolling app"""

from os import system
from platform import system as operating_system
from random import randint, randrange
from textwrap import dedent
from time import sleep
from typing import Union


dictionary_input: dict[str, str] = {
    "dice":
        "How many dice to roll?\n",
    "sides":
        "Type in the maximum number:\n",
    "confirm": """
            Your mode is {2}, you're rolling {0}d{1} dice.\n
                Is this correct? (y/n/quit)\n""",
    "includes_confirm": """
            Your mode is {2}, you're rolling {0} dice from numbers:
            {1}\n
                Is this correct? (y/n/quit)\n""",
        "mode": """
        Please select a number of your desired mode:
            1) Normal
            2) Increments of 10 (0 included)
            3) Selective (Only numbers specified by user)
            4) Exclude (Do not repeat numbers)
            5) Exit the app\n""",
    "first": """
                Type \"review\" to view numbers,
                Type \"remove\" to delete numbers,
                Type \"done\" to finish.""",
    "next":
        "Type in your number:\n"}

mode_input: dict[int, str] = {
    1: "Normal",
    2: "Increments",
    3: "Selective",
    4: "Exclude"
}


def user_input() -> Union[list[int], list[list[int]]]:
    """Option selection"""
    choice: list[int] = []
    confirmation: str = ""
    while confirmation.upper() != "Y":
        # ask for mode
        mode: str = input(dedent(dictionary_input["mode"]))
        try:
            mode_numeric: int = int(mode)
        except ValueError:
            print("Only numbers accepted\n\n")
            continue
        if mode_numeric == 5:
            break
        sides: list[int] = user_sides(mode_numeric)
        dice: int = user_dice(sides, mode_numeric)
        # confirmation from user
        if mode_numeric != 3:
            confirmation = input(
                dedent(dictionary_input["confirm"]).format(
                    dice, *sides, mode_input[mode_numeric]))
        else:
            confirmation = input(
                dedent(dictionary_input["includes_confirm"])
                .format(dice, sides,
                        mode_input[mode_numeric]))
        if confirmation.upper() != "QUIT":
            # choice[0], choice[1], choice[2] = dice, sides, mode_numeric
            choice.append(dice)
            choice.append(mode_numeric)
            choice.extend(sides)
        else:
            break
    return choice


def user_dice(sides: list[int], mode: int) -> int:
    """Get dice from user input"""
    if len(sides) > 1:
        return len(sides)
    if mode == 4:
        return sides[0]
    dice: int = 0
    while dice < 1:
        try:
            dice = int(input(dictionary_input["dice"]))
            if dice < 1:
                raise ValueError
        except ValueError:
            print("Only positive numbers\n\n")
            continue
    return dice


def user_sides(mode: int) -> list[int]:
    """Get dice sides from user input"""
    sides: list[int] = []
    while len(sides) < 1 or sides[0] == 0:
        # check for increment of 10 while in increments mode
        if mode == 3:
            # selective numbers options
            sides = number_inclusion(sides)
            if len(sides) < 1:
                continue
        elif mode == 2:
            while sides[0] % 10 != 0 or sides[0] == 0:
                sides = [int(input(dictionary_input["sides"]))]
                if sides[0] % 10 != 0 or sides[0] == 0:
                    print(f"{sides[0]} is not an increment of 10")
                    continue
        else:
            try:
                sides = [int(input(dictionary_input["sides"]))]
                if sides[0] < 1:
                    raise ValueError
            except ValueError:
                print("Only positive numbers\n\n")
                continue
    return sides


def number_inclusion(numbers: list[int]) -> list[int]:
    """Function used with mode Selective, stores user numbers"""
    temp_input: Union[int, str] = ""
    print(dedent(dictionary_input["first"]))
    while str(temp_input).upper() != "DONE":
        temp_input = input(dedent(dictionary_input["next"]))
        # input validation
        if temp_input.upper() not in ["DONE", "REVIEW", "REMOVE"]:
            try:
                if int(temp_input) < 0:
                    print("Only positive integers accepted")
                    raise ValueError
                if int(temp_input) in numbers:
                    print("Number is already on the list")
                    raise ValueError
                numbers.append(int(temp_input))
                print(f"added number {temp_input} to selection")
                continue
            except ValueError:
                print("Unsuported option")
                continue
        if str(temp_input).upper() == "REVIEW":
            print(f"Saved numbers are:\n{numbers}")
            continue
        if str(temp_input).upper() == "REMOVE":
            print(f"Saved numbers are:\n{numbers}")
            try:
                temp_remove: int = int(
                    input("Which number would you like to remove?\n"))
                numbers.remove(temp_remove)
                print("Number removed")
            except ValueError:
                print("Select a number from your list.\n\n")
    print(f"Saved numbers are:\n{numbers}")
    return numbers


# def destruct(choice: tuple[list[int], list[int]]) -> list[int]:
#     """Destructuring tuple and returning list"""
#     destructured_choice: list[int] = []
#     if len(choice[1]) < 1:
#         destructured_choice = choice[0]
#     else:
#         destructured_choice = choice[0] + choice[1]
#     return destructured_choice


def number_generator(dice: int, face: list[int], mode: int) -> list[int]:
    """Populating list with random numbers"""
    result: list[int] = []
    if mode == 1:
        for _ in range(dice):
            result.append(randint(1, face[0]))
    elif mode == 2:
        for _ in range(dice):
            result.append(randrange(0, face[0]+1, 10))
    elif mode == 3:
        pass
    elif mode == 4:
        dice = len(face)
        numbers = [*range(1, face[0]+1)]
        while len(result) < dice:
            temp_result = randint(1, face[0])
            if temp_result in numbers:
                result.append(temp_result)
                numbers.remove(temp_result)
    return result


def roll_dice(dice: int, face: list[int], mode: int) -> list[int]:
    """Rolling the dice"""
    if mode == 3:
        return []
    timer = 0.01
    all_dice = []
    while timer < 1:
        for _ in range(dice):
            all_dice = number_generator(dice, face, mode)
            print(all_dice)
        sleep(timer)
        timer *= 1.25
        clear_terminal()
    return all_dice


def dice_animation(face: int) -> str:
    """Printing animated dice roll"""
    return str(face)


def replace_numbers_with_dice(face: int) -> str:
    """Used to replace numbers with dice printed sideways"""
    return str(face)


def clear_terminal() -> None:
    """Terminal cleaning for proper animation display"""
    if operating_system() == "Windows":
        def clear():
            return system("cls")
        clear()  # on Windows systems
    else:
        system("clear")  # on Unix systems


def run() -> None:
    """Main function wrapping everything"""
    choice = user_input()
    print(choice)
    # print(destruct(my_tuple))
    # if my_tuple[0][2] == 0:
    #     return
    # result: list[int] = roll_dice(*my_tuple[0])
    # if len(result) < 1:
    #     return
    # print(result)


run()
