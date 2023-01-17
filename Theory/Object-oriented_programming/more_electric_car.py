"""
Напишем метод __repr__ для класса ElectricCar:
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

    def __repr__(self):
        return f"ElectricCar('{self.color}', " \
            f"{self.consumption}, " \
            f"{self.bat_capacity}, " \
            f"{self.mileage})"

# Код для проверки работы метода:
electric_car = ElectricCar(color="белый", consumption=15, bat_capacity=90)
print(repr(electric_car))
electric_car_1 = ElectricCar(color="чёрный", consumption=17, bat_capacity=80)
print([electric_car, electric_car_1])

"""
Опишем операцию сложения для объектов класса ElectricCar: возвращается новый объект класса ElectricCar, 
у которого цвет такой же как у левого слагаемого, а уровень заряда батареи, ёмкость батареи, 
расход энергии на 100 км пути и общий пробег вычисляется как сумма соответствующих атрибутов слагаемых объектов:
"""

def __add__(self, other):
    new_car = ElectricCar(self.color,
                          self.consumption + other.consumption,
                          self.bat_capacity + other.bat_capacity,
                          self.mileage + other.mileage)
    new_car.reserve = self.reserve + other.reserve
    return new_car

# Код для проверки метода:
electric_car = ElectricCar(color="белый", consumption=15, bat_capacity=90)
electric_car_1 = ElectricCar(color="чёрный", consumption=17, bat_capacity=80)
electric_car.start_engine()
electric_car_1.start_engine()
electric_car.drive(300)
electric_car_1.drive(100)
new_electric_car = electric_car + electric_car_1
print(new_electric_car)

# Вывод программы:

# Электромобиль. Цвет: белый. Пробег: 200 км. Остаток заряда: 138.0 кВт*ч.