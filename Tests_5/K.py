"""
Найдётся всё

Поиск информации — одна из основных нужд в современном мире.
Создайте программу, которая реализует маленький компонент поисковой системы.

Формат ввода
Вводится натуральное число N — количество страниц, среди которых требуется произвести поиск.
В каждой из последующих N строк записаны заголовки страниц.
В последней строке записан поисковый запрос.

Формат вывода
Вывести все заголовки страниц, в которых присутствует поисковый запрос (регистр не имеет значения).
Порядок заголовков должен сохраниться.

Ввод:
3
Яндекс выпустил задачник по программированию
На соревнованиях по программированию победил любитель питона
Как заказать Яндекс.Такси?!
яндекс

Вывод:
Яндекс выпустил задачник по программированию
Как заказать Яндекс.Такси?!
"""

number = int(input())
list_temp = []
for i in range(1, number + 1):
    temp = input()
    list_temp.append(temp)
    if i >= number:
        yandex = input()
        for string in list_temp:
            if yandex.lower() in string.lower():
                print(string)