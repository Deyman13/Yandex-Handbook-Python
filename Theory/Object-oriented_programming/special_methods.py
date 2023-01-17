"""Рассмотрим назначение некоторых специальных методов."""

"""Метод __repr__ вызывается стандартной функцией repr и возвращает строку, которая является 
представлением объекта в формате инициализации. Этот метод может быть также полезен, если 
необходимо вывести информацию об объектах, когда они являются элементами коллекции.

Метод __repr__ в Python выдает текстовое или строковое представление сущности или объекта. 
Этот процесс вызывается всякий раз при вызове метода repr() для какой-то сущности. 
Можно сказать, что методы repr() и __repr__ взаимозаменяемы. """

string = 'Hy! I am John'
print (repr(string))
print (repr(5.0/11.0))
# Output:
# 'Hy! I am John'
# 0.45454545454545453

import datetime
td = datetime.datetime.now()
print(td.__str__())
print(td.__repr__())
# Output:
# 2022-01-26 08:17:46.276609
# datetime.datetime(2022, 1, 26, 8, 17, 46, 276609)


"""
Методы для операций сравнения:
__lt__(self, other) – <;
__le__(self, other) – <=;
__eq__(self, other) – ==;
__ne__(self, other) – !=;
__gt__(self, other) – >;
__ge__(self, other) – >=.
"""
class Clock:
    __DAY = 86400   # число секунд в одном дне
 
    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY
 
    def get_time(self):
        s = self.seconds % 60            # секунды
        m = (self.seconds // 60) % 60    # минуты
        h = (self.seconds // 3600) % 24  # часы
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"
 
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")
    
        return other if isinstance(other, int) else other.seconds
    
    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc
 
    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc


# То есть, для определения операций сравнения достаточно в классе определить только три метода: ==, <, <=, 
# если остальные являются их симметричной противоположностью. 
# В этом случае язык Python сам подберет нужный метод и выполнит его при сравнении объектов.

"""
Метод __call__(arg1, arg2, ...) вызывается, когда сам объект вызывается как функция с аргументами.
"""

class Counter:
    def __init__(self):
        self.__counter = 0

c = Counter()

# Обратите внимание на круглые скобки после имени класса. В общем случае – это оператор вызова, 
# например, так можно вызывать функции. Но, как видите, так можно вызывать и классы. 
# В действительности, когда происходит вызов класса, то автоматически запускается магический 
# метод __call__ и в данном случае он создает новый экземпляр этого класса

class Counter:
    def __init__(self):
        self.__counter = 0
 
    def __call__(self, *args, **kwargs):
        print("__call__")
        self.__counter += 1
        return self.__counter

# Здесь мы выводим сообщение, что был вызван данный метод, затем увеличиваем счетчик counter для текущего 
# объекта на 1 и возвращаем его.

"""
Методы для работы с объектом как с коллекцией:
__getitem__(self, key) используется для получения элемента коллекции по ключу self[key];
__setitem__(self, key, value) используется для записи значения по ключу self[key] = value;
__delitem__(self, key) используется для удаления ключа и соответствующего ему значения;
__len__(self) вызывается стандартной функцией len
__contains__(self, item) вызывается при проверке принадлежности значения item объекту-коллекции self с помощью оператора in.

Давайте разберемся для чего они нужны и как их можно использовать. 
Предположим, что мы создаем класс для представления студентов:
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

s1 = Student('Сергей', [5, 5, 3, 2, 5])

# В объекте s1 имеется локальное свойство marks со списком студентов. Мы можем к нему обратиться и выбрать любую оценку:
print(s1.marks[2])

# Но что если мы хотим делать то же самое, но используя только ссылку на объект s1:

print(s1[2])

# Если сейчас запустить программу, то увидим сообщение об ошибке, что наш класс (объект) не 
# поддерживает такой синтаксис. Как вы, наверное, уже догадались, поправить это можно с 
# помощью магического метода __getitem__. Запишем его в нашем классе, следующим образом:
def __getitem__(self, item):
    return self.marks[item]

# Теперь ошибок нет и на экране видим значение 3. Однако, если указать неверный индекс:
print(s1[20])

# то получим исключение IndexError, которое сгенерировал список marks. 
# При необходимости, мы можем сами контролировать эту ошибку, если в методе __getitem__ пропишем проверку:
def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

# При запуске программы видим наше сообщение «Неверный индекс». Также можно сделать проверку на тип индекса:
print(s1['abc'])

# для списков он должен быть целым числом. Поэтому дополнительно можно записать такую проверку:
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

def __getitem__(self, item):
    if not isinstance(item, int):
        raise TypeError("Индекс должен быть целым числом")
 
    if 0 <= item < len(self.marks):
        return self.marks[item]
    else:
        raise IndexError("Неверный индекс")

# То есть, здесь возможны самые разные вариации обработки и проверки исходных данных, прежде чем 
# обратиться к списку marks и вернуть значение.

# Теперь давайте предположим, что хотели бы иметь возможность менять оценки студентов, используя синтаксис:
s1[2] = 4
print(s1[2])

# Сейчас, после запуска программы будет ошибка TypeError, что объект не поддерживает операцию присвоения, 
# так как в классе не реализован метод __setitem__. Давайте добавим и его:
def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")
 
        self.marks[key] = value

# Однако, если мы сейчас укажем несуществующий индекс:
s1[6] = 4

# то операция присвоения новой оценки приведет к ошибке. Если предполагается использовать такую возможность, 
# то реализовать ее можно, следующим образом:
def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")
 
        if key >= len(self.marks):
            off = key + 1# - en\(self.marks)
            self.marks.extend([None]*off)
 
        self.marks[key] = value

# Если индекс превышает размер списка, то мы расширяем список значениями None до нужной длины 
# (с помощью метода extend), а затем, в последний элемент записываем переданное значение value. 
# Теперь, при выполнении команд:
s1[10] = 4
print(s1.marks)

#Увидим список:
[5, 5, 3, 2, 5, None, None, None, None, None, 4]

# То есть, он был расширен до 10 элементов и последним элементом записано 4. 
# И так можно прописывать любую нужную нам логику при записи новых значений в список marks.

"""
Математические операции:
__add__(self, other) – self + other;
__sub__(self, other) – self - other;
__mul__(self, other) – self * other;
__matmul__(self, other) – self @ other;
__truediv__(self, other) – self / other;
__floordiv__(self, other) – self // other;
__mod__(self, other) – self % other;
__divmod__(self, other) – divmod(self, other);
__pow__(self, other) – self ** other;
__lshift__(self, other) – self << other;
__rshift__(self, other) – self >> other;
__and__(self, other) – self & other;
__xor__(self, other) – self ^ other;
__or__(self, other) – self | other;
__radd__(self, other) – other + self;
__rsub__(self, other) – other - self;
__rmul__(self, other) – other * self;
__rmatmul__(self, other) – other @ self;
__rtruediv__(self, other) – other / self;
__rfloordiv__(self, other) – other // self;
__rmod__(self, other) – other % self;
__rdivmod__(self, other) – divmod(other, self);
__rpow__(self, other) – other ** self;
__rlshift__(self, other) – other << self;
__rrshift__(self, other) – other >> self;
__rand__(self, other) – other & self;
__rxor__(self, other) – other ^ self;
__ror__(self, other) – other | self;
__iadd__(self, other) – self += other;
__isub__(self, other) – self -= other;
__imul__(self, other) – self *= other;
__imatmul__(self, other) – self @= other;
__itruediv__(self, other) – self /= other;
__ifloordiv__(self, other) – self //= other;
__imod__(self, other) – self %= other;
__ipow__(self, other) – self **= other;
__ilshift__(self, other) – self <<= other;
__irshift__(self, other) – self >>= other;
__iand__(self, other) – self &= other;
__ixor__(self, other) – self ^= other;
__ior__(self, other) – self |= other.

Покажем отличие методов математических операций с буквами r и i в начале имени от методов, без этих букв:
"""
class A:

    def __init__(self):
        self.value = 10

    def __add__(self, other):
        return "Выполняется метод __add__."

    def __radd__(self, other):
        return "Выполняется метод __radd__."

    def __iadd__(self, other):
        self.value += other
        return self

    def __str__(self):
        return f"value: {self.value}."

        
a = A()
print(a + 1)
print(1 + a)
a += 1
print(a)
# Выполняется метод __add__.
#Выполняется метод __radd__.
#value: 11.

"""
Для операции a + 1 был использован метод __add__. Для операции 1 + a был использован метод __radd__. 
А для операции += использован __iadd__. Обратите внимание: при выполнении методов, начинающихся с 
буквы i недостаточно только изменить атрибуты объекта, нужно ещё вернуть объект из метода, иначе в объект запишется None.
"""






