from point_class import Point

class Circle(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.__r = r

    @classmethod
    def constructor(cls, center, r):
        x = center.getX()
        y = center.getY()
        return cls(x, y, r)

    def __call__(self):
        print(super().__call__())
        print("radius", self.__r)

p = Point(1,2)
c1 = Circle(1, 2, 3)
c1()
c2 = Circle.constructor(p, 3)
c2()