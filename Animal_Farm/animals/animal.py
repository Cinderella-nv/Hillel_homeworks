class Animal:
    def __init__(self, name: str, age: int, say_word: str, preferred_food: set, health: bool):
        """
        Класс отвечает за симуляцию жизнедеятельности животного на ферме
        :param name: имя животного
        :param age: возраст животного
        :param say_word: какой "фразой" животное симулирует разговор
        :param preferred_food: рацион питания
        :param health: проверка здоровья
        """
        self.animal_type = '???'
        self.name = name
        self.age = age
        self.say_word = say_word
        self.preferred_food = preferred_food
        self.health = health
        self.hungry = True

    def __str__(self):
        return f'{self.animal_type} {self.name}'

    def say(self):
        """
        Животное произносит заготовленные "фразы" для привлечения внимания в чате :)
        """
        print(f'{self} говорит: {self.say_word}')

    def eat(self, food: str):
        """
        Метод отвечает за симуляцию еды у животного на ферме
        Если предложенная еда есть в preferred_food, то животное наестся и self.hungry = False
        иначе животное не покушает
        :param food: что кушаем
        """
        if not self.hungry:
            return
        if food in self.preferred_food:
            print(f'{self} кушает {food}')
            self.hungry = False
        else:
            print(f'{self} такое не ест: {food}')
            self.say()

    def treat(self, hours: int):
        """
        Метод ухаживания за животным
        :param hours: сколько часов мы проводим с животным
        :return: что получаем взамен
        """
        raise NotImplementedError

    def visit_a_doctor(self):
        """
        Метод проверки визита к доктору
        """
        if self.health:
            print(f'{self.animal_type} {self.name} только что от ветеринара и прекрасно себя чувствует!')
        else:
            print(f'{self.animal_type} {self.name} нуждается в визите к ветеринару!')

