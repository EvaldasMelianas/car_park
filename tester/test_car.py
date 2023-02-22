from data_classes.car import Car
from data_classes.driver import Driver
from datetime import datetime
import unittest


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car(yearly_mileage=69000, plate_number="GFD532", fuel_type="Diesel",
                       exploit_cost=12000.0, service_at_date=datetime(2024, 12, 13),
                       categories="B", fuel_consumption=15, insure_at_date=datetime(2023, 12, 13))
        self.car.driver = Driver(vacation=(datetime(2023, 2, 15)), category='B', pay_km=0.3, vacation_duration=5)
        self.car.today = datetime(2023, 2, 22)

    def test_needs_insurance(self):
        self.assertFalse(self.car.needs_insurance())
        self.car.insure_at_date = datetime(2021, 12, 13)
        self.assertTrue(self.car.needs_insurance())
        self.car.insure_at_date = datetime(1989, 2, 21)
        self.assertTrue(self.car.needs_insurance())

    def test_needs_service(self):
        self.assertFalse(self.car.needs_service())
        self.car.service_at_date = datetime(2021, 2, 21)
        self.assertTrue(self.car.needs_service())
        self.car.service_at_date = datetime(2056, 6, 13)
        self.assertFalse(self.car.needs_service())

    def test_cost_by_driving(self):
        self.assertEqual(46.25, self.car.calculate_vehicle_cost(150, 1.8))
        self.car.yearly_mileage, self.car.exploit_cost, self.car.fuel_consumption = 53240, 9865, 8.6
        self.assertEqual(63.8, self.car.calculate_vehicle_cost(399.5, 1.7))
        self.car.yearly_mileage, self.car.exploit_cost, self.car.fuel_consumption = 1000, 36.2, 100
        self.assertNotEqual(16361.69, self.car.calculate_vehicle_cost(10273, 1.59))

    def test_driver_check_if_vacation(self):
        self.assertTrue(self.car.check_if_vacation())
        self.car.driver.vacation_duration = 7
        self.assertFalse(self.car.check_if_vacation())
        self.car.driver.vacation = datetime(2022, 2, 22)
        self.assertTrue(self.car.check_if_vacation())

    def test_driver_check_for_capability(self):
        self.assertTrue(self.car.check_for_capability())
        self.car.driver.category, self.car.categories = 'd', 'D'
        self.assertTrue(self.car.check_for_capability())
        self.car.driver.category, self.car.categories = 'b', 'e'
        self.assertTrue(self.car.check_for_capability())
