
import math


def get_fact_values(n=10):
    fact_values = []
    for i in range(n):
        fact_values.append(math.factorial(i))

    return fact_values


def get_nth_digit(number, n):
    if n < 0:
        return 0
    else:
        return get_0th_digit(number / 10**n)


def get_0th_digit(number):
    return int(round(10 * ((number/10.0)-(number/10))))


def digit_count(number):

    i = 0
    while (number / 10**i) != 0:
        i += 1

    return i


def equals_fact_sum(number, fact_values):

    if number < 3:
        return False 

    sum_of_facts = 0 

    for i in range(digit_count(number)):

        sum_of_facts += fact_values[get_nth_digit(number, i)]

        if sum_of_facts > number:
            return False 

    return sum_of_facts == number


def factorial_digit_sum():
    fact_values = get_fact_values()

    bound = upper_bound()
    sum_over_fact_sums = 0
    i = 0

    while i <= bound:
        if equals_fact_sum(i, fact_values):
            sum_over_fact_sums += i
    
        i += 1

    return sum_over_fact_sums


def upper_bound():

    i = 0
    while digit_count(i)*math.factorial(9) >= i:
        i += 10

    return i

### TESTS ###

assert get_nth_digit(0, 0) == 0
assert get_nth_digit(1459, -1) == 0
assert get_nth_digit(1459, 0) == 9
assert get_nth_digit(1459, 1) == 5
assert get_nth_digit(1459, 2) == 4
assert get_nth_digit(1459, 3) == 1
assert get_nth_digit(1459, 4) == 0

assert equals_fact_sum(145, get_fact_values())
assert not equals_fact_sum(1, get_fact_values())
assert not equals_fact_sum(2, get_fact_values())
assert not equals_fact_sum(10, get_fact_values())

assert digit_count(0) == 0
assert digit_count(1) == 1
assert digit_count(18) == 2
assert digit_count(123) == 3

### TESTS ###


print factorial_digit_sum()

# 145 + 40585 = 40730

