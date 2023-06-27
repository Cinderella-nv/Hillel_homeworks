from random import choices, randint, random


class Cat:
    """
    Класс Cat, реализует животное Кот
    """
    def __init__(self, name: str, age: int, breed: str):
        """
        : param name : принимает имя создаваемого обьекта Cat
        : param age : принимает возраст создаваемого обьекта Cat
        : param breed : принимает породу создаваемого обьекта Cat
        self.hours_outdoor - свойство кота, сколько он уже погулял сегодня
        self.hungry - свойство кота, голоден ли он
        self.cat_voice - свойство кота - сколько раз он промяукал (уровень голода)
        self.food - список еды, которую кот употребляет
        """
        self.name = name
        self.age = age
        self.breed = breed
        self.hungry = False
        self.hours_outdoors = 0
        self.cat_voice = 0
        self.food = ['fish', 'beef', 'chicken', 'milk', 'sour cream', 'soup', 'porridge']

    def __str__(self):
        """
        Метод, возвращающий строку описание свойств кота
        : return : строка с описанием свойств кота
        """
        return f'{self.name} is {self.age}. He is {self.breed}.\nIs he hungry? - {self.hungry}!\nHow many hours he was outdoor? - {self.hours_outdoors}.'

    def get_outdoor(self):
        """
        Метод - отправить кота погулять, считает количество часов на прогулке и считает уровень голода кота по количеству мяукания
        """
        hours = randint(0, 5)
        if self.hours_outdoors > 5:
            print(f'{self.hours_outdoors} hours!! Enough!! Go to eat!')
        else:
            if hours == 0:
                print('You are fool of energy, you should go outdoor!')
                self.hours_outdoors = False
                self.hungry = False
                self.cat_voice = randint(0, 1)
            elif hours >= 1 <= 3:
                print(f'You are good cat, being outdoor {hours} hours!')
                self.hours_outdoors += hours
                self.hungry = True
                self.cat_voice = randint(2, 5)
            else:
                print(f'You must be very hungry! Being outdoor {hours} hours')
                self.hours_outdoors += hours
                self.hungry = True
                self.cat_voice = randint(6, 10)

    def get_cat_voice(self):
        """
        Метод, печатающий голос кота - количество мяуканий, зависящих от уровня голода и проведенных часов на прогулке
        """
        print('-'.join(["meu"] * self.cat_voice).title())

    def get_eat(self, cats_food):
        """
        Метод - кормить кота, в зависимости от уровня голода выдает такое же количество еды и проверяет ест ли кот то,
        чем мы его кормим. В случае успешной кормежки отмечаем, что кот уже не голоден.
        : param cats_food :  еда, которой мы пытаемся покормить кота
        """
        if self.cat_voice == 0 or self.cat_voice == 1:
            print(f'You are not hungry! Go outdoor, please, {self.name}!')
        elif self.cat_voice > 1 < 5:
            if cats_food in self.food:
                print(f'Bon appetite, yumi-yumi {cats_food}!')
                self.hungry = False
            else:
                print(f"Our {self.name} won't eat {cats_food}!")
        else:
            if cats_food in self.food:
                print(f'Bon appetite, sweetie {self.name}, yumi-yumi {cats_food}!')
                self.hungry = False
            else:
                print(f"Our {self.name} won't eat {cats_food}!")

    def is_cat_outdoor(self) -> bool:
        """
        Метод проверяет гулял кот или нет
        : return : булевое значение - True - гулял, False - не гулял
        """
        if self.hours_outdoors != 0:
            return True
        else:
            return False

    def is_cat_eat(self) -> bool:
        """
        Метод проверяет голоден кот или нет
        : return : булевое значение - True - голоден, False - не голоден
        """
        if self.hungry:
            return True
        else:
            return False