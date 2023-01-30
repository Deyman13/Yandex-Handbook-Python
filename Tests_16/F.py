"""
Матрица умножения

Напишите функцию multiplication_matrix, которая принимает размер матрицы (N) и 
возвращает массив описывающий таблицу умножения N на N.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод:
print(multiplication_matrix(3))

Вывод:
[[1 2 3]
 [2 4 6]
 [3 6 9]]
"""

import numpy as np


def multiplication_matrix(n):
    return np.array([[(i + 1) * (j + 1) for j in range(n)] for i in range(n)])
