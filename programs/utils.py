import sys
import os


def clear_screen():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        # TODO: Have to convert else to elif for Linux/MAC
        os.system('clear')


def get_input(
    msj='Enter an command',
    err_msj='Sorry! No such command exists',
    program_name='',
    commands=()
):
    while True:
        req_cmd = input(f'\n({program_name}) {msj} : ').lower()

        if req_cmd == 'exit' or req_cmd == 'e':
            clear_screen()
            return False

        res = list(filter(lambda prog: req_cmd in prog[0], commands))
        if len(res) == 0:
            print(err_msj)
            continue

        clear_screen()
        return res[0][1]
