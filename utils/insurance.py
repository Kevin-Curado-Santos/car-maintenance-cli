import datetime

class InsuranceManager:
    def __init__(self, car_manager):
        self.car_manager = car_manager

    def add_insurance(self, car_id, policy_number, provider, premium_amount):
        """
        Add insurance details for a specific car.
        Args:
            car_id (int): The ID of the car for which to add insurance details.
            policy_number (str): The policy number.
            provider (str): The insurance provider's name.
            start_date (str): The start date of the insurance coverage in YYYY-MM-DD format.
            end_date (str): The end date of the insurance coverage in YYYY-MM-DD format.
            premium_amount (float): The premium amount for the insurance policy.

        Returns:
            bool: True if adding insurance details is successful, False otherwise.
        """
        
        start_date = datetime.date.today().strftime("%Y-%m-%d")
        end_date = (datetime.date.today() + datetime.timedelta(days=365)).strftime("%Y-%m-%d")
        
        car = self.car_manager.get_car(car_id)
        if car:
            if 'insurance' not in car:
                car['insurance'] = []

            car['insurance'].append({
                'policy_number': policy_number,
                'provider': provider,
                'start_date': start_date,
                'end_date': end_date,
                'premium_amount': premium_amount
            })

            self.car_manager.save_data()
            print(f"Insurance details added for {car['make']} {car['model']} ({start_date} - {end_date}).")
            return True
        else:
            print(f"Car with ID {car_id} not found.")
            return False

    def list_insurance(self, car_id):
        """
        List insurance details for a specific car.
        Args:
            car_id (int): The ID of the car for which to list insurance details.
        """
        car = self.car_manager.get_car(car_id)
        if car and 'insurance' in car:
            print(f"Insurance details for {car['make']} {car['model']} (ID: {car_id}):")
            for insurance_entry in car['insurance']:
                print(f"Policy Number: {insurance_entry['policy_number']}")
                print(f"Provider: {insurance_entry['provider']}")
                print(f"Coverage Period: {insurance_entry['start_date']} to {insurance_entry['end_date']}")
                print(f"Premium Amount: {insurance_entry['premium_amount']:.2f} EUR")
                print()
        else:
            print(f"Car with ID {car_id} not found or no insurance details recorded.")
