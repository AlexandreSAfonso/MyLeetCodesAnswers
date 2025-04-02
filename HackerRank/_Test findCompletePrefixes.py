#!/bin/python3

import math
import os
import random
import re
import sys

def findCompletePrefixes(names, query):
    # Write your code here
    results = []
    for item in query:
        count = 0
        for name in names:
            if len(item) < len(name) and name.startswith(item):  # Certifique-se de que `item` é uma string
                count += 1
        results.append(count)
    return results

if __name__ == '__main__':

    names = ['jackson', 'jacques', 'jack']
    query = ['jack']
    result = findCompletePrefixes(names, query)

# quantos nomes na lista têm esse prefixo, considerando as seguintes regras:

# O prefixo deve ser estritamente menor que o nome completo.
# O prefixo deve coincidir com o início do nome.