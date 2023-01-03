"""
Властелин Чисел: Две Башни
Во времена, когда люди верили в великую силу чисел, оказалось, что волшебник Пифуман предал все народы и стал 
помогать Зерону.

Чтобы посетить башни обоих злодеев одновременно, нам следует разделить магию числа, которое защищало нас в дороге.

Чтобы поделить трёхзначное число, нам нужно составить из него минимально и максимально возможные двухзначные числа.

Формат ввода
Одно трёхзначное число.

Формат вывода
Два защитных числа для каждого отряда, записанные через пробел.

Ввод:
103

Вывод:
10 31
"""

number = int(input())
a = number // 10 // 10 % 10
b = number // 10 % 10
c = number % 10
M = [a, b, c]
max_num = max(M)
min_num = min(M)


def secondmax(numbers):
    numbers.remove(max(numbers)) # удаляем максимум прошлый
    max_number = max(numbers) # создаем новый максимум
    return max_number # возвращаем это значение


second_max = secondmax(M)
if (min_num == 0):
    print(f"{second_max}{min_num} {max_num}{second_max}")
else:
    print(f"{min_num}{second_max} {max_num}{second_max}")
