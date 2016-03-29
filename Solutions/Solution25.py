
import sys
sys.setrecursionlimit(10500)

def digit_count(number):
	return len(str(number))

def fib_containing_nth(n):

	fib_digits = 0
	index = 0
	while fib_digits < n:
		fib_digits = digit_count(fib(index))

		index += 1
	return index

def fib(i):
	return fib_helper(i, {})
	
def fib_helper(i, fib_cache):
	if i <= 1:
		return 1 
	elif i == 2:
		return 2
	elif fib_cache.has_key(i):
		return fib_cache[i]
	else:
		fibval = fib_helper(i-1, fib_cache) + fib_helper(i-2, fib_cache)
		fib_cache[i] = fibval
		return fibval

assert fib(1) == 1
assert fib(2) == 2
assert fib(3) == 3
assert fib(4) == 5
assert fib(5) == 8

assert fib_containing_nth(3) == 12

print("fib with nth: ", fib_containing_nth(1000))