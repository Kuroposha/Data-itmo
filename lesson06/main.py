# Ввод и вывод. Формат данных

"""
1. Стандартные потоки
    №0 - stdin - стандартный поток ввода
        input()
        sys.stdin

    №1 - stdout - стандартный поток вывода
        print()
        sys.stdout

    №2 - stderr  - стандартный поток ошибок
        ошибки интерпритатора
        sys.stderr

        *sys - байтовые строки

"""

'''
2. Файловый ввод и вывод
Низкоуровневая функция(путь к файлу+имя файла+расширение[, режим]) -
* []  - необязательный аргумент
open(filename[, mode])

Какие бывают именя файлов (пути)?
-- Абсолютные (/home/itmo/1.txt) - быстро, без ошибок
-- Относительные (1.txt, itmo/1.txt, ../) -

При работе с файлами, у питона нет проблем по переходам,
главное чтоб были права

Как открыть файл в режиме записи?
w - открывает файл в режиме записи, если ф не сущ, то создается. если сущ,
    то перезаписывает, без предупреждения, что ф есть.
a - (append) дозапись в конец. если ф не сущ - создается. если сущ - запись
    в конец
x - эксклюзивное создание файла. Откр в реж запи, если не сущ - созд,
    если сущ, то будет ошибка. (исключение, а это дорого)

Как блокируются файлы, при перезаписях?

Как открыть файл в режиме чтения?
r          - режим по-умолчанию
w+, a+, x+ - файл будет открыт в реж записи, но с возм чтения.

Виды файлов:
- Текстовые
- Бинарные (двоичные)

Для работы с Бинарными файлами к режимам нужно добавлять b.
open('1.mp3', 'rb')
t - текстовый режим (по-умолчанию).

U (obsolete) универсальный режим переноса строк.

    '''

f = open('out.txt', 'w')
f.write('01234') # все что пишется в файл должно быть строкой
f.write('56789') # Дескриптор открытого файла - работа с вн. ресурсом
f.close()#'out.txt') # Открытое - закрыть
# в файле будет одна строка 0123456789, если нам нужен перенос строки,
#то его нужно явно указать - например \n

f = open('out.txt', 'w')
f.write('Привет')
f.write('01234\n')
f.write('\t56789') # Дескриптор открытого файла - работа с вн. ресурсом
f.writelines(['AB', 'CD'])# принимает список срок, и лепит их в одну строку
f.close()#'out.txt') # Открытое - закрыть


f = open('out.txt') # == open('out.txt', 'r')
print('Прочитать файл в строку:\n{}'.format(
    f.read()
))
f.seek(0) # смещение на 0 байт, те в начало файла
print('Прочитать файл в список:\n{}'.format(
    f.readlines() # построчно читате файл - список строк на выходе
))# стрипнуть каждый эл-т
f.seek(0)
print('Прочитать файл построчно:\n{}'.format(
    f.readline()#каждый ридлайн - одна следующ стркоа
))
# чтобы прочитать файл построчно в цикле нужно
for line in f:
    print(line)

f.seek(0)
print('Прочитать из файла N байтов:\n{}'.format(
    f.read(4)
)) # кирилица во втором питоне весит по 2 байта
print('Как получить позицию курсора:\n{}'.format(
    f.tell()
))
f.close()
