class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self
    
    def displayHealth(self):
        print 'My name is: ' + self.name
        print 'I have: ' + str(self.health) + ' health'

animal = Animal('Cosmo')
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

dog = Dog('Snoopy')
dog.walk().walk().walk().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self). __init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self
    
    def displayHealth(self):
        print 'I am a Dragon'
        super(Dragon, self).displayHealth()

dragon = Dragon('ToothLess')
dragon.fly().displayHealth()

class Fish(Animal):
    def __init__(self, name):
        super(Fish, self).__init__(name)
        self.health = 180

    def swim(self):
        self.health += 10
        return self
    
    def displayHealth(self):
        print 'I am ' + self.name
        print 'I have: ' + str(self.health) + ' health'

fish = Fish('Dory')
fish.swim().swim().swim().displayHealth()