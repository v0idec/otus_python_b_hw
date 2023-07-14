from dataclasses import dataclass
from abc import ABC


class LowFuelError(Exception):
    def __init__(self):
        pass

class NotEnoughFuel(Exception):
    def __init__(self):
        pass

class CargoOverload(Exception):    
    def __init__(self):
        pass


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
            if self.started is False:
                    if self.fuel > 0:
                            self.started = True
                    else: 
                        raise LowFuelError
            else:
                print("Already stated")
 
    def move(self, distance):
        max_distance = self.fuel - self.fuel_consumption*distance
        print(max_distance)
        if distance <= max_distance:
              while distance >= 0:
                    self.fuel -= self.fuel_consumption
                    # if self.fuel == 0:
                    #      print(self.fuel)
                    #      raise NotEnoughFuel
                    # else:
                    print(self.fuel)
                    distance -= 1
                    print(distance)
        else:
              raise NotEnoughFuel



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
car.fuel = 50
car.fuel_consumption = 1
car.started = False
car.move(20)
