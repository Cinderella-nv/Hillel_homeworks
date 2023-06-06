'''Написати функцію.
ВхідніПараметри:
    ціле число
Повертає: словник з ключами days, hours, minutes, seconds та їх відповідними значеннями'''

#Функция конвертирует время и возвращает словарь с ключами: значениями - дни, часы, минуты, секунды
#:param number - целочисленное число, коротое ввел пользователь
def get_timing(number: int) -> dict:
	convert = {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}
	day = get_days(number)
	hour = get_hours(day[1])
	minute = get_minutes(hour[1])
	second = minute[1]
	convert.update({"days": day[0], "hours": hour[0], "minutes": minute[0], "seconds": second})
	return convert

#Функция возвращает кортеж из: колличество дней и остаток в секундах
def get_days(number: int) -> tuple:
	return divmod(number, (60 * 60 * 24))

##Функция возвращает кортеж из: колличество часов и остаток в секундах
def get_hours(number: int) -> tuple:
	return divmod(number, (60 * 60))

##Функция возвращает кортеж из: колличество минут и остаток в секундах
def get_minutes(number: int) -> tuple:
	return divmod(number, 60)


if __name__ == '__main__':
	while True:
		try:
			time = int(input('Enter a number\n> '))
			print(get_timing(time))
			break
		except ValueError:
			print('Uncorrect value')

