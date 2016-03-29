
def sum_of_digits(base, exponent):
    result = str(base ** exponent)
    count = 0
    for num in result:
        count += int(num)
    return count

assert sum_of_digits(2, 1000) == 1366