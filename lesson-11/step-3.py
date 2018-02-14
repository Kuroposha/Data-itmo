"""
Генератор - это функция, которя воспроизводит последовательность значений и может использоваться
при выполнении операцийю
Генератор реализует итератор, любой генератор можно проитерировать

"""
def generator():
    print('Шаг1')
    yield 1
    print('Шаг2')
    yield 2
    print('Шаг3')
    yield
    return 'eflk'
""" инструкция елд возвращает результат
"""
gen = generator()
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))
"""
внутри гененраторов не нужны ретурны
Генераторы как и декораторы
Генераторы нужны для работы с большим объемом данных

"""
def countdow(n):
    print('Генератор стартанул')
    while n:
        yield n
        n -= 1

for i in countdow(3):
    print(i)

def generator_range(start, stop):
    # for i in range(start, stop):
    #     yield i
    yield from range(start, stop)
