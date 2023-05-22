'''Написати програму, що зчитує числа від користувача поки не буде введено ключове слово sum.
Коли воно введено, програма повідомляє сумму введених чисел та завершує виконання.
Якщо користувач вводить не число і не ключове слово sum, 
програма повідомляє про некоректне введення, але продовжує виконання і пам'ятає контекст.'''

count = []
while True:
	digit = input("Please enter a number or word 'sum'!\n> ")
	if digit.isdigit():
		count += digit
		print(f"Our number is - {digit}")
		print("Push the buttom one more time!")
	elif digit == "sum":
		print(f"The sum of all the digits you entered is - {sum(map(int, count))}")
		break
	else:
		print("Uncorrect enter, try again!")