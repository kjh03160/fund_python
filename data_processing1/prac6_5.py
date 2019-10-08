height = int(input("삼각형의 높이 입력 : "))

for i in range (height):
    for j in range(i + 1):
        print("*", end="")

    print()