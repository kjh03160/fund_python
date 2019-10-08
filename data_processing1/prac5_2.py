numbers = [10, 20, 30, 40, 50]

print("리스트 numbers:", numbers)

numbers.pop(0)
numbers.pop()

print("리스트 numbers:", numbers)
sum1 = sum(numbers)
print("리스트 요소들의 합 : %d" % sum1)
print("리스트 요소들의 합 : %f" % (sum1 / len(numbers)))