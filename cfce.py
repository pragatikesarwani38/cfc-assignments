# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 12:52:13 2021

@author: hp
"""


from math import factorial
n=6
for i in range(n):
    for j in range(n-i+1):
        print(end="")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()