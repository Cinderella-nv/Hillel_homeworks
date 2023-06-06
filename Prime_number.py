'''Написати функцію
Вхідні параметри:
    ціле число (до 100)
Повертає: флаг (bool) чи є число простим
'''

#Функция проверяет число простое оно или нет, возвращает булевое значение
#:param user_number принимает целое число
def get_prime_number(user_number: int) -> bool:
	prime_number = 2
	while prime_number < user_number:
		if not user_number % prime_number:
			return False
		prime_number += 1
	else:
		return True
	
#Функция создает сэт из простых чисел в диапазоне от 1 до 100 и возвращает это сэт
def get_set_prime_numbers() -> set:
	set_prime_numbers = set()
	for number in range (2, 101):
		if get_prime_number(number):
			set_prime_numbers.add(number)
	return set_prime_numbers

if __name__ == '__main__':
	entering_number = int(input('Enter a number\n>'))
	while True:
		if entering_number > 100:
			print('Enter a number more than 0 less than 100')
		else:
			print(get_set_prime_numbers())
			print(entering_number in get_set_prime_numbers())
			break

