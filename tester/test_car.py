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
        self.assertEqual(46.25, self.object1.cost_of_driving(150, 1.8))
        self.assertEqual(80.26, self.object2.cost_of_driving(399.5, 1.7))
        self.assertEqual(4088.52, self.object3.cost_of_driving(10273, 1.59))
