def collatz(initial_bound):
    # given input, this method return
    # the index that produces the maximum
    # collatz chain within the bounds
    # of 1 ... initial_bound
    
    max_chain = 0
    max_chain_index = 0
    
    while initial_bound > 1:
        n = initial_bound
        initial_bound -= 1
        chain_count = 1
        
        while n > 1:
            chain_count += 1
            if n % 2 != 0:
                n = (3*n) + 1
            else:
                n /= 2
        
        if chain_count > max_chain:
            max_chain = chain_count
            max_chain_index = initial_bound + 1  # append subtracted term
    
    return max_chain_index


assert collatz(1000000) == 	837799
