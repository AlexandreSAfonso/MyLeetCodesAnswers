#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    # Write your code here

    minPoint = 0
    maxPoint = 0
    minCont = 0
    maxCont = 0
    i =0


    for score in scores:
        if minPoint == 0 and i == 0:
            minPoint = score

        if maxPoint == 0 and i == 0:
            maxPoint = score         

        if score < minPoint  :
            minPoint = score
            minCont = minCont + 1

        if score > maxPoint:
            maxPoint = score
            maxCont = maxCont + 1

        i = i+1

    return maxCont, minCont 

    
if __name__ == '__main__':

    #scores = [10,24,10,24] 
    #scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    # scores = [0, 9, 3, 10, 2, 20]
    scores = [0, 9, 3, 10, 2, 20]

    result = breakingRecords(scores)

    print(result)

# Breaking the Records

# Maria plays college basketball and wants to go pro. 
# Each season she maintains a record of her play. 
# She tabulates the number of times she breaks her season record 
# for most points and least points in a game. Points scored in the first game 
# establish her record for the season, and she begins counting from there.

# Example

# Scores are in the same order as the games played. She tabulates her results as follows:

#                                      Count
#     Game  Score  Minimum  Maximum   Min Max
#      0      12     12       12       0   0
#      1      24     12       24       0   1
#      2      10     10       24       1   1
#      3      24     10       24       1   1
# Given the scores for a season, determine the number of times Maria 
# breaks her records for most and least points scored during the season.

# Function Description

# Complete the breakingRecords function in the editor below.

# breakingRecords has the following parameter(s):

# int scores[n]: points scored per game
# Returns

# int[2]: An array with the numbers of times she broke her records. 
# Index  is for breaking most points records, and index  is for breaking 
# least points records.