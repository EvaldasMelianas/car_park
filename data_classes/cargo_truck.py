from dataclasses import dataclass
from data_classes.car import Car


@dataclass
class CargoTruck(Car):
    max_weight: float
    trailer: bool

    def calculate_trip(self, weight: int):
        regular_trip = -(weight // -self.max_weight)
        trailer_trip = -(weight // -(self.max_weight + 5))
        if regular_trip <= trailer_trip:
            return -(weight // -self.max_weight)
        else:
            return weight / self.max_weight
