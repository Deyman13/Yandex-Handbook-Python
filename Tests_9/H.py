"""
Файловая разница

Напишите программу, которая определяет, какие слова есть только в одном из файлов.

Формат ввода
Пользователь вводит три имени файлов.
Каждый из входных файлов содержит произвольное количество слов, разделённых пробелами и символами перевода строки.

Формат вывода
В третий файл выведите в алфавитном порядке без повторений список слов, которые есть только в одном из файлов.

Ввод:
# Пользовательский ввод:
first.txt
second.txt
answer.txt

# Содержимое файла first.txt
кофе молоко
чай печенье
велосипед

# Содержимое файла second.txt
кофе велосипед
пряник жвачка весло

Вывод:
# Содержимое файла answer.txt
весло
жвачка
молоко
печенье
пряник
чай
"""

first = input()
second = input()
answer = input()

with open(first, "r", encoding="utf-8") as f:
    first_text = f.readlines()

with open(second, "r", encoding="utf-8") as s:
    second_text = s.readlines()

result_for_first = set()
for line in first_text:
    line_split = line.replace("\n", "").split()
    for word in line_split:
        result_for_first.add(word)

result_for_second = set()
for line in second_text:
    line_split = line.replace("\n", "").split()
    for word in line_split:
        result_for_second.add(word)

with open(answer, "a", encoding="utf-8") as a:
    set_answer = result_for_first ^ result_for_second
    for word in sorted(set_answer):
        print(word, file=a)




