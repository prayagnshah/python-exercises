class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


##inheriting the class bus under Vehicle
class Bus:
    pass


##assigning the value for class Vehicle
info = Vehicle("School Volvo", 180, 12)


print("Vehicle Name: ", info.name, "Speed: ", info.max_speed, "Mileage: ", info.mileage)
