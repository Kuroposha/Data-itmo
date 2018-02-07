# SQLite
"""
СУБД - система управления БД
MySQL(мускул) (MariaDB), PostgreSQL
Oracle, MS SQL Server

СУБД занимается контролем целостности данных

SQLite - это БД в одном файле
идеально подходит:
    для куков, десктопных приложений ( локальных)
    питона (в стандартных библ)
не подойдет:
    для многопользовательских приложений
    для сервера

    # OpenSource - идеалогия

SQL - структурный язык запросов
    - DDL - Вфеф Вуаштшешщт Дфтпгыпу
     - CREARE TABL
    -DML -  дата. язык манипулирования даннных
    - INSERT INTO
    - UPDATE
    - DELETE
    - SELECT

NOSQL - для игры чата или прилож в рт

- реляционные бд
хранят файлы в виде таблиц сущностей (1 табл = 1 сущ)
таблицы должны быть связаны
связи в таблицах
1:1 n:1 1:n n:n
обязательное наличие первичного ключа, внешнего ключа
ПК может состоять из нескольких полей (составной ключ)
суррогатные ключи

- объектно-ориентированнные
- графовые БД
когда мы работаем с внешним риугкам

"""

import sqlite3

# рабоать
db = sqlite3.connect(':memmoey:')

#db = seulitre

sql="""
    CREATE TABLE IF NOT EXIST student_group (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        active TYNYINT NOT NULL DEFAULT 0
    );
    """
'''Коммит происходит автоматически только если контекстный менеджер,
а так у курсора есть метод'''
    """если исп в качестве ключа беззнаковое.
    ВЙ
какой то интерфай
    указать значение по умол, а ЗА/М ч\л\нулл

    cjplftv eybrfkmysq bljytnthbrfnjh
    когда талхба==сука писать\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


"""
# создаем объект курсора
cursor = db.cursot()

# третий шаг выполняем запросы пачткой
cursor.executescript(sql)

# выполнение

db.close()

"""
Запросы бывают двух видов:
1_ запросы на изменение данных и структур
    insert, update, delete, create table
    все кроме select
2_ запросы на выборку данных
    select
обычено такие запросы возвращают количество затронутых строк

когда не нужно получать результат?

если будет ошибка то
'""""'
# Запрос на вставку данных

sql = '''
    INSERT INTO student_group (title) VALUES (?)
'''
# sql инъекции подготовленные выражения (?)
# НЕНУЖНО ТАК СОЗДАВАТЬ КОРТЕЖИ! это строка в скобках
cursor.execute(sql, ('Python',))
cursor.execute(sql, ('PHP',))

# Запрос на выборку данных
sql = '''
    SELECT id, title, active FROM student_group
'''
# Если запрос на выборку данных (SELECT), то
# выбранные данные получаем из курсора

cursor.execute(sql)
# Получем все данные в виде списка кортежей
print(cursor.fetchall())

# Получаем данные построчно
print(cursor.fetchone())

db.close()
# закрываем соединение

"""
1) подключаемся
2) создадим курсор
3) select
4) феч
5) закрываем соединение
"""

'''with sqlite3.connect(':memory:') as conn:
    conn.execute(sql) # create table

    cursor = conn.execute(sql) # select
    #print(cursor.fetchall())'''

# Работа с исключениями
# любая ошибка - исключительная ситуация
# например хочу получить группу из базы, если группы нет, то нан или ошибка?
# а если ошибка в синтаксисе, то нужно выкинуть ошибку

# фиксить ошибку нужно с конца

try:
    n = int(input())
    import mo_dul
except ValueError:
    print('Error')
finally:
    print("выполняется всегда")

try:
    conn = sqlite3.connect(':memory:')
    # выполняем запросы
finally:
    conn.close()
# эту конструкцию заменяет контекстный менеджер


"""Удаление таблиц
DELETE FROM table WHERE pk=?
DELETE FROM table WHERE id_prod=? AND id_cost=?
DELETE FROM table WHERE id_prod=? OR id_cost=?
DELETE FROM table WHERE id_prod=? IN id_cost=?
DELETE FROM table WHERE id_prod=? NOT id_cost=?
Логика работает

быть очень остарожным с удалением. первичный ключ = ?
нет никаких предупреждений

"""
