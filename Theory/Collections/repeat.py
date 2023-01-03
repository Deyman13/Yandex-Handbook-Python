"""
repeat(object, times) — возвращает итератор, повторяющий значение object (по умолчанию бесконечное количество раз 
— либо равно значению times). Напишем программу, которая создаст список из пяти строк ABC и выведет его на экран:
"""

from itertools import repeat

result = list(repeat("ABC", 5))
print(result)

# ['ABC', 'ABC', 'ABC', 'ABC', 'ABC']
