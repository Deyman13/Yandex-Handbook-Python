"""
А роза упала на лапу Азора 4.0

Вернёмся к палиндромам — числам, словам и предложениям, которые читаются одинаково в оба направления.
Напишите программу, которая определяет, относится ли введённая строка к палиндромам.

Формат ввода
Вводится строка.

Формат вывода
Требуется вывести YES — если введенная строка является палиндромом, иначе – NO.

Ввод:
мама

Вывод:
NO
"""

string = input()
rev = reversed(string)
if list(string) == list(rev):
    print("YES")
else:
    print("NO")