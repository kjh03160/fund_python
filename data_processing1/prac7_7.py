def sum_recur(n):
    if n == 0:
        return 0
    else:
        return sum_recur(n-1) + n

def sum_iter(n):
    temp = 0
    for i in range(1, n + 1):
        temp = temp + i
    return temp


print(sum_recur(10))
print(sum_iter(10))