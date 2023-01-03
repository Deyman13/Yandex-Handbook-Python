# Функция breakpoint Обозначает точку останова и выполняет функцию отладчика кода.
# 1. Синтаксис:
#   breakpoint()
# 2. Описание:
# Функция останова breakpoint() вызывает функцию sys.breakpointhook(). По умолчанию sys.breakpointhook() в свою очередь 
# вызывает функцию pdb.set_trace().
# Использование встроенной функции breakpoint(), по крайней мере, обеспечивает удобство использования отладчика, 
# поскольку не нужно явно импортировать модуль pdb, а так же писать дополнительный код, чтобы войти в отладчик. 
# Функция breakpoint() представляет синтаксический сахар над имеющимися конструкциями.


# Простой пример использования функции breakpoint(). Есть скрипт на Python breakpoint_test.py со следующим кодом.
x = 10
y = 'Hi'
z = 'Hello'
print(y)
breakpoint()
print(z)

# Когда мы запустим этот скрипт, встретив точку останова в коде интерпретатор затормозит процесс исполнения, 
# открыв консоль отладчика PDB, что позволит нам детально разобраться в происходящем. 
# Чтобы прервать PDB-сессию и продолжить выполнение скрипта, нажмите C и Enter.

# Hi
# > /home/script/breakpoint_test.py(7)<module>()
# -> print(z)
# (Pdb) c
# Hello

# Для управления отладкой используется переменная окружения PYTHONBREAKPOINT. 
# Если присвоить ей значение 0, то все точки останова в коде будут проигнорированы интерпретатором.

# $ PYTHONBREAKPOINT=0 python3.7 breakpoint.py

# С помощью PYTHONBREAKPOINT можно заменить встроенный модуль PDB на сторонний отладчик, например, PuDB. 
# Импорт модуля Python берет на себя. Не забудьте установить pudb (pip install pudb).

# $ PYTHONBREAKPOINT=pudb.set_trace python3.7 breakpoint.py

# По умолчанию функцией breakpoint() использует встроенный в интерпретатор отладчик PDB, который не принимает параметров, 
# однако можно заменить функцию отладки на print() и передать туда какие-то переменные.

# breakpoint.py
x = 10
y = 'Hi'
z = 'Hello'
breakpoint(x, y, z, end="<==\n")

# Запустим breakpoint_test.py, установив print() в качестве отладчика, которую будет вызывать команда breakpoint().
# $ PYTHONBREAKPOINT=print python3.7 breakpoint.py 
# 10 Hi Hello <==

# Так же можем написать свою функцию, которую будет вызывать команда breakpoint(). Например, функцию просмотра локальных переменных в коде.
# breakpoint.py
from pprint import pprint
import sys

def print_locals():
    caller = sys._getframe(1)  
    pprint(caller.f_locals)

x = 10
y = 'Hi'
z = 'Hello'
breakpoint()

# Теперь заменим значение PYTHONBREAKPOINT, используя нотацию <модуль>.<функция>:

# $ PYTHONBREAKPOINT=breakpoint_test.print_locals python3.7 breakpoint.py 
# ...
# ...
# 'pprint': <function pprint at 0x7f08536d7170>,
# 'print_locals': <function print_locals at 0x7f085218d200>,
# 'sys': <module 'sys' (built-in)>,
# 'x': 10,
# 'y': 'Hi',
# 'z': 'Hello'}








