def quick_sort_by_stars(list, p, r):
    if p < r:
        q = partition_by_stars(list, p, r)
        quick_sort_by_stars(list, p, q - 1)
        quick_sort_by_stars(list, q + 1, r)

def partition_by_stars(list, p, r):
    x = list[r].stars
    i = p - 1
    for j in range(p, r):
        if list[j].stars > x:
            i += 1

            list[j], list[i] = list[i], list[j]

    list[i + 1], list[r] = list[r], list[i + 1]

    return i + 1

def quick_sort_by_time(list, p, r):
    if p < r:
        q = partition_by_time(list, p, r)
        quick_sort_by_time(list, p, q - 1)
        quick_sort_by_time(list, q + 1, r)

def partition_by_time(list, p, r):
    refer = {
        '월' : 10,
        '화' : 30,
        '수' : 50,
        '목' : 70,
        '금' : 90,
        'x' : 120
    }
    x = list[r].class_time.split()
    if len(x) > 1:
        x = refer[x[0]] + int(x[1])
    else:
        x = refer['x']
    i = p - 1
    for j in range(p, r):
        value = list[j].class_time.split()
        if len(value) > 1:
            value = refer[value[0]] + int(value[1])
        else:
            value = refer['x']

        if value < x:
            i += 1

            list[j], list[i] = list[i], list[j]

    list[i + 1], list[r] = list[r], list[i + 1]

    return i + 1