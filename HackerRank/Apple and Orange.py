#!/bin/python3

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    countApple = 0

    countOranges = 0
    for apple in apples:
        if apple >= 0:
            land = apple + a
            if s <= land and land <= t :
                countApple = countApple + 1

    for orange in oranges:
        if orange <=0:
            land = orange + b  
            if s <= land and land <= t :
                countOranges = countOranges + 1    

    print(countApple)

    print(countOranges)

def countApplesAndOranges1(s, t, a, b, apples, oranges):
    # Write your code here
    rangeArea = []
    countApple = 0
    countOranges = 0
    
    for i in range (s, t+1):
        rangeArea.append(i)

    for apple in apples:
        land = apple + a
        if land in rangeArea:
            countApple = countApple + 1

    for orange in oranges:
        land = orange + b  
        if land in rangeArea:
            countOranges = countOranges + 1    


def countApplesAndOranges2(s, t, a, b, apples, oranges):
    # Write your code here
    rangeArea = []
    landApple =[]
    countApple = 0
    rangeApple = len(apples)
    landOranges =[]
    countOranges = 0
    rangeOranges = len(oranges)

    
    for i in range (s, t+1):
        rangeArea.append(i)

    for apple in apples:
        landApple.append(apple + a)
        land = apples[i] + a
        
        if land in rangeArea:
            countApple = countApple + 1

    for orange in oranges:
        landOranges.append(orange + b)        
        land = oranges[i] + b
        if land in rangeArea:
            countOranges = countOranges + 1    


    # for land in apples: #landApple:
    #     if land in rangeArea:
    #         countApple = countApple + 1

    # for land in oranges: #landOranges:
    #     if land in rangeArea:
    #         countOranges = countOranges + 1    
    # 
    
if __name__ == '__main__':

    #house
    s = 7
    t = 10
    
    #apple tree
    a = 4 

    #orange 
    b = 12 
    
    #falls
    apples = [2,3,-4]
    oranges =[3, -2, -4]


# # -----------------------------------------------
#     #house  
#     s = 2
#     t = 3
    
#     #apple tree
#     a = 1 

#     #orange 
#     b = 5 
    
#     #falls
#     apples = [2]
#     oranges =[-2]

# # -----------------------------------------------
#     #house  
#     s = 2
#     t = 3
    
#     #apple tree
#     a = 1 

#     #orange 
#     b = 5 
    
#     #falls
#     apples = [-2]
#     oranges =[-2]



    result = countApplesAndOranges(s, t, a, b, apples, oranges)

# Apple and Orange

# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
# Using the information given below, determine the number of apples 
# and oranges that land on Sam's house.

# In the diagram below:

# The red region denotes the house, where  is the start point, and t is the endpoint. 
# The apple tree is to the left of the house, and the orange tree is to its right.
# Assume the trees are located on a single point, where the apple tree is at point 'a', 
# and the orange tree is at point 'b'.
# When a fruit falls from its tree, it lands  units of distance from its tree of origin 
# along the x-axis. *A negative value of 'd' means the fruit fell 'd' units to the 
# tree's left, and a positive value of 'd' means it falls  units to the tree's 
# right. *

# Given the value of 'd' for 'm' apples and  oranges, determine how many 
# apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t] )?

# For example, Sam's house is between s=7 and t=10. The apple tree is located at a=4 
# and the orange at b=12. There are m=3 apples and n=3 oranges. Apples are 
# thrown apples=[2,3,-4] units distance from a, and oranges=[3,-2,-4] units distance. 
# Adding each apple distance to the position of the tree, they land at [4+2,4+3,4+(-4)]. 
# Oranges land at [12+3,12+(-2),12+(-4)]. 
# One apple and two oranges land in the inclusive range 7-10  so we print 
#  1
#  2