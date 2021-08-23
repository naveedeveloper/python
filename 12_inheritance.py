class Vehicle:
    def general_usage():
        print("General Use : Transportation")

# Inheritance
class Car(Vehicle):
    def __init__(self):
        print("I'm car.")
        self.wheels = 4
        self.has_roof = True

    def specfic_usage(self):
        print("Specific use : Family Trip , for work")

    def Properties(self):
        print("Number of Wheels : ",self.wheels)
        print("Has roof : ",self.has_roof)

class Bike(Vehicle):
    def __init__(self):
        print("I'm car.")
        self.wheels = 2
        self.has_roof = False

    def specfic_usage(self):
        print("Specific use : Trip")

    def Properties(self):
        print("Number of Wheels : ",self.wheels)
        print("Has roof : ",self.has_roof)


objB = Bike()

objB.Properties()
objB.general_usage() #Inherited Method
objB.specfic_usage()

objc = Car()

objc.Properties()
objc.general_usage()
objc.specfic_usage()

    

        