"""
На старт! Внимание! Марш!

По правилам велогонки, после квалификации каждый гонщик стартует с задержкой на секунду больше, чем у гонщика перед ним.
Первый гонщик стартует на счёт 3. Напишите программу, которая сможет автоматизировать старт всех гонщиков, участвующих в велогонке.

Формат ввода
Вводится одно натуральное число — количество участников велогонки.

Формат вывода
Требуется вывести отсчёт.

Ввод:
3

Вывод:
До старта 3 секунд(ы)
До старта 2 секунд(ы)
До старта 1 секунд(ы)
Старт 1!!!
До старта 4 секунд(ы)
До старта 3 секунд(ы)
До старта 2 секунд(ы)
До старта 1 секунд(ы)
Старт 2!!!
До старта 5 секунд(ы)
До старта 4 секунд(ы)
До старта 3 секунд(ы)
До старта 2 секунд(ы)
До старта 1 секунд(ы)
Старт 3!!!
"""

number = int(input())
temp = 3
for i in range(number):
    j = 0
    while j < temp:
        print(f"До старта осталось {temp - j} секунд(ы)")
        j += 1
    temp += 1
    print(f"Старт {i + 1}!!!")
