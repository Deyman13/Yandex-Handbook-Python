"""
Считалочка

Ребята в детском саду учат числа, и мы можем им в этом помочь.
Ребята дают нам два числа — начало и конец последовательности чисел.
Наша задача вывести все числа от начала до конца, заполнив промежуток между ними.

Формат ввода
Два числа в порядке возрастания, каждое с новой строки.

Формат вывода
Все числа от начала до конца (включительно), записанные через пробел.

Ввод:
1
10

Вывод:
1 2 3 4 5 6 7 8 9 10
"""

number1 = int(input())
number2 = int(input())
for i in range(number1, (number2 + 1)):
    print(f"{i}", end=" ")

