from conf import model
import random
from faker import Faker
import json
import re
# from itertools import cycle


OUTPUT_FILE = "output.json"

# random_book = {
#     "model": "shop_final",
#     "pk": 1,
#     "fields": {
#         "title": "test_book",
#         "year": 2020,
#         "pages": 123,
#         "isbn13": "978-`-60487-647-5",
#         "rating": 5,
#         "price": "123456.0",
#         "author": [
#             "test_author_1",
#             "test_author_2"
#         ]
#     }
# }
"""Функция генерации автора книги
    :author: автор книги
"""


def get_author():
    fake = Faker("ru")
    match = re.search(r'[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+\s+', fake.name())
    return match[0] if match else 'Not found'


"""Функция генерации стоимости книги
    :price: стоимость книги (случайное натуральное число)
"""


def get_price():
    price = float(random.uniform(0, 5000))
    return price


"""Функция генерации рейтинга книги
    :rating: рейтинг книги (случайное число с плавающей запятой от 0 до 5)
"""


def get_rating():
    rating = float(random.uniform(0, 6))
    return rating


"""Функция генерации международного стандартного книжного номера
    :isbn13: международный стандартный книжный номер (случайный набор чисес из модуля Faker)
"""


def get_isbn13():
    fake = Faker()
    for _ in range(1):
        fake.isbn13()
        return fake.isbn13()


"""Функция генерации количества страниц книги
    :pages: количество страниц книги (случайное натуральное число)
"""


def get_pages():
    pages = int(random.uniform(5, 2022))
    return pages


"""Функция генерации года выпуска книги
    :year: год выпуска книги (случайное натуральное число)
"""


def get_year():
    year = int(random.uniform(1000, 2022))
    return year


"""Функция возврата названия книги
    :title: название книги
"""


def get_title():
    # if match == re.search(r'"(.|\n)+?"'):
    line = random.choice(open('books.txt', encoding="utf-8").readlines())
    return line


"""Функция возврата счетчика генерации нового объекта
    :pk: счетчик (по умолчанию = 1)
"""


def get_pk(pk=1):
    return pk


"""Функция возврата переменной model, импортированной из config.py
# model: 'shop_final.book'
"""


def get_model():
    return model


"""Функция генератора списка словарей
# pk: счетчик вызова объекта
"""


def generator(pk):
    book_list = []  # создаем пустой список
    for i in range(pk, 101, 1):  # запускаем цикл с генерацией 100 словарей
        random_book = {"model": model,  # создаем словарь с параметрами книги
                       "pk": i,
                       "field": {
                           "title": get_title(),
                           "year": get_year(),
                           "pages": get_pages(),
                           "isnb13": get_isbn13(),
                           "rating": get_rating(),
                           "price": get_price(),
                           "author": [get_author(),
                                      get_author(),
                                      get_author()]}}
        # print(random_book, i)
        book_list.append(random_book)  # добавляем результат в словарь
    # print(book_list)
    with open(OUTPUT_FILE, 'w', encoding="utf-8") as f:  # открываем файл для вывода в него данных
        j = json.dumps(book_list, ensure_ascii=False, indent=4)  # сериализуем список словарей
        print(j)
        f.write(j)  # записываем результат в файл


"""Функция запроса у пользователя начального числа счетчика и запуска генератора словарей
"""


def main():
    pk = int(input("Введите с какого числа начинаем вести счет\n"))  # спрашиваем у пользователя с какого числа
    # начинаем отсчет
    generator(pk)


if __name__ == "__main__":
    main()
