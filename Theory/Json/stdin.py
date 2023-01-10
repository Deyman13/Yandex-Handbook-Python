"""
Чтобы подключить стандартный поток ввода stdin в программу, необходимо его импортировать из модуля sys:

from sys import stdin

Так как поток ввода stdin по сути выступает итератором, по его элементам (введённым строкам) можно пройти в цикле. 
Использование потока ввода показано в следующей программе:
"""

from sys import stdin

lines = []
for line in stdin:
    lines.append(line)
print(lines)

"""
Запустим программу и введём следующие данные:

Первая
Вторая
Третья
Теперь вводить данные мы можем практически бесконечно. 

Допустим, что после ввода третьей строчки нам нужно показать интерпретатору, что ввод данных завершён, 
можно выйти из цикла и продолжить работу программы. 

Для этого необходимо послать в поток ввода специальный символ — EOF (end of file), нажав в консоли сочетание 
клавиш Ctrl+Z в ОС Windows либо Ctrl+D в ОС Linux и macOS. Когда в консоли Windows появится знак ^Z, нужно 
нажать клавишу Enter — ввод прекратится, а программа выдаст список введённых пользователем строк:

['Первая\n', 'Вторая\n', 'Третья\n']

Обратите внимание — каждая строка заканчивается символом перехода на новую строку. 

Если этот символ мешает дальнейшей обработке строк, его можно убрать, применив к каждой строке метод 
rstrip("\n") перед добавлением в список:
"""
from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))
print(lines)

"""
Тогда результат работы программы для тех же введённых строк будет:

['Первая', 'Вторая', 'Третья']

Сохранить строки из потока ввода в список можно ещё проще — достаточно использовать метод readlines(). 
Главное — не забудьте о том, что символ "\n" будет в конце каждой введённой строки:
"""
from sys import stdin

lines = stdin.readlines()
print(lines)

"""
Если необходимо сохранить все данные из потока ввода в одну строковую переменную, это можно сделать с помощью метода read():
"""
from sys import stdin

text = stdin.read()
print([text])

# ['Первая\nВторая\nТретья']



