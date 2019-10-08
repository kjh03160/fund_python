def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 1, -1):
        for j in range(0, i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j + 1]
                my_list[j + 1] = my_list[j]
                my_list[j] = temp
            print(my_list)


some_list = [5,1,2,6,4,3]
bubble_sort(some_list)
print(some_list)



# def bubble_sort(my_list):
#     for i in range(len(my_list) - 1, 0, -1):
#         for j in range(0, i):
#             if my_list[j] > my_list[i]:
#                 temp = my_list[i]
#                 my_list[i] = my_list[j]
#                 my_list[j] = temp
#             print(my_list)
#
#
# some_list = [9,8,7,6,5,4,3,2,1,0]
# bubble_sort(some_list)
# print(some_list)