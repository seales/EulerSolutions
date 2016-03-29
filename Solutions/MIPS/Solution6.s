main:
	li 	$v0, 1  # syscall code to print an integer
    li  $t0, 100 # range, only input parameter
    li  $t5, 2 # holds the constant 2

    # begin squareOfSum computation
    addi $t1, $t0, 1 # increment range
    mult $t0, $t1 # t1 = (range * (range+1))
    mflo $t1

    div $t1, $t5 # t1 = (t1 / 2)
    mflo $t1

    mult $t1, $t1 # t1 = t1 ^ 2
    mflo $t1

    # begin sumOfSquares computation
    li $t2, 0 # initialize sum to 0
    li $t3, -1 # index = -1
    sumOfSquares:
        addi $t3, $t3, 1 # increment index

        mult $t3, $t3 # index ^ 2
        mflo $t4 # temporary storage
        add $t2, $t2, $t4 # sum += index ^ 2

        slt $t4, $t3, $t0
        beq $t4, 1, sumOfSquares # loop if i <= range

    sub $t1, $t1, $t2 # return: squareOfSum - sumOfSquare
    move $a0, $t1
    syscall # print
    li $v0, 10 # code to terminate
    syscall

