"""
Файловая статистика

Напишите программу, которая для заданного файла вычисляет следующие параметры:

количество всех чисел;
количество положительных чисел;
минимальное число;
максимальное число;
сумма всех чисел;
среднее арифметическое всех чисел с точностью до двух знаков после запятой.
Формат ввода
Пользователь вводит имя файла.
Файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.

Формат вывода
Выведите статистику в указанном порядке.

Ввод
# Пользовательский ввод:
numbers.txt

# Содержимое файла numbers.txt
1 2 3 4 5
-5 -4 -3 -2 -1
10 20
20 10

Вывод:
14
9
-5
20
60
4.29
"""

file = input()

with open(file, "r") as data:
    numbers = data.readlines()

result = []
for line in numbers:
    line_split = line.replace("\n", "").split()
    for num in line_split:
        result.append(int(num))

the_number_of_positive = 0

# Количество чисел:
print(len(result))

# Количество положительных чисел:
for num in result:
    if num > 0:
        the_number_of_positive += 1
print(the_number_of_positive)

# Минимальное число:
print(min(result))

# Максимальное число:
print(max(result))

# Сумма всех чисел:
print(sum(result))

# Среднее арифметическое:
print(round(sum(result) / len(result), 2))
