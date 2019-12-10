a = [90, 31, 48, 73, 8, 11, 20, 29, 65, 15]
b = [90, 31, 48, 73, 8, 11, 20, 29, 65, 15, 100]

def bubble_sort(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)-1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list

def selection_sort(list1):
    for i in range(len(list1)):
        index = i
        for j in range(i + 1, len(list1)):
            if a[index] > a[j]:
                index = j
        a[index], a[i] = a[i], a[index]
    return list1

print(selection_sort(a))
print(bubble_sort(b))
