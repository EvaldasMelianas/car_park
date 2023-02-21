from constant.car_constant import *
import unittest


class TestCargoTruck(unittest.TestCase):

    def setUp(self):
        self.object = c

    def test_calculate_trips(self):
        self.assertEqual((4, 4), c.calculate_trips(71))
        self.assertEqual((7, 7), c.calculate_trips(120))
        self.assertEqual((1, 0), c.calculate_trips(10))
        self.assertEqual((10, 10), c.calculate_trips(180))
