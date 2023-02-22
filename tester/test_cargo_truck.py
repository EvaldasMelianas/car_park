from data_classes.cargo_truck import CargoTruck
from datetime import datetime
import unittest


class TestCargoTruck(unittest.TestCase):

    def setUp(self):
        self.object = CargoTruck(yearly_mileage=50000, plate_number="ZXK452", fuel_type="Diesel", exploit_cost=10000.0,
                                 service_at_date=datetime(2022, 12, 13), categories="C",
                                 fuel_consumption=25.0, insure_at_date=datetime(2022, 12, 13),
                                 max_weight=10, trailer_weight=8)

    def test_calculate_trips(self):
        self.assertEqual((4, 4), self.object.calculate_trips(71))
        self.object.max_weight, self.object.trailer_weight = 20, 1
        self.assertEqual((10, 10), self.object.calculate_trips(210))
        self.object.max_weight, self.object.trailer_weight = 8, 0
        self.assertEqual((3, 0), self.object.calculate_trips(24))
        self.object.max_weight, self.object.trailer_weight = 2100, 300
        self.assertNotEqual((209, 204), self.object.calculate_trips(500000))
