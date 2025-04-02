#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findCompletePrefixes' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY names
#  2. STRING_ARRAY query
#

def findCompletePrefixes(names, query):
    # Write your code here

        
    matchers = query
    matching = [s for s in names if any(xs in s for xs in matchers)]

    return matching
            

#Given a list of names determine the number of names in that list for a fiven prefix

if __name__ == '__main__':
    fptr = open('output.csv', 'w')

    names = []
    
    with open("input.txt") as f:
        lis = [line.split() for line in f]        # create a list of lists
        for i in lis:              #print the list items 
            names.append(i[0])


    query_count = open('qr.csv', 'r')

    query = []

    with open("iq.txt") as f:
        lis = [line.split() for line in f]        # create a list of lists
        for i in lis:              #print the list items 
            query.append(i[0])

    result = findCompletePrefixes(names, query)


