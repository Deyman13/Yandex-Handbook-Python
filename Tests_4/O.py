"""
Числовая змейка 2.0

Воспитательнице вновь нужна программа, которая будет генерировать змейку из чисел. 
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
 1  8  9 16 17 24
 2  7 10 15 18 23
 3  6 11 14 19 22
 4  5 12 13 20 21
"""

height = int(input())
width = int(input())
temp = 1
step2 = 0
step = height * 2 - 1
for i in range(1, height + 1):
    for j in range(1, width + 1): 
        if j % 2 == 1:
            if j < width + 1:
                if height * width < 10:
                    print("{:1}".format(temp), end=" ")
                elif height * width > 10 and height * width < 100:
                    print("{:2}".format(temp), end=" ")
                else:
                    print("{:3}".format(temp), end=" ")
                temp += step
        else:
            if j < width + 1:
                if height * width < 10:
                    print("{:1}".format(temp), end=" ")
                elif height * width > 10 and height * width < 100:
                    print("{:2}".format(temp), end=" ")
                else:
                    print("{:3}".format(temp), end=" ")
                temp += i + step2
    temp = 1 + i
    step = step - 2
    step2 += 1
    print()




    

            
    
    

    



        
