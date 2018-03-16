"""
Стратегия - паттерн поведения объектов
Policy


"""
from abc import ABCMeta, abstractmethod

class Car(object):
    def __init__(self, fuel_strategy):
        self.fuel_strategy = fuel_strategy

    def drive(self):
        #делегировнаия
        self.fuel_strategy.drive()


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def drive(self):
        #делегирование чем дел отличается от полиморфизма?????
        #что такое агрегирование?????
        # self.fuel_strategy.drive()
        pass

class PetrolStrategy(Strategy):
    def drive(self):
        print('Едем на бензине')

class Diesel(Strategy):
    def drive(self):
        print('Едем на дизеле')

class ElectroStrategy(Strategy):
    def drive(self):
        print('Едем на электричестве')
