# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 01:22:04 2021

@author: hp
"""


n=5
num=1
space=n-1
for j in range(1,n+1):
    num=j
    for i in range(1,space+1):
        print(" ",end=" ")
    space=space-1
    for i in range(1,j+1):
        print(num,end=" ")
        num=num+1
    num=num-2
    for i in range(1,j):
        print(num,end=" ")
        num=num-1
    print()