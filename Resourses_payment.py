'''В функцію def потрібно передати вхідні дані, сама функція містить в собі логіку 
вирішення завдання. Функція має повернути (return) відповідь у головну частину.
Головна частина відповідає за діалог з користувачем, отримання вхідних даних 
(дозволяється та заохочується використання додаткових функцій), 
викликання функції вирішення задачі та обробка отриманої відповіді 
(виведення її на екран).'''

'''Написати програму, що рахує абонплату за комунальним лічильника 
(наприклад, електроенергії або газу).
Вхідні дані:
попередні показання
теперішні показання
тариф.
На виході:
скільки потрібно сплатити, округлено до двох цифр після коми'''

'''Функция возвращает текущие показания за месяц'''
def get_user_resourse_count() -> float:
        previous_indicator = float(input('previous_indicator:\t'))
        current_indicator = float(input('current_indicator:\t'))
        difference = current_indicator - previous_indicator
        if previous_indicator < current_indicator:
            return difference
        else:
            print("Wrong previous or current indicator")
            return get_user_resourse_count()

'''Функция возвращает сумму платежа за использованный ресурс по текущему тарифу
    :param tariff - отвечает за тариф на потребляемый ресурс
    :param difference - отвечает за разницу между вводимыми данными показателей'''
def get_tariff_resourse(tariff: float, difference: float):
        your_count = tariff * difference
        return your_count


if __name__== '__main__':
    your_count = 0
    while True:
        indication = input("Please enter - Water or Gaz or Light or Summa>\n").lower()
        if indication == "water" or indication == "gaz" or indication == "light":
            dif = get_user_resourse_count()
            count = get_tariff_resourse((float(input("Enter today's tariff:\t"))), dif)
            your_count += count
            print(your_count)
        elif indication == "summa":
            print(f'{your_count : .2f}')
            break
        else:
             print("It is not in our service\nTry again")
