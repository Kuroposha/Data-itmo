# Функции
# Линейный и функциональный подход к программированию

def Hello():
    # тело функции
    print('Hello, Python!')
    # pass

func = Hello # ссылка на функцию в переменную

Hello() # вызов функции
func() # вызов через ссылку в переменной

# Зачем функции аргументы? Чтобы передать аргументы

def hello_2(name):
    # print('Hello'+name)
    # правильно через Шаблон
    print('Hello, {}!'.format(name)) # вызов метода

# Как передавать аргументы?
# Даа способа:
# - по значению (копия)
# - по ссылке

def parse(src, output):
    # src - str
    #output - list
    src = src.strip('.')
    # метод стрип позволяет нам отрезать любое кол-во точек с нач или кон

    for i in src.split('*'):
        # метод сплит позволят резать по пробелам, или другим заданым символам
        output.append(i)
        # добавляет i

s = 'Python*is*a*programming*language'
lst = []
parse(s, lst)
print(s)
print(lst)
# любой тип данных не изм перед как ссылка, а любой изм тип передается как копия
# Позиционные аргументы
# Как задать аргументу значение по умолчанию? Чтобы вызывать ее с мин кол-вом
#аргументов
# Функция должна решать одну задачу
# максимум 6-8 аругментов в функции
    #как вернуть значение из функции
def powpow(num, qw=2): #Пеп 8 осуждает пробелы????
    #значения по ум должны быть конст.
    # обязат арг, арг по ум
    return num ** qw #, можно вернуть кортеж если просто через зпт перечислить
# возвращать можно даже ссылку на др функцию
print(powpow(2))
print(powpow(4, 3))

def tst_1(a, b):
    return b, a

a = 2
b = 5

a, b = tst_1(a, b)

# Именованные аргументы

print(powpow(qw=3, num=9))

# Переменное количество аргументов
# название функции - глагол

def summa(*args):
    # *args - tuple
    return sum(args)
def tst_2(*args, **kwargs):
    print(type(args), args) #tuple
    print(type(kwargs), kwargs) #dict


print(summa(1, 2))
print(summa(1, 2, 3, 4))
print(summa())

tst_2(1, 2, 3, a=1, b=3, c=5)

args = (10, 11, 12)
kwargs = {'d': 20, 'r': 50}

tst_2(*args, **kwargs)#key-ward-arguments
# количество элементов, разворачиваемых из списка или кортежа в функ
# должно совпадать с поз аргументами
# смешивать арг с поз и арг с им нельзя

# Замыкания

def trim(chars=None): #Функция каррирования
    # замкнутая область видимости
    def funk_in(sts):
        return sts.strip(chars)
    return funk_in

spaces_trim = trim()
slashes_trim = trim('\\/|')

print(spaces_trim)
print(spaces_trim("         username         "))

print(slashes_trim)
print(slashes_trim('///////lasts|'))
# Анонимная функция ( без имени, лямбда функция)
"""
sqrt = lambda x : x ** 0.5 #присвоение люмбда функции в переменную осуждается пепом
x = 9
print('Корень числа {} = {}'.format((x, sqrt(x)))) # ERORR!!!!!
ERORR
ls = (list(filter(lambda e: e % 2, ls))
ls = list(map(lambda e: e ** 2, ls))
ERORR
print(lst)
"""

# Рекурсивная функция
# Прямая рекурсия
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

print(factorial(5))

# The most danger type of requ
"""
Косвенная рекурсия

def a():
    b()

def b():
    a()
"""

"""
 Облости видимости переменных и время их жизни
1) Глобальная область видимости
- все кроме функций и классов
 - пока работает скрипт
  - получаем доступ из любой области видимости
   - это ЗЛО
2) Локальная область видимости
- функции, классы, лок пер
 - пока работает функ, класс
  - доступ только внутри класса, функции
   - добро
"""

glob = 666

def func_666():
    #global glob
    glob = 777
    print(glob)

func_666()
print(glob)


def wrapper():
    external = 777

    def funk_666():
        global glob
        nonlocal external # only Py3

        glob = 777
        external = 888

    funk_666()

    print(external, glob)

wrapper()


# Процедурная функция? 
