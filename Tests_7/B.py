"""
Таблица умножения 2.0

Вашему решению будет предоставлена единственная переменная n — необходимый размер таблицы умножения.

Напишите списочное выражения для генерации таблицы умножения.

Примечание
В решении не должно быть ничего, кроме списочного выражения.

Ввод:
n = 3

Вывод:
[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
"""
# Идеальное решение:
n = int(input())
print([[i * j for i in range(1, n + 1)] for j in range(1, n + 1)])

# Фактическое решение по условиям: 
[[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]

# Представление в виде цикла:
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")


