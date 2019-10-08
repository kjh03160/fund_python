numbers = []
print("다섯 개의 정수를 리트스에 입력 :")
# numbers.append(int(input("정수1:")))
# numbers.append(int(input("정수2:")))
# numbers.append(int(input("정수3:")))
# numbers.append(int(input("정수4:")))
# numbers.append(int(input("정수5:")))
for i in range(1, 6):
    numbers.append(int(input("정수%d:" % i)))
print("입력된 다섯 개의 정수 : \n", numbers)
sum1 = sum(numbers)
print("입력된 정수들의 합 : %d" % sum1)
print("입력된 정수들의 평균 : %f" % (sum1 / len(numbers)))

