# Ветвление
a = int(input('A:'))
b = int(input('B:'))

# блоки кода

if a > b:
    print('a > b')
elif a == b:
    print('a = b')
elif True:
    pass # для пустого блока кода
else:
    print('a < b')
    a += 1
    print(a)
""" Условные конструкции неявно приводят типы к логике
Пустое что угодно - ложь, полное что угодно - истина
"""

#Циклы

i = 1

while i <= 10:
    print(i)
    i +=1
p = 1
while p:
    if p ==10:
        break #часто используется
    if p == 5:
        p += 1
        continue# плохая вещь, фу
    p += 1
"""
pi = 1

while (pi <= 10) and ():
    print(i)
    i +=1
"""
# for in
#for i in range(10)

"""
иттератор. можем сгенерировать промежуток, не список, не множество,
а иттерируемый промежуток

Иттераторы и генераторы уйдут на потом
разряженный и неразряженый список
можно создать при помощи ренджа спосок из промежутка
"""
lst = [10, 11, 12 ,13]
for i in enumerate(lst): # объект для распаковки кортежей
# в переменную индекс и значение элемента списка

a = 1
b = "www"
a, b = b, a
# присовение также можно объединять
a, b = 1, 2
a = b = 1

# Срезы
s = "Hello, Python!"
s[0] #H
s[0:5] #Hello == s[:5]
s[7:] #Python == s==[7: 10]
s[::2] #Hlo yhn
s[1::2] #el,pto!
s[::-1]#!nohtyp ,olleH
#! Лучше всего не вставлять константы в код
s[-2:] #n!
# с конца с единицы, с начала от нуля
# ну и все в таком духе

# работая со списками и срезами, моэно создавать полные копии, вместо ссыдлк

# можно резать строки и списки, строки это медленно
# списки гараздо лучше
s  = []
for c in range(10):
    pass
# Методы работы со списком (Таблица методов списка)
"""
Объектаная обертка
функции уже в пн
"""
lst.append(9) #
lst.extend (10)# Расширяет список, добавляя эл-ты в конец списика
lst.insert(0, -1) # вставляет 0 на место -1
lst.remove(9)# удаляет первый найденный элемент
lst.pop[(i)] #удаяляет элемент и возвращает его (стек)
lst.count() # возвращает количество эл-тов со значением x
lst.reverse()#в отличии от среда - лучше, чем срез, потому что меньше
#тратит памяти
lst.copy()
lst.clear()
lst.sort()
len(lst) #длина списка