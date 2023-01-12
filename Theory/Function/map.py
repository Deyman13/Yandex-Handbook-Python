"""
Ещё одной полезной функцией высшего порядка в Python является map(). 
Она возвращает итератор, каждый элемент которого получен применением функции-обработчика к итерируемому объекту. 
Напишем программу, которая для списка целых чисел выведет список квадратов этих чисел:
"""

def square(x):
    return x ** 2

    
result = map(square, range(5))
print(", ".join(str(x) for x in result))
# 0, 1, 4, 9, 16


"""
В map() можно использовать стандартные функции и методы Python. 
Напишем программу, которая для списка строк выводит их в нижнем регистре:
"""

result = map(str.lower, ["abCD", "EFGh", "IJkl"])
print("\n".join(result))
# abcd
# efgh
# ijkl