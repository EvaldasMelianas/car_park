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
        self.assertEqual(54, self.object.calculate_cost_for_amount(20, 100))
        self.assertEqual(54, self.object.calculate_cost_for_amount(20, 100))
        self.assertEqual(54, self.object.calculate_cost_for_amount(20, 100))

if __name__ == '__main__':
    unittest.main()
