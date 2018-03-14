"""
Стратегия - паттерн поведения объектов
Policy


"""
from abc import ABCMeta, abstractmethod

class Car(object):
    def __init__(self, fuel_strategy):
        self.fuel_strategy = fuel_strategy

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def drive(self):
        #делегирование чем дел отличается от полиморфизма?????
        #что такое агрегирование?????
        self.fuel_strategy.drive()

class PetrolStrategy(Strategy):
    def drive(self):
        print('Едем на бензине')

class Diesel(Strategy):
