import datetime

class FuelTracker:
    def __init__(self, car_manager):
        self.car_manager = car_manager

    def log_fuel_fillup(self, car_id, date, odometer_reading, fuel_type, cost_per_unit, units_filled):
        """
        Log a fuel fill-up for a specific car.
        Args:
            car_id (int): The ID of the car for which to log the fuel fill-up.
            date (str): The date of the fuel fill-up in YYYY-MM-DD format.
            odometer_reading (float): The odometer reading at the time of the fill-up.
            fuel_type (str): The type of fuel used (e.g., "Regular", "Premium").
            cost_per_unit (float): The cost per unit of fuel (e.g., price per liter).
            units_filled (float): The number of units filled (e.g., liters).

        Returns:
            bool: True if logging is successful, False otherwise.
        """
        
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return False

        car = self.car_manager.get_car(car_id)
        if car:
            if 'fuel_log' not in car:
                car['fuel_log'] = []

            fuel_entry = {
                'date': date.strftime('%Y-%m-%d'),
                'odometer_reading': odometer_reading,
                'fuel_type': fuel_type,
                'cost_per_unit': cost_per_unit,
                'units_filled': units_filled
            }
            
            car['fuel_log'].append(fuel_entry)
            self.car_manager.save_data()
            print(f"Fuel fill-up logged for {car['make']} {car['model']} on {date}.")
            return True
        else:
            print(f"Car with ID {car_id} not found.")
            return False

    def calculate_fuel_efficiency(self, car_id):
        """
        Calculate and display the fuel efficiency for a specific car in the metric system.
        Args:
            car_id (int): The ID of the car for which to calculate fuel efficiency.
        """
        car = self.car_manager.get_car(car_id)
        if car and 'fuel_log' in car:
            fuel_log = car['fuel_log']
            if len(fuel_log) >= 2:
                first_fillup = fuel_log[0]
                latest_fillup = fuel_log[-1]
                distance_traveled = latest_fillup['odometer_reading'] - first_fillup['odometer_reading']
                fuel_used = sum(entry['units_filled'] for entry in fuel_log)
                fuel_efficiency = (fuel_used / distance_traveled) * 100

                print(f"Fuel Efficiency for {car['make']} {car['model']} (ID: {car_id}):")
                print(f"Distance Traveled: {distance_traveled} km")
                print(f"Fuel Used: {fuel_used} liters")
                print(f"Fuel Efficiency: {fuel_efficiency:.2f} L/100 km")
            else:
                print(f"At least two fuel fill-ups are required to calculate fuel efficiency for {car['make']} {car['model']}.")
        else:
            print(f"Car with ID {car_id} not found or no fuel fill-ups logged.")