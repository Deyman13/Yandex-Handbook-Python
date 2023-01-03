"""
Синтаксис:
import itertools

itertools.islice(iterable, stop)
itertools.islice(iterable, start, stop[, step])

Параметры:
    iterable - итератор,
    start - int, начало среза,
    stop - int, конец среза (не входит),
    step - int, шаг среза.

Возвращаемое значение:
итератор.
Описание:
Функция islice() модуля itertools создает итератор, который возвращает выбранные элементы из итератора iterable. 
Другими словами, получает срез итератора/генератора, для которых нельзя получить срез обычными средствами или 
встроенной функцией slice().

Если start не равен нулю, то элементы из iterable пропускаются до тех пор, пока не будет достигнут start. После 
этого элементы возвращаются последовательно, если только для шага step не установлено значение больше единицы, 
что приводит к пропуску элементов.

Если stop равен None, итерация продолжается до тех пор, пока итератор iterable не будет исчерпан. В противном 
случае он останавливается в указанной позиции stop.

Если start=None или не указан, итерация начинается с нуля.

Если step=None или не указан, то по умолчанию используется step=1.

В отличие от обычных срезов списков или кортежей, функция itertools.islice() не поддерживает отрицательные 
значения для start, stop или step.
Функция itertools.islice() может использоваться для извлечения связанных полей из данных, где внутренняя 
структура была сглажена, например, многострочный отчет может содержать поле имени в каждой третьей строке.
Функция itertools.islice() примерно эквивалентна следующему коду:
"""
import sys
def islice(iterable, *args):
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G
    s = slice(*args)
    start, stop, step = s.start or 0, s.stop or sys.maxsize, s.step or 1
    it = iter(range(start, stop, step))
    try:
        nexti = next(it)
    except StopIteration:
        # Consume *iterable* up to the *start* position.
        for i, element in zip(range(start), iterable):
            pass
        return
    try:
        for i, element in enumerate(iterable):
            if i == nexti:
                yield element
                nexti = next(it)
    except StopIteration:
        # Consume to *stop*.
        for i, element in zip(range(i + 1, stop), iterable):
            pass

# Примеры использования:
from itertools import islice

list(islice('ABCDEFG', 2))
# ['A', 'B']
list(islice('ABCDEFG', 2, 4))
# ['C', 'D']
list(islice('ABCDEFG', 2, None))
# ['C', 'D', 'E', 'F', 'G']
list(islice('ABCDEFG', 0, None, 2))
# ['A', 'C', 'E', 'G']
