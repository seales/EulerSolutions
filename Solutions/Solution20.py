import math


def sum_of_factorial(n):
    n = str(math.factorial(n))
    f_sum = 0
    for i in range(len(n)):
        f_sum += int(n[i])
    return f_sum


assert sum_of_factorial(10) == 27
assert sum_of_factorial(100) == 648