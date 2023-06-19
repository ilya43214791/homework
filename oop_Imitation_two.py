from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, brand: str, tank_volume: int | float, remaining_fuel: int | float,
                 speed: int | float):
        self.brend = brand
        self.tank_volume = tank_volume
        self.remaining_fuel = remaining_fuel
        self.speed = speed
        self.refuelings()

    def refuelings(self, fuel=5):
        self.remaining_fuel += fuel
        if self.remaining_fuel >= self.tank_volume:
            self.remaining_fuel = self.tank_volume
        return self

    def fuel_overflow_transport(self, other, value):
        target_value = min([value, other.tank_volume - other.remaining_fuel, self.remaining_fuel])
        self.remaining_fuel -= target_value
        other.remaining_fuel += target_value

    @abstractmethod
    def __str__(self):
        pass


class Machine(Transport):
    def __init__(self, number_passengers: int, airbags: bool, brand: str, tank_volume: int | float,
                 remaining_fuel: int | float,
                 speed: int | float):
        super().__init__(brand, tank_volume, remaining_fuel, speed)
        self.number_passengers = number_passengers
        self.airbags = airbags

    def __str__(self):
        return "rg"


class Bike(Transport):
    def __init__(self, cradles: bool, brand: str, tank_volume: int | float, remaining_fuel: int | float,
                 speed: int | float):
        super().__init__(brand, tank_volume, remaining_fuel, speed)
        self.cradles = cradles

    def __str__(self):
        return "rg"


car1 = Machine(number_passengers=4, airbags=True, brand="tgt", tank_volume=30, remaining_fuel=9, speed=123)

car2 = Machine(number_passengers=3, airbags=True, brand="gt", tank_volume=40, remaining_fuel=13, speed=123)

car1.fuel_overflow_transport(other=car2, value=200)
pass
