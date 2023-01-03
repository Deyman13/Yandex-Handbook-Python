"""
Меню питания 2.0

В детском саду ежедневно подают новую кашу на завтрак.

Напишите программу, которая строит расписание каш на ближайшие дни.

Формат ввода
Вводится натуральное число M — количество каш в меню. В каждой из последующих M строк записано одно название каши. 
В конце передается натуральное число N — количество дней.

Формат вывода
Вывести список каш в порядке подачи.

Примечание
Советуем изучить документацию на функцию itertools.islice, которая реализует срезы на основе итераторов.

Ввод:
5
Манная
Гречневая
Пшённая
Овсяная
Рисовая
12

Вывод:
Манная
Гречневая
Пшённая
Овсяная
Рисовая
Манная
Гречневая
Пшённая
Овсяная
Рисовая
Манная
Гречневая

Решение: Импортируем islice, repeat, chain из библотеки itertools. Вводим количество каш, и количество дней. 
Создаем список из каш. Так же создаем отдельную переменную темп, где делим количество дней на количество каш, 
чтобы потом это передать в repeat(). Создаем список из итераторов, первым делом - копируем список каш темп + 1 раз. 
Скрепляем все цепью chain(), и используем итерацию islice(), вторым аргументом передаем количество дней. 
Тем самым получаем большой список каш (настолько, чтобы хватило итераций количества дней) и на каждой итерации
выводим кашу. 
"""
from itertools import islice, repeat, chain

number_of_kashas = int(input())
kashas = [input() for kasha in range(number_of_kashas)]
number_of_days = int(input())
temp = number_of_days // number_of_kashas
for i in list(islice(chain.from_iterable(repeat(kashas, temp + 1)), number_of_days)):
    print(i)