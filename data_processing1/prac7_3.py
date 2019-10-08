def sum1(a):
    total = 0
    for i in a:
        total += i
    return total

def mean(a):
    average = sum1(a) / len(a)
    return average

def variance(a):
    variance_1 = 0
    for j in a:
        variance_1 += (j - mean(a)) ** 2
    return variance_1 / len(a)

a = [10, 4, 23, 60, 7]
print(variance(a))


from math import sqrt
def stddev(*args):
    def mean():
        return sum(args) / len(args)
    def variance(m):
        variance_1 = 0
        for j in args:
            variance_1 += (j - m) ** 2
        return variance_1 / (len(args) - 1)
    v = variance(mean())
    return sqrt(v)

print(stddev(2.3, 1.7, 1.4, 0.7, 1.9))
