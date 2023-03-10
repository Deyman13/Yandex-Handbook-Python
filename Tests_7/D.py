"""
Множество нечетных чисел

Вашему решению будет предоставлен список numbers, содержащий натуральные числа.

Напишите выражение для генерации множества всех нечётных чисел среди переданных.

Примечание
В решении не должно быть ничего, кроме выражения.

Ввод:
numbers = [1, 2, 3, 4, 5]

Вывод:
{1, 3, 5}
"""
numbers = [1, 2, 3, 4, 5]
# Идеальное решение: 
print(set([i for i in numbers if i % 2 == 1]))

# Фактическое решение по условиям:
set([i for i in numbers if i % 2 == 1])

# Представление в виде цикла:
set_1 = set()
for i in numbers:
    if i % 2 == 1:
        set_1.add(i)
print(set_1)




        

