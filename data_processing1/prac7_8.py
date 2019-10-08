def powerRecur(base, exponent):
    if exponent == 1:
        return base
    return base * powerRecur(base, exponent - 1)

def poweriter(base, exponent):
    result = 1
    for i in range(exponent):
        result = result * base
    return result

while True:
    a = input("input r or i ")
    if a  == "r" or a == "i":
        break
    else:
        print("incorrect input")

base, exponent = map(int, input("base와 exponent를 입력하시오 : ").split())
if a == "r":
    print(powerRecur(base,exponent))
else:
    print(poweriter(base,exponent))


user_input = input("재귀 함수를 실행하려면 r, 반복 함수를 실행하려면 i를 입력하시오 : ")
while True:
    if user_input != "r" and user_input != "i":
        user_input = input("잘못 입력했습니다. r 또는 i를 입력하세요 : ")
        continue
    if user_input == "r":
        base, exponent = map(int, input("base와 exponent를 입력하시오 : ").split())
        print("%d의 %d 제곱은 %d입니다." % (base, exponent, powerRecur(base, exponent)))
        break
    else:
        base, exponent = map(int, input("base와 exponent를 입력하시오 : ").split())
        print("%d의 %d 제곱은 %d입니다." % (base, exponent, poweriter(base, exponent)))
        break

#
# while True:
#     if user_input == "r":
#         base, exponent = map(int, input("base와 exponent를 입력하시오: ").split())
#         print("%d의 %d 제곱은 %d입니다." % (base, exponent, powerRecur(base, exponent)))
#         break
#     elif user_input == "i":
#         base, exponent = map(int, input("base와 exponent를 입력하시오: ").split())
#         print("%d의 %d 제곱은 %d입니다." % (base, exponent, poweriter(base, exponent)))
#         break
#     else:
#         user_input = input("잘못 입력했습니다. r 또는 i를 입력하세요")