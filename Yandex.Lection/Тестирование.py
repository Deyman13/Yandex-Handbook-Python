# Что нужно тестировать?
# 1) Тесты из условия
# 2) Общие случаи
# 3) Особые случаи

# Максимум последовательности
# 1 2 3 - максимум по краю (могут быть проблемы с индексами, поэтому стоит проверить крайние максимумы)
# 3 2 1 - максимум по краю
# 2 3 1 - общий случай (обычная ситуация, проверка работоспособности кода вообще)
# 1 1 1 - все элементы одинаковые (будет ли работать программа с одинаковыми максимумами)
# 1 - всего 1 элемент, на 1 элементе очень часто все ломается (может не зайти в какой либо из циклов и т.п.)
#   - пустая строка (могут быть большие проблемы)
# -1 -2 -3 - все отрицательные числа (код может работать например только хотя бы с 1 положительным)

# Покрытие тестами 
# Задача: даны три целых числа a, b, c
# Найдите все корни уравнения ax2 + bx + c = 0 и выведите их в порядке возрастания.
import math
a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
x1 = (-b - math.sqrt(D)) / (2 * a)
x2 = (-b + math.sqrt(D)) / (2 * a)
print(x1, x2)
# Но ответ не верен, выдает при 1 2 1 вывод = -1.0 -1.0, а должен выдавать -1.0 

# Исправляем код
import math
a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if D == 0:
    x1 = -b / (2 * a)
    print(x1)
else:
    x1 = (-b - math.sqrt(D)) / (2 * a)
    x2 = (-b + math.sqrt(D)) / (2 * a)
    print(x1, x2)
# Теперь выдает правильно, при 1 2 1 вывод = -1.0, но при 1 1 1 выдает Runtime Error

# Исправляем код
import math
a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if D == 0:
    x1 = -b / (2 * a)
    print(x1)
elif D > 0:
    x1 = (-b - math.sqrt(D)) / (2 * a)
    x2 = (-b + math.sqrt(D)) / (2 * a)
    print(x1, x2)
# Теперь в случае если D будет меньше 0, то ничего не выведется, а если больше или равно, то выведется определенный результат
# Но теперь, если ввести 0 1 1, выведет Runtime Error, а должен вывести - 1

# Модифицируем код
import math
a = float(input())
b = float(input())
c = float(input())
if a == 0: # Добавили условие, если a = 0, то сразу выводим -c / b
    print(-c / b)
else:
    D = b ** 2 - 4 * a * c
    if D == 0:
        x1 = -b / (2 * a)
        print(x1)
    elif D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print(x1, x2)
# Но даже так, при вводе 0 0 1 программа не работает, так как если b = 0, делить на 0 нельзя, выдает ошибку. 

# Модифицируем код
import math
a = float(input())
b = float(input())
c = float(input())
if a == 0:
    if b != 0: # Исправили, что если б не равно 0, то используем формулу, иначе ничего не выведем. 
        print(-c / b)
else:
    D = b ** 2 - 4 * a * c
    if D == 0:
        x1 = -b / (2 * a)
        print(x1)
    elif D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print(x1, x2)
# Теперь работает при условии 0 0 1, но при условии ввода 0 0 0, ничего не выведет, хотя должен быть ответ: Бесконечное решение

# Модифицируем код
import math
a = float(input())
b = float(input())
c = float(input())
if a == 0:
    if b != 0: 
        print(-c / b)
    if c == 0 and b == 0:
        print("Infinite number of solution")
else:
    D = b ** 2 - 4 * a * c
    if D == 0:
        x1 = -b / (2 * a)
        print(x1)
    elif D > 0: 
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print(x1, x2)
# Теперь работает и при условии 0 0 0, но теперь если ввести -5 4 1, выдаст ответ 1.0, -0.2, а должен -0.2 1.0
# Так как выводить мы должны по возрастанию, и этот момент не учли
# Если a - отрицательное число, то при выводе x1, x2 маленькое число превращается в большое и наоборот. 

# Модифицируем код
import math
a = float(input())
b = float(input())
c = float(input())
if a == 0:
    if b != 0: 
        print(-c / b)
    if c == 0 and b == 0:
        print("Infinite number of solution")
else:
    D = b ** 2 - 4 * a * c
    if D == 0:
        x1 = -b / (2 * a)
        print(x1)
    elif D > 0: 
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        if x1 < x2: # Теперь если корни стоят в обратном порядке, они выведутся правильно. 
            print(x1, x2)
        else:
            print(x2, x1)

# Поиск самого частого символа
s = input() 
answer = "" 
counter = 0 
dct = {} 
for now in s:
    if now not in dct: 
        dct[now] = 0 
    dct[now] += 1 
for key in dct:
    if dct[key] > counter:
        answer = key
print(answer)
# Ошибка в том, что мы не добавили шаг к counter (не указали лучший результат)

# Исправляем ошибку
s = input() 
answer = "" 
counter = 0 
dct = {} 
for now in s:
    if now not in dct: 
        dct[now] = 0 
    dct[now] += 1 
for key in dct:
    if dct[key] > counter:
        counter = dct[key]
        answer = key
print(answer)
# Теперь все работает отлично

