# def print_triangle(in_str):
#     for i in in_str:
#         print(i * (in_str.index(i) + 1))
#
# in_str = input("문자열 입력 : ")
# print_triangle(in_str)


def print_triange(in_str):
    line = 1
    for s in in_str:
        for i in range(line):
            print(s, end="")
        line += 1
        print()


in_str = input("문자열 입력 : ")
print_triange(in_str)