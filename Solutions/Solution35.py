
import math

# TODO - improve code quality

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

def is_prime(n):

	divisor = math.floor(math.sqrt(n))

	while (n/(divisor)) != int(n/(divisor*1.0)):
		divisor -= 1

		if int(divisor) == 1:
			return True

	return divisor == 1

def rotations(number):

	rotation_values = []

	for i in range(digit_count(number)):
		rotation_values.append(rotate(number, i))

	return rotation_values


def rotate(number, i):
	"""
	1234
	i=0 -> 1234
	i=1 -> 2341
	i=2 -> 3412
	i=3 -> 4123
	"""

	rotated_number = number 
	dcount = digit_count(number)

	i %= dcount

	while i > 0:
		nth = get_nth_digit(rotated_number, dcount-1)
		rotated_number -= (10**(dcount-1) ) * get_nth_digit(rotated_number, dcount-1)
		rotated_number = nth + (10 * rotated_number)
		i -= 1

	return rotated_number 

assert rotate(3456, 0) == 3456
assert rotate(3456, 1) == 4563
assert rotate(3456, 2) == 5634
assert rotate(3456, 3) == 6345
assert rotate(3456, 4) == 3456

def contains2InNthDigit(number):

	if number == 2:
		return -1

	i = 0 
	while i < digit_count(number):
		nth = get_nth_digit(number, i)
		if nth % 2 == 0:
			return i 

		i += 1

	return -1

def prime_rotations_less_than_n(lower, upper):

	all_prime_rotations = []

	i = lower
	counter = 0 
	while i < upper:

		counter += 1

		if counter > 10000:
			counter = 0

		nth = contains2InNthDigit(i)

		if nth == -1:

			rotations_of_i = rotations(i)
			all_prime = True 
			for rotation in rotations_of_i:
				all_prime &= is_prime(rotation)

			if all_prime:
				all_prime_rotations.append(i)
			
			i += 1
		else:
			i += 10** nth 

	return all_prime_rotations


assert len(prime_rotations_less_than_n(2, 100)) == 13

print "count: ", len(prime_rotations_less_than_n(2, 1000000))