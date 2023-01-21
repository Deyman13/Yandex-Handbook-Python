"""
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
    if not hasattr(a, '__iter__') or not hasattr(b, '__iter__'):
        raise StopIteration
    elif not all(isinstance(i, type(a[0])) for i in a + [j for j in b]):
        raise TypeError
    elif not all(x <= y for x, y in zip(a, a[1:])) or not all(x <= y for x, y in zip(b, b[1:])):
        raise ValueError
    else:
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




