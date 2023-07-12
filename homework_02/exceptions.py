"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


def check_fuel(fuel: int):
    try:
        if fuel > 5:
            print("Fuel Ok")
            return fuel
    except LowFuelError:
        if fuel <= 5:
            print(LowFuel)
            return fuel
    else:
        print("NotEnoughFuel")
        return fuel
