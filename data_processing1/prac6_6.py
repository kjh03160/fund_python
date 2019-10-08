

while True:
    height = int(input("삼각형의 높이 입력 : "))
    if height == 0:
        print("삼각형을 만들 수 없습니다.")
        break
    for i in range(height):
        for j in range(i + 1):
            print("*", end="")
        print()
