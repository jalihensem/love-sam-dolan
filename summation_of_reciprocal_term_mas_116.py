# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:47:09 2024

@author: Jali
"""

n = int(input("Enter the number you want "
              "to calculate the factorial of: "))
reciprocalTerm = 0
summation = 0
i = 1
while i <= n:
    reciprocalTerm = 1 / (i**2)
    summation = summation + reciprocalTerm
    i = i + 1
print("Sum of the first", n, "reciprocal squares", summation)

if n == 99999 : print("it is equal to limit of the sum as 𝑛 gets large")
    