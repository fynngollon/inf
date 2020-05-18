from random import randint

class Wuerfel(object):
    def __init__(self):
        self.augen = 1

    def wuerfeln(self):
        self.augen = randint(1,6)
