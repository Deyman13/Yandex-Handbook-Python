"""Опишем с помощью методов какие действия могут совершать объекты класса Car. 
По PEP8 между объявлением методов нужно поставить одну пустую строку."""

class Car: # Создаем класс Car

    def __init__(self, color, consumption, tank_volume, mileage=0):
        """Создаем метод __init__ с аргументами, которые нужно вводить
        Прописываем все объекты класса внутри метода, и присваиваем их к аргументам метода, за исключением
        констант (self.engine_on = False), так как изначально мы знаем, что изначально двигатель выключен!"""
        self.color = color
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self):
        """Создаем метод запуска двигателя в котором мы при определенных условиях сможем переключить двигатель"""
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель запущен."
        return "Двигатель уже был запущен."

    def stop_engine(self):
        """Создаем аналогично методу запуска двигателя - остановку двигателя"""
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен."
        return "Двигатель уже был остановлен."

    def drive(self, distance):
        """Создаем метод вождения автомобиля"""
        if not self.engine_on:
            return "Двигатель не запущен."
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас топлива."
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток топлива: {self.reserve} л."

    def refuel(self):
        """Метод для заполнения бака"""
        self.reserve = self.tank_volume

    def get_mileage(self):
        """Метод для получения информации о текущем пробеге"""
        return self.mileage

    def get_reserve(self):
        """Метод для получения информации об остатке топлива в баке"""
        return self.reserve

"""Создаем объект, который инициализирует аргументы класса Car с аргументами метода __init__"""
car_1 = Car(color="black", consumption=10, tank_volume=55)
print(car_1.start_engine())
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(300))
print(f"Пробег {car_1.get_mileage()} км.")
print(f"Запас топлива {car_1.get_reserve()} л.")
print(car_1.stop_engine())
print(car_1.drive(100))

"""
Обратите внимание: взаимодействие с объектом класса вне описания класса осуществляется только с помощью методов 
и прямого доступа к атрибутам не происходит. Этот принцип ООП называется инкапсуляцией.
"""
