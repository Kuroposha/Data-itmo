"""
name*            - имя пакета (продукта)
version*         - версия пакета определение версии
description      - краткое описание пакета
long_description - полное описание
url              - веб сайт (например гит)
license*         - лицензия / при создании нового пакета лучше изучить и позаботиться
                   о лицензии
author           - имя автора
author_email     - мыло автора
packeges         - пакеты, которые нужно скопировать без рекурсии!
py_modules       - модули, которые нужно скопировать
instull_requires - Прямые зависимости пакета от других пакетов
                   (вплоть до версии)
scripts          - Запускаемые из КС скрипты #centry_points
это основное
"""

from setuptools import setuptools #, find_packeges
setup(
    name='mega-math',
    version='1.0.0',
    description='Collection of mathematical formula'
    license='Apache 2.0'
    author='Kuroposha'
    author_email='xany@gm.r'
    packeges=['mega-math']

)
