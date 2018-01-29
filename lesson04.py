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

# Переменное количество аргументов

# название функции - глагол

def summa(*args):
    # *args - tuple
    return sum(args)

print(summa(1, 2))
print(summa(1, 2, 3, 4))
print(summa())

# Именованные аргументы
