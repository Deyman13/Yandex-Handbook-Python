"""
Без комментариев

Мы надеемся, вы пишите комментарии к своему коду. Если так, то интерпретатор удаляет их перед тем, как выполнить код. 
Напишите программу, которая выполняет данную функцию за интерпретатор.

Формат ввода
Вводятся строки программы.
Признаком остановки является пустая строка.

Формат вывода
Каждую строку нужно очистить от комментариев.
А если комментарий — вся строка, то выводить её не надо.

Ввод:
# Моя первая супер-пупер программа
print("What is your name?") #  Как тебя зовут?
name = input() #  Сохраняем имя
print(f"Hello, {name}!") #  Здороваемся# Конец моей супер-пупер программы

Вывод:
print("What is your name?")
name = input()
print(f"Hello, {name}!")
"""

list = []

while True:
    line = input()
    if line == '':
        break
    else:
        list.append(line)

for line in list:
    grid = line.find('#')
    if grid == 0:
        continue
    if grid > 0:
        print(line[:grid])
    else:
        print(line)
