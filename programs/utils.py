import sys
import os


def clear_screen():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        # TODO: Have to convert else to elif for Linux/MAC
        os.system('clear')
