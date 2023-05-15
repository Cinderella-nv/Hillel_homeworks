'''Написати програму, що проводить невеличкий діалог з користувачем:
Користувач вводить строку
Програма переводить строку в нижній регістр
Програма видаляє зі строки такі символи пунктуації: .,-:;?!
Програма видаляє зайві пробіли\табуляції з правого кінця строки
Програма питає користувача яке слово (або словосполучення) він бажає замінити
Програма повідомляє на якому індексі строки словосполучення присутнє
Програма питає на яке слово треба замінити
Програма виводить відформатовану строку'''

text = input('What do you think about it?\n')
text = text.lower()
print(text)

punctuations  = ('?', '.', ',', '!', ':', ';', '-')
for object in punctuations:
    text = text.replace(object, ' ')
while '  ' in text:
    text = text.replace('  ', ' ')
print(f'Keep your edited text\n{text}')

replacement = input('What word in the text do you want to change?\n')
text1 = text.index(replacement)
print(f'This is where your word is hidden - {text1}')

new_word = input('What do you think should be written?\n')
text = text.replace(replacement, new_word)
print(f'Keep your text\n{text}')


