'''
Author: Zain ElHashemite
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
'''
#Problem 1
def addOne(L):
    '''Takes a list of numbers and adds one to each element of the list'''
    if L==[]:
        return []
    else:
        return [L[0] + 1] + addOne(L[1:]) 


#Problem 2
def explode(S):
    '''Splits a string into a list of the individual characters'''
    if S=="":
        return []
    else:
        return [S[0]] + explode(S[1:])
    

#Problem 3
def myFilter(func,L):
    '''Returns a list of all elements for which func is True'''
    if L==[]:  
        return []
    elif func(L[0]):
        return [L[0]] + myFilter(func, L[1:])
    else:
        return myFilter(func, L[1:])


#Problem 4
def sumPos(L):
    '''Accepts a list and returns the sum of the positive numbers, ignoring the negative ones'''
    if L==[]:
        return 0
    elif L[0] > 0:
        return sumPos(L[1:]) + L[0]
    else:
        return sumPos(L[1:])  

