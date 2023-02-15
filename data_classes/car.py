from dataclasses import dataclass
from datetime import datetime


@dataclass
class Car:
    yearly_mileage: float
    plate_number: str
    fuel_type: str
    exploit_cost: float
    serviced_at_date: str
    categories: str
    fuel_consumption: float
    insured_at_date: str
    today = datetime.now()

    def __post_init__(self):
        self.serviced_date_obj = datetime.strptime(self.serviced_at_date, "%Y-%m-%d")
        self.insured_date_obj = datetime.strptime(self.insured_at_date, "%Y-%m-%d")

    def needs_service(self) -> bool:
        renewal_date = self.serviced_date_obj.replace(month=self.insured_date_obj.month + 1)
        return self.today.replace(month=self.today.month + 1) <= renewal_date

    def needs_insurance(self) -> bool:
        renewal_date = self.insured_date_obj.replace(month=self.insured_date_obj.month + 1)
        return self.today.replace(month=self.today.month + 1) <= renewal_date

    def cost_of_driving(self, distance: float, fuel_cost: float):
        driving_cost = distance * (self.fuel_consumption/100) * fuel_cost
        exploit_cost_km = self.yearly_mileage / self.exploit_cost
        return round(driving_cost + exploit_cost_km, 2)
