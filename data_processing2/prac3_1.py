import math
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __call__(self):
        return (self.__x, self.__y)

    def equal(self, obj1):
        if (obj1.__x == self.__x) and (obj1.__y == self.__y):
            return True
        return False

    def distance_from_origin(self):
        result = math.sqrt((self.__x) ** 2 + (self.__y)**2)
        return result

    def distancee_from_point(self, obj1):
        result = math.sqrt((self.__x - obj1.__x) ** 2  + (self.__y - obj1.__y) ** 2)
        return result

P1 = Point(1, -3)
P2 = Point(-1, 5)
P3 = Point(1, -3)

print("Point P1 :", P1())
print(P1.equal(P2))
print(P1.equal(P3))
print(P1.distance_from_origin())
print(P1.distancee_from_point(P2))