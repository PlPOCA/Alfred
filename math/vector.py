from math import sqrt


class Vector2(list):
    def __init__(self, x, y):
       self.x = x
       self.y = y

    def normalize(self):
        value = sqrt(self.x ** 2 + self.y ** 2)
        return self.__class__(value, value)
