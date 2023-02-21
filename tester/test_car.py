from constant.car_constant import a, b, c
from datetime import datetime
import unittest


class TestCar(unittest.TestCase):

    def setUp(self):
        self.object1 = a
        self.object2 = b
        self.object3 = c
        self.object1.today = datetime.strptime("2022-02-20", "%Y-%m-%d")
        self.object2.today = datetime.strptime("2022-02-20", "%Y-%m-%d")
        self.object3.today = datetime.strptime("2022-02-20", "%Y-%m-%d")

    def test_needs_insurance(self):
        self.assertTrue(self.object1.needs_insurance())
        self.assertFalse(self.object2.needs_insurance())
        self.assertFalse(self.object3.needs_insurance())

    def test_needs_service(self):
        self.assertTrue(self.object1.needs_service())
        self.assertFalse(self.object2.needs_service())
        self.assertFalse(self.object3.needs_service())

    def test_cost_by_driving(self):
        self.assertEqual(self.object1.cost_of_driving(150, 1.8), 46.25)
        self.object2.fuel_consumption = 15
        self.assertEqual(self.object2.cost_of_driving(150, 1.8), 46.06)
        self.object3.yearly_mileage, self.object3.exploit_cost = 69000, 12000
        self.assertEqual(self.object3.cost_of_driving(150, 1.8), 73.25)

if __name__ == '__main__':
    unittest.main()
