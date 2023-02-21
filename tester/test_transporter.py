from constant.car_constant import *
import unittest


class TestTransporter(unittest.TestCase):

    def setUp(self):
        self.object = b

    def test_required_for_transport(self):
        self.assertEqual(15, self.object.required_for_amount_passengers(120))
        self.assertEqual(2, self.object.required_for_amount_passengers(9))
        self.assertEqual(4, self.object.required_for_amount_passengers(32))

    def test_calculate_cost_for_amount(self):
        self.assertEqual(54, self.object.calculate_cost_for_amount(16, 150))
        self.assertEqual(24.03, round(self.object.calculate_cost_for_amount(4, 133.5), 2))
        self.assertEqual(352.08, self.object.calculate_cost_for_amount(30, 489))
