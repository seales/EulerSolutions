main:
    li  $v0, 1  # syscall code to print an integer
    li  $t0, 0  # sum
    li  $t1, 3  # firstValue
    li  $t2, 5  # secondValue 
    li  $t3, 1000   # fromValue 
    li  $t4, -1     # i
    li  $t5, 0  # mod store
    
    loop:
        addi $t4, $t4, 1  #increment i for each loop
        slt $t5, $t4, $t3 # if i < fromValue
        beq $t5, 0, return # return if !(i < fromValue)
        
        div $t4, $t1 # divide for modulus
        mfhi $t5   # store modulus in $t5
        beq $t5, 0, incrementSum # if i % firstValue == 0, add
        
        div $t4, $t2 # divide for modulus
        mfhi $t5   # store modulus in $t5
        beq $t5, 0, incrementSum # if i % secondValue == 0, add
        
        j loop # loop back
    
    incrementSum:
        #otherwise, add
        add $t0, $t0, $t4
        j loop
    
    return:
        move $a0, $t0  # store result to be printed
        syscall # print
        li $v0, 10  # syscall code to terminate
        syscall # terminate