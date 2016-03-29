//
//  Solution3.h
//  EulerSolutions
//
//  Created by seales on 1/22/14.
//  Copyright (c) 2014 seales. All righproductOfFactors reserved.
//

#ifndef EulerSolutions_Solution5_h
#define EulerSolutions_Solution5_h

#include <stdlib.h>

#define true 1
#define false 0

long productOfFactors(const int DIVISIBLE_COUNT)
{
    /**
     The input should be thought of as a interval from 1...DIVISIBLE_COUNT.
     
     Each number in this sequence can be further broken down into factors
     of smaller numbers in the interval. This function does just that.
     */
    
    int * arrayOfFactors = (int*) malloc(sizeof(int) * DIVISIBLE_COUNT);
    
    for (int i = 0; i < DIVISIBLE_COUNT; i++)
        arrayOfFactors[i] = 1; // each number given count of one
    
    int wasFactored = true;
    long product = 0;
    
    while (wasFactored) {
        wasFactored = false; // Number not yet factored.
        for (int i = 1; i < DIVISIBLE_COUNT; i++) {
            for (int j = i; j < DIVISIBLE_COUNT; j++) {
                product = (i+1) * (j+1); // offset by 1 because of 0-index array
                if (product <= DIVISIBLE_COUNT
                    && arrayOfFactors[(int) product-1] > 0 && i != j) {
                    
                    /*
                     Three conditions
                     1. Product of numbers is also within interval.
                     2. Product has count greater than 0.
                     3. Product is not a square
                     */
                    
                    // Product factored (decremented)
                    arrayOfFactors[(int)product-1]--;
                    
                    // i and j, both factors, are incremented
                    arrayOfFactors[i]++;
                    arrayOfFactors[j]++;
                    wasFactored = true;
                }
            }
        }
    }
    
    long factorsProduct = 1;
    
    // product of each number remaining after initial factoring
    for (int i = 0; i < DIVISIBLE_COUNT; i++) {
        if (arrayOfFactors[i] >= 1)
            factorsProduct *= (i+1); // offset by 1 because of 0-index array
    }
    
    free(arrayOfFactors);
    return factorsProduct;
}


long divisor(const long DIVISIBLE_COUNT)
{
    /**
     Finds the smallest number that is evenly divisible by 1...DIVISLBE_COUNT.
     */
    
    long product = productOfFactors((int)DIVISIBLE_COUNT);
    long smallest = product;
    
    for (int i = 1; i < DIVISIBLE_COUNT+1; i++)
    {
        if (product % i != 0) { // non-even division within interval; reset
            product -= DIVISIBLE_COUNT; // decrement product
            i = 1;
        } else if (i == DIVISIBLE_COUNT && product <= smallest) {
            // even division within entire interval, store as smallest, and reset
            smallest = product;
            product -= DIVISIBLE_COUNT;
            i = 1;
        }
        
        if (product < 1) break; // solution must be >= 1
    }
    
    return smallest;
}
#endif
