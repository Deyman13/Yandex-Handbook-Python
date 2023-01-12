"""
Сортировка слиянием

Мы уже реализовывали функцию merge, которая способна "слить" два отсортированных списка в один.
Чаще всего её применяют в рекурсивном алгоритме сортировки слиянием.

Напишите рекурсивную функцию merge_sort, которая производит сортировку списка.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
Трассировка вызова рекурсивной функции в обработке ответа не учитывается и показан для примера.

Ввод:
result = merge_sort([3, 2, 1])

Вывод:
# Вызов merge_sort([3, 2, 1])
# Вызов merge_sort([3])
# Вызов merge_sort([2, 1])
# Вызов merge_sort([2])
# Вызов merge_sort([1])
result = [1, 2, 3]
"""

def merge_sort(arr):
    def merge(tuple1, tuple2):
        result = []
        i = 0
        j = 0
        while i < len(tuple1) and j < len(tuple2):
            if tuple1[i] < tuple2[j]:
                result.append(tuple1[i])
                i += 1
            else:
                result.append(tuple2[j])
                j += 1
        result.extend(tuple1[i:])
        result.extend(tuple2[j:])
        return result
    
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


result = merge_sort([3, 1, 5, 3])
print(result)
