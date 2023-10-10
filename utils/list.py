from utils.expenses import ExpensesManager
from utils.insurance import InsuranceManager
from utils.maintenance import MaintenanceScheduler
from utils.service import ServiceHistory
from utils.diagnostics import DiagnosticsManager

def list_expenses(car_id, car_manager):
    """
    List expenses for a specific car.

    Args:
        car_id (int): The ID of the car.

    Returns:
        list: A list of expense entries for the car.
    """
   
    expenses_manager = ExpensesManager(car_manager)
    expenses = expenses_manager.list_expenses(car_id)
    return expenses

def list_insurance(car_id, car_manager):
    """
    List insurance details for a specific car.

    Args:
        car_id (int): The ID of the car.

    Returns:
        list: A list of insurance entries for the car.
    """
    
    insurance_manager = InsuranceManager(car_manager)
    insurance_entries = insurance_manager.list_insurance(car_id)
    return insurance_entries

def list_scheduled_maintenance(car_id, car_manager):
    """
    List scheduled maintenance for a specific car.

    Args:
        car_id (int): The ID of the car.

    Returns:
        list: A list of scheduled maintenance entries for the car.
    """
    
    maintenance_scheduler = MaintenanceScheduler(car_manager)
    maintenance_entries = maintenance_scheduler.list_scheduled_maintenance(car_id)
    return maintenance_entries

def list_service_history(car_id, car_manager):
    """
    List service history for a specific car.

    Args:
        car_id (int): The ID of the car.

    Returns:
        list: A list of service history entries for the car.
    """
    
    service_history_manager = ServiceHistory(car_manager)
    service_history_entries = service_history_manager.list_service_history(car_id)
    return service_history_entries

def list_diagnostics(car_id, car_manager):
    """
    List diagnostic information for a specific car.

    Args:
        car_id (int): The ID of the car.

    Returns:
        list: A list of diagnostic entries for the car.
    """
    
    diagnostics_manager = DiagnosticsManager(car_manager)
    diagnostic_entries = diagnostics_manager.list_diagnostics(car_id)
    return diagnostic_entries
