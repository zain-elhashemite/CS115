# Name: Zain ElHashemite
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

# CS 115 - hw3

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]




def letterScore(letter,scoreList):
    '''Takes a letter as an input and returns its worth in Scrabble'''
    if letter == scoreList[0][0]:
        return scoreList[0][1]
    else:
        return letterScore(letter, scoreList[1:])


def wordScore(S,scoreList):
    '''Takes a word as an input and returns its worth in Scrabble'''
    if S=="":
        return 0
    else:
        return wordScore(S[1:], scoreList) + letterScore(S[0],scoreList) 
    
    
    
