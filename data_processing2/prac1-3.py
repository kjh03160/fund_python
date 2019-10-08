from math import sqrt
list1 = []
while len(list1) < 10:
    list1.append(int(input("%d번째 정수 입력 : " % (len(list1) + 1))))

print(list1)

list_sum = sum(list1)
average = list_sum / len(list1)
answer = 0
for i in range(len(list1)):
    answer = answer + (list1[i] - average) * (list1[i] - average)

result = sqrt(answer / (len(list1) - 1))

print(result)