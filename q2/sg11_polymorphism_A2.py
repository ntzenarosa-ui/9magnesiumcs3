# 1. a. What is duck typing, as explained in the video? 
#       Duck typing is another way of achieving polymorphism besides Inheritance.
#    b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
#       The Car class must have the minimum necessary attributes/methods.
# 2.

#Creates Car class
class Car:
    def move(self):
        print("The car drives on the road.")

#Creates Boat class
class Boat:
    def move(self):
        print("The boat sails on water.")

#Creates Drone class
class Drone:
    def move(self):
        print("The drone flies in the sky.")

# Calls vehicle.move()
def start_trip(vehicle):
    vehicle.move()

# Creates Objects
car = Car()
boat = Boat()
drone = Drone()

# Call each object
start_trip(car)
start_trip(boat)
start_trip(drone)