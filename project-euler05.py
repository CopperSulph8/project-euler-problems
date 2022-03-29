# -*- coding: utf-8 -*-
"""
2520 is the smallest number that can be divided 
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number 
that is evenly divisible by all of the numbers 
from 1 to 20?

"""

import functools

def euclidianAlgorithm(a, b):
    if a == 0:
        return b
    return euclidianAlgorithm(b % a, a)

def lcm(a, b):
    return a*b/euclidianAlgorithm(a, b)

print(functools.reduce(lcm, range(1,21)))
