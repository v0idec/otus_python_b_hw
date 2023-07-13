"""
создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle  
from exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, cargo: int, max_cargo: int) -> None:
        self.max_cargo = 0

    def load_cargo(self, cargo: int, max_cargo: int, num: int):
        try:
            cargo += num    
            if cargo < max_cargo:
                return cargo
        except CargoOverload:
            message = "Overload pridurok"
        finally:
            return cargo

        def remove_all_cargo():
            old_cargo = 0
            cargo = old_cargo
            cargo = 0
            return old_cargo