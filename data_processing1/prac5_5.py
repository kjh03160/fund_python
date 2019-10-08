a = int(input("정수1:"))
b = int(input("정수2:"))
c = int(input("정수3:"))
tuple1 = a, b, c
print("tuple1 =", tuple1)
sum1 = sum(tuple1)
average = sum1 / len(tuple1)
print("합 : %d 평균 : %f" %(sum1, average))



######################################33
score = {1:100, 2:80, 3:90, 4:50, 5:70}

print("score =", score)

key = score.keys()
value = score.values()

value_sum = sum(value)
value_average = value_sum / len(key)

print("합 : %d, 평균 : %f" % (value_sum, value_average))


# value 리스트 추가/삭제

a = {1:[1,2,3], 2:[3,4,5]}

a[1].append(4)
print(a)
a[2].pop()
print(a)