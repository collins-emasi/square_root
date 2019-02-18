# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 09:22:03 2019

@author: pythonister
"""

epsilon = 0.0001
x = int(input("Enter a number: \n"))
low = 0.0
high = max(1.0, abs(x))
ans = (high + low)/2.0


while abs(ans**2 - abs(x)) >= epsilon:
    if ans**2 < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
if x < 0:
    ans = -ans
print("The square root of {} is close to {}".format(x, (round(ans, 2))))
