import math

s = int((input("원의 반지름을 입력하시오 : \n")))
circumference = round(2 * s * math.pi)
area = round(pow(s, 2) * math.pi)

print("반지름이 %d인 원의 둘레는 %d이고, 넓이는 %d입니다." % (int(s), circumference, area))