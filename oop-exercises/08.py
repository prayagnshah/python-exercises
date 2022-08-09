class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)

##using the isinstance() function to find that vehicle is a part of main class or not
##output will be in the boolean terms

print(isinstance(School_bus, Vehicle))
