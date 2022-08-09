class Vehicle:

    ##using init to initialize the code and reuse them later as per the needs
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


##storing the class in test
test = Vehicle(100, 60)

##printing out max_speed and mileage
print(test.max_speed)
print(test.mileage)
