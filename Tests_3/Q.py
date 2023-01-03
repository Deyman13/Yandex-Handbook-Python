"""
Чётная чистота

Мы уже достаточно знатоки, чтобы очистить число от определённых цифр, поэтому давайте напишем программу, 
которая уберёт все чётные цифры из числа.

Формат ввода
Одно натуральное число.

Формат вывода
Одно натуральное число — результат очистки.

Ввод:
1234

Вывод:
13
"""

number = list(map(int, input())) # разбиваем число на цифры и записываем в список
odd = [] # создаем новый список, куда будем складывать нечетные цифры
for i in range(len(number)):
    if number[i] % 2 == 1: # если нечетное
        odd.append(number[i]) # то закидываем это число в список odd
for num in odd:
    print(num, end="") # выводим список без пробелов