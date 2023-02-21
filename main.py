from data_classes.car import Car
from data_classes.transporter import Transporter
from data_classes.cargo_truck import CargoTruck
from datetime import datetime


car = Car(yearly_mileage=69000, plate_number="GFD532", fuel_type="Diesel",
          exploit_cost=12000.0, serviced_at_date=datetime(2022, 12, 13),
          categories="B", fuel_consumption=15, insured_at_date=datetime(2022, 12, 13))

transporter = Transporter(yearly_mileage=50000, plate_number="ASD123", fuel_type="Diesel",
                          exploit_cost=9000.0,serviced_at_date=datetime(2022, 12, 13),
                          categories="D",fuel_consumption=11.0,
                          insured_at_date=datetime(2022, 12, 13), passenger_seats=8)

cargo_truck = CargoTruck(yearly_mileage=50000, plate_number="ZXK452", fuel_type="Diesel", exploit_cost=10000.0,
                         serviced_at_date=datetime(2022, 12, 13), categories="C",
                         fuel_consumption=25.0, insured_at_date=datetime(2022, 12, 13),
                         max_weight=8, trailer_weight=0)

#print(car.needs_insurance())
#print(car.needs_service())
#print(transporter.required_for_amount_passengers(120))
#print(car.cost_of_driving(150, 1.8))
#print(transporter.required_for_amount_passengers(16))
#print(transporter.calculate_cost_for_amount(16, 100))
#print(cargo_truck.calculate_trips(24))
