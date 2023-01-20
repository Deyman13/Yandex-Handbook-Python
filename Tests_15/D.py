"""
Контроль параметров
Напишите функцию only_positive_even_sum, которая принимает два параметра и возвращает их сумму.

Если один из параметров не является целым числом, то следует вызвать исключение TypeError.
Если один из параметров не является положительным чётным числом, то следует вызвать исключение ValueError.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод:
print(only_positive_even_sum("3", 2.5))

Вывод:
Вызвано исключение TypeError
"""

def only_positive_even_sum(fstarg, scarg):
    try:
        if not isinstance(fstarg, int) or not isinstance(scarg, int):
            raise TypeError
        if not (fstarg > 0 and fstarg % 2 == 0) or not (scarg > 0 and scarg % 2 == 0):
            raise ValueError
    except TypeError:
        return "Вызвано исключение TypeError"
    except ValueError:
        return "Вызвано исключение ValueError"
    return fstarg + scarg





