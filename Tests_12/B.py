"""
Рекурсивный сумматор цифр

Рекурсия – отличный способ избавиться от циклов, особенно от while. 
Давайте вспомним одну из наших старых задач и модернизируем её.

Напишите функцию recursive_digit_sum, которая находит сумму всех цифр натурального числа.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
Трассировка вызова рекурсивной функции в обработке ответа не учитывается и показан для примера.

Ввод:
result = recursive_digit_sum(123)

Вывод:
# Вызов recursive_digit_sum(123)
# Вызов recursive_digit_sum(12)
# Вызов recursive_digit_sum(1)
# Вызов recursive_digit_sum(0)
result = 6
"""

# 1 вариант
def recursive_digit_sum(number):
    if len(str(number)) == 1:
        return int(str(number)[0])
    else:
        return int(str(number)[0]) + int(recursive_digit_sum(str(number)[1:]))


# 2 вариант
def recursive_digit_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + recursive_digit_sum(n // 10)
        

result = recursive_digit_sum(7321346)
print(result)