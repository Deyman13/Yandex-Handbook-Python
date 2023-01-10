"""
A+B+...

Наконец-то мы можем обрабатывать данные, не имея ни малейшего понятия об их количестве.

Напишите программу, которая находит сумму всех чисел введённых пользователем.

Формат ввода
Вводятся строки чисел.

Формат вывода
Одно число — сумма всех чисел в потоке ввода.

Ввод:
1 2
3 4 5
6
7 8 9 10

Вывод:
55
"""

# 1 вариант
from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip(" \n"))

summa = 0
for string in lines:
    numbers = list(map(int, string.split()))
    for num in numbers:
        summa += num
print(summa)


# 2 вариант
sum = 0
while True:
    try:
        numbers = input().split()
        for num in numbers:
            sum += int(num)
    except EOFError:
        break
print(sum)
