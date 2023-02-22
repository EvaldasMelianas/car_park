from data_classes.driver import Driver
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Union


@dataclass
class Car:
    yearly_mileage: float
    plate_number: str
    fuel_type: str
    exploit_cost: float
    service_at_date: datetime
    categories: str
    fuel_consumption: float
    insure_at_date: datetime
    driver: Union[Driver, None] = None
    today = datetime.now()

    def needs_service(self):
        next_month = (self.today.replace(day=1) + timedelta(31)).replace(day=1)
        return self.service_at_date <= next_month

    def needs_insurance(self):
        next_month = (self.today.replace(day=1) + timedelta(31)).replace(day=1)
        return self.insure_at_date <= next_month

    def calculate_vehicle_cost(self, distance: float, fuel_cost: float):
        driving_cost = distance * (self.fuel_consumption/100) * fuel_cost
        exploit_cost_km = self.yearly_mileage / self.exploit_cost
        return round(driving_cost + exploit_cost_km, 2)

    def check_for_capability(self):
        return self.categories.upper() == self.driver.category.upper()

    def check_if_vacation(self):
        end_date = (self.driver.vacation + timedelta(days=self.driver.vacation_duration)).date()
        if self.today.date() >= self.driver.vacation.date():
            return end_date < self.today.date()
        else:
            return end_date > self.today.date()
