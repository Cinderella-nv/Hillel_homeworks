'''
 +   -читає цей файл
 +   -створює індекс унікальних айді для кожного запису, тобто словник, де ключі - це згенеровані унікальні айді,
    а значення - повна інформація про позицію товару
+   -створює індекс по категоріям та брендам. Тобто словник, де ключі - це назва категорії/бренду,
    а значення - це перелік унікальних айді товарів, в яких є таке значення поля категорії/бренду
 +   -виводить на екран статистику скільки товарів є від кожного бренда та від кожної категорії
  +  -виводить на екран перелік повної інформації про кожний товар одного обраного бренда та однієї обраної категорії
    -рахує розподіл товарів по брендам для кожної категорії та виводить це на екран. Наприклад,
    в категорії Ноутбуки представлено 6 товарів від Lenovo, 8 від Mac, 10 від Dell, тощо.
    '''
import csv
import uuid


def open_csv_file_dict(filename, to_print=True) -> list:
    """
        Функция читает csv файл построчно и добавляет строки в список и выводит на экран в зависимости от флага to_print
        : param filename: csv файл
        : param to_print: булевое значение
        : return: список из строк читаемого файла
    """
    with open(filename, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
        if to_print:
            print(reader)
            for row in rows:
                print(row)
        return rows


def create_position_id_index(all_data: dict, column_name: str) -> dict:
    """
        Функция создает индексы по выбранной колонке для принимаемого словаря
        : param all_data: принимаемый словарь, у которого ключ - айдишник, а значение - описание товара
        : param column_name: имя колонки, по которой создаются индексы
        : return: словарь с ключем - индекс и значением - айдишники
    """
    new_index = dict()
    for i, data_entry in all_data.items():
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()
        new_index[data_entry[column_name]].append(i)
    return new_index


def print_position_id_index(all_data: dict, position_index: dict):
    """
        Функция выводит на экран индексированный список в виде словаря с полным описанием товара, который запрашивает пользователь
        : param all_data: принимаемый словарь, где ключ - это айдишник, а значение - полная информация о товаре
        : param position_index: принимаемый индексированный  словарь, где ключ - название выбранной колонки, значение - айдишники

    """
    search_item = input("What would you want to find or push Enter to see all list?")
    if search_item != '':
        for index_key, position_values in position_index.items():
            if search_item == index_key:
                print(f'Items of searching {index_key}')
                for i in position_values:
                    print('  ', all_data[i])
            elif search_item not in position_index:
                print('Not found your searching item')
                break
    else:
        for index_key, position_values in position_index.items():
            print(f'Items searching {index_key}')
            for i in position_values:
                print('  ', all_data[i])


def create_unique_id_index(all_data: list) -> dict:
    """
        Функция создвет уникальные айдишники для каждой позиции списка
        : param all_data: принимаемый список товаров
        : return: словарь, где ключ - уникальный айдишник, а значение - описание товара
    """
    unique_id = dict()
    for id_value in all_data:
        unique_id[uuid.uuid4().int] = id_value
    return unique_id


def print_unique_id_index(position_index: dict):
    """
        Функция выводит на экран словарь, где ключ - индекс, а значение - уникальные айдишники
        : param position_index: словарь, где ключ - индекс, а значение - уникальные айдишники
    """
    for index_key, position_values in position_index.items():
        print(f'Ids of searching {index_key}')
        for i in position_values:
            print('  ', i)

def get_quantity_indexes(position_index: dict):
    """
        Функция считает количесво товаров в каждом индексе и  выводит на экран статистику сколько товара в каждом индексе
        : param position_index: словарь, где ключ - индекс, а значение - список айдишников
    """
    for index_key, position_values in position_index.items():
        print(f' {index_key} have {len(position_values)} items')


def list_category_brand(all_data: dict) -> dict:
    """
        Функция считает распределение товаров по брендам для каждой категории и выводит на экран статистику
        категория/бренд/количество товаров
        : param all_data: принимаемый словарь, где ключ - это айдишник, а значение - полная информация о товаре
        : return: возвращает словарь, где ключ - это категория,  а значение - словарь, в котором ключ- бренд, значение - список
        айдишников
    """
    dict_category = create_position_id_index(all_data, 'category')
    dict_brand = create_position_id_index(all_data, 'brand')
    category_brand_index = dict()
    for category, id_index_category in dict_category.items():
        if category not in category_brand_index:
            category_brand_index[category] = dict()
        for brand, id_index_brand in dict_brand.items():
            if brand not in category_brand_index[category]:
                category_brand_index[category][brand] = list()
            for i in id_index_category:
                for j in id_index_brand:
                    if i == j:
                        category_brand_index[category][brand].append(i)
    for category, id_index_category in category_brand_index.items():
        for brand, id_index_brand in id_index_category.items():
            print(f'The {category} brand {brand} we have {len(id_index_brand)} items')
    return category_brand_index


if __name__ == "__main__":
    print_file = input("Enter Yes or No for print file after reading\n>").lower()
    if print_file == 'yes':
        print_file = True
    else:
        print_file = False
    tech_inventory = open_csv_file_dict('tech_inventory.csv', to_print=print_file)
    id_inventory = create_unique_id_index(tech_inventory)

    print("Creating dictionary for brands")
    index_brand = create_position_id_index(id_inventory, 'brand')
    print_position_id_index(id_inventory, index_brand)

    print("Creating dictionary for categories")
    index_category = create_position_id_index(id_inventory, 'category')
    print_position_id_index(id_inventory, index_category)

    print("Our statistics")
    get_quantity_indexes(index_brand)
    get_quantity_indexes(index_category)
    list_category_brand(id_inventory)