"""
Зайка — 7

Вновь поищем заек за окном поезда.

Формат ввода
В первой строке записано натуральное число N — количество выделенных придорожных местностей.
В каждой из N последующих строк записано описание придорожной местности.

Формат вывода
Для каждой строки нужно найти положение первого зайки.
Если в строке нет заек, то об этом нужно непременно сообщить.

Примечание
Для символов в строках используйте нумерацию с 1.

Ввод:
3
березка елочка зайка волк березка
сосна зайка сосна елочка зайка медведь
сосна сосна сосна белочка сосна белочка

Вывод:
16
7
Заек нет =(
"""

number = int(input())
list_temp = []
for i in range(number):
    temp = input()
    list_temp.append(temp)
for string in list_temp:
    if "зайка" in string:
        print(string.index("зайка") + 1) # указываем индекс первого вхождения зайки
    else:
        print("Заек нет =(")
