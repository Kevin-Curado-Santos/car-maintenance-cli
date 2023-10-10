import json

class Car:
    def __init__(self, data_file):
        self.data_file = data_file
        self.cars = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.cars, file, indent=4)

    def add_car(self, make, model, year, vin, purchase_date):
        car_id = len(self.cars) + 1
        car = {
            'id': car_id,
            'make': make,
            'model': model,
            'year': year,
            'vin': vin,
            'purchase_date': purchase_date
        }
        self.cars.append(car)
        self.save_data()
        return car_id

    def get_car(self, car_id):
        for car in self.cars:
            if car['id'] == car_id:
                return car
        return None

    def list_cars(self):
        return self.cars

    def delete_car(self, car_id):
        car = self.get_car(car_id)
        if car:
            self.cars.remove(car)
            self.save_data()
        else:
            print(f"Car with ID {car_id} not found.")
