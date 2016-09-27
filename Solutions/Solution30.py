

def get_nth_digit(number, n):
    if n < 0:
        return 0
    else:
        return get_0th_digit(number / 10**n)


def get_0th_digit(number):
    return int(round(10 * ((number/10.0)-(number/10))))


def digit_count(number):
    return len(str(number))

def nth_digit_sum_upper_bound(n):
    i = 0
    while digit_count(i)*9**n >= i:
        i += 10

    return i


def sum_digits_equals_nth_power(number, n):

    if number < 2:
        return False 

    summation = 0 

    for i in range(digit_count(number)):

        summation += get_nth_digit(number, i) ** n

        if summation > number:
            return False 

    return summation == number


assert sum_digits_equals_nth_power(1634, 4)
assert sum_digits_equals_nth_power(8208, 4)
assert sum_digits_equals_nth_power(9474, 4)
assert not sum_digits_equals_nth_power(9574, 4)

def sum_of_numbers_with_nth_digit_sum_equality(n):

    i = 0
    bound = nth_digit_sum_upper_bound(n)

    summation = 0
    while i <= bound:
        if sum_digits_equals_nth_power(i, n):
            summation += i

        i += 1

    return summation

print sum_of_numbers_with_nth_digit_sum_equality(5)
