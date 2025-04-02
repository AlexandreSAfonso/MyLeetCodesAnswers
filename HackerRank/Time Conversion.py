#!/bin/python3

import math
import os
import random
import re
import sys

def convert24(s): 
    
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if s[-2:] == "AM" and s[:2] == "12": 
        return "00" + s[2:-2] 
        
    # remove the AM     
    elif s[-2:] == "AM": 
        return s[:-2] 
    
    # Checking if last two elements of time 
    # is PM and first two elements are 12 
    elif s[-2:] == "PM" and s[:2] == "12": 
        return s[:-2] 
        
    else: 
        
        # add 12 to hours and remove PM 
        return str(int(s[:2]) + 12) + s[2:8] 


if __name__ == '__main__':

    print(convert24("08:05:45 PM"))


# Time Conversion

# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: 
#     - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
#     - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example
#     s = '12:01:00PM'
#     Return '12:01:00'.

#     s = '12:01:00AM'
#     Return '00:01:00'.

# Function Description

# Complete the timeConversion function in the editor below. It should return a new string 
# representing the input time in 24 hour format.

# timeConversion has the following parameter(s):

#     string s: a time in 12 hour format
# Returns

#     string: the time in 24 hour format

# Input Format

#     A single string s that represents a time in 12-hour clock 
#     format (i.e.: hh:mm:ssAM or hh:mm:ssPM).