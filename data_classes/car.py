from dataclasses import dataclass
from datetime import datetime, timedelta


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
    today = datetime.today()

    def needs_service(self) -> bool:
        serviced_date = datetime.strptime(self.serviced_at_date, "%Y-%m-%d")
        renewal_date = serviced_date + timedelta(days=30)
        return self.today.date() >= renewal_date.date()

    def needs_insurance(self) -> bool:
        insurance_date = datetime.strptime(self.insured_at_date, "%Y-%m-%d")
        renewal_date = insurance_date + timedelta(days=365)
        return self.today.date() >= renewal_date.date()

    def cost_of_driving(self, distance: float, fuel_cost: float):
        driving_cost = distance * (self.fuel_consumption/100) * fuel_cost
        exploit_cost_km = self.yearly_mileage / self.exploit_cost
        return round(driving_cost + exploit_cost_km, 2)
