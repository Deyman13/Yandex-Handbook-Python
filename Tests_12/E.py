"""
Накопление результата

В некоторых случаях полезно накапливать результат, а затем получать его единым списком.

Реализуйте декоратор result_accumulator, который модернизирует функцию с неопределенным количеством 
позиционных параметров следующим образом:

 - Добавляет именованный параметр method со значением по умолчанию accumulate;
 - При вызове функции с параметром method равным accumulate, результат сохраняется в очередь 
(для каждой функции в собственную), а функция ничего не возвращает;
 - При вызове функции с параметром method равным drop, возвращается все накопленные результаты, а очередь сбрасывается.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод:
@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))

Вывод:
None
None
[8, 16, 2]
None
[-6, 45]
"""

def result_accumulator(fn):
    def wrapper(*args, **kwargs):
        wrapper.results.append(fn(*args))
        if kwargs.get('method') == 'drop':
            res, wrapper.results = wrapper.results, []
            return res
    wrapper.results = []
    return wrapper

