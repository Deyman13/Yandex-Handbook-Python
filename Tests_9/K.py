"""
Файловая статистика 2.0

Напишите программу, которая для заданного файла вычисляет следующие параметры:

количество всех чисел;
количество положительных чисел;
минимальное число;
максимальное число;
сумма всех чисел;
среднее арифметическое всех чисел с точностью до двух знаков после запятой.
Формат ввода
Пользователь вводит два имени файла.
Первый файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.

Формат вывода
Выведите статистику во второй файл в формате JSON.

Ключи значений задайте соответственно:

count — количество всех чисел;
_positivecount — количество положительных чисел;
min — минимальное число;
max — максимальное число;
sum — сумма всех чисел;
average — среднее арифметическое всех чисел с точностью до двух знаков после запятой.

Ввод:
# Пользовательский ввод:
numbers.txt
statistics.json

# Содержимое файла numbers.txt
1 2 3 4 5
-5 -4 -3 -2 -1
10 20
20 10

Вывод:
# Содержимое файла statistics.json
{
    "count": 14,
    "positive_count": 9,
    "min": -5,
    "max": 20,
    "sum": 60,
    "average": 4.29
}
"""

import json

file = input()
json_format = input()

with open(file, "r") as data:
    numbers = data.readlines()

result = []
for line in numbers:
    line_split = line.replace("\n", "").split()
    for num in line_split:
        result.append(int(num))

count = len(result)
positive_count = 0
for i in result:
    if i > 0:
        positive_count += 1
minimum = min(result)
maximum = max(result)
summa = sum(result)
average = round(summa / count, 2)
statistics = {"count": count, 
              "positive_count": positive_count, 
              "min": minimum, 
              "max": maximum, 
              "sum": summa, 
              "average": average}

with open(json_format, "w", encoding="utf-8") as j:
    json.dump(statistics, j, ensure_ascii=False, indent="\t")
