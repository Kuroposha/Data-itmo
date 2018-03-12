# ORM - Object-Relational Mapping

from datetime import datetime

from pony.orm import (
    Required, Optional, Set, PrimaryKey,
    LongStr
)

from app import pony


db = pony.db


class Category(db.Entity):
    """Категория товара"""
    title = Required(str, 50)
    description = Optional(LongStr)
    parent = Optional('Category', reverse='categories')
    media = Set('Media')
    products = Set('Product')
    categories = Set('Category', reverse='parent')


class Product(db.Entity):
    """Товар"""
    title = Required(str, 255)
    price = Required(float)
    description = Optional(LongStr)
    categories = Set(Category)
    comments = Set('Comment')
    media = Set('Media')
    order_items = Set('OrderItem')
    cart_items = Set('CartItem')


class Customer(db.Entity):
    """Покупатель"""
    phone = Required(str, 20, unique=True)
    email = Optional(str, 100)
    name = Optional(str, 255)
    discount = Optional(float, default=1) # размер скидки
    orders = Set('Order')
    cart = Optional('Cart')


class Order(db.Entity):
    """Заказ"""
    customer = Required(Customer)
    status = Required('Status')
    created = Optional(datetime, default=datetime.now)
    order_items = Set('OrderItem')


class Status(db.Entity):
    """Справочник статус"""
    name = PrimaryKey(str, 50)
    orders = Set('Order')


class OrderItem(db.Entity):
    product = Required(Product)
    amount = Optional(int, default=1, min=1)
    order = Required(Order)


class Cart(db.Entity):
    """Корзина"""
    customer = Optional(Customer, nullable=True)
    cart_items = Set('CartItem')


class CartItem(db.Entity):
    """Продукт в корзине"""
    product = Required(Product)
    amount = Optional(int, default=1, min=1)
    cart = Required('Cart')


class Page(db.Entity):
    """Страница сайта"""


class Language(db.Entity):
    """Язык - справочник"""


class Media(db.Entity):
    """Мультимедиа ресурс"""
    categories = Set('Category')
    products = Set('Product')


class Comment(db.Entity):
    """Комментарии"""
    product = Required('Product')
