main:
    # max collatz chain computation given initialBound

    li $t0, 1000 # parameter: initialBound
    li $t1, 0 # maxChain
    li $t6, 0 # maxChainIndex
    li $t4, 0 # chainCount

    outerLoop:

        li $t2, 1 # constant 1
        slt $t5, $t1, $t4 # if (maxChain < chainCount)
        beq $t2, $t5, updateMaxChain

    resumeAfterUpdate:
        li $t2, 2 # constant 2
        slt $t3, $t0, $t2
        li $t2, 1 # constant 1
        beq $t3, $t2 return # if (initialBound < 2)

        move $t3, $t0 # n = initialBound
        addi $t0, $t0, -1 # decrement initialBound
        li $t4, 1 # chainCount = 1

    innerLoop:
        li $t2, 2 # constant 2
        slt $t5, $t3, $t2
        li $t2, 1 # constant 1
        beq $t2, $t5, outerLoop # if (n < 2)

        addi $t4, $t4, 1 # increment chainCount

        li $t2, 2 # constant 2
        div $t3, $t2 # n/2, mflo = mod
        mfhi $t5 # t5 = n % 2

        li $t2, 0 # constant 0
        bne $t2, $t5, zeroModBranch # jump if n % 2 != 0

        li $t2, 2 # constant 2
        div $t3, $t2
        mflo $t3 # n = n / 2

        j innerLoop

    zeroModBranch:
        li $t2, 3 # constant 3
        mult $t2, $t3
        mflo $t3  # t3 = 3 * n
        addi $t3, $t3, 1 # n = n + 1
        j innerLoop

    updateMaxChain:
        move $t1, $t4 # maxChain = chainCount
        addi $t6, $t0, 1 # maxChainIndex = initialBound + 1 (reverse decrement)
        j resumeAfterUpdate

    return:
        li $v0, 1 # syscall code to print integer
        move $a0, $t6 # store maxChainIndex in return register
        syscall # print
        li $v0, 10 # code to terminate
        syscall

