"""
Лекция 5. Модули, пакеты, дистрибуция пакетов(распространение)

Модуль - это обычный файл-Python

Названия для модуля имеют теже ограничения, что и остальные в пай
Регистр!

- Исполняемый (запускаемый / главный) модуль также называется MAIN
"""
#-- КАк импортировать модуль? --

#1. Испортировать целиком ( весь сразу)
#inpost mod.submod,subsu  вариант импорта
# submod.fun
import sq_shapes
#имп. одно имя. точка - доступ к именам в модуле, и лать имя этой фукци

# 2. Частичный импорт
from sq_shapes import calculata_triangle_area, calculata_circle_area
# импортируем только нужные нам имена.. в режиме рид онли
print(sq_shapes.calculata_triangle_area(3, 6, 12))
print(sq_shapes.calculata_square_area(5))

# 3. Импорт из модуля всех имен в текущий модуль
from sq_shapes import *
__all__ = (
    'calculata_circle_area',
    'calculata_square_area',
    'calculata_triangle_area',
    'calculata_rectangle_area'
)
# Звездочка - это плохо, но это позволять залить все, что есть
# можно прописать

# Константы формиркодом, у н коф\нфликт по делам

#print(sq_shapes.debug.defg)error
sq_shapes.debug = True
print(genus)
print(sq_shapes.debug)
# вывод переменной окружения
#наш проект - python.path -sys.path линия поиска метода
# область видимости модуля - в модуле могут быть глоб пре, а в проге будут лок.
# можно юзать одинаковые имена в разных модулях
"""
Плюсы модулей:
1) модули компилируются пайтоном .pyc
2) для ускорения проги лучше убирать все лишнее из мейн. пай (некомп файлы)
3) pyc' и можно отдать вместо исх кода
4) в момент вызова интерпритатора мы можем передать ему нек доп аргументы
 -O оптимизированные пик файлы
-OO убирает все комментарии, и оптимизирует код
5) он загружается только один раз (импортируется), но это можно фиксить
6) Пай может искать модули в тек дир и ниже, но не выше

"""