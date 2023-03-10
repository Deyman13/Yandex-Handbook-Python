
"""
Длины всех слов

Вашему решению будет предоставлена строка sentence слов, разделённых пробелами.

Напишите списочное выражения для генерации списка длин слов.

Примечание
В решении не должно быть ничего, кроме списочного выражения.

Ввод:
sentence = 'Мама мыла раму'

Вывод:
[4, 4, 4]
"""
sentence = "Мама мыла раму"
# Идеальное решение:
print([len(i) for i in input().split(" ")])

# Фактическое решение по условияем:
[len(i) for i in sentence.split(" ")]

# Представление в виде цикла:
for i in sentence:
    print(len(i), end=" ")


