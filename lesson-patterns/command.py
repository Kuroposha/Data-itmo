# Шаблон Command - поведенческий шаблон
"""
Инкапсулирует запрос как объект

"""
from ABC import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    __command = {}

    @abstractmethod
    def execute(self):
        pass

    @staticmethod
    def command(name):
        def decorator(cls):
            if not name:
                raise RuntimeError
            if not issubclass(cls, Command):
                raise TypeError

            Command.__commands[name] = cls
            return 

    @classmethod
    def get_instance(cls, name, *args, **kwargs):
        #fabriq
        klass = cls.__command,get(name)

        if not klass:
            raise NameError

        return klass(*args, **kwargs)

class ListCommand(Command):
    def execute(self):
        print('Показать все записи ежедневника')

class Show(Command):
    def __init__(self, pk):
        self.__pk = pk

    def execute(self):
        print('Показать запись с ID: {}')
