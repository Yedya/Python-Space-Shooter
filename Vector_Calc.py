import math

class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    @classmethod
    def from_points(cls, P1, P2):
        return cls( P2[0] - P1[0], P2[1] - P1[1] )
    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude
    # rhs stands for Right Hand Side
    def __add__(self, rhs):
        return Vector(self.x + rhs.x, self.y + rhs.y)
    def __sub__(self, rhs):
        return Vector(self.x - rhs.x, self.y - rhs.y)
    def __neg__(self):
        return Vector(-self.x, -self.y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    def __div__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)