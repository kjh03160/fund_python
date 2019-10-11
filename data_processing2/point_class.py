import math

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __call__(self):
        return "(" + str(self.__x) + "," + str(self.__y) + ")"

    def equal(self, p):
        if (self.__x == p.__x) and (self.__y == p.__y):
            return True
        else:
            return False

    def distance_from_origin(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    def distance_from_point(self, p):
        return math.sqrt((p.__x - self.__x) ** 2 + (p.__y - self.__y) ** 2)

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y
