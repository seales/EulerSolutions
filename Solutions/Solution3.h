//
//  Solution3.h
//  EulerSolutions
//
//  Created by seales on 1/22/14.
//  Copyright (c) 2014 seales. All rights reserved.
//

#ifndef EulerSolutions_Solution3_h
#define EulerSolutions_Solution3_h

#define true 1
#define false 0

#include <math.h>
#include <stdio.h>

long isPrime(long value)
{
    long i = 2;
    const float SQUARE = sqrt(value);
    
    /*
     A pattern exists in which 1...sqrt(x) is the reversal of sqrt(x)...1.
     Thus, only 1...sqrt(x) should be computed to check for prime.
    */
    
    while (i <= SQUARE) {
        if (value % i == 0)
            return false;
        ++i;
    }
    
    return true;
}

long largestPrimeFactor(long value)
{
    /**
     Largest prime factor of value parameter.
     */
    
    long i = sqrt(value);
    while (i > 2) {
        if (value % i == 0 && isPrime(i))
            return i;
        --i;
    }
    
    return -1;
}

#endif
