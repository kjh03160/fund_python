def quick_sort(list, p, r):
    if p < r:
        q = partition(list, p, r)
        quick_sort(list, p, q - 1)
        quick_sort(list, q + 1, r)

def partition(list, p, r):
    x = list[r]
    i = p - 1
    for j in range(p, r):
        if list[j] < x:
            i += 1
            list[j], list[i] = list[i], list[j]

    list[i + 1], list[r] = list[r], list[i + 1]
    return i + 1

a = [31, 8, 48, 73, 11, 3, 20, 29, 65, 15]
quick_sort(a, 0, len(a) - 1)
print(a)