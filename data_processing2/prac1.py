a, b = map(float, input("두 수 입력 : ").split())
second = int(input("1 ~ 4 사이 입력 : "))
while not(1<= second <=4):
    second = int(input("다시 1 ~ 4 사이 입력 : "))

if second == 1:
    print(a + b)
elif second == 2:
    print(a - b)
elif second == 3:
    print(a * b)
else:
    print(a / b)