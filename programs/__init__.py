import os

from utils import *
from emoji import start as start_emojies
from calculator import start as start_calc


os.system("title My Utility Programs")
clear_screen()

PROGRAMS = (
    (('emoji', 'em'), start_emojies),
    (('calculator', 'calc'), start_calc),
)


def start():
    while True:
        cmd = get_input('Which program do you want to start', 'Sorry! No such program exists', 'base', PROGRAMS)
        if cmd is False:
            break
        cmd()



if __name__ == '__main__':
    start()
