"""
Генератор Фибоначчи

Числа Фибоначчи весьма интересная последовательность и используется в различных математических задачах. 
В ней каждый следующий элемент равен сумме двух предыдущих. Математики начинают эту последовательность 
с двух единиц, но мы же с вами программисты, поэтому привыкли вести счет с нуля.

Напишите генератор fibonacci, который последовательно возвращает заданное количество чисел Фибоначчи по 
"правилам программистов".

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод:
print(*fibonacci(5))

Вывод:
0 1 1 2 3
"""

# 1 вариант через возврат генератора (yield)
def fibonacci(n, a=0, b=1):
    if n == 0:
        return
    yield a
    yield from fibonacci(n - 1, b, a + b)


# 2 вариант через списки
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
        return fib_seq