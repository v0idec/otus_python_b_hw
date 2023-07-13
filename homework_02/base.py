from abc import ABC
from exceptions import LowFuelError, CargoOverload, NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0      
    
    def __init__(self, weight: int, fuel: int, fuel_consumption: int) -> None:
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption      

    def start(self, started: bool, fuel: int):
        self.started = started
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
