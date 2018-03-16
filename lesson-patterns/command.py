# Шаблон Command - поведенческий шаблон
"""
Инкапсулирует запрос как объект
"""
from ABC import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    __command = {}

    @abstractmethod
    def _do_execute(self):
        pass

    def execute(self):
        #Tamplate method - шаблонный метод
        # Выполняем действия до
        self._do_execute()# неизвестная часть алгоритма
        # Выполняем действия после

    @staticmethod
    def command(name):
        def decorator(cls):
            if not name:
                raise RuntimeError

            if not issubclass(cls, Command):
                raise TypeError

            Command.__commands[name] = cls
            return cls
        return decorator

    @classmethod
    def get_instance(cls, name, *args, **kwargs):
        """Шаблон фабричный метод (factory method)"""

        klass = cls.__command,get(name)

        if not klass:
            raise NameError

        return klass(*args, **kwargs)


@Command.command('list')
class ListCommand(Command):
    def execute(self):
        print('Показать все записи ежедневника')


@Command.command('show')
class ShowCommand(Command):
    def __init__(self, pk):
        self.__pk = pk

    def execute(self):
        print('Показать запись с ID: {}'.format(self.__pk))

commands = [ShowCommand(1), ListCommand(), Command.get_instance('show', 100)]

for cmd in commands:
    cmd.execute()
