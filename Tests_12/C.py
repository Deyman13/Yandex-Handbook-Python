"""
Многочлен N-ой степени

Напишите функцию make_equation, которая по заданным коэффициентам строит строку, описывающую 
валидное с точки зрения Python выражение без использования оператора возведения в степень.

Многочлен второй степени с коэффициентами a, b и c, например, можно записать в виде:
((a) * x + b) * x + c

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
Трассировка вызова рекурсивной функции в обработке ответа не учитывается и показан для примера.

Ввод:
result = make_equation(3, 2, 1)

Вывод:
# Вызов make_equation(3, 2, 1)
# Вызов make_equation(3, 2)
# Вызов make_equation(3)
result = '((3) * x + 2) * x + 1'
"""

# Все представленные варианты решают данную задачу, но принимается только первый вариант. 

# 1 вариант:
def make_equation(*coefs):
    if len(coefs) == 1:
        return str(coefs[0])
    else:
        return '(' + make_equation(*coefs[:-1]) + ') * x + ' + str(coefs[-1])


# 2 вариант:
def make_equation(a, *coefs):
    equation = str(a)
    for i, coef in enumerate(coefs):
        equation = f"({equation}) * x + {coef}"
    return equation


# 3 вариант:
def make_equation(a, *coef, is_first=True):
    if len(coef) == 0:
        return str(a)
    else:
        if is_first:
            return "(" * len(coef) + f"{a}) * x + {make_equation(*coef, is_first=False)}"
        else:
            return f"{a}) * x + {make_equation(*coef, is_first=False)}"


result = make_equation(3, 2, 1)
print(result)




