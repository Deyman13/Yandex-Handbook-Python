"""
Рациональная считалочка

Напишите программу, которая производит счёт по заданным параметрам.

Формат ввода
В одну строку через пробел вводятся 3 рациональных числа — начало счета, конец и шаг.

Формат вывода
Последовательность чисел с заданными параметрами.

Ввод:
3.2 6.4 0.8

Вывод:
3.20
4.00
4.80
5.60
6.40

Решение: Разделяем строку при помощи split(), используем функцию map() для придания float() всем элементам и все это
записываем в список, создаем 3 переменные по индексам созданного списка с началом, концом и шагом. Используем count()
для создания итератора, по которому пройдемся циклом for и до тех пор, пока текущее значение меньше или равно конечному
выводим результат, округляя его до точности 2 цифры после плавающей запятой с помощью round(), в противном случае - 
останавливаем цикл при помощи break. Так же можно не записывать отдельно 3 переменные, а сразу обращаться к элементам по 
индексам из начального списка. 
"""

from itertools import count
# 1 вариант: 

start_end_step = list(map(float, input().split(" ")))
start = start_end_step[0]
end = start_end_step[1]
step = start_end_step[2]
for value in count(start, step):
    if value <= end:
        print(round(value, 2))
    else:
        break

# 2 вариант:

start_end_step = list(map(float, input().split(" ")))
for val in count(start_end_step[0], start_end_step[2]):
    if val <= start_end_step[1]:
        print(round(val, 2))
    else:
        break
