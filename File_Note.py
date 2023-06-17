"""
Написати програму, для ведення та перегляду нотаток.
Програма пропонує користувачу вводити ключові слова, та опрацьовує їх.
Перелік ключових слів:
    add - додати нотатку. Користувач вводить текст нотатки, який зберігається у програмі та є дійсним до її завершення
    earliest - виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
    latest - виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої
    longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
    shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшоїдо найдовшої
"""


COMMANDS = ['add', 'earliest', 'latest', 'longest', 'shortest', 'exit']


def get_commands():
    """
    Функция выводит на экран список доступных пользователю команд
    """
    for item in COMMANDS:
        print(item)
    print("Make your choice")


def get_add_note(notes1: list) -> list:
    """
    Функция принимает список, добавляет заметку, введенную пользователем в принятый список
    : param1 : список заметок
    : return : список заметок
    """
    word = input("What's new? - ").lower()
    notes1.append(word)
    return notes1


def get_earl_note(notes1: list) -> list:
    """
    Функция принимает список, и сортитует заметки от первой введенной пользоватлем
    : param1 : список заметок
    : return : список заметок от первой введенной пользователем до той, которую он указал
    """
    if len(notes1) >= 1:
        count = int(input(f'In your list are {len(notes1)} elements.\nHow much earliest notes do you want to see?\n> '))
        notes1 = notes1[:count]
        return notes1
    return notes1


def get_late_note(notes1: list) -> list:
    """
    Функция принимает список, и сортирует в обратном порядке
    : param1: список заметок
    : return: список заметок от последней введенной пользователем до той, которую он указал
    """
    if len(notes1) >= 1:
        count = int(input(f'In your list are {len(notes1)} elements.\nHow much latest notes do you want to see?\n> '))
        notes1 = notes1[::-1]
        notes1 = notes1[:count]
        return notes1
    return notes1


def get_longest_note(notes1: list) -> list:
    """
    Функция принимает список, и сортитует заметки по длине
    : param1 : список заметок
    : return : список заметок от длинной до короткой, в количестве, которое указал пользователь
    """
    notes1 = sorted(notes1, reverse=True, key=lambda item: len(item))
    count = int(input(f'In your list are {len(notes1)} elements.\nHow much notes do you want to see?\n> '))
    notes1 = notes1[:count]
    return notes1


def get_short_note(notes1: list) -> list:
    """
    Функция принимает список, и сортитует заметки по длине
    : param1 : список заметок
    : return : список заметок от короткой до длинной, в количестве, которое указал пользователь
    """
    notes1 = sorted(notes1, reverse=False, key=lambda item: len(item))
    count = int(input(f'In your list are {len(notes1)} elements.\nHow much notes do you want to see?\n> '))
    notes1 = notes1[:count]
    return notes1


if __name__ == '__main__':
    get_commands()
    notes = []
    while True:
        note = input('Choose any command from list\n> ')
        if note == 'add':
            print(' '.join(get_add_note(notes)))
        elif note == 'earliest':
            print('\n'.join(get_earl_note(notes)))
        elif note == 'latest':
            print('\n'.join(get_late_note(notes)))
        elif note == 'longest':
            print('\n'.join(get_longest_note(notes)))
        elif note == 'shortest':
            print('\n'.join(get_short_note(notes)))
        elif note == 'exit':
            print("Have a nice day!")
            quit()
        else:
            print("Let's do it again?")
