'''Написати програму що перевіряє чи є введена строка дзеркальною (паліндромом). 
Наприклад, слово "довод", фраза "Аби ріці риба" або числа 84348 та 45677654 - дзеркальні. 
Вхідну строку треба перевести в один регістр, позбавити пробілів, табуляцій, 
переносів на нову строку та розділових знаків.
Вхідні дані:
строка
На виході
Відповідь чи є строка паліндромом'''

while True:
    message = input('Enter something interesting\n> ').lower()
    punctuations  = (' ', '?', '.', ',', '!', ':', ';', '-', '    ', '\n')
    for char in punctuations:
        message = message.replace(char, '')
    if message == message[::-1]:
        print(f"Your message '{message}' is pallindrome")
        break
    else:
        print("Ups!")

