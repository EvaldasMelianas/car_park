from dataclasses import dataclass
from data_classes.car import Car

@dataclass
class Transporter(Car):
    passenger_seats: int

    def required_for_amount_passengers(self, amount: int):
        return -(amount // -self.passenger_seats)

    def calculate_cost_for_amount(self, amount: int, distance: int, fuel_cost: float):
        vehicle_count = self.required_for_amount_passengers(amount)
        km_cost = self.exploit_cost / self.yearly_mileage
        return distance * km_cost * fuel_cost * vehicle_count
