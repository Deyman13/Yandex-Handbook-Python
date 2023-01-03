"""
Ранее мы говорили о том, что встроенные типы данных в Python могут быть изменяемыми или неизменяемыми. 
Для того, чтобы понять, на что это влияет, рассмотрим каким образом Python хранит в памяти значения переменных. 
Когда мы создаём в программе переменную, интерпретатор назначает ей уникальное число -- идентификатор. 
Узнать идентификатор переменной можно с помощью встроенной функции id(). Каждый раз, когда в уже существующую 
переменную в программе записывается новое значение, ей назначается новый идентификатор. Проверим это на примере:
"""
x = 5
print(id(x))
x = 10
print(id(x))
# Вывод программы (значения будут меняться от запуска к запуску программы):

# 2198530255152
# 2198530255184
"""
Мы видим, что идентификатор переменной x поменялся при записи нового значения.

На самом деле, в самих переменных хранится вовсе не значение, а ссылка на это значение в некоторой области оперативной 
памяти компьютера. Это означает, что если в программе присвоить значение одной переменной в другую, то обе переменные 
будут иметь одинаковые ссылки на это значение, и переменные будут одним объектом с одинаковым идентификатором, а 
встроенный оператор is, проверяющий, что объекты являются одним и тем же (имеют одинаковые идентификаторы), для 
этих переменных вернёт значение True:
"""
x = 1
y = x
print(id(x))
print(id(y))
print(x is y)
# Вывод программы (значения будут меняться от запуска к запуску программы):

# 2109716588848
# 2109716588848
# True
"""
Обратите внимание, что равенство переменных не означает, что они являются одним и тем же объектом в программе 
(имеют одинаковые ссылки на значения):
"""
x = [el ** 2 for el in range(5)]
y = [el ** 2 for el in range(5)]
print(x == y)
print(x is y)
# Вывод программы:

# True
# False
"""
В примере мы создали два списка с одинаковыми значениями. 
Однако в программе это будут два разных объекта, имеющих разные идентификаторы.
"""


