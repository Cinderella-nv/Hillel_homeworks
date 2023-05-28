'''Написати програму, що зчитує числа від користувача поки не буде введено ключове слово sum.
Коли воно введено, програма повідомляє сумму введених чисел та завершує виконання.
Якщо користувач вводить не число і не ключове слово sum, 
програма повідомляє про некоректне введення, але продовжує виконання і пам'ятає контекст.'''

suma = 0
while True:
	num = input("Please enter a number or word 'sum'!\n> ")
	if num == "sum":
		print(f"The sum of all the digits you entered is {suma}")
		break
	elif num.isdigit() or (num[0] == "-" and num[1:].isdigit()): 
		suma += float(num)
		print(f"Our number is {num}")
		print("Push the buttom one more time!")
	elif num.find(".") >= 0 and num[0:num.find(".")].isdigit() and num[num.find(".") + 1:].isdigit():
		suma += float(num)
		print(f"Our number is {num}")
		print("Push the buttom one more time!")
	elif num.isdigit() or (num[0] == "-" and num.find(".") >= 0 and num[1:num.find(".")].isdigit() and num[num.find(".") + 1:].isdigit()):
		suma += float(num)
		print(f"Our number is {num}")
		print("Push the buttom one more time!")
	else:
		print("Incorrect value, please try again")

