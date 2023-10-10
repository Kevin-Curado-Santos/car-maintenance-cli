import utils.car as car
import os


print("Car Manager CLI")
file = 'data/cars.json'
if not os.path.exists(file) or os.path.getsize(file) == 0:
    with open(file, 'w') as f:
        f.write('[]')
car_manager = car.Car('data/cars.json')

# call car.py
car_id = car_manager.add_car('Toyota', 'Camry', 2018, '12345678901234567', '2020-01-01')
car_manager.get_car(car_id)
car_manager.list_cars()
print()



print("Maintenance Manager CLI")
# call maintenance.py
import utils.maintenance as maintenance

maintenance_manager = maintenance.MaintenanceScheduler(car_manager)
maintenance_manager.schedule_maintenance(car_id, 'Oil Change', '2022-01-15')
maintenance_manager.list_scheduled_maintenance(car_id)
maintenance_manager.check_due_maintenance()
print()

    

print("Fuel Manager CLI")
# call fuel.py 
import utils.fuel as fuel

fuel_manager = fuel.FuelTracker(car_manager)
# fill up twice 
fuel_manager.log_fuel_fillup(car_id, '2020-01-01', 10000, 'Regular', 1.25, 50)
fuel_manager.log_fuel_fillup(car_id, '2020-01-15', 10500, 'Regular', 1.25, 40)
fuel_manager.calculate_fuel_efficiency(car_id)
print()



print("Service Manager CLI")
# call service.py
import utils.service as service

service_manager = service.ServiceHistory(car_manager)
service_manager.record_service(car_id, 'My Garage', '2020-01-01', 'Oil Change', 50)
service_manager.list_service_history(car_id)
print()



print("Expenses Manager CLI")
# call expenses.py
import utils.expenses as expenses

expenses_manager = expenses.ExpensesManager(car_manager)
expenses_manager.add_expense(car_id, '2020-01-01', 'Car Wash', 10)
expenses_manager.list_expenses(car_id)
print()



print("Diagnostics Manager CLI")
# call disgnostics.py
import utils.diagnostics as diagnostics

diagnostics_manager = diagnostics.DiagnosticsManager(car_manager)
diagnostics_manager.record_diagnostics(car_id, '2020-01-01', 'P0123', 'Engine light on')
diagnostics_manager.list_diagnostics(car_id)
print()

print("Insurance Manager CLI")
# call insurance.py
import utils.insurance as insurance

insurance_manager = insurance.InsuranceManager(car_manager)
insurance_manager.add_insurance(1, 'ABC123XYZ', 'Insurance Co. A', '2022-01-01', '2023-01-01', 800.0)
insurance_manager.list_insurance(car_id)
print()

# remove car
car_manager.delete_car(car_id)
car_manager.list_cars()
