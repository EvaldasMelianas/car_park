from data_classes.car import Car
from data_classes.transporter import Transporter
from data_classes.cargo_truck import CargoTruck


a = Car(yearly_mileage=20000, plate_number="GFD532", fuel_type="Diesel", exploit_cost=6000.0,
        serviced_at_date="2022-12-13", categories="B", fuel_consumption=8.0, insured_at_date="2023-05-14")
b = Transporter(yearly_mileage=50000, plate_number="ASD123", fuel_type="Diesel", exploit_cost=9000.0,
                serviced_at_date="2022-12-29", categories="D",
                fuel_consumption=11.0, insured_at_date="2023-05-02", passenger_seats=8)
c = CargoTruck(yearly_mileage=50000, plate_number="ZXK452", fuel_type="Diesel", exploit_cost=10000.0,
               serviced_at_date="2022-02-01", categories="C", fuel_consumption=25.0, insured_at_date="2022-05-28",
               max_weight=12, trailer=True)

#print(b.needs_insurance())
#print(b.cost_of_driving(150, 1.8))
#print(b.required_for_amount_passengers(16))
#print(b.calculate_cost_for_amount(16, 100, 1.8))
print(c.calculate_trip(50))
