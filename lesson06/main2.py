# Форматы данных

data = {
    'users': [
        {
            'id': 1,
            'name': 'Linus TORV'
            'skills': ('C++', 'C', 'Linux')
            'is_developer': True
        },
        {
            'id': 2,
            'name': 'Richard Stall'
            'skills': ('C', 'GNU')
            'is_developer': True
        }
    ]
}

# Pickle - аннотивный формат. двоичные файлы

import pickle


with open('users.pickle', 'wb') as f: # для записи двоичного файла
    pickle.dump(data, f)

with open('users.pickle', 'rb') as f:
    print(pickle.load(f))#принимает файловый дискриптор и возвращ сервиз. строку

    # такой файл читает только питон

# Json - JavaScript Object Notation - кроссязычный формат

import json

with open('users.json', 'w') as f:
    json.dump(data, f)

with open('users.json') as f:
    print(json.load(f))
    # для джейсона нет кортежа - это список(массив)

"""

with open('users.json', 'w') as f:
    json.dump(data, f, indent=4)
    """

# CSV
"""
в таких файлах - одна строчка = одна запись(сущность)
пищут через поля
'''
id;name;skills;is_developer
1;Linus TORV;C,C++,Linux;1
2;Richard Stall;C,GNU;1
'''
"""
import csv

with open('users.csv', 'w') as f:
    users = data.get('users')# метод словарей проверяет физическое значение в словаре

    if users:
        fieldnames = users[0].keys()
        # позволяет получать ключи из словаря, но работать будет как список

        writer = csv.DictWriter(f, fieldnames=fieldnames)# Класс DictWriter
        # порядок записи через кейс не работет

        write.writeheader()

        for user in users:
            writer.writerow(user)

with open('users.csv') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)
# можно сделать csv файл и открыть его в экселе, но обратно из csv сложно
# собрать приличный файл

#INI (conf)
"""
ini не поддерживает дерево.
нужно сочинять
db_host = localhost
db_user = root
db_pass = toor
db_name = my_blog
или
db.host = localhost
db.user = root
db.pass = toor
db.name = my_blog

и тд

никакого модуля, позволяющего писать эти файлы нет.
но есть конфиг для чтения.
нет однозначного формата чтения.
нет типов данных
"""
#lxml - распарсит языки разметки

'''
XML - пенсионный тип
Extended MARKUP Language

это дерево. должен быть корень. шапка и тд.

'''
