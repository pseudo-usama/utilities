from pyperclip import copy as to_clipboard


emojies = [
    (['question', 'q'], '❓')
]


while True:
    command = input('Which emoji you want to copy : ')

    res = list(filter(lambda emoji: command in emoji[0], emojies))
    if len(res) == 0:
        print('No such emoji exists')
        continue

    requested_emoji = res[0][1]
    to_clipboard(requested_emoji)
    print(f'{requested_emoji} is copied to clipboard')
