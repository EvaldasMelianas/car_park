from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Car:
    yearly_mileage: float
    plate_number: str
    fuel_type: str
    exploit_cost: float
    serviced_at_date: datetime
    categories: str
    fuel_consumption: float
    insured_at_date: datetime
    today = datetime.now()

    def needs_service(self):
        renew = (self.serviced_at_date + timedelta(730)).replace(day=1)
        next_month = (self.today.replace(day=1) + timedelta(31)).replace(day=1)
        return renew <= next_month

    def needs_insurance(self):
        renew = (self.insured_at_date + timedelta(365)).replace(day=1)
        next_month = (self.today.replace(day=1) + timedelta(31)).replace(day=1)
        return renew <= next_month

    def cost_of_driving(self, distance: float, fuel_cost: float):
        driving_cost = distance * (self.fuel_consumption/100) * fuel_cost
        exploit_cost_km = self.yearly_mileage / self.exploit_cost
        return round(driving_cost + exploit_cost_km, 2)
