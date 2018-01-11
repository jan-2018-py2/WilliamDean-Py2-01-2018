class Product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.price = price
        self.status = status
        self.tax = float(price) * 0.10

class Returns(Product):
    def __init__(self, price, item_name, weight, brand, status, reason):
        super(Returns, self).__init__(item_name, weight, brand, status, reason)
        self.display_all()
        if (reason == 1):
            self.status = 'defective'
            self.price = 0 
        elif (reason == 2):
            self.status = 'used'
            self.price = 0.8 * self.price
        else:
            status = 'for sale'
            self.price = price
        # return self
    
    def display_all(self):
        print 'Brand: ' + str(self.brand)
        print 'Product Name: ' + str(self.item_name)
        print 'Weight: ' + str(self.weight) + ' grams' 
        print 'Price: $' + str(self.price)
        print 'Tax: $' + str(self.tax)        
    
    def sell(self, status):
        self.status = 'sold'
   

product1 = Returns('iphone', 600, 'iPhone', 500, 'Apple', 2)
# product1.returns(1)
print product1
# product1.returns(1)

# product2 = Product(35, 'Echo Dot', 100, 'Amazon', 'for sale')
# product2.returns(2)
# print product2.status