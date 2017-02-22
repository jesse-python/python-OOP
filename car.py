class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def display_all(self):
        print "This car's price is " + str(self.price) + " with a tax of " + str(self.tax) + ", speed is " + str(self.speed) + " mph, fuel is " + str(self.fuel) + ", and mileage is " + str(self.mileage)

car1 = Car(2500000, 250, 50, 200)
print car1.price
print car1.tax
car1.display_all()

car2 = Car(5000, 50, 10, 99999)
car2.display_all()

car3 = Car(159,456,45,5489)
car3.display_all()

car4 = Car(159,548,78,548)
car4.display_all()

car5 = Car(156,151,2685,18)
car5.display_all()
