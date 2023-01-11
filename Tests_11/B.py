"""
Генератор матриц

Напишите функцию make_matrix, которая создаёт, заполняет и возвращает матрицу заданного размера.

Параметры функции:

size — кортеж (ширина, высота) или одно число (для создания квадратной матрицы);
value — значение элементов списка (по-умолчанию 0).
Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод
result = make_matrix(3)
Вывод
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
"""

# 1 вариант
def make_matrix(size, value=0):
    if isinstance(size, int):
        size = (size, size)
    return [[value] * size[0] for i in range(size[1])]


# 2 вариант
def make_matrix(size, value=0):
    result_matrix = []
    if isinstance(size, int):
        size = (size, size)
    for i in range(size[0]):
        result_matrix.append([value] * size[1])
    return result_matrix



