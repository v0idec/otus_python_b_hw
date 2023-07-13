from dataclasses import dataclass
from abc import ABC


class LowFuelError(Exception):
    def __init__(self, message: str):
        self.message = message
        print(message)


class NotEnoughFuel(Exception):
    def __init__(self, message: str):
        self.message = message


class CargoOverload(Exception):
    def __init__(self, message: str):
        self.message = message


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0      
    
    def __init__(self, weight: int, fuel: int, fuel_consumption: int) -> None:
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption    

    def start(self):
        fuel = 10
        self.started = started
        print(started)
        if started is False:
            if fuel > 0:
                message = "Car started"
                started = True
                print(message)
            else:
                message = "Uebok"
                raise LowFuelError(message=message)


    def move(self, fuel: int, fuel_consumption: int):
        pass




@dataclass
class Engine:
    volume: int
    pistons: int

class Car(Vehicle):
    engine = None
    
    def set_engine(self, engine, volume, pistons):
        engine = Engine(volume=volume, pistons=pistons)
        return engine


car = Vehicle(1, 0, 3)
car.fuel = 10
car.started = False
car.start()
