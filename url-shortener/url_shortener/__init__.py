"""
Обработчики и меню

соглашение о наименовании! привести все фанкции к общему виду

программу нужно завершать корректно, поэтому под свою прогу нужно обозначить
свои коды завершения(указания ошибок)
"""
import sys

from url_shortener import storage

get_connection = lambda: storage.connect('shortener.sqlite')

def action_add():
    """Добавить URL-адрес"""
    url = input('\nВведите URL-адрес: ')

    with get_connection() as conn:
        short_url = storage.add_url(conn, url)

    print('Короткий URL-адрес: {}'.format(short_url))

def action_find():
    """Найти оригинальный URL-адрес"""


def action_find_all():
    """Вывести все URL-адреса"""


def action_show_menu():
    """ Показать меню. """
    print('''
1. Добавить URL-адрес
2. Найти оригинальный URL-адрес
3. Вывести все URL-адреса
m. Показать меню
q. Выход
''')


def action_exit():
    """Выход"""
    sys.exit(0)# 0 - отсутствие ошибок


def main():
    with get_connection() as conn:
        storage.initialize(conn)

    # подключение к бд
    actions = {
        '1': action_add,
        '2': action_find,
        '3': action_find_all,
        'm': action_show_menu,
        'q': action_exit,
    }

    action_show_menu()

    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            try:
                action()
            except Exception as e:
                print(e)
        else:
            print('Не известная команда')
