"""
НЕ РЕШЕНА ВЕРНО!!!

Слияние с проверкой

Когда-то вы уже писали функцию merge, которая производит слияние двух отсортированных кортежей.

Давай-те её немного переработаем.

Введём систему проверок:

если один из параметров не является итерируемым объектом, то вызовите исключение StopIteration;
если значения входных параметров содержат «неоднородные» данные, то вызовите исключение TypeError;
если один из параметров не отсортирован, то вызовите исключение ValueError.
Проверки следует проводить в указанном порядке.

Если параметры прошли все проверки, верните итерируемый объект, являющийся слиянием двух переданных.

Примечание
В решении не должно быть вызовов требуемых функций.

Ввод:
print(*merge(35, (1, 2, 3)))

Вывод:
Вызвано исключение StopIteration
"""

def merge(a, b):
    try:
        if not (hasattr(a, '__iter__') and hasattr(b, '__iter__')):
            raise StopIteration
        if not all(isinstance(i, type(a[0])) for i in a) or not all(isinstance(i, type(b[0])) for i in b):
            raise TypeError
        if a != sorted(a) or b != sorted(b):
            raise ValueError
    except StopIteration:
        return "Вызвано исключение StopIteration"
    except TypeError:
        return "Вызвано исключение TypeError"
    except ValueError:
        return "Вызвано исключение ValueError"
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
        j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return tuple(result)


print(*merge(35, (1, 2, 3)))
print(*merge([3, 2, 1], range(10)))





    