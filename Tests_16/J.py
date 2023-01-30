"""
Лесенка

Напишите функцию stairs, принимающую вектор и возвращающую матрицу, в которой каждая строка является 
копией вектора со смещением.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод:
print(stairs(np.arange(3)))

Вывод:
[[0 1 2]
 [2 0 1]
 [1 2 0]]
"""

import numpy as np


def stairs(vector):
    length = len(vector)
    matrix = np.zeros((length, length), dtype=int)
    for i in range(length):
        matrix[i, :] = np.roll(vector, i)
    return matrix