# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 00:33:50 2021

@author: hp
"""


n=(int)(input("Enter a number"))
c=0
while(n>0):
    c=c+1
    n=n//10
print(c)