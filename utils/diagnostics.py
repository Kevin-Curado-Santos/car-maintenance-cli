import datetime

class DiagnosticsManager:
    def __init__(self, car_manager):
        self.car_manager = car_manager

    def record_diagnostics(self, car_id, date, diagnostic_code, description):
        """
        Record car diagnostics and error codes for a specific car.
        Args:
            car_id (int): The ID of the car for which to record diagnostics.
            date (str): The date when the diagnostics were recorded in YYYY-MM-DD format.
            diagnostic_code (str): The diagnostic code or error code.
            description (str): A description of the diagnostics or error.

        Returns:
            bool: True if recording diagnostics is successful, False otherwise.
        """
        
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return False
        
        car = self.car_manager.get_car(car_id)
        if car:
            if 'diagnostics' not in car:
                car['diagnostics'] = []

            car['diagnostics'].append({
                'date': date,
                'diagnostic_code': diagnostic_code,
                'description': description
            })

            self.car_manager.save_data()
            print(f"Diagnostics recorded for {car['make']} {car['model']} on {date}.")
            return True
        else:
            print(f"Car with ID {car_id} not found.")
            return False

    def list_diagnostics(self, car_id):
        """
        List car diagnostics and error codes for a specific car.
        Args:
            car_id (int): The ID of the car for which to list diagnostics.
        """
        car = self.car_manager.get_car(car_id)
        if car and 'diagnostics' in car:
            print(f"Diagnostics for {car['make']} {car['model']} (ID: {car_id}):")
            for diagnostic in car['diagnostics']:
                print(f"Date: {diagnostic['date']}, Diagnostic Code: {diagnostic['diagnostic_code']}")
                print(f"Description: {diagnostic['description']}")
                print()
        else:
            print(f"Car with ID {car_id} not found or no diagnostics recorded.")

