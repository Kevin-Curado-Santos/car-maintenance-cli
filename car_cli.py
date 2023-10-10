import argparse
import os
import datetime
from utils.car import Car
from utils.fuel import FuelTracker
from utils.maintenance import MaintenanceScheduler
from utils.service import ServiceHistory
from utils.expenses import ExpensesManager
from utils.insurance import InsuranceManager
from utils.list import (
    list_expenses,
    list_insurance,
    list_scheduled_maintenance,
    list_service_history,
    list_diagnostics,
)

fuel_price_factors = {
    "gasoline 95": 1.559,  
    "gasoline 98": 1.778,  
    "diesel": 1.601,    
    "LPG": 0.727,
}

maintenance_types = [
    "oil change",
    "tire pressure check",
    "brake fluid change",
    "brake pad change", 
    "wheel alignment",
    "air filter change",
    "cabin filter change",
    "spark plug change",
    "timing belt change",
    "battery change"
]

services_provider = [
    "Audi",
    "BMW",
    "Mercedes",
    "Volkswagen",
    "Ford",
    "Toyota",
    "Honda",
    "Hyundai",
    "Renault",
    "Peugeot"
    "Garage Barloworld",
    "Garage Bosch",
    "Garage Continental",
    "Garage Delphi",
]

services_list = [
    ("oil change", 50),
    ("tire pressure check", 10),
    ("brake fluid change", 30),
    ("brake pad change", 50),
    ("wheel alignment", 30),
    ("air filter change", 20),
    ("cabin filter change", 20),
    ("spark plug change", 30),
    ("timing belt change", 100),
    ("battery change", 150)
]

def validate_year(year):
    year = int(year)
    if year not in range(1900, 2022):
        raise argparse.ArgumentTypeError(f"Invalid year: {year}. Please choose a year between 1900 and 2021.")
    return year

car_data_file = 'data/cars.json'
if not os.path.exists(car_data_file) or os.path.getsize(car_data_file) == 0:
    with open(car_data_file, 'w') as file:
        file.write('[]')
car_manager = Car(car_data_file)

fuel_tracker = FuelTracker(car_manager)
maintenance_scheduler = MaintenanceScheduler(car_manager)
service_history = ServiceHistory(car_manager)
expenses_manager = ExpensesManager(car_manager)
insurance_manager = InsuranceManager(car_manager)

parser = argparse.ArgumentParser(description="Car Maintenance CLI Assistant")

subparsers = parser.add_subparsers(title="Commands", dest="command")

add_car_parser = subparsers.add_parser("add", help="Add a new car")
add_car_parser.add_argument("make", type=str, help="Car make")
add_car_parser.add_argument("model", type=str, help="Car model")
add_car_parser.add_argument("year", type=validate_year, help="Car manufacturing year (choose from 1900 to 2021)")
add_car_parser.add_argument("vin", type=str, help="Car VIN (Vehicle Identification Number)")

add_car_parser.usage = "car_cli.py add <make> <model> <year> <vin>"

fuel_parser = subparsers.add_parser("fuel", help="Fuel-related commands")
fuel_parser.add_argument("car_id", type=int, help="Car ID")
fuel_parser.add_argument("eff", type=str, default="", nargs="?", help="Calculate fuel efficiency (km/l)")

maintenance_parser = subparsers.add_parser("maintenance", help="Maintenance-related commands")
maintenance_parser.add_argument("car_id", type=int, help="Car ID")

service_parser = subparsers.add_parser("service", help="Service-related commands")
service_parser.add_argument("car_id", type=int, help="Car ID")

expenses_parser = subparsers.add_parser("expenses", help="Expenses-related commands")
expenses_parser.add_argument("car_id", type=int, help="Car ID")

insurance_parser = subparsers.add_parser("insurance", help="Insurance-related commands")
insurance_parser.add_argument("car_id", type=int, help="Car ID")

list_parser = subparsers.add_parser("list", help="List car-related information")
list_parser.add_argument("car_id", type=int, help="Car ID")
list_parser.add_argument("category", type=str, choices=["expenses", "insurance", "maintenance", "service", "diagnostics"],
                        help="Category of information to list")

