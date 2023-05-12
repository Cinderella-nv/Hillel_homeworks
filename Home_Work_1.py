'''1. Hаписати програму, яка конвертує градуси у радіани
(або навпаки, за бажанням, але вкажіть що саме обрали!). 180 градусів - це Pi радіан.
Взідні дані:
градуси (або радіани).
На виході:
конвертована величина (градуси або радіани) округлена до 5 цифр після коми'''

PI = 3.14
DEGREE = 180

degree = float(input("Degrees are "))
radian = f'{degree * (PI/DEGREE) : .2f}'
print(radian)

radians = float(input("Radians are "))
degrees = f'{radians * (DEGREE/PI) : .2f}'
print(degrees)

'''2. Написати програму, що рахує абонплату за комунальним лічильника 
(наприклад, електроенергії або газу).
Вхідні дані:
попередні показання
теперішні показання
тариф.
На виході:
скільки потрібно сплатити, округлено до двох цифр після коми'''

rate = float(input("What is the gas price? "))
current_gas_counter = float(input("Сurrent meter readings are - "))
previous_gas_counter = float(input("Previous meter readings are - "))
total_amount = f'{rate * (current_gas_counter - previous_gas_counter) : .2f}'
print(total_amount)

'''3. Написати програму, що рахує податок від надхождення на рахунок підприємця.
Вхідні дані:
розмір надходження
відсоток податка
На виході:
скільки потрібно сплатити податку
скільки залишиться чистого прибутку
(обидва значення округлені до двох цифр після коми)'''

tax = float(input("What is your income tax? "))
profit = float(input("How much income? "))
income_tax = profit / (100 * tax)
clear_income = profit - income_tax
print(f'{clear_income : .2f}')

'''4. Написати програму що рахує витрати на паливо.
Вхідні дані:
витрачання палива автомобілем за 100км
сьогоднішня ціна 1 л палива
скільки кілометрів треба здолати
На виході:
скільки грошей на це піде, округлено до двох цифр після коми'''

gasolin_price = float(input("What is the price of petrol now? "))
fuel_consumption = float(input("What is the fuel consumption of your car per 100 km? "))
distance = float(input("How many km do you need to drive? "))

your_expenses = (fuel_consumption / 100) * distance * gasolin_price
print(f'{your_expenses : .2f}')
