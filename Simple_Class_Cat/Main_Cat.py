from random import choices, randint, random
from Cat_class import Cat

if __name__ == '__main__':

    cats = [
        Cat('Tom', 2, 'Scotish'),
        Cat('Main', 5, 'Maine Coon'),
        Cat('Bonya', 1, 'Sphinx'),
        Cat('Felix', 1, 'Siamese'),
        Cat('Saymon', 3, 'Persian'),
        Cat('Oscar', 4, 'British')
        ]
    food = ['fish', 'beef', 'chicken', 'milk', 'banana', 'bread', 'onion', 'sour cream', 'soup', 'porridge', 'potato', 'mango']
    random_cat = randint(0, 5)
    print("Let's meet our cat!")
    print(cats[random_cat])
    print(f"Go to walk {cats[random_cat].name}")
    if cats[random_cat].is_cat_outdoor():
        print("He is already walking")
    else:
        cats[random_cat].get_outdoor()
    print(f'Are you hungry? {cats[random_cat].hungry}')
    cats[random_cat].get_cat_voice()
    if cats[random_cat].is_cat_outdoor():
        print("He is already walking")
    else:
        cats[random_cat].get_outdoor()
    print("let's eat!")
    for random_food in choices(food, k=cats[random_cat].cat_voice):
        cats[random_cat].get_eat(random_food)
    print(f"Are you still hungry, {cats[random_cat].name}, darling?")
    print(cats[random_cat].is_cat_eat())
    print(f"Did you have a walk today, {cats[random_cat].name}?")
    print(cats[random_cat].is_cat_outdoor())

