traffic_light = "Green"

class Vehicle:
    speed_limit = 60
    def __init__(self):
        pass
    def start_engine():
        print("Engine Started")

class Car(Vehicle):
    def __init__(self, make):
        self.make = make
    def start_engine():
        x = "Car"
        print(f'{x} engine started')

class Bike(Vehicle):
    def __init__(self, bike_type):
        self.type = bike_type
    def start_engine():
        y = "Bike"
        print(f'{y} engine started')

Vehicle.start_engine()
Car.start_engine()
Bike.start_engine()