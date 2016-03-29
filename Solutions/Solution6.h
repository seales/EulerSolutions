//
//  Solution3.h
//  EulerSolutions
//
//  Created by seales on 1/22/14.
//  Copyright (c) 2014 seales. All rights reserved.
//

#ifndef EulerSolutions_Solution6_h
#define EulerSolutions_Solution6_h

#include <math.h>

long squareOfSum(const int range)
{
    return pow(((range * (range+1)) / 2), 2);
}

long sumOfSquares(const int range)
{
    long sum = 0;
    for (int i = 0; i <= range; i++)
        sum += pow(i, 2);
    
    return sum;
}

long sumAndSquareDifference(const int range)
{
    return squareOfSum(range) - sumOfSquares(range);
}

#endif
