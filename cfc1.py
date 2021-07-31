# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:16:53 2021

@author: hp
"""

credit= (int)(input("Enter credit points"))
if(credit<4500):
    print("Rising Star")
elif(credit>=4500 or credit<6000):
    print("Mega Leader")
elif(credit>=6000 or credit<7500):
    print("Gega Leader")
else:
    print("Tera Leader")