"""
НЕ РЕШЕНА ПРАВИЛЬНО!!!

Редизайн таблицы умножения
Согласитесь, что предыдущие таблицы умножения выглядят не очень красиво. 
Давайте зададим для всех столбцов одинаковую ширину, а значения в ячейках выровним по центру.
И да, заказчик попросил ещё добавить в таблицу рамки между ячейками.

Формат ввода
В первой строке записан требуемый размер таблицы. Во второй строке — ширина столбцов.

Формат вывода
Таблица умножения заданного размера и вида.

Примечание
В данный момент визуализация примеров работает не корректно.

Ввод:
3
3

Вывод:

 1 | 2 | 3 
-----------
 2 | 4 | 6 
-----------
 3 | 6 | 9 
"""

number = int(input())
width = int(input())
max_len = width * number + number
length = width // 2
space = " "
for i in range(1, number + 1):
    for j in range(1, number + 1):
        if j < number:
            print(str(i * j).center(width), end="|")
        else:
            print(str(i * j).center(width), end=" ")
    print()
    print("-" * (max_len - 1))
    