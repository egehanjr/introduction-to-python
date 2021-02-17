# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:04:18 2021

@author: Egehan
"""

import random

maxvalue = int(input("Specify the maximum value of range for selecting random primes numbers: ")) ##It takes the max value of range from user.
numrange = range(0, maxvalue) 
primenumbers = []
### This code block intent for checks the number prime or not.
for i in numrange:
    if i > 1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            primenumbers.append(i)
            ###
            
randomprimes = random.choices(primenumbers,k=9) ## With using random library this function selects 9 random numbers from primenumbers list.

matrix = [[0,0,0], [0,0,0], [0,0,0]]
t = 0
for x in range(3):
    for y in range(3):
        matrix[x][y]  = randomprimes[t]
        t = t + 1
print("The Result Matrix is ",matrix) ## Placed the prime numbers chose into the 3x3 matrix created and printed them.
