"""
Циклический генератор

Напишите генератор cycle, который принимает список и работает аналогично итератору itertools.cycle.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод:
print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))

Вывод:
1 2 3 1 2
"""

def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element

print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))
