"""
Мухи отдельно, котлеты отдельно

Вернёмся в магазин, хозяин которого уже привык полагаться на всемогущую автоматизацию.

Помогите ему разобраться с одной проблемой. Далее его история: «Пару дней назад я купил две партии котлет и по 
случайности высыпал их на один прилавок. Общий вес котлет составил N килограмм, а ценник — M рублей за килограмм.
Сегодня я обнаружил, что накладные на эти виды котлет потерялись, но я помню, что первый вид котлет стоил K_1 
рублей за килограмм, а второй — K_2

Помогите мне вспомнить вес каждой партии котлет, чтобы поставить их на учёт.

Формат ввода
В первой строке записано натуральное число N
Во второй строке — натуральное число M
В третьей строке — натуральное число K_1 
В четвёртой строке — натуральное число K_2 


Причём доподлинно известно, что второй вид котлет стоит меньше, чем первый.

Формат вывода
Два натуральных числа, записанных через пробел — вес обеих партий котлет.

Ввод:
32
285
300
240

Вывод:
24 8
"""

a = int(input()) # Всего килограмм
b = int(input()) # Рублей за килограмм
c = int(input()) # Сумма за килограмм первой партии
d = int(input()) # Сумма за килограмм второй партии
sum = a * b # Общая потраченная сумма
x = a * (d - b) / (d - c) 
y = a - x
print(f"{int(x)} {int(y)}")
