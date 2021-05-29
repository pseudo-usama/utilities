from pyperclip import copy as to_clipboard


EMOJIES = (
    (('question', 'q'), '❓'),
)


def start():
    while True:
        command = input('Which emoji you want to copy : ')

        if command == 'exit':
            break

        res = list(filter(lambda emoji: command in emoji[0], EMOJIES))
        if len(res) == 0:
            print('Sorry! no such emoji exists\n')
            continue

        requested_emoji = res[0][1]
        to_clipboard(requested_emoji)
        print(f'{requested_emoji} is copied to clipboard\n')


if __name__ == '__main__':
    start()
