import math

def triangle_numbers(count):
    triangle_sum = 0
    
    # this interval is not proven and may not hold for all cases
    for i in range(1, count**3):
        x = factor_count(triangle_sum)
        if x >= count:
            break

        triangle_sum += i

    return triangle_sum


def factor_count(number):
    count = 0
    if number == 1:
        return 1
    else:
        for i in range(1, int(math.ceil(math.sqrt(number)))):
            if number % i == 0:
                if i ** 2 == number:
                    count += 1
                else:
                    count += 2
        return count

assert triangle_numbers(500) == 76576500

