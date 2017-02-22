class Bike(object):
    def __init__(self, price, max_speed, miles):
        print "New Bike"
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "This bike's price is " +  str(self.price) + ", max speed is " + str(self.max_speed) + ", and mileage is " + str(self.miles)
    def ride(self):
        print "Riding"
        self.miles += 10
    def reverse(self):
        print "Reversing"
        self.miles -= 5

Bike1 = Bike(200, 25, 73)


print Bike1.displayInfo()
print Bike1.ride()
print Bike1.displayInfo()
print Bike1.reverse()
print Bike1.displayInfo()
