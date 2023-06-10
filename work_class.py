from datetime import datetime


class Machine:
    def __init__(self, producer: str, brand: str, fuel_consumption: float, year_made=2020, run=0):
        self.year_made = year_made
        self.producer = producer
        self.brand = brand
        self.run = run
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f"Machine:\nYear made:{self.year_made},\nProducer:{self.producer},\nBrand:{self.brand},\nRun:{self.run},\nFuel Consumption:{self.fuel_consumption},\nage machine:{self.years} "

    @property
    def years(self):
        years_car = datetime.today().year
        return years_car - self.year_made


machine_honda = Machine(producer="Honda", brand="Civic", fuel_consumption=8.1)
machine_skoda = Machine(producer="Skoda", brand="Oktavia", fuel_consumption=6.0)
machine_volkswagen = Machine(producer="Volkswagen", brand="Jetta", fuel_consumption=7.3)

print(machine_volkswagen.__dict__)
