"""
Властелин Чисел: Возвращение Цезаря
До победы над злом остался один шаг — разрушить логово Зерона.

Для этого нужно создать трёхзначное магическое число, которое будет сильнее двух двухзначных защитных чисел Зерона.

Самый простой способ создать сильное число: * первой взять максимальную цифру из всех защитных чисел; 
* последней — минимальную; * в середину поставить сумму оставшихся без учёта переноса разряда.

Помогите одолеть зло.

Формат ввода
В двух строках записаны защитные числа Зерона.

Формат вывода
Одно трёхзначное число, которое приведёт к победе.

Ввод:
31
11

Вывод:
321
"""

number = int(input())
number2 = int(input())
a = number // 10 % 10
b = number % 10
c = number2 // 10 % 10
d = number2 % 10
M = [a, b, c, d]
max_num = max(M)
min_num = min(M)


def secondmax(numbers):
    numbers.remove(max(numbers))
    max_number = max(numbers)
    return max_number


def secondmin(numbers):
    numbers.remove(min(numbers))
    min_number = min(numbers)
    return min_number


sec_max = secondmax(M)
sec_min = secondmin(M)
sum = sec_max + sec_min
print(f"{max_num}{sum % 10}{min_num}")
