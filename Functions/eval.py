# Позволяет выполнить строку-выражение с кодом на Python.

# 1. Синтаксис:
#   eval(expression, globals=None, locals=None)

# 2. Параметры:
#   expression - строка-выражение, которую требуется исполнить. Либо объект кода, что возвращает compile(),
#   globals=None - словарь глобального пространства, относительно которого следует исполнить выражение,
#   locals=None - переменные локального пространства, в котором следует исполнить выражение.

# 3. Возвращаемое значение:
#   результат выполнения строки-выражения.

# 4. Описание:
# Функция eval() выполняет строку-выражение, переданную ей в качестве обязательного аргумента и возвращает 
# результат выполнения этой строки.
# Аргументами eval() являются строка-выражение expression, которую требуется исполнить и необязательные глобальные 
# globals и локальные locals значения. Передаваемые в функцию глобальные переменные должны быть словарем dict. 
# Передаваемые локальные переменные могут быть любым отображающим объектом.

# Если глобальные переменные указаны, но словарь globals не содержит атрибута __builtins__ данные переданного словаря 
# со значениями будут дополнены данными общего глобального пространства, перед разбором выражения. Таким образом, 
# выражение будет иметь доступ ко всем встроенным модулям.

# Если локальные locals переменные не указаны, то используется словарь глобального пространства.

# Если оба словаря опущены, выражение выполняется с глобальными и локальными значениям и в среде, где функция eval() 
# вызывается. 
# Обратите внимание, что eval() не имеет доступа к вложенным областям
# Функция eval() также может быть использована для выполнения кода, который возвращает функция compile(). 
# Если объект кода в compile() собран в режиме exec будет возвращено None.
# Функции eval() можно передавать результаты функций globals() и locals().
# Если вам необходимо выполнить динамический код, записанный в строку, то обратитесь к документации по функции exec().

# Примеры выполнения строки-выражения с кодом функцией eval().
x = "print('Привет')"
eval(x)
# Привет

y = 'print("5 + 10 =", (5+10))'
eval(y)
# 5 + 10 = 15

s=3
eval('s==3')
# True

eval('s + 1')
# 4

eval('s')
# 3

eval('str(s)+"test"')
# '3test'

# В eval() запрещены и операции присваивания

# Аргумент globals опционален. Он содержит словарь, обеспечивающий доступ eval() к глобальному пространству имен. 
# С помощью глобальных переменных можно указать eval(), какие глобальные имена использовать при выполнении выражения.

