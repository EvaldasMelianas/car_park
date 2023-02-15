from data_classes.car import Car
from data_classes.transporter import Transporter
from data_classes.cargo_truck import CargoTruck
from datetime import datetime


a = Car(yearly_mileage=20000, plate_number="GFD532", fuel_type="Diesel", exploit_cost=6000.0,
        serviced_at_date=datetime.strptime("2022-12-13", "%Y-%m-%d"),
        categories="B", fuel_consumption=8.0, insured_at_date=datetime.strptime("2022-12-13", "%Y-%m-%d"))
b = Transporter(yearly_mileage=50000, plate_number="ASD123", fuel_type="Diesel", exploit_cost=9000.0,
                serviced_at_date=datetime.strptime("2022-02-13", "%Y-%m-%d"), categories="D",
                fuel_consumption=11.0, insured_at_date=datetime.strptime("2022-12-13", "%Y-%m-%d"), passenger_seats=8)
c = CargoTruck(yearly_mileage=50000, plate_number="ZXK452", fuel_type="Diesel", exploit_cost=10000.0,
               serviced_at_date=datetime.strptime("2022-12-13", "%Y-%m-%d"), categories="C",
               fuel_consumption=25.0, insured_at_date=datetime.strptime("2022-12-13", "%Y-%m-%d"),
               max_weight=10, trailer_weight=8)

#print(a.needs_service())
#print(b.cost_of_driving(150, 1.8))
#print(b.required_for_amount_passengers(16))
#print(b.calculate_cost_for_amount(16, 100))
#print(c.calculate_trips(20))
