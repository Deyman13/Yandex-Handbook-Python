"""
Таблица истинности
Вся современная электронно-вычислительная техника строится на Булевой алгебре, которая оперирует истинностью и 
ложностью высказываний. Любой язык программирования содержит логические операции (в Python это and, or, not).

Чаще всего для работы со сложными высказываниями прибегают к методу под названием «Таблица истинности».
Суть метода проста — рассматриваются все возможные значения входных переменных и для них вычисляется результат.

Разработайте программу, которая для введённого сложного логического высказывания строит таблицу истинности.

Формат ввода
Вводится логическое выражение от трех переменных (a, b, c) валидное для языка Python.

Формат вывода
Выведите таблицу истинности данного выражения.

Примечание
Для выполнения Python кода, записанного в строках, существуют две замечательные функции: exec и eval.

Ввод:
not a or b and c

Вывод:
a b c f
0 0 0 1
0 0 1 1
0 1 0 1
0 1 1 1
1 0 0 0
1 0 1 0
1 1 0 0
1 1 1 1
"""

result = input().split()
print(f'a b c f')
for n in range(0, 8):
    num = bin(n)
    num = num.replace('b', '0')
    a = int(num[-3])
    b = int(num[-2])
    c = int(num[-1])
    f = 1 if eval(" ".join(result)) else 0
    print(f'{a} {b} {c} {f}')