args = parser.parse_args()


if args.command == "fuel":
    car_id = args.car_id
    date = datetime.date.today().strftime("%Y-%m-%d")
    while True:
        odometer_reading = int(input("Enter odometer reading: "))
        if odometer_reading >= 0:
            break
        else:
            print("Invalid odometer reading. Please enter a positive integer.")
    while True:
        fuel_type = input("Enter fuel type (gasoline 95, gasoline 98, diesel, LPG): ")
        if fuel_type in fuel_price_factors:
            break
        else:
            print("Invalid fuel type. Please choose from the following: gasoline 95, gasoline 98, diesel, LPG")  
    while True:
        units_filled = float(input("Enter fuel amount (in liters): "))
        if units_filled > 0:
            break
        else:
            print("Invalid fuel amount. Please enter a positive number.")
    fuel_cost = units_filled * fuel_price_factors[fuel_type]

    fuel_tracker.log_fuel_fillup(car_id, date, odometer_reading, fuel_type, (fuel_price_factors[fuel_type]), units_filled)
    if args.eff == "eff":
        fuel_tracker.calculate_fuel_efficiency(car_id)
elif args.command == "maintenance":

    car_id = args.car_id
    print("Maintenance types:")
    for maintenance_type in maintenance_types:
        print(f"\t{maintenance_type}: {maintenance_types[maintenance_type]} EUR")
    maintenance_id = int(input("\nEnter maintenance type: (1-10)"))
    maintenance_type = maintenance_types[maintenance_id - 1]
    maintenance_date = input("Enter maintenance date (YYYY-MM-DD): ")

    maintenance_scheduler.schedule_maintenance(car_id, maintenance_type, maintenance_date)
elif args.command == "service":

    car_id = args.car_id
    print("Service providers:")
    for service_provider in services_provider:
        print(f"\t{service_provider}")
    service_provider = input("\nEnter service provider: ")
    print("Service types:")
    for service_type, service_cost in services_list:
        print(f"\t{service_type}: {service_cost} EUR")
    service_id = int(input("\nEnter service type: (1-10)"))
    description = services_list[service_id - 1][0]
    cost = services_list[service_id - 1][1]
    service_date = input("Enter service date (YYYY-MM-DD): ")

    service_history.record_service(car_id, service_provider, service_date, description, cost)
elif args.command == "expenses":

    car_id = args.car_id
    expense_type = input("Enter expense type: ")
    expense_amount = float(input("Enter expense amount: EUR"))
    expense_date = input("Enter expense date (YYYY-MM-DD): ")

    expenses_manager.add_expense(car_id, expense_type, expense_amount, expense_date)
elif args.command == "insurance":

    car_id = args.car_id
    policy_number = input("Enter policy number: ")
    provider = input("Enter insurance provider: ")
    premium_amount = float(input("Enter premium amount: EUR"))

    insurance_manager.add_insurance(car_id, policy_number, provider, premium_amount)
elif args.command == "add":

    make = args.make
    model = args.model
    year = args.year
    vin = args.vin


    car_manager.add_car(make, model, year, vin)

    print(f"New car '{make} {model}' added to your profile.")
elif args.command == "list":
    
    car_id = args.car_id
    category = args.category
    if category == "expenses":
        entries = list_expenses(car_id, car_manager)
    elif category == "insurance":
        entries = list_insurance(car_id, car_manager)
    elif category == "maintenance":
        entries = list_scheduled_maintenance(car_id, car_manager)
    elif category == "service":
        entries = list_service_history(car_id, car_manager)
    elif category == "diagnostics":
        entries = list_diagnostics(car_id, car_manager)
    else:
        print(f"Invalid category: {category}")
        entries = []

    if entries:
        print(f"{category.capitalize()} for Car ID {car_id}:")
        for entry in entries:
            print(entry)
    else:
        print(f"No {category} found for car with ID {car_id}")
else:
    parser.print_help()
