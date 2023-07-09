
def get_list_fibonacci(index: int) -> list:
    """
    Функция генерирует числа Фибаначчи и записывает их в список
    :param index: принимает индекс последнего элемента последовательности из чисел Фионаччи
    :return: возвращает список из последовательности чисел Фибоначчи
    """
    list_fibonacci = []
    if index == 0:
        list_fibonacci.append(index)
        return list_fibonacci
    elif index == 1:
        list_fibonacci.append(0)
        list_fibonacci.append(1)
        return list_fibonacci
    else:
        list_fibonacci.append(0)
        list_fibonacci.append(1)
        for num in range(2, index + 1):
            number = list_fibonacci[num - 1] + list_fibonacci[num - 2]
            list_fibonacci.append(number)
        return list_fibonacci


def get_word(line: str) -> list:
    """
    Функция принимает строку от пользователя и возвращает список слов
    :param line: принимаемая строка
    :return: список слов из строки
    """
    words_list = []
    punctuations = ('?', '.', ',', '!', ':', ';', '-')
    for j in punctuations:
        line = line.replace(j, ' ')
    while '  ' in line:
        line = line.replace('  ', ' ')
    words_list = line.split(' ')
    return words_list


if __name__ == '__main__':
    a = int(input('Enter a last index in list\n> '))
    my_list = get_list_fibonacci(a)
    for item in my_list:
        print(item)
    print('*' * 20)
    my_str = input('Say something\n> ')
    for word in get_word(my_str):
        print(word)
