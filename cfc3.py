# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:30:41 2021

@author: hp
"""


def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)
a=(int)(input("Enter number"))
b=(int)(input("Enter number"))
print(gcd(a,b))