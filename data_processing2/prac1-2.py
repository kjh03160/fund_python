from math import sqrt

a, b, c = map(int, input().split())


if (a < b + c) and (b < a + c) and (c < b + a):
    s = (a + b + c) / 2
    answer = sqrt(s * (s - a) * (s - b) * (s - c))
    print(answer)

else:
    print("삼각형 불가")