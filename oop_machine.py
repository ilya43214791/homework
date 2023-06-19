from abc import ABC, abstractmethod

class Machine(ABC):

    def __init__(self, car_brand: str, tank_volume: int, rest_of_fuel: int, speed: int, car_mileage: int):
        self.car_brand = car_brand
        self.tank_volume = tank_volume
        self.rest_of_fuel = rest_of_fuel
        self.speed = speed
        self.car_mileage = car_mileage

    def refueling(self, amount_of_fuel):

        if self.rest_of_fuel + amount_of_fuel > self.tank_volume:
            self.rest_of_fuel = self.tank_volume
        else:
            self.rest_of_fuel = self.rest_of_fuel + amount_of_fuel
        print(f'Зараз пального: {self.rest_of_fuel}')

    def drains_fuel(self, other, amount_of_fuel=10):
        result = self.rest_of_fuel - amount_of_fuel
        result += other.rest_of_fuel




    @abstractmethod
    def __str__():
        pass

class Car(Machine):

    def __init__(self, number_passengers=4, airbags=False, car_brand='', tank_volume=40,
                 rest_of_fuel=0, speed=100, car_mileage=0):
        super().__init__(car_brand, tank_volume, rest_of_fuel, speed, car_mileage)

        self.number_passengers = number_passengers
        self.airbags = airbags


class Motorcycle(Machine):

    def __init__(self, presence_stroller=False, car_brand='', tank_volume=0,
                 rest_of_fuel=0, speed=0, car_mileage=0):
        super().__init__(car_brand, tank_volume, rest_of_fuel, speed, car_mileage)

        self.presence_stroller = presence_stroller



my_car = Car(airbags=True, tank_volume=40)


