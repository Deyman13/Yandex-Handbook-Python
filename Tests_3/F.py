"""
НОД

В одном из местных НИИ часто требуется находить наибольший общий делитель (НОД) двух чисел.
Вам уже доверяют, как одному из лучших «автоматизаторов» в округе, так что руководство НИИ решило заказать ПО у вас.

Формат ввода
Вводится два натуральных числа, каждое на своей строке.

Формат вывода
Требуется вывести одно натуральное число — НОД двух данных чисел.

Примечание
Самый распространенный способ поиска НОД — алгоритм Эвклида.

Ввод:
12
42

Вывод:
6
"""

# Через цикл:
def gcd(a, b):
    if a > b:
        temp = a
    else:
        temp = b
    for i in range(1, temp + 1): # В диапазоне от 1 до самого большого числа из двойки чисел.
        if ((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd


a = int(input())
b = int(input())
print(gcd(a, b))
