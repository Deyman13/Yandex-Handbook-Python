"""
Маршрут построен

Навигация была важна во все времена.
Нам достался архив маршрутов движения, но их оказалось так много, что без автоматизации мы с ними не справимся во век. 
Каждый маршрут представляет собой последовательность шагов в одном из четырех направлений: * СЕВЕР; * ВОСТОК; * ЮГ; * ЗАПАД.

Напишите программу, чтобы по заданному маршруту она определяла, в какой именно точке мы окажемся.
Для простоты будем считать, что в начале маршрута мы находимся в точке (0; 0).

Формат ввода
Вводятся инструкции маршрута в виде:
<направление>
<количество шагов>
Ввод завершается строкой СТОП.

Формат вывода
Два целых числа — координаты конечной точки маршрута.

Ввод:
СЕВЕР
2
ВОСТОК
2
СТОП

Вывод:
2
2
"""

direction = input()
stop_word = "СТОП"
coordinate_x = 0
coordinate_y = 0
while direction != stop_word:
    if direction == "СЕВЕР":
        coordinate_y += int(input())
    if direction == "ВОСТОК":
        coordinate_x += int(input())
    if direction == "ЮГ":
        coordinate_y -= int(input())
    if direction == "ЗАПАД":
        coordinate_x -= int(input())
    direction = input()
print(coordinate_y)
print(coordinate_x)
