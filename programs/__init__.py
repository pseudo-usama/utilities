from utils import *
from emoji import start as start_emojies


PROGRAMS = (
    (('emoji', 'em'), start_emojies),
)


def start():
    while True:
        command = input('\nWhich program do you want to start : ')

        if command == 'exit' or command == 'e':
            break

        res = list(filter(lambda prog: command in prog[0], PROGRAMS))
        if len(res) == 0:
            print('Sorry! no such commands')
            continue

        clear_screen()
        res[0][1]() # Calling requested program
        clear_screen()


if __name__ == '__main__':
    start()
