from dataclasses import dataclass
from datetime import datetime
from dateutil import relativedelta


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

    def needs_attention(self, date):
        renew = date + relativedelta.relativedelta(years=1)
        return self.today + relativedelta.relativedelta(months=1) >= renew

    def cost_of_driving(self, distance: float, fuel_cost: float):
        driving_cost = distance * (self.fuel_consumption/100) * fuel_cost
        exploit_cost_km = self.yearly_mileage / self.exploit_cost
        return round(driving_cost + exploit_cost_km, 2)
