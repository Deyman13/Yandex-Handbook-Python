"""
permutations(iterable, r) — возвращает итератор, значениями которого являются перестановки без повторений из 
элементов итерируемого объекта iterable. Если значение r не задано, элементы итератора имеют ту же длину, что 
и iterable. Иначе длина равна r. Пример:
"""

from itertools import permutations

values = list(permutations("АБВ"))
print(values)

# [('А', 'Б', 'В'), ('А', 'В', 'Б'), ('Б', 'А', 'В'), ('Б', 'В', 'А'), ('В', 'А', 'Б'), ('В', 'Б', 'А')]

from itertools import permutations

values = list(permutations("АБВ", 2))
print(values)

# [('А', 'Б'), ('А', 'В'), ('Б', 'А'), ('Б', 'В'), ('В', 'А'), ('В', 'Б')]
