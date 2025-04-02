#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    # Write your code here
    aSum = 0
    bSum = 0
    
    counter = len(a)
    i = 0
    while i < counter:
        
        if a[i] > b[i]:
            aSum += 1
        if a[i] < b[i]:
            bSum += 1

        i += 1
    
    return aSum, bSum

    # INTEGER_ARRAY_A = sum(a)
    # INTEGER_ARRAY_B = sum(b)
    # return np

if __name__ == '__main__':
    
    a = [5, 6, 7]

    b = [3, 6, 10] 

    print(compareTriplets(a, b))


# Compare the Triplets

# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b

# Alice and Bob each created one problem for HackerRank. 
# A reviewer rates the two challenges, awarding points on a scale 
# from 1 to 100 for three categories: problem clarity, originality, and difficulty.

# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), 
# and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

# The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], 
# and a[2] with b[2].

# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.
# Comparison points is the total points a person earned.

# Given a and b, determine their respective comparison points.