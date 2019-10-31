class Student:
    def __init__(self, name, StID):
        self.__name = name
        self.__StID = StID

    def __call__(self):
        return "Name = " + self.__name + " Student ID : " + str(self.__StID)


class UnderGraduateSt(Student):
    def __init__(self, name, StID, club):
        super().__init__(name, StID)
        self.__club = club

    def __call__(self):
        info = super().__call__() + " club = " + self.__club
        return info


class GraduateSt(Student):
    def __init__(self, name, StID, advisor):
        super().__init__(name, StID)
        self.__advisor = advisor

    def __call__(self):
        info = super().__call__() + " advisor = " + self.__advisor
        return info

st1 = GraduateSt('g', 2018, 'd')
st2 = UnderGraduateSt('h', 2019, 'prf')
print(st1())
print(st2())