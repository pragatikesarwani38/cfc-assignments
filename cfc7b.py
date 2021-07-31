# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 00:36:19 2021

@author: hp
"""


n=(int)(input("Enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()