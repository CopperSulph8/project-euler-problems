# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers 
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(n):
    n = str(n)
    if n[::-1] == n:
        return True
    else:
        return False

palindromes = []
for i in range(100,999):
    for j in range(i, 999):
        if isPalindrome(i*j):
            palindromes.append(i*j)

print(max(palindromes))
