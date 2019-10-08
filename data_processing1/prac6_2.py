a = int(input("첫 번째 정수 입력 : "))
b = int(input("두 번째 정수 입력 : "))
op = input("연산자 입력 : ")

if op == "+":
    print(("%d + %d = %d") % (a, b, a + b))
elif op == "*":
    print(("%d * %d = %d") % (a, b, a * b))
elif op == "/":
    if b == 0:
        print("%d / %d 계산을 수행할 수 없습니다." % (a, b))
    else:
        print(("%d / %d = %f") % (a, b, a / b))
else:
    print(a, op, b, "계산을 수행할 수 없습니다.")