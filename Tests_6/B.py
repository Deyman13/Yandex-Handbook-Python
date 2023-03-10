"""
Символическая разница

А ещё в промышленных задачах часто требуется находить общее среди данных, полученных из раных источников.
Напишите программу, которая по двум строкам определяет их общие символы.

Формат ввода
Вводится две строки.

Формат вывода
Требуется вывести все символы этой строки без повторений.
Порядок вывода не имеет значения.

Ввод:
змееед
велосипед

Вывод:
ед

Решение: Вводим 2 слова и превращаем в список неповторяющихся букв благодаря множеству, объединяем два множества для проверки
того, какие буквы есть и в первом и втором множествах, те что подошли - выводим в терминал, порядок вывода букв неважен. 
"""

str1 = set(input()) 
str2 = set(input()) 
str_intersection = str1 & str2 
for i in str_intersection: 
    print(i, end="") 
