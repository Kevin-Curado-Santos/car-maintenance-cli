import datetime

class MaintenanceScheduler:
    def __init__(self, car_manager):
        self.car_manager = car_manager

    def schedule_maintenance(self, car_id, task, due_date):
        """
        Schedule a maintenance task for a specific car.
        Args:
            car_id (int): The ID of the car to schedule maintenance for.
            task (str): The description of the maintenance task (e.g., "Oil Change").
            due_date (str): The due date for the maintenance task in YYYY-MM-DD format.

        Returns:
            bool: True if scheduling is successful, False otherwise.
        """
        
        try:
            due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return False

        car = self.car_manager.get_car(car_id)
        if car:
            if 'maintenance_schedule' not in car:
                car['maintenance_schedule'] = []

            car['maintenance_schedule'].append({
                'task': task,
                'due_date': due_date.strftime('%Y-%m-%d')
            })

            car['last_maintenance_date'] = due_date.strftime('%Y-%m-%d')

            self.car_manager.save_data()
            print(f"Maintenance task '{task}' scheduled for {car['make']} {car['model']} on {due_date}.")
            return True
        else:
            print(f"Car with ID {car_id} not found.")
            return False

    def list_scheduled_maintenance(self, car_id):
        """
        List all scheduled maintenance tasks for a specific car.
        Args:
            car_id (int): The ID of the car to list maintenance tasks for.
        """
        car = self.car_manager.get_car(car_id)
        if car and 'maintenance_schedule' in car:
            print(f"Scheduled maintenance tasks for {car['make']} {car['model']} (ID: {car_id}):")
            for task_info in car['maintenance_schedule']:
                print(f"Task: {task_info['task']}, Due Date: {task_info['due_date']}")
        else:
            print(f"Car with ID {car_id} not found or no maintenance tasks scheduled.")

    def check_due_maintenance(self):
        """
        Check for due maintenance tasks and provide reminders.
        """
        today = datetime.date.today()
        cars = self.car_manager.list_cars()

        for car in cars:
            if 'maintenance_schedule' in car:
                for task_info in car['maintenance_schedule']:
                    due_date = datetime.datetime.strptime(task_info['due_date'], '%Y-%m-%d').date()
                    if due_date < today:
                        print(f"Reminder: Maintenance task '{task_info['task']}' for {car['make']} {car['model']} (ID: {car['id']}) was due on {due_date}.")
                    elif due_date == today:
                        print(f"Reminder: Maintenance task '{task_info['task']}' for {car['make']} {car['model']} (ID: {car['id']}) is due today.")
                    else:
                        print(f"Reminder: Maintenance task '{task_info['task']}' for {car['make']} {car['model']} (ID: {car['id']}) is due on {due_date}.")