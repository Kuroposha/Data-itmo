# генераторы списков
"""
[expression for item1 itarable1 if conditional1
            for item2 itarable2 if conditional2
            ....
            for itemN itarableN in conditionalN]
"""
numbers = [1, 1, 2, 2, 3, 3]

squares = [i * i for i in numbers]
odd = [i for i in numbers if i % 2]

# points = []
#
# for x in range(3):
#     for y in range(3):
#         points.append((x, y))

points = [(x, y) for x in range(3)
                 for y in range(3)]

#Генераторы множеств
s = {i for i in numbers}# == set(numbers)

# Генераторы словарей

keys = ['id', 'original_url', 'short_url', 'created']
values = [1, 'http://ya.ru', '/1', '2018']

data = {k: v for i, k in enumerate(keys)
             for j, v in enumerate(values) if i == j}

data = dict(zip(keys, values))

for k, v in zip(keys, values):
    print(k, v)
print(type(zip()))
