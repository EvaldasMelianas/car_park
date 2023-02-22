from data_classes.transporter import Transporter
from datetime import datetime
import unittest


class TestTransporter(unittest.TestCase):

    def setUp(self):
        self.transporter = Transporter(yearly_mileage=50000, plate_number="ASD123", fuel_type="Diesel",
                                       exploit_cost=9000.0, service_at_date=datetime(2022, 12, 13),
                                       categories="D", fuel_consumption=11.0,
                                       insure_at_date=datetime(2022, 12, 13), passenger_seats=8)

    def test_required_for_transport(self):
        self.assertEqual(15, self.transporter.required_for_amount_passengers(120))
        self.transporter.passenger_seats = 50
        self.assertEqual(1, self.transporter.required_for_amount_passengers(28))
        self.transporter.passenger_seats = 4
        self.assertEqual(929, self.transporter.required_for_amount_passengers(3716))

    def test_calculate_cost_for_amount(self):
        self.assertEqual(54, self.transporter.calculate_cost_for_amount(16, 150))
        self.transporter.yearly_mileage, self.transporter.exploit_cost, self.transporter.fuel_consumption\
            = 120000, 15000, 10
        self.assertEqual(16.625, self.transporter.calculate_cost_for_amount(4, 133), 2)
        self.transporter.yearly_mileage, self.transporter.exploit_cost, self.transporter.fuel_consumption\
            = 1, 1, 1
        self.assertNotEqual(1956.0, self.transporter.calculate_cost_for_amount(30, 489))
