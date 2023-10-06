#Zain ElHashemite
#CS115 HW 1: 1/29/2023
#I pledge my honor that I have abided by the Stevens Honor System

from cs115 import *
import math

def mult(x,y):
    '''Returns the product of x and y'''
    return x*y

def factorial(n):
    '''Returns the factorial of a positive integer'''
    return reduce(mult,range(1,n+1))


def add(x,y):
    '''Returns the sum of x and y'''
    return x+y

def mean(L):
    '''Returns the mean (average) of a list of numbers L'''
    return (reduce(add, L))/(len(L))
    
