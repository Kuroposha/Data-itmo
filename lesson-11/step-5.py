# Выражения - генераторы или генераторные выражения

numbers = [1, 1, 2, 2, 3, 3]

squares = (i * i for i in numbers)
# это не кортеж, это генератор
print(type(squares))

with open('../url-shortener/url_shortener/__init__.py') as f:
    lines = (line.strip() for line in f)
    decorators = (d for d in lines if d.find('@') != -1)
    print(list(decorators))
"""вне контектстного менеджера ничего нельзя сделать с генератором, который на него ссылается
сопрорграммы.
внимание, генератор может принимать значения, это и является сопрограммой
"""
