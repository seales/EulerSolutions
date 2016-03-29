//
//  Solution2.h
//  EulerSolutions
//
//  Created by seales on 1/22/14.
//  Copyright (c) 2014 seales. All rights reserved.
//

#ifndef EulerSolutions_Solution2_h
#define EulerSolutions_Solution2_h

int evenFibonacci(int limit)
{
    /**
     Sum of even numbers in fibonacci sequence from 0...limit.
     */
    
    int fibonacciCurrent = 2;
    int fibonacciPrevious = 1;
    int evenSum = 0;
    
    while (fibonacciCurrent < limit) {
        if (fibonacciCurrent % 2 == 0)
            evenSum += fibonacciCurrent;
        
        fibonacciCurrent = fibonacciCurrent + fibonacciPrevious;
        fibonacciPrevious = fibonacciCurrent - fibonacciPrevious;
    }
    
    return evenSum;
}

#endif
