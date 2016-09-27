//
//  main.c
//  EulerSolutions
//
//  Created by seales on 1/16/14.
//  Copyright (c) 2014 seales. All rights reserved.
//

// NOTE - reduce include clutter?

#include "Solution1.h"
#include "Solution2.h"
#include "Solution3.h"
#include "Solution4.h"
#include "Solution5.h"
#include "Solution6.h"
#include "Solution7.h"
#include "Solution8.h"
#include "Solution9.h"
#include "Solution10.h"

#include <assert.h>
#include <stdio.h>

void tests()
{
    assert(multipleSum(3, 5, 1000) == 233168); // Solution1
    assert(evenFibonacci(4000000) == 4613732); // Solution2
    assert(largestPrimeFactor(600851475143) == 6857); // Solution3
    assert(longestPalindrome(3) ==  906609); // Solution4
    assert(divisor(20) == 232792560); // Solution5
    assert(sumAndSquareDifference(100) == 25164150); // Solution6
    assert(nthPrime(10001) == 104743); // Solution7
  //  assert(greatestProduct(5, "/1000digits.txt") == 40824); // Solution8
    assert(pythagoreanTriple(1000) == 31875000); // Solution9
    assert(primeSummation(2000000) == 142913828922); // Solution10
    printf("All tests have passed.\n");
  
}

int main(int argc, const char * argv[])
{
  //  tests();
    
    printf("here: %d\n", (multipleSum(3, 5, 1000)));
    
    return 0;
}







