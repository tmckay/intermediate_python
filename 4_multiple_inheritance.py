class Vehicle(object):

    def go(self):
        print 'forward'

class Turbo(object):

    def go(self):
        print 'fast'

class Bus(Vehicle, Turbo):

    def __init__(self):
        self.go()

Bus()
