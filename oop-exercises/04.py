class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


##inheriting the class Bus in vehicle
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):

        ##returning the constant value 50 and mandatory step
        return super().seating_capacity(capacity=50)


##assigning the values in school_bus
School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())
