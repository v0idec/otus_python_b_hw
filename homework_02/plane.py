"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo: int


    def __init__(self, weight: int, fuel: int, fuel_consumption: int, max_cargo) -> None:
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo


    def load_cargo(self, load_cargo: int):
            loaded_cargo = self.cargo + load_cargo  
            if loaded_cargo <= self.max_cargo:
                self.cargo = loaded_cargo
            else:
                raise CargoOverload


    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
