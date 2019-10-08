numbers = []
numbers.extend([10, 20, 30, 40, 50])

sum1 = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
print("리스트 numbers:", numbers)
print("리스트 요소들의 합 : %d" % sum1)
print("리스트 요소들의 합 : %f" % (sum1 / len(numbers)))


numbers_1 = []
for i in range(10, 60, 10):
    numbers_1.append(i)

def sum(list):
    temp = 0
    for i in range(len(list)):
        x = list[i]
        temp = temp + x
    return temp

print("리스트 numbers:", numbers)
print("리스트 요소들의 합 : %d" % sum(numbers_1))
print("리스트 요소들의 합 : %f" % (sum(numbers_1) / len(numbers)))


