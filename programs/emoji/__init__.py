from pyperclip import copy as to_clipboard

from utils import *


EMOJIES = (
    (('question', 'q'), '❓'),
)


def start():
    while True:
        emoji = get_input('Which emoji you want to copy', 'Sorry! no such emoji exists', 'emoji', EMOJIES)
        if emoji is False:
            break
        copy_emoji(emoji)


def copy_emoji(emoji):
    to_clipboard(emoji)
    print(f'{emoji} is copied to clipboard\n')


if __name__ == '__main__':
    start()
