

# TODO - improve code quality

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

	if a_is_prime:
		factors.append(a)

	if b_is_prime:
		factors.append(b)
	
	if not a_is_prime and not b_is_prime:

		return find_factors(a, find_factors(b, factors))
	elif not a_is_prime and b_is_prime:

		return find_factors(a, factors)
	elif a_is_prime and not b_is_prime:

		return find_factors(b, factors)
	else:

		return factors

def get_0th_digit(number):

	while digit_count(number) > 15:
		number -= 10**(digit_count(number)-1)
	
	return int(round(10 * ((number/10.0)-(number/10))))

def get_nth_digit(number, n):

	if n < 0:
		return 0
	else:
		return get_0th_digit(number / 10**n)

def digit_count(number):
	return len(str(number))

def concat_number(number, bound, dig_count):
	
	while digit_count(number) > 10** dig_count :
		number -= 10**(digit_count(number)-1)

	new_num = 0
	for j in range(dig_count-1, -1, -1):
		nth = get_nth_digit(number,j)
		new_num += nth * (10 **j)

	return new_num

def summation_count(n, digit_count, concat=True):

	bound = 10 ** (digit_count)

	summation = 1
	for i in range(2, n+1):
		ith_prime_factors = find_factors(i, [])

		while 1 in ith_prime_factors:
			ith_prime_factors.remove(1)

		inner_sum = 0
		for factor in ith_prime_factors:
			inner_loop_sum = factor

			for j in range(1, i):
				inner_loop_sum *= factor
				if inner_loop_sum > bound:

					if concat:
						inner_loop_sum = concat_number(inner_loop_sum, bound, digit_count)

			if inner_sum == 0:
				inner_sum = inner_loop_sum
			else:
				inner_sum *= inner_loop_sum

			if concat:
				inner_sum = concat_number(inner_sum, bound, digit_count)

		summation  += inner_sum
		if summation > bound and concat:
			summation = concat_number(summation, bound, digit_count)

	return summation

def getcount(n, m):
	summ = 0
	for i in range(1, n+1):
		summ += i **i 

	return concat_number(summ, 1, m)

#print("get count: ", getcount(11, 10))

assert getcount(11, 10) == 5716741928
assert getcount(12, 10) == 1817190184
assert getcount(13, 10) == 6923782437
assert getcount(14, 10) == 3749340453
assert getcount(15, 10) == 4130199828
assert getcount(16, 10) == 7839751444

assert getcount(17, 10) == 4176515621

#print("178: ", summation_count(17, 10))

print getcount(1000, 10)

## new answer #48: 5674695789