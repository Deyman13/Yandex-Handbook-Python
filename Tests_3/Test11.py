"""
Цифровая сумма
Иногда требуется манипулировать с цифрами чисел.
Одно из самых простых действий, которое можно совершить — найти сумму цифр числа. Напишите программу, чтобы выполнить это действие.

Формат ввода
Вводится одно натуральное число.

Формат вывода
Требуется вывести одно натуральное число — сумму цифр исходного.

Ввод:
12345

Вывод:
15
"""

num = int(input())
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print(sum)
