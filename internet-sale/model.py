"""
ORM - object-relational mapper
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

class Category(object):
    """Категория товара"""
    title = str
    description = str
    parent #ссылка на саму себ
    media
    products

class Product(object):
    """Товар"""
    title = str
    price = float
    description = str
    categories
    comment
    media


class Customer(object):
    """Покупатель"""
    discuont = float #размер скидки
    phone = str
    email = str
    name = str

class Order(object):
    """Заказ"""
    customer
    order_items
    status
    created


class Status(object):
    """Справочник"""
    name = str

class Cart(object):
    """Корзина"""
    customer
    cart_items


class CartItem(object):
    """Продукт в корзине"""
    product
    amount

class OrderItems(object):
    """Продукт в заказе"""
    product
    amount



class Page(object):
    """Страница сайта"""

# PonyORM & Flask

class Language(object):
    """Язык - справочник"""

class Media(object):
    """Мультимежиа ресурс"""

class Comment(object):
    """отзывы или комментарии"""

"""Связь с соцсетями можно вписать через сторонние библиотеки"""
class Sale(object):
    """Банеры под акции и распродажи"""
    """Размер скидки, промокод"""
    #Обсуждается
