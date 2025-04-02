#!/bin/python3

import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    # Write your code here

    lenCandles = len(candles)
    maxCandles = max(candles)
    count = 0
    for i in range (0, lenCandles):
        if candles[i] == maxCandles:
            count+=1
    return count


if __name__ == '__main__':
    a =  [3, 2, 1, 3]

    expected = 2

    result = birthdayCakeCandles(a)

    print(result)

# Birthday Cake Candles

# You are in charge of the cake for a child's birthday. You have decided the cake
# will have one candle for each year of their total age. They will only be able 
# to blow out the tallest of the candles. Count how many candles are tallest.

# Example
#     candles=[4,4,1,3]

# The maximum height candles are 4 units high. There are 2 of them, so return 2.
