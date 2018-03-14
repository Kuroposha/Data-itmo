from abc import ABCMeta, abstractmethod
from random import rangrange

#Observer - Наблюдатель
class Subject(metaclass=ABCMeta):
    def __init__(self):
        self.__observes = []

    def add_observer(self, observer):
        assert isinstance(observer, Observer)
        self.__observes.append(observer)

    def remove_observer(self, observer):
        if observer in self.__observes:
            self.__observes.remove(observer)

    def notify_observer(self):
        for observer in self.__observes:
            observer.handle_event(self)

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def handle_event(self, subject):
        pass


class LoginHandler(Subject):
    def __init__(self):
        super().__init__()
        self.result = None

    def authorize(self, login, password):
        """
        Результаты работы:
            1. Успешный вход
            2. Ошибка

        Требования:
            1. Нужно логировать все успешные входы
            2. Нужно логировать все ошибки при входе
            3. Ошибка провайдера, посылаем cookie
        """
        self.result = randrange(3)
        self.notify_observers
class LoggerObserver(Observer):
    def handle_event(self, subject):
        if subject.result == 0:
            print('Пишем в access.log')


class ErrorObserver(Observer):
    def handle_event(self, subject):
        if subject.result == 1:
            print('Пишем в error.log')


class CookieObserver(Observer):
    def handle_event(self, subject):
        if subject.result == 2:
            print('Посылаем Cookie')

subject = LoginHandler()
subject.add_observer(LoggerObserver())
subject.add_observer(ErrorObserver())
subject.add_observer(CookieObserver())

subject.authorize('root', 'toor')
"""Создание объекта события. ПРочитать о наблюдателях сраных. Они помогут в игре!"""
