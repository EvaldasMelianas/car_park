from dataclasses import dataclass
from data_classes.car import Car


@dataclass
class CargoTruck(Car):
    max_weight: float
    trailer: bool

    def calculate_trips(self, weight: int):
        regular, trailer = 0, 0
        while weight > 0:
            weight -= self.max_weight
            regular += 1
            if weight > 0:
                weight -= 5
                trailer += 1
        return regular, trailer