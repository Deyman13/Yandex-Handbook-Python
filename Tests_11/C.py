"""
Функциональный нод 2.0

Напишите функцию gcd, которая вычисляет наибольший общий делитель последовательности чисел.
Параметрами функции выступают натуральные числа в произвольном количестве, но не менее одного.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод:
result = gcd(3)

Вывод:
result =  3
"""

# Очевидно, что будет работать, но не является нормальным решением)
def gcd(*numbers):
    import math
    return math.gcd(*numbers)


# 1 вариант
def gcd_2(*numbers):
    def _gcd(a, b):
        if b == 0:
            return a
        return _gcd(b, a % b)

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = _gcd(result, numbers[i])
    return result


# 2 вариант
def gcd_3(*numbers):
    if isinstance(numbers, int):
        numbers = (numbers, numbers)
    for i in range(len(numbers)):
        for j in range(1, max(numbers) + 1):
            if numbers[i] % j == 0 and numbers[i - 1] % j == 0:
                gcd = j
    return gcd


# Тесты
result_1 = gcd(36, 48, 156, 100500)
result_2 = gcd_2(36, 48, 156, 100500)
result_3 = gcd_3(36, 48, 156, 100500)

print(result_1)
print(result_2)
print(result_3)