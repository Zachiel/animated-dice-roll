import os
from platform import system as system
from time import sleep as sleep
from random import randint


def clear(): return os.system('cls')


def rolling(dice, face):
    result = []
    for roll in range(dice):
        result.append(randint(1, face))
    return result


def clear_terminal():
    if system() == "Windows":
        clear()  # on Windows System
    else:
        os.system('clear')  # on Linux System


def rolldice(dice, face):
    timer = 0.001
    while timer < 1:
        all_dice = []
        for roll in range(dice):
            all_dice = rolling(dice, face)
        sleep(timer)
        timer *= 1.5
        clear_terminal()
        print(all_dice)


rolldice(10, 20)
