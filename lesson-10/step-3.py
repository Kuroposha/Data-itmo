# Декоратор с параметрами

#! Внимание более трех декораторов в коде - моветон
"""
def decorator_with_params(debag=False): #любые аргументы
    def decorator(func):
        def wrapper(*args, **kwargs):
            if debag:
                print('Do something wrong...')
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_params() - если применяется декоратор с параметрами нужны скобки обязательно
def func():
    pass
"""
#в файл
# пихаем функцию в переменную, чтобы не вызывать ее по пятьсот раз
from datetime import datetime

def log(filename):
    template = '''
[{now:%Y-%m-%d %H:%M:%S}] Function: "{func}" called with:
    -> positional arguments: {args}
    -> keyword arguments: {kwargs}
Returns: {result}
'''
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            with open(filename, 'a') as f:
                f.write(template.format(now=datetime.now(),
                                        func=func.__name__,
                                        args=args,
                                        kwargs=kwargs,
                                        result=result))
            return result
        return wrapper
    return decorator

@log('log.txt')
def func(a,b):
    return a + b

func(1, 2)
func(4, 5)
