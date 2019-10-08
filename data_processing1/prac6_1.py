a, b, c = map(int, input("삼각형 세 변의 길이를 입력하시오: ").split())

from math import sqrt

s = (a + b + c) / 2

list_1 = []
list_1.append(a)
list_1.append(b)
list_1.append(c)
list_1.sort()

if list_1[2] >= list_1[1] + list_1[0]:
    print("삼각형이 불가능합니다.")

else :
    print("삼각형이 가능합니다.")
    square = sqrt(s * (s - a) * (s - b) * (s - c))
    print("넓이 : %f" % square)