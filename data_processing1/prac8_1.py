# 최댓값 찾고 맨뒤로 보내고 무한루프 !

# max 인덱스 추출
# def find_max(L):
#     max = 0
#     for i in range(1, len(L)):
#         if L[max] <L[i] :
#             max = i
#     return max
#
# def selection_sort(list):
#     for j in range(len(list) - 1, 0, -1):
#         # for i in range(len(list)):
#         max_number_index = find_max(list)
#         temp1 = max_number_index
#
#         value = list[j]
#         if value < list[max_number_index]:
#             max_number_index = j
#
#         temp = list[max_number_index]
#         list[max_number_index] = list[temp1]
#         list[temp1] = temp


#
# some_list = [2, 4, 0, 1]
# selection_sort(some_list)
# print(some_list)

def selection_sort(list):
    for last in range(len(list) -1, 0, -1):
        max_inx = 0
        for i in range(1, last + 1):       # 최댓값 인덱스 찾는 부분!!!!!
            if list[i] > list[max_inx]:
                max_inx = i
        temp = list[last]                   # 최댓값을 찾아서 맨 뒤의 숫자와 바꿔 보내는 것!
        list[last] = list[max_inx]          # 해당하는 i와 바꾸는게 아님!
        list[max_inx] = temp
        # print(list)

some_list = [11, 3, 6, 4, 2, 12, 1, 2]
selection_sort(some_list)
print(some_list)
