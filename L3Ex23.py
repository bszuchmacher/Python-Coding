class CarLot:
    floors = 0
    total_spots = 0

    def __init__(self, floors, total_spots):
        self.floors = floors
        self.totalspots = total_spots

    def set_floors(self, floors_val):
        self.floors = floors_val

    def set_total_spots(self, total_spots):
        self.total_spots = total_spots

    def get_floors(self):
        return self.floors

    def get_total_spots(self):
        return self.total_spots

my_carlot = CarLot(4, 30)
print(my_carlot.get_total_spots())

# #3===
# Build class vehicle:
# b) Build getters and setters

class Vehicle:
    powered = 0
    human = 0

    def __init__(self, powered, human):
        self.powered = powered
        self.human = human

    def set_powered(self, powered_val):
        self.powered = powered_val

    def set_human(self, human):
        self.human = human

    def get_powered(self):
        return self.powered

    def get_human(self):
        return self.human


my_vehicle = Vehicle (0, 30)
print(my_vehicle.get_human())

#4

# Build classes bike and car:
# a) Inherit from vehicle

