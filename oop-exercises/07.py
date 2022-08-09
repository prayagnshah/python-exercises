class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)

## using the function type to find its attribute
print(type(School_bus))

##ouput

# '__main__.Bus' which means that it belongs to main class Vehicle and subclass Bus
