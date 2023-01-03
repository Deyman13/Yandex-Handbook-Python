"""
Полностью программа с классами, полиморфной функцией и пример их использования представлена ниже:
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


class ElectricCar:

    def __init__(self, color, consumption, bat_capacity, mileage=0):
        self.color = color
        self.consumption = consumption
        self.bat_capacity = bat_capacity
        self.reserve = bat_capacity
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
            return "Малый заряд батареи."
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток заряда: {self.reserve} кВт*ч."

    def recharge(self):
        self.reserve = self.bat_capacity

    def get_mileage(self):
        return self.mileage

    def get_reserve(self):
        return self.reserve

    def get_consumption(self):
        return self.consumption


def range_reserve(car):
    return car.get_reserve() / car.get_consumption() * 100


car_1 = Car(color="black", consumption=10, tank_volume=55)
car_2 = ElectricCar(color="white", consumption=15, bat_capacity=90)
print(f"Запас хода: {range_reserve(car_1)} км.")
print(f"Запас хода: {range_reserve(car_2)} км.")

"""
В нашей программе можно заметить, что классы Car и ElectricCar имеют много общих атрибутов и методов. 
Это привело к дублированию кода. В следующей главе мы познакомимся с наследованием — принципом ООП, 
позволяющим устранить подобную избыточность кода."""