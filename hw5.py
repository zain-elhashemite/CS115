'''
@author:   Zain ElHashemite
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5: Memoization

To receive full credit, you MUST USE MEMOIZATION!
We will be testing the efficiency of your program
and you will lose points if your program does not use
memoization to improve performance.

'''

def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]

    HINTS: base cases for Lucas numbers are n=0 -> 2, n=1 -> 1
           n>=2 -> recursive case, sum of previous two numbers'''
    
    memo={}
    def lucas_help(n):
        if n==0:
            return 2
        elif n==1:
            return 1
        elif n in memo:
            return memo[n]
        else:
            memo[n] = lucas_help(n-1) + lucas_help(n-2)
            return memo[n]

    return lucas_help(n)

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.
    
    NOTE: if you get errors with "unhashable type: 'list'",
    convert the coins list to a TUPLE'''
    memo={}
    def change_help(amount, coins):
        if amount == 0:
            return 0
        
        elif amount < 0 or coins == []:
            return float('inf')
        
        elif (amount, tuple(coins)) in memo:
            return memo[(amount, tuple(coins))]
        
        else: #use it or lose it
            use = change_help(amount-coins[-1], coins) + 1
            lose = change_help(amount, coins[:-1])
            memo[(amount, tuple(coins))] = min(use, lose)
            
            return memo[(amount, tuple(coins))]
    
    return change_help(amount, coins)

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100])) # 4
print(fast_change(292, [1, 5, 10, 20, 50, 100])) # 7
print(fast_change(673, [1, 5, 10, 20, 50, 100])) # 11
print(fast_change(724, [1, 5, 10, 20, 50, 100])) # 12
print(fast_change(888, [1, 5, 10, 20, 50, 100])) # 15
