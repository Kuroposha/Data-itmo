"""
Обработчики и меню

соглашение о наименовании! привести все функции к общему виду

программу нужно завершать корректно, поэтому под свою прогу нужно обозначить
свои коды завершения(указания ошибок)

Обработкич, назвагте команды и выводимый текст должны быть в одном месте
"""
from collections import OrderedDict, namedtuple
import sys

from url_shortener import storage

get_connection = lambda: storage.connect('shortener.sqlite')

ACTIONS = OrderedDict()
Action = namedtuple('Action', ('func', 'title'))


def menu_action(cmd, title):
    def decorator(func):
        ACTIONS[cmd] = Action(func, title)
    return decorator
#где враппер? цель - заполнить словарик, менять поведение не нужно, значит враппер нам не нужен.


@menu_action('1', 'Добавить URL-адрес')
def action_add():
    """Добавить URL-адрес"""
    url = input('\nВведите URL-адрес: ')

    with get_connection() as conn:
        short_url = storage.add_url(conn, url)

    print('Короткий URL-адрес: {}'.format(short_url))


@menu_action('2', 'Найти оригинальный URL-адрес')
def action_find():
    """Найти оригинальный URL-адрес"""


#как вытаскивать из заголовка текст
@menu_action('3', 'Вывести все URL-адреса')
def action_find_all():
    """Вывести все URL-адреса"""
    with get_connection() as conn:
        urls = storage.find_all(conn)

        for url in urls:
            # template = '{short_url} - {original_url} - {created}'
            # template.format(short_url=url['short_url'])
            template = '{url[short_url]} - {url[original_url]} - {url[created]}'
            print(template.format(url=url))
            #попробовать строку превратить в даетайм


@menu_action('m', 'Показать меню.')
def action_show_menu():
    """ Показать меню. """
    menu = []

    for cmd, action in actions.items():
        menu.append('{}. {}'.format(cmd, action.title))

    # menu.append('\nВведите команду: ')
    print('\n'.join(menu))


@menu_action('kokoko','ололо')
def action_kokoko():
    print('Пыщь!!!11')


@menu_action('g', 'Выход')
def action_exit():
    """Выход"""
    sys.exit(0)# 0 - отсутствие ошибок


def main():
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()#ругается и говорит что TypeError: 'NoneType' object is not callable
-11
    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            try:
                action.func()
            except Exception as e:
                print(e)
        else:
            print('Не известная команда')
