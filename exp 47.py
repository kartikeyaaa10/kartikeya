class Vehicle:
    def fuel_type(self):
        print("General fuel type: Petrol/Diesel/Electric")

class Car(Vehicle):
    def fuel_type(self):
        print("Car fuel type: ev")

v = Vehicle()
v.fuel_type() 

c = Car()
c.fuel_type()  