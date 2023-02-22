from data_classes.driver import Driver
from data_classes.car import Car
from data_classes.transporter import Transporter
from data_classes.cargo_truck import CargoTruck
from datetime import datetime



car = Car(yearly_mileage=69000, plate_number="GFD532", fuel_type="Diesel",
          exploit_cost=12000.0, service_at_date=datetime(2024, 12, 13),
          categories="B", fuel_consumption=15, insure_at_date=datetime(2023, 12, 13))

transporter = Transporter(yearly_mileage=50000, plate_number="ASD123", fuel_type="Diesel",
                          exploit_cost=9000.0, service_at_date=datetime(2024, 12, 13),
                          categories="D", fuel_consumption=11.0,
                          insure_at_date=datetime(2023, 12, 13), passenger_seats=8)

cargo_truck = CargoTruck(yearly_mileage=50000, plate_number="ZXK452", fuel_type="Diesel", exploit_cost=10000.0,
                         service_at_date=datetime(2024, 12, 13), categories="E",
                         fuel_consumption=25.0, insure_at_date=datetime(2023, 12, 13),
                         max_weight=20, trailer_weight=1)

car.driver = Driver(vacation=(datetime(2023, 2, 15)), category='B', pay_km=0.3, vacation_duration=5)
transporter.driver = Driver(vacation=(datetime(2023, 2, 15)), category='D', pay_km=0.3, vacation_duration=5)
cargo_truck.driver = Driver(vacation=(datetime(2023, 2, 15)), category='E', pay_km=0.3, vacation_duration=5)
