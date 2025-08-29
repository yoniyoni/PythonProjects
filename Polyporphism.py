# Base class
class Vehicle:
    def move(self):
        pass  # This will be overridden in child classes

# Child classes with different behavior
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Demonstrate polymorphism
vehicles = [Car(), Plane(), Bicycle()]

for v in vehicles:
    v.move()  # Same method name, different behavior depending on the object
