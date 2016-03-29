//
//  Solution7.h
//  EulerSolutions
//
//  Created by seales on 1/22/14.
//  Copyright (c) 2014 seales. All rights reserved.
//

#ifndef EulerSolutions_Solution7_h
#define EulerSolutions_Solution7_h

#include "Solution3.h"


long nthPrime(const int n)
{
    int primeCount = 0;
    long i = 1;
    
    while (primeCount < n) {
        if (isPrime(++i))
            primeCount++;
    }
    
    return i;
}



#endif
