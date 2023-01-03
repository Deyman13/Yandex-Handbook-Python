"""
Простая задача 3.0
Вспомним, что простые числа — те натуральные числа, у которых два делителя: оно само и 1.
Напишите программу для определения количества простых чисел среди введённых.

Формат ввода
В первой строке записано число N Во всех последующих N строках — по одному числу.

Формат вывода
Требуется вывести общее количество простых чисел среди введённых (кроме N).

Ввод:
5
1
2
3
4
5

Вывод:
3
"""

number = int(input())
counter = 0


def is_prime(temp):
    if temp < 2:
        return False
    for i in range(2, int(temp ** 0.5 + 1)):
        if temp % i == 0:
            return False
    else:
        return True


for i in range(number):
    temp = int(input())
    if is_prime(temp) is True:
        counter += 1
print(counter)
