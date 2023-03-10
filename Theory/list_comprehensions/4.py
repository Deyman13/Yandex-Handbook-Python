"""
Переменные неизменяемых типов данных могут изменить своё значение только путём создания новой переменной с тем же именем 
и с новым идентификатором. К неизменяемым типам относят int, float, str, tuple. Изменение идентификатора целочисленной 
переменной при операции присваивания было показано в одном из примеров выше.

К изменяемым типам данных относят set, list, dict. Переменные изменяемых типов данных могут изменить своё значение 
без создания новой переменной с тем же именем. При этом у переменной сохранится тот же идентификатор. Для этого можно 
воспользоваться операциями и методами, которые меняют значения в коллекции. Покажем, что метод append() и операция += для 
списков меняет исходный объект, не создавая новый:
"""
numbers = [1, 2, 3]
print(f"{numbers}, id = {id(numbers)}")
numbers += [4]
print(f"{numbers}, id = {id(numbers)}")
# Вывод программы:

# [1, 2, 3], id = 2095932585856
# [1, 2, 3, 4], id = 2095932585856
"""
Обратите внимание: операция присваивания (=) всегда создаёт новую переменную с новым идентификатором, 
даже для изменяемых типов данных:
"""
numbers = [1, 2, 3]
print(f"{numbers}, id = {id(numbers)}")
numbers = numbers + [4]
print(f"{numbers}, id = {id(numbers)}")
# Вывод программы:

# [1, 2, 3], id = 1438332303232
# [1, 2, 3, 4], id = 1438341470336
"""
У переменной изменился идентификатор, значит она была создана заново.

Так как вместо значения в переменных хранится ссылка на область памяти, где записано это значение, то для изменяемых 
типов данных нужно помнить о том, что если две переменных изменяемого типа имеют одинаковые ссылки на значение, то 
изменение одной из этих переменных повлечёт за собой одновременное изменение и другой. Покажем это на примере:
"""
x = [1, 2, 3]
y = x
print(x is y)
x[0] = 0
print(x)
print(y)
print(x is y)
# Вывод программы:

# True
# [0, 2, 3]
# [0, 2, 3]
# True

"""
В примере мы видим, что до и после изменения списка x, список y имеет ту же ссылку на значение в памяти. 
То есть x и y являются одним и тем же объектом в программе. Поэтому изменение значение в списке x вызвало и изменение списка y. 
Хотя теперь мы знаем, что никакого изменения списка y не было, просто изменилось общее значение, на которое ссылаются 
переменные x и y.

Если создать копию списка x с помощью среза, включающего все его элементы, то будет создан новый, независимый от 
исходного список с новым идентификатором:
"""
x = [1, 2, 3]
y = x[:]
print(x is y)
x[0] = 0
print(x)
print(y)
print(x is y)
# Вывод программы:

# False
# [0, 2, 3]
# [1, 2, 3]
# False

"""Интересной задачей является создание копии вложенного списка. Полный срез вернёт список, в котором внутренние списки 
будут ссылаться на те же значения, что и у исходного. Покажем это на примере:
"""
numbers = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
numbers_copy = numbers[:]
print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])
# Вывод программы:

# [True, True, True]
"""
В результате получили список, состоящих из значений как в исходном, но никак не связанный с исходным.

Полный срез для копирования списка можно заменить стандартным методом copy(). А для копирования вложенных коллекций можно 
использовать функцию deepcopy() из модуля copy. Пример копирования вложенного списка с использованием deepcopy:
"""
from copy import deepcopy

numbers = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
numbers_copy = deepcopy(numbers)
print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])
# Вывод программы:

# [False, False, False]
