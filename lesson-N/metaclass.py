# Метаклассы
"""
Класс - шаблон для создания объектов
Метакласс - шаблон для создания классов
(кто создает метакласс? - ТИП)
"""
import weakref

#слабые ссылки
def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

Person = type('Person', (object,), {
    '__init__': __init__,
    '__str__': lambda self: '{} {}'.format(self.firstname, self.lastname)
})

print(Person)
print(type(Person))

class DemoMeta(type):
    def __new__(mcs, name, bases, d):
        """Настоящий конструктор
        name     - Имя создаваемого типа
        bases    - Кортеж базовых типов
        d        - словарь атрибутов
        при работе с методом нью обязательно надо что л возвращать
        а также передавать ссылку на cls
        """
        print('Выделение памяти под класс:\n', name, bases, d)
        return super().__new__(mcs, name, bases, d)


    def __init__(cls, name, bases, d):
        """Не конструктор, а инициализатор"""
        print('Инициализация класса:\n', name, bases, d)
        super().__init__(name, bases, d)

    def __call__(cls, *args, **kwargs):
        """ Метод для вызова объектов"""
        print('Создание экземпляра (объекта):\n', args, kwargs)
        return super().__call__(*args, **kwargs)

#six => with_metaclass()
class DemoClass(metaclass=DemoMeta):
    """__metaclass__ only Python2"""
    def __new__(cls, *args, **kwargs):
        print('Выделение памяти под экземпляр(объект):\n', args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print('Инициализация экзепляра (объекта):\n', args, kwargs)


# demo = DemoClass(1, True, status='OK')
# demo2 = DemoClass(2, False, status='NotOK')

class RememberMeta(type):
    def __init__(cls, name, bases, d):
        """hasattr(true/false), getattr(value/exception/3), setattr(установка атрибута), delattr(удаление атрибута)"""
        if not hasattr(cls, '__instances_cache'):
            cls.__instances_cache = []
        super().__init__(name, bases, d)

    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        cls.__instances_cache.append(weakref.ref(obj))
        return obj


    def get_instance_cache(cls):
        return [r() for r in cls.__instances_cache if r()]


class Ship(metaclass=RememberMeta):
    def __init__(self, tp, x=-1, y=-1, rotation=0):
        self.type = self.health = tp
        self.x = x
        self.y = y
        self.rotation = rotation


class Field(metaclass=RememberMeta):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

field = Field(10, 10)
field.add_ship(Ship(4))
field.add_ship(Ship(3))

print(Field.get_instance_cache())
print(Ship.get_instance_cache())

del field

print(Field.get_instance_cache())
print(Ship.get_instance_cache())
