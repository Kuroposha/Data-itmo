# Декораторы

""" особенность питона
Декоратор - это функция, основное назначение которой заключается в том,
чтобы оборачивать другие функции или классы.

Замыкания.

функция в функции
ленивые вычисления - внутри одной функ вып другая вунк долгая и сложная.
внешняя функция будет возвращять ссылку
"""
from time import time
from urllib.request import urlopen

# def page(url):
#     def get():
#         return urlopen(url).read()
#     return get
#
# python = page('http://python.org')
# print(python())

def factorial(n):
    f = 1

    for i in range(1, n+1):
        f *= i

    return f

# Переменное количество аргументов
def benchmark(func, *args, **kwargs):
    started = time() # ввозвращяет время от эпохи линукс в секндаз
    result = func(*args, **kwargs)
    worked = time() - started
    print('Функция {} выполнилась за {:f} микросекунд'.format(func.__name__, worked * 1e6))
    return result
# :f - магия например флоат, формат даты или еще какую радость

print(benchmark(factorial, 50))
# print(benchmark(python))
