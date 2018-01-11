class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0 

    def displayinfo(self):
        print 'Price is: $' + str(self.price)
        print 'Max Speed:' + str(self.max_speed) + 'mph'
        print 'Total Miles:' + str(self.miles) + 'miles'

    def drive(self):
        print 'Driving'
        self.miles += 10

    def reverse(self):
        print 'Reversing'
        if self.miles >= 5:
            self.miles -= 5

bike1 = Bike(499.99, 18)
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayinfo()

bike2 = Bike(1999.99, 30)
bike2.drive()
bike2.drive()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

