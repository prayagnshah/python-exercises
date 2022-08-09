class Vehicle:

    ##defining a class variable which needs to be constant
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


school = Vehicle(" School Volvo", 180, 12)
car = Car("Audi Q5", 240, 18)
print(school.color, school.name, school.max_speed, school.mileage)
print(car.color, car.name, car.max_speed, car.mileage)
