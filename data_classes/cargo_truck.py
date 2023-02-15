from dataclasses import dataclass
from data_classes.car import Car


@dataclass
class CargoTruck(Car):
    max_weight: float
    trailer_weight: int = None

    def calculate_trips(self, weight: int):
        pass
