def power(base, exponent):
    result = 1
    for i in range(exponent):
        result = result * base
    return result

base, exponent = map(int, input("base와 exponent를 입력하시오: ").split())
#power1 = power(int(base), int(exponent))
print("%d의 %d 제곱은 %d입니다." % (base, exponent, power(base, exponent)))


def sum_list(list1):
    result = 0
    for i in list1:
        result += i
    return result

print(sum_list([10, 20]))