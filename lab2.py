# Name: Zain ElHashemite
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.  

# CS 115 - lab2



def dot(L, K):
    '''Returns the dot product of lists L and K'''
    if L==[] or K==[]:
        return 0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])


def ind(e, L):
    '''Returns the first index where e is found in a list or string L,
    if e is not in L then the length of L is returned'''
    if L==[] or L=="":
        return 0
    else:
        if e == L[0]:
            return 0
        else:
            return 1 + ind(e, L[1:])
    


def removeAll(e, L):
    '''Removes all instances of e from a list L and returns the new list'''
    if L==[]:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])

