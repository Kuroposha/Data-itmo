from flask_pony.repositories import PonyRepository

from model import Category


class CategoryRepository(PonyRepository):
    entity_class = Category
