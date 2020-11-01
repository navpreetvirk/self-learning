# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:32:15 2020

@author: Navpreet Virk

This program asks the user to input 10 integers, and then prints the largest
odd number that was entered. If no odd number was entered, it prints a
message to that effect.
"""

inputCount = 1

largestSoFar = 0

while inputCount <= 10:
    numberInput = int(input("Enter (" + str(inputCount) + " of 10) integers: "
                            ))
    
    if numberInput % 2 == 1 and numberInput > largestSoFar:
        largestSoFar = numberInput
        
    inputCount += 1
    
if largestSoFar > 0:
    print("Largest odd number that was entered:", largestSoFar)
else:
    print("No odd number was entered.")