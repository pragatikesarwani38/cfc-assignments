# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:09:24 2021

@author: hp
"""


n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    for j in range(2*(n-i)):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(2*(n-i-1)):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
   
    print()

        