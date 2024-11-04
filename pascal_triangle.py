# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:05:34 2024

@author: Jali
"""

def factorial(n):
    product = 1
    for i in range(1, n+1):
        product = product * i
    return product

def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def pascals_triangle(num):
    triangle = []
    for n in range(num):
        row = [] #row by row
        for k in range(n + 1):
            coefficient = binomial(n, k)
            row.append(coefficient)
        triangle.append(row)
    maxwidth = len(str(triangle[-1][len(triangle[-1]) // 2])) + 2 #width of largest number + padding
    for n in range(num):
        leadingspaces = (maxwidth * (num - n - 1)) // 2
        print(" " * leadingspaces, end="") #print alignment
        for coefficient in triangle[n]:
            print(str(coefficient).center(maxwidth), end="")
        print()
#Main program
num = int(input("enter a number of rows of Pascal's triangle: "))
while num <= 0:
    num = int(input("bro enter a valid number pls"))
pascals_triangle(num)
    
    



