#Author: Moleboheng Madela
#Date: 2025-04-15
#Activity 2: Polymorphism Challenge:

# Step 1: Define the base class Vehicle

class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Car class overrides move()
class Car(Vehicle):
    def move(self):
        print("Driving on the road.")

# Plane class overrides move()
class Plane(Vehicle):
    def move(self):
        print("Flying in the sky.")

# Boat class overrides move()
class Boat(Vehicle):
    def move(self):
        print("Sailing on water.")

# This function accepts any type of vehicle and calls its move method
def travel(vehicle):
    vehicle.move()  # Polymorphism in action — method changes based on object type

# Step 3: Create instances of each vehicle
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Step 4: Use the same function for different vehicle types
print("\nPolymorphism Demo:")
travel(my_car)     # Calls Car.move()
travel(my_plane)   # Calls Plane.move()
travel(my_boat)    # Calls Boat.move()

