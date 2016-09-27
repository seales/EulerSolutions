
def get_nth_digit(number, n):
    if n < 0:
        return 0
    else:
        return get_0th_digit(number / 10**n)


def get_0th_digit(number):
    return int(round(10 * ((number/10.0)-(number/10))))


def cancels(numerator, denominator):

    if get_nth_digit(numerator, 0) != 0 != get_nth_digit(denominator, 0) and numerator < denominator:

        full_divide = numerator / (denominator*1.0)
        possible = False 
        if get_nth_digit(numerator, 0) == get_nth_digit(denominator, 0):
            
            partial_divide = get_nth_digit(numerator, 1) / (get_nth_digit(denominator, 1)*1.0)
            possible  = possible or partial_divide == full_divide
        if get_nth_digit(numerator, 1) == get_nth_digit(denominator, 0):
            
            partial_divide = get_nth_digit(numerator, 0) / (get_nth_digit(denominator, 1)*1.0)
            possible  = possible or partial_divide == full_divide
        if get_nth_digit(numerator, 0) == get_nth_digit(denominator, 1):
            
            partial_divide = get_nth_digit(numerator, 1) / (get_nth_digit(denominator, 0)*1.0)
            possible  = possible or partial_divide == full_divide
        if get_nth_digit(numerator, 1) == get_nth_digit(denominator, 1):
            
            partial_divide = get_nth_digit(numerator, 0) / (get_nth_digit(denominator, 0)*1.0)
            possible  = possible or partial_divide == full_divide
        return possible


    return False

def products(n):

    product = 0

    numerator_product = 1
    denominator_product = 1


    for i in range(10, n):
        for j in range(10, n):
            
            if cancels(i, j):
                numerator_product *= i 
                denominator_product *= j

    return numerator_product / (denominator_product * 1.0)

print products(100)

assert cancels(49, 98)
assert not cancels(30, 50)
assert not cancels(77, 44)

assert not cancels(44, 77)

assert not cancels(47, 77)