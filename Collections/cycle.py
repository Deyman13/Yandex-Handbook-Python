"""
cycle(iterable) — принимает на вход итерируемый объект, а возвращает итератор, который бесконечно циклически 
перебирает значения коллекции. Напишем программу, которая выводит строку длиной 10 символов, циклически перебирая 
символы входной строки ABC:
"""

from itertools import cycle

max_len = 10
s = ""
for letter in cycle("ABC"):
    if len(s) < 10:
        s += letter
    else:
        break
print(s)

# ABCABCABCA
