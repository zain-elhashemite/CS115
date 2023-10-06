#Zain ElHashemite
#I pledge my honor that I have abided by the Stevens Honor System.

def knapsack(capacity, items):
    '''returns the maximum value you can steal given the capacity
    of your knapsack'''
    if capacity == 0:
        return 0 
    elif items == []:
        return 0
    elif items[0][0] > capacity:
        return knapsack(capacity, items[1:])
    else:
        use = items[0][1] + knapsack(capacity - items[0][0], items[1:])
        lose = knapsack(capacity, items[1:])
        return max(use,lose)
    
