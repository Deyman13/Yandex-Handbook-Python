"""
Преобразование в строку
Вашему решению предоставлен список натуральных чисел numbers.

Напишите выражение для генерации строки, представляющей собой отсортированный список чисел, записанных через 
дефис, окружённый пробелами, без повторений.

Примечание
В решении не должно быть ничего, кроме выражения.

Ввод:
numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]

Вывод:
'1 - 2 - 3 - 4 - 6 - 7 - 10'
"""
numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]
# Стандартное решение:
print(" - ".join(str(i) for i in sorted({j for j in numbers})))

# Фактическое решение:
" - ".join(str(i) for i in sorted({j for j in numbers}))

# Представление в виде цикла:
st = set()
for i in numbers:
    st.add(i)
print(" - ".join(str(i) for i in st))

