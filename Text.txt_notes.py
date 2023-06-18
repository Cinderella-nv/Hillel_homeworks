import os

COMMANDS = ['add', 'earliest', 'latest', 'longest', 'shortest', 'delete', 'exit']


def get_commands():
    """
    Функция выводит на экран список доступных пользователю команд
    : return : строка - обращение к пользователю
    """
    for item in COMMANDS:
        print(item)
    return "Make your choice"



def get_add_note(notes1: list) -> list:
    """
    Функция принимает список, добавляет заметку, введенную пользователем в принятый список
    : param1 : список заметок
    : return : список заметок
    """
    word = input("What's new? - ")
    notes1.append('- ' + word + '\n')
    return notes1

def get_saved_note(notes1: list, file):
    """
    Функция принимает список и сохраняет его в файл
    : param1 : список заметок
    : param2 : файл, в который сохраняются заметки
    : return : строка результата выполнения функции
    """
    for quote in notes1:
        file.write(quote)
    return 'File was already saved'


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

def get_del_note(notes1):
    """
    Функция принимает список, выводит в консоль индекс и заметку под этим индексом, удаляет выбранную пользователем
    заметку
    : param1 : список заметок
    : retutn : редактированный список
    """
    for index, item in enumerate(notes1):
        print(index, item)
    count = int(input(f'In your list are {len(notes1)} elements.\nWhat note do you want to delete?\n> '))
    notes1.pop(count)
    return notes1


if __name__ == '__main__':
    print(get_commands())
    notes = []
    text_file = input('Enter a file_name for reading\n> ')
    if os.path.isfile(text_file):
        with open(text_file, mode='r', encoding='utf-8') as quotes_file:
            notes = quotes_file.readlines()
    else:
        quotes_file = open(text_file, mode='a', encoding='utf-8')

    while True:
        note = input('Choose any command from list\n> ')
        if note == 'add':
            print(''.join(get_add_note(notes)))
        elif note == 'earliest':
            print('\n'.join(get_earl_note(notes)))
        elif note == 'latest':
            print('\n'.join(get_late_note(notes)))
        elif note == 'longest':
            print('\n'.join(get_longest_note(notes)))
        elif note == 'shortest':
            print('\n'.join(get_short_note(notes)))
        elif note == 'delete':
            print('\n'.join(get_del_note(notes)))
        elif note == 'exit':
            text_file = input('Enter a file_name for saving changes\n> ')
            with open(text_file, mode='w', encoding='utf-8') as quotes_file:
                print(get_saved_note(notes, quotes_file))
            print("Have a nice day!")
            quit()
        else:
            print("Let's do it again?")
