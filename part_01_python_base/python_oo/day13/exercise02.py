class Car:
    def __init__(self, speed, brand):
        self.speed = speed
        self.brand = brand


class ElectricVehicle(Car):
    def __init__(self, speed, brand, battery_capacity, charging_power):
        super().__init__(speed,brand)

        self.battery_capacity = battery_capacity
        self.charging_power = charging_power


e01 = ElectricVehicle(500, "艾威", "600kW·h", "900kW")
c01 = Car(998, "艾威")
