"""
НЕ РЕШЕНА ПРАВИЛЬНО!!!

Числовой квадрат
К сожалению, и змейки детям надоели, поэтому воспитательнице нужна новая программа. 
Напишите программу, которая строит числовой квадрат требуемого размера.

Формат ввода
В первой строке записано число N — высота и ширина числового квадрата.

Формат вывода
Требуется вывести сформированный числовой квадрат требуемого размера.
Чтобы квадрат был красивым, каждый его столбец — одинаковой ширины.

Ввод:
5

Вывод:
1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1
"""

number = int(input())
for i in range(number):
    for j in range(number):
        if j == 0 or j == number - 1 or i == 0 or i == number - 1:
            print(1, end=" ")
        elif j > 1 and i > 1 and j < number - 2 and i < number - 2:
            print(3, end=" ")
        else: 
            print(2, end=" ")     
    print()

    

