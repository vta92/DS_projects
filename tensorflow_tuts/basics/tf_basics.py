# pythonic.py
import math
import time
class Ring(object):
# class variables
    date = time.strftime("%Y-%m-%d", time.gmtime()) # today's date "YYYY-mm-dd" 
    center = 0.0 # center of the ring
    def __init__(self, date=date, metal="Copper", radius=5.0,
                price=5.0, quantity=5):
        """ init is not the constructor, but the initializer which
        initialize the instance variable
        self : is the instance
        __init__ takes the instance 'self' and populates it with the radius,
        metal, date etc. and store in a dictionary.
        self.radius, self.metal etc. are the instance variable which
        must be unique.
        """
        self.date = date
        self.metal = metal
        self.radius = radius
        self.price = price
        self.quantity = quantity
    def cost(self):
        return self.price * self.quantity
    def area(self):
        return math.pi * self.radius**2
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    
class Box(Ring):
    """ Modified perimeter for creating the box """
    def perimeter(self): # override the method 'perimeter' # perimeter is increased 2.0 times
        #return Ring.perimeter(self) * 2.0
        #result = super().perimeter()*2
        result= Ring.perimeter(self)*2
        return result
    
def main():
    r = Ring()
    print("Center of the Ring is at:", Ring.center) # modify class variable r = Ring(price=8) # modify only price
    print("Radius:{0}, Cost:{1}".format(r.radius, r.cost()))
    print("Radius:{0}, Perimeter:{1:0.2f}".format(r.radius, r.perimeter()))
    
if __name__ == '__main__':
    main()
    b = Box(r)
    print(b.perimeter())
    
    