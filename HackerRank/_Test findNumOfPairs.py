#!/bin/python3

import math
import os
import random
import re
import sys


def findNumOfPairs1(a, b):
    # Write your code here
    used = [False] * len(b)  # Rastreamento para elementos usados em `b`
    count = 0

    for num in a:
        for j in range(len(b)):
            if not used[j] and num > b[j]:
                # Par válido encontrado
                used[j] = True
                count += 1
                break  # Avança para o próximo elemento de `a`
                
    return count



def findNumOfPairs(a, b):
    # Sort both arrays
    a.sort()
    b.sort()

    i, j = 0, 0  # Pointers for both arrays
    pairs = 0

    # Traverse both arrays
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            # If a[i] > b[j], we can form a pair
            pairs += 1
            j += 1  # Move pointer for b to the next element
        # Move pointer for a to the next element
        i += 1
    
    return pairs



def max_pairs1(a, b):
    import bisect
    # Ordena o array a
    a.sort()
    
    # Inicializa o número de pares
    pairs = 0
    n = len(a)
    
    # Itera sobre cada elemento de b
    for b_val in b:
        # Usamos a busca binária para encontrar o primeiro valor em a que é maior que b_val
        idx = bisect.bisect_right(a, b_val)
        
        # Se encontramos um valor maior que b_val, formamos um par
        if idx < n:
            pairs += 1
            a.pop(idx)  # Remove o valor utilizado em a
            
    return pairs    

def max_pairs(a, b):
    # Ordena o array 'a'
    a.sort()
    
    # Inicializa o número de pares
    pairs = 0
    n = len(a)
    
    # Itera sobre cada elemento de b
    for b_val in b:
        # Procura por um valor em a que seja maior que b_val
        for i in range(len(a)):
            if a[i] > b_val:
                pairs += 1
                # Remove o valor de 'a' usado para o par
                a.pop(i)
                break
    return pairs    

if __name__ == '__main__':

# consider two arrays of integer, a[n] and b[n]. 
# what is the maximum number of pairs that can be formed where [i] > b[i]? 
# Eache element can be in no more then one pair

# Find them maximum number of such

# Sample
# a=[1,2,3]
# b=[1,2,1]

# return no more them 2 pairs can be formed, so return 2


    a = [1, 2, 3, 4, 5]
    b = [6, 6, 1, 1, 1]

    print(max_pairs(a, b))

    result = findNumOfPairs(a, b)


    
