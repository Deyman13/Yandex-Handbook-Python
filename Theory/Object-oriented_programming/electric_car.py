"""
Давайте напишем ещё один класс для электромобилей. 
Их отличие будет заключаться в замене топливного бака на заряд аккумуляторной батареи:
"""

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

"""
Напишем функцию range_reserve(), которая будет определять для автомобилей классов Car и ElectricCar запас хода 
в километрах. Функции, которые могут работать с объектами разных классов, называются полиморфными. А сам 
принцип ООП называется полиморфизмом.
"""
