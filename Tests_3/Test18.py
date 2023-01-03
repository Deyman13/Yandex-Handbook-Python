"""
Простая задача 2.0
В банке решили переписать программу для шифрования данных и попросили, чтобы вы взяли на себя часть данной задачи. 
Напишите программу для разложения числа на простые множители. Только внимательно, ведь работать придётся вновь с простыми числами.

Формат ввода
Вводится одно натуральное число.

Формат вывода
Требуется составить математическое выражение — произведение простых неубывающих чисел, которое в результате даёт исходное.

Ввод:
120

Вывод:
2 * 2 * 2 * 3 * 5
"""

def factors(number, d=2):
    while number > 1:
        n1, n2 = divmod(number, d)
        if n2:
            d += 1
        else:
            yield d
            number = n1

n = int(input())
print('{}' .format(' * '.join(map(str, factors(n)))))
