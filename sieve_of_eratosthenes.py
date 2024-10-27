# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:13:24 2024

@author: Jali
"""
number = []
n = int(input("Enter a positive integer: "))
numbers = list(range(2, n+1))
for i in range(2, int(n**0.5) + 1):
   if numbers[i-2]:
       for j in range(i*i, n+1, i):
            numbers[j-2] = 0
numbers.sort()
k = numbers.count(0)
numbers = numbers[k:]
print(numbers)
print("\nThere are", len(numbers), "prime numbers up to", n)
