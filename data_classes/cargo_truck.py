from dataclasses import dataclass
from data_classes.car import Car
import math

@dataclass
class CargoTruck(Car):
    max_weight: float
    trailer_weight: int = None

    def calculate_trips(self, weight: int):
        trailer = weight / (self.max_weight + self.trailer_weight)
        regular = weight / self.max_weight
        if math.ceil(regular) <= math.ceil(trailer):
            return math.ceil(regular)
        else:
            return math.ceil(trailer), math.ceil(regular - trailer)
