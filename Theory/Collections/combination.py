"""
combinations(iterable, r) — возвращает итератор, значениями которого выступают сочетания (без повторений) 
длиной r элементов итерируемого объекта iterable. Пример:
"""

from itertools import combinations

values = list(combinations("АБВ", 2))
print(values)

# [('А', 'Б'), ('А', 'В'), ('Б', 'В')]

"""
combinations_with_replacement(iterable, r) — возвращает итератор, значениями которого выступают сочетания 
(с повторениями) длиной r элементов итерируемого объекта iterable. Пример:
"""

from itertools import combinations_with_replacement

values = list(combinations_with_replacement("АБВ", 2))
print(values)

# [('А', 'А'), ('А', 'Б'), ('А', 'В'), ('Б', 'Б'), ('Б', 'В'), ('В', 'В')]
