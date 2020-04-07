from L3Ex23 import CarLot


class Vehicle(CarLot):
    bicycle = 4
    cars = 6

    def __init__(self, bicycle, cars):
        self.bicycle = bicycle
        self.cars = cars

    def set_bicycle(self, bicycle):
        self.bicycle = bicycle

    def set_cars(self, cars):
        self.cars = cars

    def get_bicycle(self):
        return self.bicycle

    def get_cars(self):
        return self.cars


vehicle = Vehicle(bicycle, cars)
vehicle.cars(cars)
