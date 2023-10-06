#Lab 1, 2/3/2023
#Zain ElHashemite
#I pledge my honor that I have abided by the Stevens Honor System.

from math import factorial
from cs115 import *

def add(x,y):
    '''Returns the sum of x and y'''
    return x+y

def inverse(n):
    '''This function takes a number "n" and returns its inverse'''
    return (1/n)

def e(n):
    '''Approximates e using a Taylor expansion by adding the first n terms of the sequence'''
    if n==0:
        return 1
    else:
        e = 1
        
        L = range(1,n+1)
        L1 = map(factorial,L)
        L2 = map(inverse, L1)
        L3 = reduce(add,L2)

        return e+L3
        
    
        
        
