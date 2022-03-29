# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, 
and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

import math

def isPrime(n): # Using primality criteria to avoid factorisation 
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f += 6
        return True
  
iterations = 1    
primes = 1
required = 1
while iterations < 10001:
    required += 2
    if isPrime(required):
        iterations += 1

print(required)
