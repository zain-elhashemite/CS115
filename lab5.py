'''
Created on 3/10/2023
@author:   Zain ElHashemite
Pledge:    I pledge my honor that I have adbided by the Stevens Honor System.
CS115 - Lab 5
'''
import time
from cs115 import *
words = []
HITS = 10

memo = {}


def fastED(S1, S2):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    if (S1, S2) in memo:
        return memo[(S1, S2)]
    if len(S1) == 0:
        return len(S2)
    if len(S2) == 0:
        return len(S1)
    if S1[0] == S2[0]:
        result = fastED(S1[1:], S2[1:])
    else:
        substitution = 1 + fastED(S1[1:], S2[1:])
        insertion = 1 + fastED(S1, S2[1:])
        deletion = 1 + fastED(S1[1:], S2)
        result = min(substitution, insertion, deletion)
    memo[(S1, S2)] = result
    return result


def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return map(lambda x: (fastED(user_input, x), x), words)
    

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
