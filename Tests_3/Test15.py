"""
Зайка - 4
Давайте вновь поиграем с детьми и поможем им найти заек.

Формат ввода
В первой строке записано натуральное число N — количество выделенных придорожных местностей. 
В каждой из N последующих строках — описание придорожной местности.

Формат вывода
Количество строк, в которых есть зайка.

Ввод:
3
березка елочка зайка волк березка
сосна сосна сосна елочка грибочки медведь
сосна сосна сосна белочка сосна белочка

Вывод:
1
"""

number_of_str = int(input())
counter = 0
for i in range(number_of_str):
    if "зайка" in input():
        counter += 1
print(counter)