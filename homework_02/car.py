"""
создайте класс `Car`, наследник `Vehicle`
"""

from base import Vehicle
from engine import Engine


class Car(Vehicle):
    engine = None
    
    def set_engine(self, engine, volume, pistons):
        engine = Engine(volume=volume, pistons=pistons)
        return engine
