//
//  Solution10.h
//  EulerSolutions
//
//  Created by seales on 2/9/14.
//  Copyright (c) 2014 seales. All rights reserved.
//

#ifndef EulerSolutions_Solution10_h
#define EulerSolutions_Solution10_h

#include "Solution3.h"

long primeSummation(int interval)
{
    long sum = 0;
    for (int i = 2; i < interval; i++)
        if (isPrime(i))
            sum += i;
    
    return sum;
}

#endif
