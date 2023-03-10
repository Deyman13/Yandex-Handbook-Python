"""
Шахматная подготовка

Представьте, что вы пишете компьютерную игру «Шахматы». Вам надо смоделировать шахматную доску, 
которая представляет собой матрицу. Чёрная клетка представляется нулём, а белая — единицей. 
Если смотреть на доску сверху, то левая верхняя клетка — белая.

Напишите функцию make_board, которая принимает размер шахматной доски, и возвращает матрицу, моделирующую заданную доску.

Установите тип элементов матрицы int8.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод:
print(make_board(4))

Вывод:
[[1 0 1 0]
 [0 1 0 1]
 [1 0 1 0]
 [0 1 0 1]]
"""

import numpy as np


def make_board(n: int):
    return np.array([[not (i + j) % 2 for i in range(n)] for j in range(n)], dtype=np.int8)

