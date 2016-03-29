//
//  Solution8.h
//  EulerSolutions
//
//  Created by seales on 2/8/14.
//  Copyright (c) 2014 seales. All rights reserved.
//

#ifndef EulerSolutions_Solution8_h
#define EulerSolutions_Solution8_h

#define ASCII_INT_OFFSET 48

#include <stdio.h>
#include <assert.h>

double greatestProduct(int n, char * file)
{
    /**
     Finds the greatest product of n-consecutive numbers contained in a file.
     */
    
    FILE *fp = fopen(file, "r");
    int product = 1;
    int largestProduct = 1;
    int num = 0;
    int counter = 0;
    int nNumbers[n];
    
    for (int i = 0; i < n; i++)
        nNumbers[i] = 0; // initialize to 0
    
    if (fp) {
        while ((num = getc(fp)) != EOF) {
            num -= ASCII_INT_OFFSET;
            if (num >= 0 && num <= 9) { // an integer
                product = 1;
                 
                for (int i = 0; i < n; i++)
                    product *= nNumbers[i];
                 
                nNumbers[counter++%n] = num;
               
                if (product > largestProduct)
                    largestProduct = product;
            }
        }
        fclose(fp);
    } else {
        printf("Invalid file.\n");
    }
    
    return largestProduct;
}


#endif
