# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 00:15:34 2024

@author: Muhammad Ghazali bin Md Apandi
"""

a = int(input("The first positive integer."))
b = int(input("The second positive integer."))
minimum = min(a, b) 
difference = a - b  
if minimum > difference:
  (minimum, difference) = (difference, minimum)
else:
    (minimum, difference) = (minimum, difference)
while minimum != difference:
    difference = difference - minimum 
    minimum = min(difference, minimum) 
    if minimum == 0:
        minimum = minimum + difference
    
    
print("The greatest common divisor between ", a," and", b," is", minimum)