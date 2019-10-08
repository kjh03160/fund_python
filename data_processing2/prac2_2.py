# while True:
#     x1, y1 = map(int, input("fist : ").split())
#     x2, y2 = map(int, input("second : ").split())
#     if (x1 == x2) or (y1 == y2):
#         print("사각형 생성 불가")
#         continue
#     else:
#         break
#
# width = abs(x1 - x2)
# height = abs(y1 - y2)
#
# print(width * height)

def powerIter(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
        # print(base)
    return result


base, exponent = map(int, input("base와 exponent를 입력하시오 : ").split())
print("%d 의 %d 제곱은 %d 입니다." %(base, exponent, powerIter(base,exponent)))

