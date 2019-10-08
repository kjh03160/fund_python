class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def check(self):
        if (self.__x1 == self.__x2) or (self.__y1 == self.__y2):
            return False
        return True

    def area(self):
        if self.check():
            result = (abs(self.__x1 - self.__x2) * abs(self.__y1 - self.__y2))
            return result
        return 0

    def __call__(self):
        if self.check():
            print("(%d, %d) (%d, %d) (%d, %d), (%d, %d) area = %d" %(self.__x1, self.__y1, self.__x2, self.__y1,self.__x1, self.__y2,self.__x2, self.__y2, self.area()))
        else:
            print("cannot")

    def equal(self, r):
        if self.area() == r.area():
            return True
        return False

# class Error(Exception):
#     pass

rec1 = Rectangle(1, 1, 2, 3)
rec2 = Rectangle(-2, 2, -1, 4)
rec3 = Rectangle(3, 4, 3, 5)

print("<<<<사각형1>>>>")
rec1()
print("<<<<사각형2>>>>")
rec2()
print("<<<<사각형3>>>>")
rec3()

if rec1.equal(rec2):
    print("사각형1과 사각형2의 모양은 같습니다.")
else:
    print("사각형1과 사각형2의 모양은 다릅니다.")

'''
private 변수를 외부에서 바꾸기 위해서는 mutator 메소드 사용
get 메소드, set 메소드 사용

def getPrivate(self): return(self.__private)
def setPrivate(self, s) : self.__private = s

obj = P()
obj.setPrivate("PRivate)
print(obj.getPrivate())


메소드에 제약 조건을 둘 수 있음 ex)권한, 값의 범위 등등


'''