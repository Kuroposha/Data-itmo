# ООП. Классы и объекты
# НАзвания Классов CamelCase без цифр
"""
Зачем нужны свойства?
- свойства, атрибуты, свойства-члены, поля
это данные объекта.
можно создавать динамически, но можно убрать создание свойств на лету
Объекты - изменяемый тип данных, передается по ссылке, не копированием, можем
хранить несколько
Объекты - структурные типы данных.
Зачем нужны методы?
- метод - это функция объявленная в контексте класса
это поведение объекта
Позволяют
- менять состояние объекта,
- получать состояние объекта,
- взаимодействовать с объектом

ЗАчем нужен конструктор?
в питоне есть магические методы, они вызываются неявно, в момент опред действий
__init__ - метод конструктора вызывается неявно в момент создания объекта
- нужен,чтобы проинициализировать объект (экземпляра)
не для сложных вычислений. только для основных свой ств объекта
имена аргументов могут отличаться от имен свойств, но это не удобно, количество
свойств не ограничено, но необязательно передавать все.
пример fio
если не нужно инициализировать объект, то конструктор не нужен

свойства нужно защищать от вмешательства из вне.
при помощи сеттера и геттера

"""

 class Person(object):
     def __init__(self,
                  firstname,
                  lastname,
                  phone=None):
         '''Конструктор'''
         self.firstname = firstname
         self.lastname = lastname
         self.phone = phone
         self.head = 1

    def get_name(self):
        '''getter - получатель'''
        return '{} {}'.format(self.firstname,
                              self.lastname)

    def set_firstname(self, firstname):
        '''setter - установщик'''
        self.firstname = firstname

    def is_killed(self):
        return bool(self.head)

    def kill(self):
        self.head = 0

#Все методы на

#self - это ссылка на текущий экземпляр объекта
#!Внимание, лучше всего писать в стилях, обратносовместимых с предыдущей версией
#создание объекта, или создание экземпляра объекта
person_1 = Person('Вася', 'Пупкин', '+79991234567')
person_2 = Person('Иммануил', 'Кант')

# person_1.firstname = 'Вася'
# person_1.lastname = 'Пупкин'
# person_1.phone = '+79991234567'

#Чтение значение из свойства
print(person_1.firstname)
print(person_1.get_name())
'''
Наследование.
- создание нового класса на базе существующего
- новый класс называется дочерний (ребенок)
- класс, от которого наследуем называется базовым(родительским)
наследование нужно для того, чтобы обозначить более спцифичный класс

Множественное наследование
class A(object): pass
class B(object): pass
class C(A, B): pass
Множественное наследование это плохо, это вызывает ошибки при совмещении классов
(одноименные методы беда)

'''
class Developer(Person):
    def __init__(self,
                 firstname,
                 lastname,
                 skills,
                 phone=None):
        super().__init__(firstname, lastname, phone) #позволяет наследовать от
        # родительского класса, можно в третьем питоне исп без аргументов
        #Python 2
        #super(Developer, self).__init__(firstname, lastname, phone)
        self.skills = skills


linus = Developer('Linus', 'Torvalds', ['C++', 'Linux'])
print(linus.getname())

"""
Статические свойства и методы
это
св-ва и методы, объявленные в контексте класса
Есть контекст объекта - работа в конексте объекта, все методы с селф это методы,
привязанные к объекту
 и контекст класса
 если мы объявляем кк, то нам не нужно создавать объект, чтобы оно действовало

Статика - общая для всех объектов!
Как питон находит свойств
у каждого объекта есть дир -
и дикт - словарь атрибутов для данного объекта
статика это очень круто

Статические методы - можно выхзывать не создаывая объект
Статический метод === метод класса
Синглтон - название шаблона объекта одиночки. сколько бы не создавали объектов
это будет один и тодже экземпляр

статика работает быстрее и фабрики работают на ней

# """

class Singleton(object):
    instance = None # статическое св-во

    # @staticmethod
    # def get_instance():
    #     # фабрика
    #     if not Singleton.instance:
    #         Singleton.instance = Singleton()
    #     return Singleton.instance
    @classmethod
    def get_instance(cls):
        #тоже статичесий методж но с классом в аргументе( ссылкой на текущий класс)
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

            
obj1 = Singleton.get_instance()
obj2 = Singleton.get_instance()
print(obj1, obj2)
print(obj1 is obj2)

# print(Singleton.instance)#None
# s = Singleton()
# print(s.instance)#None
# s.instance = 666
# print(Singleton.instance)#None
# print(s.instance)#666
#
# print(s.__dir__())
# print(s2.__dir__())
