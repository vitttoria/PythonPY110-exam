from conf import model
import random
from faker import Faker
from itertools import repeat
# import re
import json
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
    # match = re.fullmatch(, string)
    return fake.name()


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


def get_pk():
    pk = 1
    return pk


"""Функция возврата переменной model, импортированной из config.py
# model: 'shop_final.book'
"""


def get_model():
    return model


"""Создание словаря с описанием книги"""
random_book = {"model": model,
               "pk": get_pk,
               }

"""Создание словаря внутри словаря с описанием параметров книги"""
random_book["field"] = {"title": get_title(),
                        "year": get_year(),
                        "pages": get_pages(),
                        "isnb13": get_isbn13(),
                        "rating": get_rating(),
                        "price": get_price(),
                        "author": [get_author(),
                                   get_author(),
                                   get_author()]}

"""Функция запуска генератора словарей
# list_: список словарей
"""


def main():
    for list_ in repeat(random_book, 100):
        print(list_)
        with open(OUTPUT_FILE, 'w'):
            j = json.dumps(list_, ensure_ascii=False, indent=4)
            print(j)


if __name__ == "__main__":
    main()
