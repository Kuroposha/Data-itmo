"""
ORM - db.Entity-relational mapper
или объектно реляционное отображение
ооп которое связывает бд с объектно ориентированным кодом
бд это важно
создаем таблицы, колонки в них, внешние и первичные ключи.
в каждм орм реализован шабломн проектирования дата маппер
"дата маппер - это программная прослойка, разделяющая объект и базу данных
при использовании дм объекты не нуждаются в знаниях о том, что есть некая бд"
работа в орме с рипозиториями (сущности_)
хороший орм кеширует запросы
ленивая загрузка - жадная загрузка(при обращении к объекту, пони пытается все загрузить)


"""
from datetime import datetime

from pony.orm import (
    Database,
    Required, Optional, Set, PrimaryKey,
    LongStr
    )

db = Database('sqlite', 'estore.sqlite', create_db=True)
# db.bind() если без аргументов

class Category(db.Entity):
    """Категория товара"""
    title = Required(str, 50)
    description = Optional(LongStr)
    parent #ссылка на саму себ
    media
    products


class Product(db.Entity):
    """Товар"""
    title = Required(str, 500)
    price = Required(float)
    description = Optional(LongStr)
    categories
    comment
    media


class Customer(db.Entity):
    """Покупатель"""
    discuont = Optional(float, default=1) #размер скидки, где 1 это 100%
    phone = Required(str, 20)
    email = Optional(str, 100)
    name = Optional(str, 255)

class Order(db.Entity):
    """Заказ"""
    customer
    order_items
    status
    created = Optional(datetime)

    def before_insert(self):
        super().before_insert()
        self.creater = datetime.now()

class Status(db.Entity):
    """Справочник"""
    name = PrimaryKey(str, 50)

class Cart(db.Entity):
    """Корзина"""
    customer
    cart_items


class CartItem(db.Entity):
    """Продукт в корзине"""
    product
    amount = Optional(int, default=1, min=1)

class OrderItems(db.Entity):
    """Продукт в заказе"""
    product
    amount = Optional(int, default=1, min=1)

#
#
# class Page(db.Entity):
#     """Страница сайта"""
#
# # PonyORM & Flask
#
# class Language(db.Entity):
#     """Язык - справочник"""
#
# class Media(db.Entity):
#     """Мультимежиа ресурс"""
#
# class Comment(db.Entity):
#     """отзывы или комментарии"""
# #
# """Связь с соцсетями можно вписать через сторонние библиотеки"""
# class Sale(db.Entity):
#     """Банеры под акции и распродажи"""
#     """Размер скидки, промокод"""
#     #Обсуждается
