//
//  Solution3.h
//  EulerSolutions
//
//  Created by seales on 1/22/14.
//  Copyright (c) 2014 seales. All rights reserved.
//

#ifndef EulerSolutions_Solution4_h
#define EulerSolutions_Solution4_h

#define true 1
#define false 0
#define OFFSET 2

#include <math.h>
#include <stdio.h>

int isPalindrome(long product)
{
    // amount of digits + 1 for '/0' character + 1 for OFFSET (TODO - here)
    int logBase10 = (int) (log(product) / log(10)) + OFFSET;
    char productChars[logBase10];
    
    snprintf(productChars, logBase10, "%d", (int)product);
    
    int back = logBase10 - OFFSET;
    int front = 0;
    
    while (productChars[front] == productChars[back]) {
        if (++front >= --back) 
            return true;
    }
    
    return false;
}

long longestPalindrome(int n)
{
    /**
     Finds the largest numerical palindrome for the product of nth-digit numbers.
     
     Both numbers begin as the largest nth-digit number.
     
     The first is decremented each outer iteration and the second each inner.
     Thus, every combination is satisfied in this search that terminates when
     one number goes below the lower bound of the smallest nth-digit number.
     */
    
    const long UPPER_BOUND = (long) pow(10, n) - 1; // largest n-th digit number
    const long LOWER_BOUND = (long) pow(10, n-1); // smallest n-th digit number
    long first = UPPER_BOUND;
    long second = UPPER_BOUND;
    long product = 0;
    long largestPalindrome = -1;

    while (first >= LOWER_BOUND) {
        while (second >= LOWER_BOUND) {
            product = first * second;
            if (isPalindrome(product) && (product > largestPalindrome))
                largestPalindrome = product;
            --second;
        }
        second = first - 1;
        --first;
    }

    return largestPalindrome;
}

#endif
