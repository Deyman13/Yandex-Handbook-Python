"""
Первому игроку приготовиться 2.0

Во многих играх порядок ходов определяется броском кубика или монетки, а в нашей первым ходит тот, чье имя лексикографически меньше. 
Определите, кто из игроков будет ходить первым.

Формат ввода
В первой строке записано одно натуральное число N — количество игроков.
В каждой из последующих N строк указано одно имя игрока.

Формат вывода
Имя игрока, который будет ходить первым.

Ввод:
3
Вова
Аня
Боря

Вывод:
Аня
"""

number_of_players = int(input())
array = list()
for i in range(number_of_players):
    name = input()
    array.append(name)
print(min(array))





