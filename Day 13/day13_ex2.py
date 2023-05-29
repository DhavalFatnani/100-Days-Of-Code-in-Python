# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 02:56:03 2023

@author: ASUS
"""

year = int(input("which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year.")
        else:
            print("Not Leap Year.")
    else:
        print("Leap Year.")
else:
    print("Not Leap Year.")
