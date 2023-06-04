'''Програма перевіряє чи існує трикутник по введеним сторонам 
та відображає його периметр та площу якщо він існує. 
Потрібно реалізувати чотири функції:
    Зчитування сторони трикутника (саме додатнього числа, 
		а не того що може ввести користувач) та повернення цього значення
    Перевірка можливості існування трикутника та поверненням True/False
    Підрахунок периметру трикутника
    Підрахунок площі трикутника
Усі функції мають приймати параметри, не використовувати нічого з 
зовнішньої області видимості та користуватись return, 
Головна частина відповідає за діалог з користувачем та основну логіку 
(виклик усіх функцій у вірному порядку та вивід відповіді)'''

# Функция считывает сторону треугольника и возвращает значение
def get_sides_of_triangle(side_number: int) -> float:
    try:
        side_of_triangle = float(input(f"Enter lenght {side_number} side of the triangle - "))
        if side_of_triangle <= 0:
            print('Enter a positive number')
            return get_sides_of_triangle()
        else:
            return side_of_triangle
    except ValueError:
        print("Enter a number, dude!")
        return get_sides_of_triangle()

# Функция проверает возможность существования треугольника и возвращает bool
def is_triangle(triangle: list) -> bool:
    first = triangle[0] + triangle[1] > triangle[2]
    second = triangle[1] + triangle[2] > triangle[0]
    third = triangle[0] + triangle[2] > triangle[1]
    if first and second and third:
        return True
    else:
        return False

# Функция считает периметр треугольника и возвращае значение
def get_perimeter_of_triangle(triangle: list) -> float:
    perimeter_of_triangle = triangle[0] + triangle[1] + triangle[2]
    return perimeter_of_triangle

# Функция считает площадь треугольника и возвращает значение
def get_area_of_triangle(triangle: list) ->float:
    half_p = get_perimeter_of_triangle(triangle) / 2
    area_of_triangle = ((half_p * (half_p- triangle[0]) * (half_p - triangle[1]) * (half_p - triangle[2])) ** 0.5)
    return area_of_triangle


if __name__ == '__main__':
    sides = []
    for number in range(1, 4):
        side = get_sides_of_triangle(number)
        sides.append(side)
    if is_triangle(sides):
        print(f'Perimeter of our triangle - {get_perimeter_of_triangle(sides)}')
        print(f'Area of our triangle - {get_area_of_triangle(sides): .2f}')

