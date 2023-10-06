'''
Created on  4/24/23
@author(s): Salvatore Matteis, Zain ElHashemite
Pledge:     I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
# You may write helpers if you see fit. Remember: do not
# import anything, and do not use loops.

def numToBinary(n):
    '''Returns the string with the binary representation of a postive integer n unless if n is 0 then an empty string is returned'''
    if n == 0:
        return ""
    return numToBinary(int(n / 2)) + str(n%2)

def filler(s):
    '''complete 5 digit if the binary string is not long enough, fills the higher digits with 0'''
    return "0" * (5 - len(s)) + s

def binaryToNum(s):
    '''Returns the appropriate integer corresponding to the binary representation of s'''
    if s == "":
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])


def compress(S):
    '''compresses a 64-bit binary image (represented as 1's
    and 0's) using a run-length encoding'''
    def helper(S, x):
        '''returns an array of ["0", 0], the first element shows if it is a 1 or 
        0 then the second element shows how long the 1 or 0 is'''
        if S =="":
            return [x]
        if S[0] != x[0] and x[1] != 0:
            return [x] + helper(S[1:], [S[0]]+[1])
        return helper(S[1:], [S[0]] + [x[1]+1])
    def compress2(L):
        '''Takes the result from the helper function and returns a binary string base 10.'''
        if L ==[]:
            return ""
        if L[0][1]>MAX_RUN_LENGTH:
            return "1111100000" + compress2([[L[0][0]] + [L[0][1]-31]] + L[1:])
        return filler(numToBinary(L[0][1])) + compress2(L[1:])
    return ("00000" if S[0] == "1" else "") + compress2(helper(S, ["0",0]))

        

def uncompress(C):
    '''uncompresses a run-length encoding to its original
    64-bit binary image'''
    def uncompress2(C):
        '''uncompresses the binary and returns a list of 0 and 1'''
        if C =="":
            return []
        return [binaryToNum(C[0:COMPRESSED_BLOCK_SIZE])] + uncompress2(C[COMPRESSED_BLOCK_SIZE:])
    def helper2(L, num):
        '''Takes result and returns original binary string'''
        if L ==[]:
            return ""
        return ("0" if num else "1") * L[0]+ helper2(L[1:], not num)
    return helper2(uncompress2(C), True)
        
    
