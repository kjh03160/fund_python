def triangle(height):
    for i in range(0, height):
        for j in range(i + 1):
            print("*", end = "")
        print()

height = int(input("삼각형의 높이 입력 : "))
triangle(height)


def triangle():
    height = int(input("삼각형의 높이 입력 : "))    # height를 정의 안에 넣으면 파라미터 불필요

    for i in range(0, height):
        for j in range(i + 1):
            print("*", end = "")
        print()

triangle()