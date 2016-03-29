import math

def even_divisor_sum(n):
    count = 0
    for i in range(2, int(math.sqrt(n))):
    	
        if n % i == 0 and n != i:
        	if i != n/i:
        		count += i + (n/i)
        	else:
        		count += i
    return count + 1

def divisor_sums(n):
    sums = [0]*(n)
    for i in range(1, n+1):
    	sums[i-1] = even_divisor_sum(i)
    return sums


def amicable_sums(n):
    sums = divisor_sums(n)
    sum_of_sums = 0
    b, a = 0, 0
     
    for i in range(n):
    	i = int(i)
        b = sums[i]
        a = i+1
        
        # the 1 subtracted from b is because of 0-indexed arrays
        if int(b-1) < n and a == sums[int(b-1)] and a != b:  
            sum_of_sums += i + 1
    
    return sum_of_sums

assert even_divisor_sum(220) == 284
assert even_divisor_sum(284) == 220
assert amicable_sums(9999) == 31626


print "Tests pass!"
