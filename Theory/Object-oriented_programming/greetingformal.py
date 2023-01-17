"""
Наследование может производиться сразу от нескольких классов. 
В таком случае базовые классы перечисляются через запятую. 
Производный класс унаследует атрибуты и методы обоих базовых классов.

Напишем программу, в которой будут следующие классы:

GreetingFormal. При инициализации объектов этого класса создаётся атрибут formal_greeting, 
содержащий строку "Добрый день,". В этом классе также есть метод greet_formal, 
который принимает аргумент name и возвращает строку с приветствием по имени.

GreetingInformal. При инициализации объектов этого класса создаётся атрибут informal_greeting, 
содержащий строку "Привет,". В этом классе также есть метод greet_informal, 
который принимает аргумент name и возвращает строку с приветствием по имени.

GreetingMix. Этот класс наследуется от двух предыдущих и может приветствовать пользователя по имени обоими методами.
"""

class GreetingFormal:

    def __init__(self):
        self.formal_greeting = "Добрый день,"

    def greet_formal(self, name):
        return f"{self.formal_greeting} {name}!"


class GreetingInformal:

    def __init__(self):
        self.informal_greeting = "Привет,"

    def greet_informal(self, name):
        return f"{self.informal_greeting} {name}!"


class GreetingMix(GreetingFormal, GreetingInformal):

    def __init__(self):
        GreetingFormal.__init__(self)
        GreetingInformal.__init__(self)


mixed_greeting = GreetingMix()
print(mixed_greeting.greet_formal("Пользователь"))
print(mixed_greeting.greet_informal("Пользователь"))


# Добрый день, Пользователь!
# Привет, Пользователь!


"""
Обратите внимание на метод __init__ класса GreetingMix. 
В нём вместо вызова метода базового класса через функцию super() используется непосредственный 
вызов из базовых классов с указанием имён этих классов. Такой вызов необходим из-за того, 
что метод __init__ присутствует в обоих базовых классах и происходит конфликт. 
Интерпретатор при использовании функции super() в нашем примере использовал бы 
метод того класса, который стоит левее при перечислении в объявлении производного класса. 
В нашем примере это привело бы к тому, что __init__ из класса GreetingInformal не был 
бы вызван и в производном классе не произошла бы инициализация атрибута informal_greeting. 
Тогда при вызове метода greet_informal было бы вызвано исключение AttributeError.

На основе операции наследования перепишем пример про автомобили из прошлых глав. 
Пусть класс ElectricCar наследуется от класса Car. Методы init и drive будут расширены. 
Метод recharge создан в производном классе. А остальные методы и атрибуты наследуются без изменений.
"""

class Car:

    def __init__(self, color, consumption, tank_volume, mileage=0):
        self.color = color
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель запущен."
        return "Двигатель уже был запущен."

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен."
        return "Двигатель уже был остановлен."

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен."
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас топлива."
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток топлива: {self.reserve} л."

    def refuel(self):
        self.reserve = self.tank_volume

    def get_mileage(self):
        return self.mileage

    def get_reserve(self):
        return self.reserve

    def get_consumption(self):
        return self.consumption


class ElectricCar(Car):

    def __init__(self, color, consumption, bat_capacity, mileage=0):
        super().__init__(color, consumption, bat_capacity, mileage)
        self.bat_capacity = bat_capacity

    def drive(self, distance):
        super().drive(100)
        return f"Проехали {distance} км. Остаток заряда: {self.reserve} кВт*ч."

    def recharge(self):
        self.reserve = self.bat_capacity


electric_car = ElectricCar(color="white", consumption=15, bat_capacity=90)
print(electric_car.start_engine())
print(electric_car.drive(100))


"""
Описание класса ElectricCar существенно сократилось за счёт использования наследования.

Давайте посмотрим, что выведет функция print, если передать в неё объект созданного нами класса ElectricCar. 
Добавим в программу следующий код:

print(electric_car)
Вывод программы:

<__main__.electriccar object at 0x000002365ddd8a00>
Такой вывод говорит нам только о том, что переменная electric_car является объектом класса ElectricCar и 
расположена по определённому адресу в памяти. Можно этот вывод сделать более информативным. 
Когда в функцию print для вывода передаётся аргумент, не являющийся строкой, к нему применяется 
стандартная функция str. При этом в классе, к которому относится аргумент, для аргумента 
вызывается специальный (ещё говорят "магический") метод __str__. Остаётся только описать, 
какую строку вернёт этот метод. И тогда это значение и будет выводиться функцией print. 

Дополним класс ElectricCar методом __str__:
"""

def __str__(self):
    return f"Электромобиль. " \
           f"Цвет: {self.color}. " \
           f"Пробег: {self.mileage} км. " \
           f"Остаток заряда: {self.reserve} кВт*ч."

electric_car = ElectricCar(color="белый", consumption=15, bat_capacity=90)
print(electric_car.start_engine())
print(electric_car.drive(100))
print(electric_car)


# Двигатель запущен.
# Проехали 100 км. Остаток заряда: 75.0 кВт*ч.
# Электромобиль. Цвет: белый. Пробег: 100 км. Остаток заряда: 75.0 кВт*ч.


"""
Специальных методов в Python довольно много. 
Они нужны для описания взаимодействия с объектами при помощи стандартных операций и встроенных функций. 
Описание специальных методов называется перегрузкой операторов (operator overloading).

Имена специальных методов выделены слева и справа двумя символами подчёркивания. Как можно заметить, 
метод __init__ также является специальным.
"""