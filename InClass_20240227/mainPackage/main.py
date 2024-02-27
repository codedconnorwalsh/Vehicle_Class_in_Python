# main.py

from vehiclePackage.vehicleClass import *

if __name__ == "__main__":
    # instantiate an object of type vehicle
    myCorvette = Vehicle("Car", 120)
    myCorvette.printType()
    
    maximum_speed = myCorvette.getSpeed()
    print("Maximum speed:", maximum_speed)
    
    myPontiac = Vehicle("Car", 100)
    mySpeedboat = Vehicle("Boat", 170)
    myApollo = Vehicle("Spaceship", 17600)
    
    myVehicleList = [myPontiac, mySpeedboat, myApollo]
    
    for Vehicle in myVehicleList:
        Vehicle.printType()
        print(Vehicle.getSpeed())