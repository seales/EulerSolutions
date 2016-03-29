//
//  Solution9.h
//  EulerSolutions
//
//  Created by seales on 2/9/14.
//  Copyright (c) 2014 seales. All rights reserved.
//

#ifndef EulerSolutions_Solution9_h
#define EulerSolutions_Solution9_h

#include <math.h>

int pythagoreanTriple(int sum)
{
    for (int i = 1; i < sum; i++) {
        for (int j = i; j < sum; j++) {
            for (int k = j; k < sum; k++) {
                if ((k+j+i) == sum
                            && (pow(i, 2) + pow(j, 2)) == pow(k, 2)) {
                    return k * j * i;
                }
            }
        }
    }
    
    return -1;
}


#endif
