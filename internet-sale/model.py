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
from time import sleep

from pony.orm import (
    Database,
    Required, Optional, Set, PrimaryKey,
    LongStr,
    set_sql_debug, show
    )

db = Database('sqlite', 'estore.sqlite', create_db=True)
# db.bind() если без аргументов

class Category(db.Entity):
    """Категория товара"""
    title = Required(str, 50)
    description = Optional(LongStr)
    parent = Optional('Category', reverse='categories') #ссылка на саму себ
    media = Set('Media')
    products = Set('Product')
    categories = Set('Category', reverse='parent')

class Product(db.Entity):
    """Товар"""
    title = Required(str, 500)
    price = Required(float)
    description = Optional(LongStr)
    categories = Set('Category')
    comments = Set('Comment')
    media = Set('Media')
    order_items = Set('OrderItem')
    cart_items = Set('CartItem')

class Customer(db.Entity):
    """Покупатель"""
    discuont = Optional(float, default=1) #размер скидки, где 1 это 100%
    phone = Required(str, 20, unique=True)
    email = Optional(str, 100)
    name = Optional(str, 255)
    orders = Set('Order')
    cart = Optional('Cart')

class Order(db.Entity):
    """Заказ"""
    customer = Required('Customer')
    order_items = Set('OrderItem')
    status = Required('Status')
    created = Optional(datetime, default=datetime.now)

    def before_insert(self):
        super().before_insert()
        self.creater = datetime.now()

class Status(db.Entity):
    """Справочник"""
    name = PrimaryKey(str, 50)
    orders = Set('Order')

class Cart(db.Entity):
    """Корзина"""
    customer = Optional('Customer', nullable = True)
    cart_items = Set('CartItem')

class CartItem(db.Entity):
    """Продукт в корзине"""
    product = Required('Product')
    amount = Optional(int, default=1, min=1)
    cart = Required('Cart')

class OrderItem(db.Entity):
    """Продукт в заказе"""
    products = Set('Product')
    amount = Optional(int, default=1, min=1)
    order = Required('Order')

# class Page(db.Entity):
#     """Страница сайта"""
# PonyORM & Flask
# class Language(db.Entity):
#     """Язык - справочник"""

class Media(db.Entity):
    """Мультимежиа ресурс"""
    categories = Set('Category')
    products = Set('Product')

class Comment(db.Entity):
    """отзывы или комментарии"""
    products = Set('Product')
# #
# """Связь с соцсетями можно вписать через сторонние библиотеки"""
# class Sale(db.Entity):
#     """Банеры под акции и распродажи"""
#     """Размер скидки, промокод"""
#     #Обсуждается
set_sql_debug(True)
db.generate_mapping(create_tables=True)

#дб сессию можно юзать через КМ или декоратор
with db_session:
    # # customer = Customer(phone='+79992100246')
    # customer = Customer[1]
    # status = Status(name = "'i'm drowse")
    #
    sleep(5)
    # order = Order(customer=customer,
    #               status=status)
    # show(order)
    #
    # sleep(5)
    # order = Order(customer=customer,
    #               status=status)
    # show(order)
