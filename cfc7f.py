# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 12:58:54 2021

@author: hp
"""


row=5
col=2*row-1
i=0
while i<row:
    j=0
    while j<col:
        if((col//2)-i<=j<=(col//2)+i):
            print("*",end=" ")
        else:
            print(" ",end="")
        j=j+1
    print(" ")
    i=i+1
i=0
while i<row:
    j=0
    while j<col:
        if(i<=j<=col-1-i):
            print("*",end=" ")
        else:
            print(" ",end="")
        j=j+1
    print(" ")
    i=i+1
        
