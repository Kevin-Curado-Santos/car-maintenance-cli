import datetime

class ExpensesManager:
    def __init__(self, car_manager):
        self.car_manager = car_manager

    def add_expense(self, car_id, date, description, amount):
        """
        Add an expense related to a specific car.
        Args:
            car_id (int): The ID of the car for which to add the expense.
            date (str): The date of the expense in YYYY-MM-DD format.
            description (str): A description of the expense.
            amount (float): The cost of the expense.

        Returns:
            bool: True if adding the expense is successful, False otherwise.
        """
        
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return False
        
        car = self.car_manager.get_car(car_id)
        if car:
            # Initialize the expenses list if it doesn't exist
            if 'expenses' not in car:
                car['expenses'] = []

            car['expenses'].append({
                'date': date,
                'description': description,
                'amount': amount
            })

            self.car_manager.save_data()
            print(f"Expense added for {car['make']} {car['model']} on {date}.")
            return True
        else:
            print(f"Car with ID {car_id} not found.")
            return False

    def list_expenses(self, car_id):
        """
        List expenses related to a specific car.
        Args:
            car_id (int): The ID of the car for which to list expenses.
        """
        car = self.car_manager.get_car(car_id)
        if car and 'expenses' in car:
            print(f"Expenses for {car['make']} {car['model']} (ID: {car_id}):")
            for expense in car['expenses']:
                print(f"Date: {expense['date']}, Description: {expense['description']}, Amount: {expense['amount']:.2f} EUR")
        else:
            print(f"Car with ID {car_id} not found or no expenses recorded.")
