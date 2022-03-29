# -*- coding: utf-8 -*-
"""
Find the difference between the sum of the squares
of the first one hundred natural numbers 
and the square of the sum.

"""

def sumSquare(n):
    return (n * (n + 1) * (2*n + 1)) * 1/6

def squareSum(n):
    return (1/2 * n * (n + 1))**2

print(abs(sumSquare(100)-squareSum(100)))

