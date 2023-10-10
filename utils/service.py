import datetime

class ServiceHistory:
    def __init__(self, car_manager):
        self.car_manager = car_manager

    def record_service(self, car_id, service_provider, service_date, description, cost):
        """
        Record a service performed on a specific car.
        Args:
            car_id (int): The ID of the car on which the service was performed.
            service_provider (str): The name of the service provider or workshop.
            service_date (str): The date when the service was performed in YYYY-MM-DD format.
            description (str): A description of the service performed.
            cost (float): The cost of the service.

        Returns:
            bool: True if recording is successful, False otherwise.
        """
        
        try:
            service_date = datetime.datetime.strptime(service_date, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return False

        car = self.car_manager.get_car(car_id)
        if car:
            if 'service_history' not in car:
                car['service_history'] = []

            service_entry = {
                'service_provider': service_provider,
                'service_date': service_date.strftime('%Y-%m-%d'),
                'description': description,
                'cost': cost
            }

            car['service_history'].append(service_entry)
            self.car_manager.save_data()
            print(f"Service recorded for {car['make']} {car['model']} on {service_date}.")
            return True
        else:
            print(f"Car with ID {car_id} not found.")
            return False

    def list_service_history(self, car_id):
        """
        List the service history for a specific car.
        Args:
            car_id (int): The ID of the car for which to list service history.
        """
        car = self.car_manager.get_car(car_id)
        if car and 'service_history' in car:
            print(f"Service History for {car['make']} {car['model']} (ID: {car_id}):")
            for service_entry in car['service_history']:
                print(f"Service Date: {service_entry['service_date']}, Service Provider: {service_entry['service_provider']}")
                print(f"Description: {service_entry['description']}, Cost: {service_entry['cost']:.2f} EUR")
                print()
        else:
            print(f"Car with ID {car_id} not found or no service history recorded.")