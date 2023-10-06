'''
Created on 3/24/2023
@author:   Zain ELHashemite
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''


#Written Questions:
#1. 42 in base 2 is 101010

#2. In the case that a given number is odd, the rightmost bit will be the
#   remainder of an odd number divided by 2, which is 1. Conversely, the rightmost
#   bit of an even number will be the remainder of an even number divided by 2, which is 0.

#3. If we eliminate the rightmost bit of a base2 number, the original number will be halved.
#   Ex. 1010 = 10 -> 101 = 5

#4. N is Even: Assuming we have Y, then we can simply append a 0 to the end of the base2 number
#   so: 101 = 21, append 0 -> 1010 = 42, thus equalling N = 2Y
#   N is Odd: We can simply append a 1 to the end of the base2 number
#   so: 1000 = 8, append 1 -> 10001 = 17, thus equalling N = 2Y + 1

#5. The ternary representation of 59 is 2012, to get this we must divide 59 by 3 until the quotient is 0
#   59/3 = R2, 19/3 = R1, 6/3 = R0, 2/3 = R2, 0/3 = 0, read backwards and get 2012 

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2 == 1

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if isOdd(n) == True:
        return (numToBinary(n//2) + '1')
    else:
        return (numToBinary(n//2) + '0')

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return (binaryToNum(s[:-1])*2) + int(s[-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    num = numToBinary(binaryToNum(s) + 1)
    if len(num) > 8:
        return num[1:9]
    if len(num) < 8:
        return (8-len(num)) * '0' + num
    return num

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n==0:
        return
    return count(increment(s), n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n < 3:
        return str(n % 3)
    return numToTernary(n//3) + str(n%3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    return 3*ternaryToNum(s[:-1]) + int(s[-1])
