"""
Числовая змейка
Увы, обыкновенные прямоугольники детям быстро наскучили. Теперь воспитательнице требуется новая программа. 
Напишите программу, которая строит числовую змейку требуемого размера.

Формат ввода
В первой строке записано число N — высота числового прямоугольника.
Во второй строке указано число M — ширина числового прямоугольника.

Формат вывода
Нужно вывести сформированную числовую змейку требуемого размера.
Чтобы прямоугольник был красивым, каждый его столбец следует сделать одинаковой ширины.

Ввод:
4
6

Вывод:
 1  2  3  4  5  6
12 11 10  9  8  7
13 14 15 16 17 18
24 23 22 21 20 19
"""

height = int(input())
width = int(input())
temp = 1
for i in range(1, height + 1):
    for j in range(width):
        if i % 2 == 1:
            if height * width < 10:
                print("{:1}".format(temp), end=" ")
            elif height * width > 10 and height * width < 100:
                print("{:2}".format(temp), end=" ")
            else:
                print("{:3}".format(temp), end=" ")
            if j < width - 1:
                temp += 1
        elif i % 2 == 0:
            if height * width < 10:
                print("{:1}".format(temp), end=" ")
            elif height * width > 10 and height * width < 100:
                print("{:2}".format(temp), end=" ")
            else:
                print("{:3}".format(temp), end=" ")
            if j < width - 1:
                temp -= 1
    temp += width
    print()
