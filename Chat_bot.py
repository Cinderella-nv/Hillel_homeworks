'''Напишіть програму, яка буде симулювати примітивне бото-спілкування.
Програма має зчитувати строку-звернення від користувача, 
після чого - шукати ключові слова в цьому зверненні та відповідати заготовленими фразами.
Реалізуйте наступні пари ключові слова => заготовлена фраза:

    Привіт / Хай / Доброго дня => Доброго вечора, я бот з України!
    Як справи? / Що робиш? / Чим займаєшся? => Вчусь програмувати на Python!
    Фільм / Кінотеатр / Серіал => Соррі що втручуюсь, не знаю про що йдеться мова, 
    але подивіться серіал/фільм ваша відповідь, він просто бомба!
    Бувай / Надобраніч / Гудбай / До зустрічі => Побачимось у мережі, I'll be back.
    Завершити виконання програми
    Ключових слів не знайдено => Дуже цікаво, але, нажаль, нічого не зрозуміло :(
    Якщо хочете, можете додати свої пари теж, або замінити існуючі, 
    але має бути не менше 3 пар та одна з них - вихід з діалогу. 
    Рекомендую поки не занурюватись занадто глибоко - 
    через декілька занять ми зможемо зробити цього бота на більш цікавому рівні, 
    тому не марнуйте час зараз.'''



print("Let's start!")

while True:
	greet = input("Greetings\n> ").title()
	if greet == "Hi" or greet == "Hola" or greet == "Hello":
		print("Good evening, I'm a bot from Ukraine")
		break
	else:	
		print("Something went wrong")
	

while True:
	name = input("Write a name\n> ")
	if name.isalpha() and len(name) > 2:
		print(f"Glad to see you here, {name.title()}! What's new?")
		print("How can I help you?")
		break
	else:
		print("Did you forget your name?")

while True:
    interests = input("What are your interests?\n> ").title()
    if interests == "Series":
        print(f"I advise you {name.title()} to watch the cool {interests} - Mr.Robot")
        break
    elif interests == "Movie":
        print(f"I advise you {name.title()} to watch the cool {interests} - Tenet")
        break
    elif interests == "Documentary":
        print(f"I advise you {name.title()} to watch  the cool {interests} - Alien Worlds")
        break
    else:
        print(f"Sorry, I do not understand {name.title()} what it is about")
	
while True:
	waygoing = input("Say me Goodbay\n> ").title()
	if waygoing == "Bye" or waygoing == "Goodbye" or waygoing == "Bye-Bye":
		print(f"See you online {name.title()}")
		break
	else:	
		print("Very interesting, but, unfortunately, nothing is clear :(")
print("Don't worry! Be happy!")

