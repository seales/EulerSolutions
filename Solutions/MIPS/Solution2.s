main:
	li 	$v0, 1  # syscall code to print an integer
	li	$t0, 2	# fibCurrent
	li	$t1, 1	# fibPrevious
	li	$t3, 0	# evenSum
	li  $t4, 0	# jump boolean / mod result
	li 	$t5, 4000000	# limit
	li 	$t6, 2 # divide by immediate 2
	
	loop:
		div $t0, $t6 # divide for modulus
		mfhi $t4   # store modulus in $t4
		bne $t4, 0, skipAdd # if not divisible by 2, no add
		add $t3, $t3, $t0
	skipAdd:
		add $t0, $t0, $t1 # update fibCurrent
		sub $t1, $t0, $t1 # update fibPrevious
		slt $t4, $t0, $t5 
		beq $t4, 1, loop # loop if fibCurrent < limit
		move $a0, $t3  # store result to be printed
		syscall # print
		li $v0, 10  # syscall code to terminate
		syscall # terminate
	