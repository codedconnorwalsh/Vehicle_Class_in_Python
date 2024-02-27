# vehiclClass.py
'''
Vehicle Class
this class models a vehicle on a used car lot
'''

# constructor is called when an object is instantiated
class Vehicle:
    def __init__(self, type, max_speed = None):
        self.type = type;
        # self._thisisprivate = 42 # this is a weak attempt to "support" data hiding
        self.max_speed = max_speed;
    def printType(self):
        print(self.type);
        
    def getSpeed(self):
        return self.max_speed
    
if __name__ == "__main__":
# Some code to test the class would go here.
# If there's no code, just pass
    pass