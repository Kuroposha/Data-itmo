import os.path as Path
import sqlite3
# можно поменять на другое хранилище
from .converter import convert, inverse

# Все SQL завпросы лучше всего вводить в виде констант,
#а также определить, где будут лежать эти запросы



SQL_SELECT_ALL = '''
    SELECT
        id, original_url, short_url, created
    FROM
        shortener
'''
SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'

SQL_SELECT_URL_BY_ORIGIN = SQL_SELECT_ALL + ' WHERE original_url=?'
# не использовать форма или процент! разобраться с вере и вопросиком

SQL_INSERT_URL = '''
    INSERT INTO shortener (original_url) VALUES (?)
'''

SQL_UPDATE_SHORT_URL = '''
    UPDATE shortener SET short_url=? WHERE id=?
'''
# Если пропустить WHERE можно потереть данные во всей таблице

def dickt_factory(cursor, row):
    d = {}

    print(cursor.description)
    print(row)

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d

def connect(db_name=None):
    """Устанавливает соединение с БД """
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dickt_factory

    return conn


def initialize(conn, creation_script=None):
    """Инициализирует структуру БД """
    if creation_script is None:
        creation_script = Path.join(Path.dirname(__file__),\
                          'resourses', 'schema.sql')# позволяет склеивать пути
                          #с разделителем тек сисит
        # возвращает род. кат из файла
    with conn, open(creation_script) as f:
        #если ресурс не создан в КМ, то КМ не закрывает этот ресурс
        conn.executescript(f.read())

def add_url(conn, url, domain=''):
    """Добавляет УРЛ адрес в БД"""
    #делаем урл адрес однозначным
    #/post
    #/post/
    url = url.rstrip('/')
    #/post/ => /post

    # нужна конфигурация и нужны валидаторы
    if not url:
        raise RuntimeErroe('URL can not be empty.')

    with conn:
        found = find_url_by_origin(conn, url)

        if found:
            return found.get('short_url')

        cursior = conn.execute(SQL_INSERT_URL, (url,))

        pk = cursior.lastrowid
# lastrowid содержит последний набранный идентификатор в последней таблице
        short_url = '{}/{}'.format(domain.strip('/'), convert(pk))
# на месте пк появится конверт в нашу СС

        conn.execute(SQL_UPDATE_SHORT_URL, (short_url, pk))

    return short_url

def find_url_by_origin(conn, url):
    """Найти короткий урл по оригинальному"""
    url = url.rstrip('/')

    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_ORIGIN, (url,))
        return cursor.fetchone()


def find_all(conn):
    """НАйти все адреса в БД"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()
        #return conn.execute(SQL_SELECT_ALL).fetchall

def find_url_by_pk (conn, pk):
    """Найти УРЛ по первичному ключу"""
    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_PK(pk,))
        return cursor.fetchall()

def find_url_by_short(conn, short_url):
    """Найти оригинальный урл по короткому"""
    short_url = short_url.rsplit('/', 1).pop()
    #получим список с одним эл-том, всегда когда режем сплитом, получаем 1 элт
    # регулярные выражения
    pk = invers(short_url)
    return find_url_by_pk(conn, pk)
# работает не до конца правильно. сравнить с оригинальным кодом
