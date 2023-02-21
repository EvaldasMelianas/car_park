from data_classes.car import Car
from datetime import datetime
import unittest


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car(yearly_mileage=69000, plate_number="GFD532", fuel_type="Diesel",
                       exploit_cost=12000.0, serviced_at_date=datetime(2022, 12, 13),
                       categories="B", fuel_consumption=15, insured_at_date=datetime(2022, 12, 13))
        self.car.today = datetime(2023, 2, 21)

    def test_needs_insurance(self):
        self.assertFalse(self.car.needs_insurance())
        self.car.insured_at_date = datetime(2021, 12, 13)
        self.assertTrue(self.car.needs_insurance())
        self.car.insured_at_date = datetime(1989, 2, 21)
        self.assertTrue(self.car.needs_insurance())

    def test_needs_service(self):
        self.assertFalse(self.car.needs_service())
        self.car.serviced_at_date = datetime(2021, 2, 21)
        self.assertTrue(self.car.needs_service())
        self.car.serviced_at_date = datetime(2056, 6, 13)
        self.assertFalse(self.car.needs_service())

    def test_cost_by_driving(self):
        self.assertEqual(46.25, self.car.cost_of_driving(150, 1.8))
        self.car.yearly_mileage, self.car.exploit_cost, self.car.fuel_consumption = 53240, 9865, 8.6
        self.assertEqual(63.8, self.car.cost_of_driving(399.5, 1.7))
        self.car.yearly_mileage, self.car.exploit_cost, self.car.fuel_consumption = 1000, 36.2, 100
        self.assertNotEqual(16361.69, self.car.cost_of_driving(10273, 1.59))
