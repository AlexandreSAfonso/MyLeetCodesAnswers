#!/bin/python3

import math
import os
import random
import re
import sys



def miniMaxSum(arr):
    # Write your code here
    lenArr = len(arr)
    arraySum = sum(arr)
    tmpArraySum = 0
    minArr = arraySum
    maxArr = 0

    for n in  arr:
        print('sum of array is', arraySum, ', without', n, 'the sum is', arraySum - n)
        tmpArraySum = arraySum - n
        if tmpArraySum < minArr:
            minArr = tmpArraySum

        if tmpArraySum > maxArr:
            maxArr = tmpArraySum            
        
    
    print(minArr,  maxArr)

if __name__ == '__main__':
    
    a =  [1, 2, 3, 4, 5]
    result = miniMaxSum(a)


# Mini-Max Sum

# Given five positive integers, find the minimum and maximum 
# values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line 
# of two space-separated long integers.

# Example
# arr=[1,3,5,7,9]

# The minimum sum 1+3+5+7+9 is 16 and the maximum 3+5+7+9 sum is 24 . 
# The function prints 16 24
