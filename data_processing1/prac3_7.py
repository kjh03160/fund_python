(x1, y1) = input("첫 번째 좌표 입력 : \n").split()
(x2, y2) = input("두 번째 좌표 입력 : \n").split()
s = (int(x2) - int(x1)) * (int(y1) - int(y2))

print("좌표1(%s, %s), 좌표2(%s, %s), 사각형 넓이 : %d" % (x1, y1, x2, y2, s))


point_1 = input("첫 번째 좌표 입력 : \n").split()
x1, y1 = int(point_1[0]), int(point_1[1])

point_2 = input("두 번째 좌표 입력 : \n").split()
x2, y2 = int(point_2[0]), int(point_2[1])


s = (x2 - x1) * (y1 - y2)

print("좌표1(%d, %d), 좌표2(%d, %d), 사각형 넓이 : %d" % (x1, y1, x2, y2, s))