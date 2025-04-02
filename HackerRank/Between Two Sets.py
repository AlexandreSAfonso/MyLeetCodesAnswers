#!/bin/python3

import math
import os
import random
import re
import sys



def getTotalX(a, b):
    # Write your code here

    result = 0

    for i in range(max(a), min(b)+1):
        isFactorMult = True
        for elemt in a:
            if i % elemt !=0:
                isFactorMult = False
                break

        for elemt in b:
            if elemt % i !=0:
                isFactorMult = False
                break
        
        if isFactorMult == True:
            result += 1

    return result

    
if __name__ == '__main__':

    a = [1,44,5,8,35] 
    b =  [35,12,44,7,42,31]

    # a = [2,6] 
    # b =  [24,36]

    result = getTotalX(a, b)

# Between Two Sets

# There will be two arrays of integers. Determine all integers that satisfy 
# the following two conditions:

#     1) The elements of the first array are all factors of the integer being considered
#     2) The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

# Example
#   a=[2,6]
#   b=[24,36]

# There are two numbers between the arrays: 6 and 12.
#     6%2=0, 6%6=0, 24%6=0 and 36%6=0 for the first value.
#     12%2=0, 12%6=0 and 24%12=0, 36%12=0  for the second value. 
# Return 2.

# Function Description

# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.

# getTotalX has the following parameter(s):

#     int a[n]: an array of integers
#     int b[m]: an array of integers
# Returns

#     int: the number of integers that are between the sets

# Input Format

# The first line contains two space-separated integers, n and m, the number of 
# elements in arrays a and b.
# The second line contains n distinct space-separated integers a[i] where 0<=i<n.
# The third line contains m distinct space-separated integers b[j] where 0<=j<m.