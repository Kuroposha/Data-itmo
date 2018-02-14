#Декораторы
"""
служи оберткой для другой ф или класса.

главная цель - изменить или расширить возможности
оборачив объекта
принимает в кач арг только ссылку на функ
"""
from functools import reduce, lru_cache
from time import time
import pickle

# def decorator(func):
#     def wrapper():
#         return func()
#     return wrapper
# # стандартный вид декоратора
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
# # стандартный вид декоратора  c переменными
# """Перед опред функции пишем"""

# # @decorator
# # def factorial(n)   :
# #     return reduce(lambda f, x: f * x, range(1, n+1))
# # #редьюс изучить
# print(factorial(50))

def benchmark(func):
    def wrapper(*args, **kwargs):
        started = time() # ввозвращяет время от эпохи линукс в секндаз
        result = func(*args, **kwargs)
        worked = time() - started
        print('Функция {} выполнилась за {:f} микросекунд'.format(func.__name__, worked * 1e6))
        return result
    return wrapper

# @benchmark
# def factorial(n):
#     f = 1
#
#     for i in range(1, n+1):
#         f *= i
#     print f
#     return f


def cache(func):
    memory = {}

    def wrapper(*args, **kwargs):
        key = pickle.dumps((args, sorted(kwargs.items())))

        if key not in memory:
            memory[key] = func(*args, **kwargs)

        return memory[key]
    return wrapper
# @benchmark
# @cache
# def factorial(n)   :
#     return reduce(lambda f, x: f * x, range(1, n+1))
# не правильно
# factorial = benchmark(factorial)

print(factorial(50))
print(factorial(50))

@cache
@benchmark
def factorial(n)   :
    return reduce(lambda f, x: f * x, range(1, n+1))
#правильно
