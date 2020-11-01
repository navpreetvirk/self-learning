# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:17:12 2020

@author: Navpreet Virk

This pogram examines three variables (x, y, and z) and prints the largest odd
number among them. If none of them are odd, it prints a message to that
effect.
"""

x = 265
y = 145
z = 789


print("x: ", x)
print("y: ", y)
print("z: ", z)

largestSoFar = 0

if x % 2 == 1 or y % 2 == 1 or z % 2 == 1:
    if x % 2 == 1 and x > largestSoFar:
        largestSoFar = x
        
    if y % 2 == 1 and y > largestSoFar:
        largestSoFar = y
    
    if z % 2 == 1 and z > largestSoFar:
        largestSoFar = z
    
    print("Largest odd number is: ", largestSoFar)
else:
    print("None of variables (x, y and z) are odd.")