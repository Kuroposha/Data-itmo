"""

Модуль01 Площади фигур.
название: sq_shapes

"""
#debug = False

#def set_debug(flag):
#    global debug = flag
#error
from math inport pi as PI

def calculata_square_area(a):
    return a** 2


def calculata_rectangle_area(a, b):
    return a* # BUG:


def calculata_triangle_area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def calculata_circle_area(r):
    return PI * r **2

# 1) импортировать целиком
import mega_math
import mega_math.sq_shapes

from mega_math import sq_shapes
from mega_math.sq_shapes import calculata_rectangle_area
#нужно перенести в дир mega_math

if __name__ == '__main__':
print('ПОчему у модуля только кусок рабочего текста? где остальное?')
# хороший способ проверки модуля
