"""
Корень зла 2

В одной из первых лекций вы уже решали задачу о поиске корней квадратного уравнения. Давайте модернизируем её.

Напишите функцию find_roots, принимающую три параметра: коэффициенты уравнения и возвращающую его 
корни в виде кортежа из двух значений.

Так же создайте два собственных исключения NoSolutionsError и InfiniteSolutionsError, которые будут 
вызваны в случае отсутствия и бесконечного количества решений уравнения соответственно.

Если переданные коэффициенты не являются рациональными числами, вызовите исключение TypeError.

Примечание
В решении не должно быть вызовов требуемых функций.

Ввод:
print(find_roots(0, 0, 1))

Вывод:
Вызвано исключение NoSolutionsError
"""


class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    try:
        x1 = float(0.00)
        x2 = float(0.00)
        if a == 0 and b == 0 and c == 0:
            raise InfiniteSolutionsError
        elif a == 0 and b != 0 and c != 0:
            x1 = -(c / b)   
            return x1 
        elif a == 0 and b == 0 and c != 0:
            raise NoSolutionsError
        elif a == 0 and b != 0 and c == 0:
            x1 = 0
            return x1
        else:
            disc = (b ** 2) - (4 * a * c)
            if disc == 0:
                return (-b / (2 * a), -b / (2 * a))
            elif disc > 0:
                x1 = (-b - (disc ** 0.5)) / (2 * a)
                x2 = (-b + (disc ** 0.5)) / (2 * a)
                return min(x1, x2), max(x1, x2)
            elif disc < 0:
                raise NoSolutionsError
    except TypeError:
        return "Вызвано исключение TypeError"
    except NoSolutionsError:
        return "Вызвано исключение NoSolutionsError"
    except InfiniteSolutionsError:
        return "Вызвано исключение InfiniteSolutionsError"


print(find_roots(1, 2, 1))

