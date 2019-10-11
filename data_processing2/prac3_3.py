from point_class import Point

class Rectangle:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2

    def check(self):
        if (self.__p2.getX() == self.__p1.getX()) or (self.__p2.getY() == self.__p1.getY()):
            return False
        return True

    def area(self):
        if self.check():
            result = (abs(self.__p1.getX() - self.__p2.getX()) * abs(self.__p1.getY() - self.__p2.getY()))
            return result
        return 0

    def __call__(self):
        if self.check():
            print("(%d, %d) (%d, %d) (%d, %d), (%d, %d) area = %d" % (self.__p1.getX(), self.__p1.getY(), self.__p2.getX(), self.__p1.getY(),self.__p1.getX(), self.__p2.getY(), self.__p2.getX(), self.__p2.getY(), self.area()))
        else:
            print("cannot")

    def equal(self, r):
        self_a = abs(self.__p1.getX() - self.__p2.getX())
        self_b = abs(self.__p1.getY() - self.__p2.getY())
        r_a = abs(r.__p1.getX() - r.__p2.getX())
        r_b = abs(r.__p1.getY() - r.__p2.getY())
        if (self.area() == r.area()) and ((self_a == r_a) or (self_a == r_b)) and ((self_b == r_a) or (self_b == r_b)):
            return True
        return False

rec1 = Rectangle(Point(1,1),Point(2,3))
rec2 = Rectangle(Point(-2,2),Point(-1,4))
rec3 = Rectangle(Point(3,4),Point(3,5))
print("<<<사각형1>>>")
rec1()
print("<<<사각형2>>>")
rec2()
print("<<<사각형3>>>")
rec3()
if rec1.equal(rec2):
    print("사각형1과 사각형2의 모양은 같습니다.")
else:
    print("사각형1과 사각형2의 모양은 다릅니다")