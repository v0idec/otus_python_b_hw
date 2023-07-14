from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel
#from exceptions import LowFuelError, NotEnoughFuel

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
            while self.fuel > 0:
                    self.fuel -= self.fuel_consumption
                    print(self.fuel)
                    distance -= 1
                    print(distance)
        else:
            raise NotEnoughFuel
                