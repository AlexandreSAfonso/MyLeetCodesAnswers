#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    # Write your code here

    positiveCount = 0
    negativeCount = 0
    zeroCount = 0
    totalCount = len(arr)
    
    i = 0
    while i < totalCount:
        if arr[i] > 0:
            positiveCount += 1
        elif arr[i] < 0:
            negativeCount += 1
        else:
            zeroCount += 1
        
        i += 1


    ratios1 = positiveCount / float(totalCount)

    ratios2 = negativeCount / float(totalCount)

    ratios3 = zeroCount / float(totalCount)
    
    print(ratios1)
    print(ratios2)
    print(ratios3)

if __name__ == '__main__':
    
    a =  [-4, 3, -9, 0, 4, 1]

    result = plusMinus(a)


# Plus Minus

# Given an array of integers, calculate the ratios of its elements that are positive, 
# negative, and zero. 
# Print the decimal 6 value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. 
# The test cases are scaled to six decimal places, though answers with absolute 
# error of up to 10^(-4) are acceptable.

# Example: 
#     arr =[1,1,0,-1,-1]

# There are  elements, two positive, two negative and one zero. 
# Their ratios are ,  and . Results are printed as:

#     0.400000
#     0.400000
#     0.200000

# Other Example:  
#     arr = [-4, 3, -9, 0, 4, 1]

# Return

#     0.500000
#     0.333333
#     0.166667