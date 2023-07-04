from .animal import Animal
from random import randint


class Cat(Animal):
    """
    Класс отвечает за симуляцию животного курица
    """
    def __init__(
            self,
            name: str,
            age: int,
            say_word='Мур-Мур'
    ):
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'кролик', 'курица'},
            health=True
        )
        self.animal_type = 'Кошка'

    def treat(self, hours: int) -> str:
        """
        Ухаживая за кошкой должное количество времени, мы получаем 10 кусь за палец
        Если меньше - от 1 до 5 кусь
        :param hours: сколько часов ухаживаем
        :return: от 1 до 10 кусь
        """
        if hours > 2:
            print(f'Вы ухаживаете за {self} {hours} часов и получаете десять кошачьих кусь')
            return 'Клшачьих кусь: 10 шт.'
        print(f'Вы ухаживаете за {self} {hours} часов и получаете немного кошачьих кусь')
        return f'Кошачьих кусь: {randint(1, 5)}'
