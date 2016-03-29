//
//  Solution1.h
//  EulerSolutions
//
//  Created by seales on 1/22/14.
//  Copyright (c) 2014 seales. All rights reserved.
//

#ifndef EulerSolutions_Solution1_h
#define EulerSolutions_Solution1_h

int multipleSum(int firstValue, int secondValue, int fromValue)
{
    /**
     Finds the sum of all numbers from 0...fromValue that are
     multiples of the two numbers firstValue and secondValue.
     */
    
    int sum = 0;
    
    for (int i = 0; i < fromValue; i++) {
        if (i % firstValue == 0 || i % secondValue == 0)
            sum += i;
    }
    
    return sum;
}

#endif
