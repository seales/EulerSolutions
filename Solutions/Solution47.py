
import math


def find_factors(n, factors):

	if n == 1:
		return factors

	divisor = math.floor(math.sqrt(n))
	
	# loop until integer divisor found
	while (n/divisor) != int(n/(divisor*1.0)):
		divisor -= 1

		if int(divisor) == 1:
			break

	a = int(n/(divisor*1.0))
	b = int(divisor)
	a_is_prime = is_prime(int(n/(divisor*1.0)))
	b_is_prime = is_prime(b)

	if a_is_prime and a not in factors:
		factors.append(a)

	if b_is_prime and b not in factors:
		factors.append(b)
	
	if not a_is_prime and not b_is_prime:

		return find_factors(a, find_factors(b, factors))
	elif not a_is_prime and b_is_prime:

		return find_factors(a, factors)
	elif a_is_prime and not b_is_prime:

		return find_factors(b, factors)
	else:

		return factors

def is_prime(n):

	divisor = math.floor(math.sqrt(n))

	while (n/(divisor)) != int(n/(divisor*1.0)):
		divisor -= 1

		if int(divisor) == 1:
			return True

	return divisor == 1


def first_of_consecutive_prime_factors(n):

	index = 2
	current_prime_factors = []
	consecutive_prime_factor_count = 0

	while True:
		
		previous_number = index
		current_prime_factors = find_factors(index, [])
		
		if len(current_prime_factors) == n:
			consecutive_prime_factor_count += 1
		else:
			consecutive_prime_factor_count = 0

		if consecutive_prime_factor_count == n:
			return index - n + 1

		index += 1

### TEST IS PRIME METHOD ###
assert not is_prime(10)
assert is_prime(2)
assert is_prime(1)
assert is_prime(13)
assert not is_prime(15)

### TEST FIND FACTORS METHOD ###
factors_found = find_factors(4, [])
assert len(factors_found) == 1
assert 2 in factors_found

factors_found = find_factors(646,[])
assert len(factors_found) == 3
assert 19 in factors_found
assert 17 in factors_found
assert 2 in factors_found

print first_of_consecutive_prime_factors(4)