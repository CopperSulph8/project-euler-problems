# -*- coding: utf-8 -*-
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import math

n = 600851475143

if n % 2 == 0:
    lastdiv = 2
    n = n // 2
    while n % 2 == 0:
        n = n // 2
else:
    lastdiv = 1 

p_1 = 3
p_n = math.sqrt(n) # every num n can have at most one prime factor > sqrt(n)

while n > 1 and p_1 <= p_n:
    if n % p_1 == 0:
        n = n // p_1
        lastdiv = p_1
        while n % p_1 == 0:
            n = n // p_1
        
    p_1 = p_1 + 2
    
if n == 1:
    print(lastdiv)
else:
    print(n)
