# Функция bin Преобразует целое число в двоичную строку.
# 1. Синтаксис:
#   bin(x)
# 2. Параметры:
#   x - целое число
# 3. Возвращаемое значение:
#   двоичная строка с префиксом 0b.
# 4. Описание:
# Функция bin() преобразует целое число в двоичную строку с префиксом 0b.
# Результатом будет binary string - двоичная версия заданного целого числа x.

# Примеры преобразований чисел в двоичную систему счисления.
bin(3)
# Вывод:
'0b11'
bin(-10)
# Вывод:
'-0b1010'
### Если префикс 0b является НЕ желательным , вы можете использовать любой из следующих способов.
format(14, '#b'), format(14, 'b')
# ('0b1110', '1110')
f'{14:#b}', f'{14:b}'
# ('0b1110', '1110')
print (format(14, 'b'))
print (format(14, '#b'))


