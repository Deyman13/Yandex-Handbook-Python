"""
Потоковый НОД

Напишите программу, находящую наибольшие общие делители для всех переданных в стандартный поток 
последовательностей чисел.

Формат ввода
Вводятся строки чисел, разделённых пробелами.

Формат вывода
Последовательность чисел — наибольшие общие делители всех последовательностей.

Ввод:
2 1000 20 34
36 12
3 96 12
6
7 8 9 10

Вывод:
2
12
3
6
1
"""
from math import gcd
from sys import stdin

lines = [list(map(int, line.rstrip("\n").split())) for line in stdin]

for i in [j for j in lines]:
    print(gcd(*i))