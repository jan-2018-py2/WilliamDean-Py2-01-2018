class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for x in args:
            if type(x) == list or type(x) == tuple:
                for y in x:
                    self.result += y
            else:
                self.result += x
        return self
        
MathDojo.add(2).add(2,5).subtract(3,2).result