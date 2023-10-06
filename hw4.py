# NAME: Zain ElHashemite
# PLEDGE: I pledge my honor that I have abided by the Stevens Honor System.


def add_rows(prev_row):
    '''generates the next row in Pascal's Triangle given prev_row'''
    if prev_row==[]:
        return []
    elif prev_row==[1]:
        return [1]
    else:
        return [prev_row[0]+prev_row[1]]+add_rows(prev_row[1:])

def pascal_row(n):
    '''returns the nth row of terms in Pascal's Triangle, with n=0 representing the top of the
    triangle that contains one term'''
    if n==0: #1st base case
        return [1]
    elif n==1: #2nd base case
        return [1,1]
    else:
        return [1] + add_rows(pascal_row(n - 1))

def pascal_triangle(n):
    '''returns a list containing each row of Pascal's Triangle up to the nth row. Each row is
    expressed as a sublist within the main list'''
    def helper(acc, n):
        if (acc==[] and n==0):
            return []
        elif n==0:
            return [[1]] + acc
        else:
            return helper([pascal_row(n)] + acc, n-1)
    return helper([],n)

def test_pascal_row():
    '''tests the pascal_row function'''
    assert pascal_row(0)==[1]
    assert pascal_row(1)==[1,1]
    assert pascal_row(2)==[1,2,1]
    assert pascal_row(3)==[1,3,3,1]
    assert pascal_row(4)==[1,4,6,4,1]
    assert pascal_row(5)==[1,5,10,10,5,1]

def test_pascal_triangle():
    '''tests the pascal_trianlge function'''
    assert pascal_triangle(1)==[[1],[1,1]]
    assert pascal_triangle(2)==[[1],[1,1],[1,2,1]]
    assert pascal_triangle(3)==[[1],[1,1],[1,2,1],[1,3,3,1]]
    assert pascal_triangle(4)==[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    
