
"""
Делители

Вашему решению будет предоставлено множество numbers.

Продумайте выражение для генерации словаря содержащего информацию о делителях каждого из заданных чисел.

Примечание
В решении не должно быть ничего, кроме выражения.

Ввод:
numbers = {1, 2, 3, 4, 5}

Вывод:
{1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4], 5: [1, 5]}
"""
numbers = {1, 2, 3, 4, 5}
# Стандартное решение: 
print({i: [j for j in range(1, i + 1) if i % j == 0] for i in numbers})

# Фактическое решение по условиям:
{i: [j for j in range(1, i + 1) if i % j == 0] for i in numbers}

# Представление в виде цикла:
dct = dict()
for i in numbers:
    for j in range(1, i + 1):
        if i % j == 0:
            if i not in dct:
                dct[i] = [j]
            else:
                dct[i].append(j)
print(dct)
