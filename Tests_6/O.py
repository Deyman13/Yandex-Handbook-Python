"""
Двоичная статистика!

У программистов особые отношения с двоичной системой счисления.
Продолжим тренировки в статистической обработке данных и проанализируем данные числа.
Напишите программу, которая для переданных чисел вычисляет:

количество разрядов;
количество единиц;
количество нулей.
Формат ввода
Вводится последовательность чисел, записанных через пробел.

Формат вывода
Вывести список словарей с требуемой статистикой.

Примечание
Порядок словарей обязан совпадать с порядком переданных чисел.
Порядок ключей в словаре не имеет значения.

Ввод:

5 8 12
Вывод:
[
    {
        "digits": 3,
        "units": 2,
        "zeros": 1
    },
    {
        "digits": 4,
        "units": 1,
        "zeros": 3
    },
    {
        "digits": 4,
        "units": 2,
        "zeros": 2
    }
]

Решение: Числа вводятся через пробел, поэтому создаем список из введенных чисел, разделенных с помощью split() и используем
map() для придания всем элементам int значения (по умолчанию строчные). Для получения количества цифр в числе используем функцию
len(), для получения количества нулей и единиц .count(), для того, чтобы конвертировать десятичное число в двоичное - 
используем bin(), но используя bin мы получим в начале 0b, которые необходимо убрать при помощи .replace(). Все это выводим 
в нужном виде. 
"""

n = list(map(int, input().split(" ")))
print("[")
for i in n:
    print("\t{")
    print(f'\t\t"digits": {len(bin(i).replace("0b", ""))},')
    print(f'\t\t"units": {bin(i).replace("0b", "").count("1")},')
    print(f'\t\t"zeros": {bin(i).replace("0b", "").count("0")}')
    print('\t},' if i != n[len(n)-1] else '\t}')
print("]")
