import math

class ComplexNumber:
    def __init__(self, x, y):
        self.__real = x
        self.__imag = y


    def setReal(self, x):
        self.__real = x

    def setImag(self, y):
        self.__imag = y

    def getReal(self):
        return self.__real

    def getImag(self):
        return self.__imag

    def magnitude(self):
        z = math.sqrt(self.__real ** 2 + self.__imag ** 2)
        return z

    def add(self, n):
        real = n.getReal()
        imag = n.getImag()
        a = self.__real
        b = self.__imag
        new = ComplexNumber(a + real, b + imag)
        return new

    def subtract(self, n):
        real = n.getReal()
        imag = n.getImag()
        a = self.__real
        b = self.__imag
        new = ComplexNumber(a - real, b - imag)
        return new

    def __call__(self):
        print("%f %+fj" % (self.__real, self.__imag))
        print("Magnitude : %f" % self.magnitude())

    @staticmethod
    def add2complex(n1, n2):
        real = n1.getReal() + n2.getReal()
        imag = n1.getImag() + n2.getImag()
        return ComplexNumber(real, imag)

import sys
def setNumber(n):
    try:
        a = (input("input real_part number : "))
        if not a.isdigit():
            raise Exception("숫자가 아닙니다.")
        n.setReal(a)
        b = (input("input imag_part number : "))
        if not a.isdigit():
            raise Exception("숫자가 아닙니다.")
        n.setImag(b)

    except Exception as err:
        print(err)
        sys.exit(0)

n1 = ComplexNumber(0, 0)
n2 = ComplexNumber(0, 0)
setNumber(n1)
setNumber(n2)
print("n1:")
n1()
print("n2:")
n2()
n3 = n1.add(n2)
print("n1+n2:")
n3()
print("n1-n2:")
n1.subtract(n2)()
