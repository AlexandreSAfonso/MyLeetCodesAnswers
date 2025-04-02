#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(a):
    # Write your code here
        
    for i in range(1, a+1):
        
        print(' ' * (a  - i) + '#' * i)
    
    
if __name__ == '__main__':
    a = 6

    b = [3, 6, 10] 

    result = staircase(a)


# Staircase detail

# This is a staircase of size :

#            #
#           ##
#          ###
#         ####
# Its base and height are both equal to . It is drawn using # symbols and spaces. 
# The last line is not preceded by any spaces.

# Write a program that prints a staircase of size .

# Function Description

# Complete the staircase function in the editor below.

# staircase has the following parameter(s):

# int n: an integer
# Print

# Print a staircase as described above.
