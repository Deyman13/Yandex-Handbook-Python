"""
Шахматный «обед»

Напишите функцию can_eat, которая принимает положение коня и другой фигуры в виде кортежей из двух координат, 
а возвращает булево значение: True если конь съедает фигуру и False иначе.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод:
result = can_eat((2, 1), (4, 2))

Вывод:
result = True
"""

def can_eat(knight_pos, figure_pos):
    x1, y1 = knight_pos
    x2, y2 = figure_pos

    # Конь может съесть фигуру только если она расположена в одном из 8 возможных полей
    return abs(x1 - x2) == 2 and abs(y1 - y2) == 1 or abs(x1 - x2) == 1 and abs(y1 - y2) == 2