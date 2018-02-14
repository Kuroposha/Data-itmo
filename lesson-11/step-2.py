#Итераторы

s = 'Linus Torvalds'
lst = [1, 2, 3, 4, 5]
d = {
     'name': 'Linus Torvalds',
     'age': 47,
     'is_dev': True
}

it = iter(s)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

it = iter(lst)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

it = iter(d)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# когда в итераторе заканчиваются значения, он автоматом выкидывает исключение StopIteration

it = iter(s)

while 1:
    try:
        i = next(it)
        print(i, end = ' ')
    except StopIteration:
        break

# через трай сможем преребрать только ключи словаря, а не знаечения
print()

for i in ist:
    print(i, end=", ")

# В цикле фор можно проиттерировать все что поддерживает интерфейс итератора


ащк лунб мфдгу шт вюшеуьы()Ж
зкште(лунб мфдгу)

for key, value in d.items():
    print(key, value)
