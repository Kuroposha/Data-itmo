# Шаблоны проектирования - Patterns
"""
1) Имя
2) Задача(проблема)
3) Решение
4) Результат

Использование UML
1) Диаграммы классов
2) Диаграммы использования(последовательности)
3) Диаграмма участников
Шаблоны проектирования не являются решением.
Шаблоны проектирования редко используются поштучно.

Шаблоны делятся на три группы
1) Порождающие (возвращают объекты)
2) Структурные (задает архитектуру проекта)
3) Поведенческие (описывают поведение объеков)
"""
# Singleton - шаблон проектирования класса, возвращ. только 1 экз

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Registry(object):
    __slots__ = ('__params',)
    
    def __init__(self):
        self.__params = {}

    def __iter__(self):
        return iter(self.__params.items())

    def __getattribute__(self, key):
        # print(key)
        try:
            return super().__getattribute__(key)
        except AttributeError:
            return self.__params.get(key)

    def __setattr__(self, key, value):
        # print(key, value)
        try:
            super().__setattr__(key, value)
        except AttributeError:
            self.__params[key] = value

    def __delattr__(self, key):
        try:
            super().__delattr__(key)
        except AttributeError:
            del self.__params[Key]

r = Registry()
r2 = Registry()

print(r == r2, r is r2)

r.db_host = 'localhost'
r2.ponos = 'puss'
r2.skans = 'kserit'

print(r2.db_host, r2.db_user)
print(r2.__dict__)

for key, value in r:
    print(key, value)
