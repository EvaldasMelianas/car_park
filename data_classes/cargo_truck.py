from dataclasses import dataclass
from data_classes.car import Car
import math


@dataclass
class CargoTruck(Car):
    max_weight: float = 10
    trailer_weight: int = 0

    def calculate_trips(self, weight: int):
        with_trailer = math.ceil(weight / (self.max_weight + self.trailer_weight))
        regular = math.ceil(weight / self.max_weight)
        if regular <= with_trailer:
            return regular, 0
        else:
            trailer_trips = math.ceil((weight - self.max_weight * math.ceil(with_trailer)) / self.trailer_weight)
            return with_trailer, trailer_trips
