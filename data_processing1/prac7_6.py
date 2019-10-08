# def find_max(L):
#     max = L[0]
#     for i in range(len(L)):
#         for j in range(i + 1, len(L)):
#             if L[i] < L[j]:
#                 max = L[j]
#     return max

# def find_max(L):
#     max = L[0]
#     for i in L[1:]:
#         if i > max:
#             max = i
#     return max

def find_max(L):
    max = 0
    for i in range(1, len(L)):
        if L[max] <L[i] :
            max = i
    return max


# def find_min(L):
#     min = L[0]
#     for i in L[1:]:
#         if min > i:
#             min = i
#     return min

def find_min(L):
    min = 0
    for i in range(1, len(L)):
        if L[min] > L[i]:
            min = i
    return min

def mini(list):
    for i in list:
        for j in range(list.index(i) + 1, len(list)):
            if i > list[j]:
                minimal = list[j]
    return minimal



L = [1, 3, 4, 2, 0, 10, 20, 3]
print(find_max(L))
print(mini(L))
print(L[find_max(L)])
print(L[find_min(L)])

